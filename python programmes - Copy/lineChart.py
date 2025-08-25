import matplotlib.pyplot as plt
x=[0,10,15,20,25,30,35, 40]
y1=[10,15,20,25,30,15,0]
y2=[10,12,16,12,2,10,0]
plt.plot(x,y1,linestyle="dashed",marker='D')
plt.plot(x,y2,linestyle="dashed",marker='D')
plt.title('velocity-Time Graph')
plt.xlabel('Time(s)')
plt.ylabel('Velocity m/s')
plt.xlim(10,35)
plt.ylim(10,35)

plt.show()