# Gradient descent for linear regression
# y = mx + b
# loss =  (y-yhat)**3 / 2

#Initialise some parameters
import numpy as np

X = np.random.randn(10,1)
y = 2*X+np.random.randn()

#Parameters
w = 0.0
b = 0.0
learning_rate = 0.01

def descent(x, y, w,b,learning_rate):
    dldw = 0
    dldb = 0
    N = X.shape[0]

    for xi, yi in zip(x,y):
        # loss = (y-(wx+b))**2
        dldw += -2*xi*(yi-(w*xi+b))
        dldb += -2*(yi-(w*xi+b))
    # make update
    w = w - learning_rate*(1/N)*dldw
    b = b - learning_rate*(1/N)*dldb
    return w,b

for epochs in range(400):
    w, b  = descent(X,y,w,b,learning_rate)
    yhat = w*X+b
    loss = np.divide(np.sum((y-yhat)**2,axis=0), X.shape[0])
    print(f"epochs:{epochs} loss:{loss} w:{w} b{b}")
print(X)
print(y)