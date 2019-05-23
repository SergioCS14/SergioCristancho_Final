import numpy as np

err = 1

T_g = np.array([73,28,59,52,39,137])

x_0=np.random.uniform(4,80)
y_0=np.random.uniform(5,200)
t_0=0
v_0=np.random.uniform(0.1,0.5)

def model(x,y,t,v):
    d1 = np.sqrt((x-4)**2+(y-100)**2)
    d2 = np.sqrt((x-10)**2+(y-5)**2)
    d3 = np.sqrt((x-12)**2+(y-80)**2)
    d4 = np.sqrt((x-80)**2+(y-50)**2)
    d5 = np.sqrt((x-50)**2+(y-50)**2)
    d6 = np.sqrt((x-40)**2+(y-200)**2)
    return v*np.array([d1,d2,d3,d4,d5,d6])+t_0

def comp(T):
    return np.dot(T_g-T,T_g-T);

T_0 = model(x_0,y_0,t_0,v_0)

count = 0
while (comp(T_0) > err):
    x_1 = x_0 + np.random.uniform(-1,1)
    y_1 = y_0 + np.random.uniform(-1,1)
    t_1 = t_0 + np.random.uniform(-2,2)
    v_1 = v_0 + np.random.uniform(-0.1,0.1)
    T_1 = model(x_0,y_0,t_0,v_0)
    if comp(T_1) < comp(T_0):
        x_0 = x_1
        y_0 = y_1
        t_0 = t_1
        v_0 = v_1
    count = count + 1
    if count == 10000:
        break

print("coordenada x: ",x_0," +/- ",1)
print("coordenada y: ",y_0," +/- ",1)
print("tiempo lanzamiento: ",t_0," +/- ",2)
print("velocidad del sonido: ", v_0, " +/- ",0.01)
#print(T_0,comp(T_0))
    