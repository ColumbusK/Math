import matplotlib.pyplot as plt
import numpy as np
import random as r
from decimal import Decimal
import time

# sigmoid函数 y = 1/1+e^-(b+wx)

arr = np.arange(-10, 10, dtype=np.float16)

def linear(x, w=2, b=10):
    return w*x+b


def sig(linear, c=10):
    res = c*1/(1+np.e**-linear)
    # Decimal控制小数位数，限制计算量
    # res = Decimal(res).quantize(Decimal("0.000000001"), rounding="ROUND_HALF_UP")
    return float(res)


# lis = [linear(x) for x in arr]
# print(lis)

# sigs = [sig(x) for x in lis]
# print(sigs)

# plt.plot(arr, lis, "r-")
# plt.plot(arr, sigs, "b--")


# 随机生成参数拟合sigmoid
def arg_w(s, e):
    """随机产生w参数"""
    return r.randint(s, e)
    
    
def arg_b(s, e):
    """随机产生bias"""
    return r.randint(s, e)


def arg_c(s, e):
    return r.randint(s, e)


# 计时装饰器
def timer(func):
    def wrapper(*args):
        start = time.time()
        res = func(*args)
        end = time.time()
        print(">>>: 运行时间{:.2f}秒".format(end-start))
        return res
    return wrapper



arr = np.arange(-10, 10, dtype=np.int8)


def sigs_sum(d2):
    arr = np.array(d2, dtype=np.float16)
    return np.sum(arr, axis=0)
    

@timer
def draw_sig(s, e, t):
    sig_ls = []
    for i in range(t):
        w = arg_w(s, e)
        b = arg_b(s, e)
        c = arg_c(s, e)
        lis = [linear(x, w=w, b=b) for x in arr]
        sigs = [sig(x, c=c) for x in lis]
        print(i, sigs)
        sig_ls.append(sigs)
        plt.plot(arr, sigs, 'r--')
    
    sig_sum = sigs_sum(sig_ls)
    plt.plot(arr, sig_sum, 'b-')
    plt.show()
    return sig_ls
    

ls = draw_sig(-10, 10, 10)
print(ls)


plt.show()
plt.close()