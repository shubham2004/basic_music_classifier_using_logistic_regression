#this code is for catagorizing song into sad song or party song using its tempo and beats as per training dataset provoded by tainner code
import math
s1=0
s2=0
s0=0
al=100
#here x1(tempo) and x2(beats/sec) are traing set taken using tempo and beat extraction code
x1=[103.36,129.2,152,161.5,103.36,161.5,161.5,107.67,123.05,198.77,143.55,80.75,136,152,89.1,152,129.2,123.05,136,107.67,129.2,89.1,99.38,68,123.05,61.52,129.2,95.7,129.2]
avgx1=sum(x1)/len(x1)
difx1=max(x1)-min(x1)
for i in range (len(x1)):#normalizing training set
    x1[i]=(x1[i]-avgx1)/(max(x1)-min(x1))
x2=[201,196,216,201,159,246,153,208,197,191,180,199,145,142,106,93,124,139,127,124,130,136,114,131,89,129,143,104,136]
avgx2=sum(x2)/len(x2)
difx2=max(x2)-min(x2)
for i in range (len(x2)):# normalizing training set
    x2[i]=(x2[i]-avgx2)/(max(x2)-min(x2))
#traing example result here 0 is sad song 1 is party song
y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]#traing example result here 0 is sad song 1 is party song
#initializing weights
q0=1
q1=1
q2=1
#traing logicistic model to get weights to fit in data
for i in range(10000):
    for j in range(len(x1)):
        y1=q0+q2*x2[j]
        y1=1/(1+math.exp(-y1))#sigmoid function
        d0=(y1-y[j])
        d1=(y1-y[j])*x1[j]
        d2=(y1-y[j])*x2[j]
    q0=q0-al*d0
    q1=q1-al*d1
    q2=q2-al*d2
#printing weights
print(q0)
print(q1)
print(q2)
while(True):
    t=float(input('tempo  '))
    b=float(input('beats  '))
    #give input of new song's tempo and beats it will give output of the song type
    ans=q0+q1*(t)+q2*(b)
    print(ans)
    ans=1/(1+(math.exp(-ans)))
    ans=round(ans)#roungind off
    print(ans)
    if ans==1:
        print('its a party song')
    if ans==0:
        print('its a sad song')
