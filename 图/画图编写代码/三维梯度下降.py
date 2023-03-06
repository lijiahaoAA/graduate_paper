# coding=gbk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

#f(w1,w2) = w1^2 + w2^2 + 2*w1*w2 + 500
def targetFunction(W): #Ŀ�꺯��
 w1,w2 = W
 return w1 ** 2 + w2**2 + 2*w1*w2+500

def gradientFunction(W): #�ݶȺ������ֱ��w1,w2��ƫ��
 w1,w2 = W
 w1_grad = 2*w1+2*w2
 w2_grad = 2*w2 + 2*w1
 return np.array([w1_grad,w2_grad])

def batch_gradient_distance(targetFunc,gradientFunc,init_W,learning_rate = 0.01,tolerance = 0.0000001): #�����㷨
 W = init_W
 target_value = targetFunc(W)
 counts = 0 #���ڼ������
 while counts<5000:
  gradient = gradientFunc(W)
  next_W = W-gradient*learning_rate
  next_target_value = targetFunc(next_W)
  if abs(next_target_value-target_value) <tolerance:
   print("�˽��������", counts, "��ѭ��")
   return next_W
  else:
   W,target_value = next_W,next_target_value
   counts += 1



if __name__ == '__main__':
 np.random.seed(0) #��֤ÿ��������������Ľ��һ��
 init_W = np.array([np.random.random(),np.random.random()]) #�����ʼ��w1,w2
 w1,w2 = batch_gradient_distance(targetFunction,gradientFunction,init_W)
 print(w1,w2)
 #��ͼ
 x1=np.arange(-10,11,1) #Ϊ�˻��ƺ�����ԭͼ��
 x2=np.arange(-10,11,1)

 x1, x2 = np.meshgrid(x1, x2) # meshgrid :3D����ϵ

 z=x1**2 + x2**2 + 2*x1*x2+500

 fig = plt.figure()
 ax = Axes3D(fig)
 ax.plot_surface(x1, x2, z) #����3D����ϵ�еĺ���ͼ��
 ax.scatter(w1,w2, targetFunction([w1,w2]), s=50, c='red') #�����Ѿ��ҵ��ļ�ֵ��
 ax.legend() #ʹ����ϵΪ����״

 plt.show() #��ʾ