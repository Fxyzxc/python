from machine import I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
from machine import Pin, PWM
import _thread

pwm_13 = PWM(Pin(13)) #17      # 定义控制对象
pwm_13.freq(50)                # 定义频率为50分之1秒

qwe_15 = PWM(Pin(15)) #20      
qwe_15.freq(50)

led = Pin(25, Pin.OUT) 

def you_15():
    qwe_15.duty_u16(6276)
    time.sleep(0.1)
    qwe_15.deinit()
        
def zuo_15():                # 上
    qwe_15.duty_u16(3276)
    time.sleep(0.1)
    qwe_15.deinit()

def you_13():
    pwm_13.duty_u16(3576)
    time.sleep(0.1)
    pwm_13.deinit()
    
def zuo_13():
    pwm_13.duty_u16(6276)
    time.sleep(0.1)
    pwm_13.deinit()

def led_1(t,r):
    led.toggle() # led灯
    time.sleep(t)# 每0.7闪烁一次
    led.toggle()
    time.sleep(r)
    led.toggle()
    time.sleep(t)
    led.toggle()
    time.sleep(r)
    print("led执行完毕")

def zong(w,e):
    you_13()  # 左
    zuo_15()        # 上 
    time.sleep(w)
    zuo_13()    # 右
    you_15()        # 下
    time.sleep(e)
    zuo_13()        # 右
    time.sleep(w)
    you_15()        # 下
    you_13()        # 左
    time.sleep(e)
    you_13()        # 左
    zuo_15()        # 上
    time.sleep(w)
    zuo_13()        # 右
    you_15()
    #time.sleep(1)
    zuo_15()
    time.sleep(1.5)
    print("舵机执行完毕")

def duoxiancheng():
    print("执行")
    time.sleep(1.5)
    try:
        _thread.start_new_thread(led_1, (1,2))
        _thread.start_new_thread(zong, (2,1))
    except:
        print("Error: unable to start thread")

duoxiancheng()
