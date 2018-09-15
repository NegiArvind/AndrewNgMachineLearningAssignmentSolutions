import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt('ex1data1.txt', delimiter=',')
print(data)
x, y = data[:, 0], data[:, 1]  # first column(0 index) data will be stored into x and second
# one into y
print(x)
print(y)
m = x.size


def computeCost(x, y, theta):
    m = x.size
    hypothesis = np.dot(x, theta)  # multiply two matrix
    # print(hypothesis)
    res = np.power(np.subtract(hypothesis, y), 2)
    # print(res)
    result = np.sum(res) / (2 * m)
    return result

def gradientDescent(x,y,theta,alpha,iteration):

    m=y.shape[0] # size of y array

    # In numpy array are passed using references
    theta1=theta.copy() # copying theta into theta1

    cost_history=[]
    for i in range(iteration):
        hypothesis=np.dot(x,theta1)
        subResult=np.subtract(hypothesis,y)
        gdPart=[]
        for j in range(theta1.size):
            # x[:,j] is used to multiply result with a particular column
            res= np.sum(np.dot(subResult, x[:,j]))
            result=res*alpha/m
            gdPart.append(result)

        theta1=np.subtract(theta1,np.array(gdPart))
        cost_history.append(computeCost(x,y,theta1))

    return theta1,cost_history


def drawGraph(x, y):
    plt.title("Food Truck Data profit Graph")
    plt.xlabel("population of city in 10,000s")
    plt.ylabel("profit in $ 10,000")
    plt.plot(x, y, 'ro', mec="k")  # mec circle edge color


# The numpy function stack joins arrays along a given axis.
x = np.stack([np.ones(m), x], axis=1)  # axis=0 for row and axis=1 for column
print(x)

cost = computeCost(x, y, np.array([-1, 2]))  # here 0.0 is theta1 and 0.0 is theta2
print("Cost= %.2f" % cost)  # precision upto 2

# initialize fitting parameters
theta = np.zeros(2) # initializing theta array with zeros

# some gradient descent settings
iterations = 1500
alpha = 0.01

theta, j_history = gradientDescent(x,y, theta, alpha, iterations)
print(j_history)

print('Theta found by gradient descent: {:.4f}, {:.4f}'.format(*theta))

print('Expected theta values (approximately): [-3.6303, 1.1664]')

drawGraph(x[:,1],y)
plt.plot(x[:,1],np.dot(x,theta),'-') # it will plot hypothesis line
plt.legend(['Training data', 'Linear regression'])
plt.show()
