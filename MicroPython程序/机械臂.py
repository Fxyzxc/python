from machine import Pin, PWM  # 导入模块
import time


# 定义引脚， 频率:50
qwe_15 = PWM(Pin(15))       
qwe_15.freq(50)

qwe_2 = PWM(Pin(2))       
qwe_2.freq(50)

qwe_13 = PWM(Pin(13))       
qwe_13.freq(50)

# 定义函数
def duoji_1(you):              # 舵机1
    qwe_15.duty_u16(you)
    time.sleep(0.1)            # 调整速度
def duoji_2(pu):
    qwe_2.duty_u16(pu)
    time.sleep(0.1)
def duoji_3(bt):
    qwe_13.duty_u16(bt)
    time.sleep(0.1)
#      0°    90°  180°
li = [1635, 4915, 8192]   

#rmv = 4915 #int(input("请输入1635 4915 8192:"))
# 定义类
class duoji_a:                 # 一号舵机 类
    rm = 4915
    rmv = None
    rmv_1= None
    def xunhuan_1(self):       # 定义成员方法
        while self.rm <= self.rmv: # rm大于等于8192循环条件结束
            duoji_1(self.rm)
            print(f"==>.{self.rm}") 
            self.rm += 100     # 调整每次循环角度加rm

    def xunhuan_2(self):
        while self.rm > self.rmv_1:
            duoji_1(self.rm)
            print(f"<==.{self.rm}")
            self.rm -= 100
    
    def xunhuan_0(self):       # 舵机复位
        duoji_1(4915)
        
class duoji_b:                 # 二号舵机 类
    rm = 4915
    rmv = None
    rmv_2 = None
    def xunhuan_a(self):
        while self.rm <= self.rmv:
            duoji_2(self.rm)
            print(f"==>.{self.rm}")
            self.rm += 100 

    def xunhuan_b(self):
        while self.rm > rmv_2:
            duoji_2(self.rm)
            print(f"<==.{self.rm}")
            self.rm -= 100
    
    def xunhuan_c(self):
        duoji_2(4915)
        
class duoji_c:                 # 三号舵机 类
    rm = 4915
    rmv = None
    rmv_3 = None
    def xunhuan_l(self):
        while self.rm <= self.rmv:
            duoji_3(self.rm)
            print(f"==>.{self.rm}")
            self.rm += 100 

    def xunhuan_ll(self):
        while self.rm > rmv_2:
            duoji_3(self.rm)
            print(f"<==.{self.rm}")
            self.rm -= 100
    
    def xunhuan_lll(self):
        duoji_3(4915)

up = duoji_a()        
erhao_2 = duoji_b()         
san_hao = duoji_c()        

a = "a"
b = "b"
c = "c"
# 字典
zidian = [{
    'a':"a",
    'b':"b",
    'c':"c"
    }]
ab = str(input("请输入舵机1 a/b/c:"))  # 输入1号指定参数
af = str(input("请输入舵机2 a/b/c:"))  # 输入2号指定位置
sh = str(input("请输入舵机2 a/b/c:"))  # 输入3号指定位置

def pd(v):                            # 判断舵机调整位置
    for zi_dian1 in zidian:
        if v == zi_dian1['a']:
            up.rmv = int(input("请输入4915<a："))
            up.xunhuan_1()
        elif v == zi_dian1['b']:
            up.rmv_1 = int(input("请输入4915>b："))
            up.xunhuan_2()
        elif v == zi_dian1['c']:
            up.xunhuan_0()
        else:
            print("您输入的不是a/b/c")

def cs(e):
    for zi_dian2 in zidian:
        if e == zi_dian2['a']:
            erhao_2.rmv = int(input("请输入4915<a："))
            erhao_2.xunhuan_a()
        elif e == zi_dian2['b']:
            erhao_2.rmv_2 = int(input("请输入4915>b："))
            erhao_2.xunhuan_b()
        elif e == zi_dian2['c']:
            erhao_2.xunhuan_c()
        else:
            print("您输入的不是a/b/c")
            
def shh(m):
    for zi_dian3 in zidian:
        if m == zi_dian3['a']:
            san_hao.rmv = int(input("请输入4915<a："))
            san_hao.xunhuan_l()
        elif m == zi_dian3['b']:
            san_hao.rmv_3 = int(input("请输入4915>b："))
            san_hao.xunhuan_ll()
        elif m == zi_dian3['c']:
            san_hao.xunhuan_lll
        else:
            print("您输入的不是a/b/c")
            

pd(ab)
cs(af)
shh(sh)




