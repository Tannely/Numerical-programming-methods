import math
x = [0.01, 0.06, 0.11, 0.16, 0.21, 0.26]
y = [0.9918, 0.9519, 0.9136, 0.8769, 0.8416, 0.8077]
#x= [0., 0.2, 0.4, 0.6, 0.8, 1.]
#y =[1.2715, 2.4652, 3.6443, 4.8095, 5.9614, 7.1005]
h = x[1]-x[0] #крок 0,05
q1 = (0.027-x[0])/h
q2 = (0.416-x[-1])/h
#q1= (0.1-x[0])/h
#q2= (0.9-x[0-1])/h
def dy(y,j):
    m1=[]
    for i in range(len(y)):
        m1.append(y[i]-y[i-1]) 
    m1.pop(0)   #видалення елементу
    if j ==1:
        return m1
    else:
        j-=1          
        return dy(m1,j) 

yx1 =y[0]+q1*dy(y,1)[0]+q1*(q1-1)*dy(y,2)[0]/math.factorial(2)+q1*(q1-1)*(q1-2)*dy(y,3)[0]/math.factorial(3)+q1*(q1-1)*(q1-2)*(q1-3)*dy(y,4)[0]/math.factorial(4)+q1*(q1-1)*(q1-2)*(q1-3)*(q1-4)*dy(y,5)[0]/math.factorial(5)
print ("Newton's first interpolation formula")
print (yx1)
yx2 =y[5]+q2*dy(y,1)[4]+q2*(q2+1)*dy(y,2)[3]/math.factorial(2)+q2*(q2+1)*(q2+2)*dy(y,3)[2]/math.factorial(3)+q2*(q2+1)*(q2+2)*(q2+3)*dy(y,4)[1]/math.factorial(4)+q2*(q2+1)*(q2+2)*(q2+3)*(q2+4)*dy(y,5)[0]/math.factorial(5)
print ("\n\nNewton's second interpolation formula")
print (yx2)