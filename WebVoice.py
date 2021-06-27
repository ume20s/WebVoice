import webiopi
import subprocess
import urllib.parse

GPIO = webiopi.GPIO
LED_P = 23
t = "こんにちは"

def setup():
    GPIO.setFunction( LED_P, GPIO.OUT )
    GPIO.digitalWrite( LED_P, False )

@webiopi.macro
def TalkPi(tt):
    t = urllib.parse.unquote(tt)
    GPIO.digitalWrite( LED_P, True )
    open_jtalk=['open_jtalk']
    mech=['-x','/var/lib/mecab/dic/open-jtalk/naist-jdic']
    htsvoice=['-m','/usr/share/hts-voice/mei/mei_normal.htsvoice']
    #htsvoice=['-m','/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice']
    speed=['-r','0.7']
    outwav=['-ow','test.wav']
    cmd=open_jtalk+mech+htsvoice+speed+outwav 
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(t.encode('utf-8'))
    c.stdin.close()
    c.wait()
    aplay = ['aplay','-q','test.wav']
    wr = subprocess.Popen(aplay)
    GPIO.digitalWrite( LED_P, False )
