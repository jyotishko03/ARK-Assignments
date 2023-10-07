import numpy as np
import matplotlib.pyplot as plt

scan = np.loadtxt('laserscan.dat') #distances in a numpy array
angle = np.linspace(-np.pi/2, np.pi/2, np.shape(scan)[0], endpoint='true') #angles wrt laser finder



def T(Q, x, y):
    return np.array([[np.cos(Q),-np.sin(Q),x], [np.sin(Q),np.cos(Q), y], [0,0,1]])

def p(x,y):
    return np.array([[x],[y],[1]])

T_A=T(np.pi/4,1,0.5) #pose of robot wrt global
T_B=T(np.pi,0.2,0) #pose of laser wrt robot

#co-ords of points wrt laser
x_l=[]
y_l=[]

for i in range(len(scan)):
    x_l.append(scan*np.cos(angle))
    y_l.append(scan*np.sin(angle))

plt.scatter(x_l,y_l)
plt.show()

T_net=np.matmul(T_A,T_B) #to get global co-ords by multiplying with T_net

#to store global points
x_g=[]
y_g=[]

for j in range(len(x_l)):
    pose_g=np.matmul(T_net, p(x_l[j], y_l[j]))
    x_g.append(pose_g[0][0])
    y_g.append(pose_g[1][0])

pose_l_g=np.matmul(T_A,p(0.2,0)) #global position of laser


#plotting the points finally
plt.scatter(x_g,y_g, color='black', s=5, marker='.')
plt.scatter(1,0.5, color='blue', s=50, marker='s') #postion of robot
plt.scatter(pose_l_g[0][0],pose_l_g[1][0], color='red', s=10)
plt.show()