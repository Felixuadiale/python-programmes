import matplotlib.pyplot as plt
x=[0,5,10,15,20,25,30]
y1=[10,15,20,25,30,15,0]
y2=[10,12,16,12,2,10,0]
plt.plot(x,y1,linestyle="dashed",marker='D')
plt.plot(x,y2,linestyle="dashed",marker='D')
plt.title('velocity-Time Graph')
plt.xlabel('velocity m/s')
plt.ylabel('Time(s)')
plt.xlim(5,25)
plt.ylim(5,25)

plt.show()