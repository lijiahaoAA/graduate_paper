# coding=gbk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

#f(w1,w2) = w1^2 + w2^2 + 2*w1*w2 + 500
def targetFunction(W): #目标函数
 w1,w2 = W
 return w1 ** 2 + w2**2 + 2*w1*w2+500

def gradientFunction(W): #梯度函数：分别对w1,w2求偏导
 w1,w2 = W
 w1_grad = 2*w1+2*w2
 w2_grad = 2*w2 + 2*w1
 return np.array([w1_grad,w2_grad])

def batch_gradient_distance(targetFunc,gradientFunc,init_W,learning_rate = 0.01,tolerance = 0.0000001): #核心算法
 W = init_W
 target_value = targetFunc(W)
 counts = 0 #用于计算次数
 while counts<5000:
  gradient = gradientFunc(W)
  next_W = W-gradient*learning_rate
  next_target_value = targetFunc(next_W)
  if abs(next_target_value-target_value) <tolerance:
   print("此结果经过了", counts, "次循环")
   return next_W
  else:
   W,target_value = next_W,next_target_value
   counts += 1



if __name__ == '__main__':
 np.random.seed(0) #保证每次运行随机出来的结果一致
 init_W = np.array([np.random.random(),np.random.random()]) #随机初始的w1,w2
 w1,w2 = batch_gradient_distance(targetFunction,gradientFunction,init_W)
 print(w1,w2)
 #画图
 x1=np.arange(-10,11,1) #为了绘制函数的原图像
 x2=np.arange(-10,11,1)

 x1, x2 = np.meshgrid(x1, x2) # meshgrid :3D坐标系

 z=x1**2 + x2**2 + 2*x1*x2+500

 fig = plt.figure()
 ax = Axes3D(fig)
 ax.plot_surface(x1, x2, z) #绘制3D坐标系中的函数图像
 ax.scatter(w1,w2, targetFunction([w1,w2]), s=50, c='red') #绘制已经找到的极值点
 ax.legend() #使坐标系为网格状

 plt.show() #显示