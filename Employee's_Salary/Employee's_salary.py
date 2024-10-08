import numpy as np
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from perceptron import Perceptron

X,Y,coef = make_regression(n_samples=50, n_features=1, n_informative=1, noise=10, coef=True, random_state=1)

Y=Y.reshape(-1,1)


X = np.interp(X, (X.min(), X.max()), (0, 20))
Y = np.interp(Y, (Y.min(), Y.max()), (20000, 150000))

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)

#Training
W=np.random.rand(1,1)
b=np.random.rand(1,1)

lr_W=0.0001
lr_b=0.1
epochs=50
perceptron=Perceptron(W,b,lr_W,lr_b,epochs)
perceptron.fit(X_train,Y_train)

#Predict_with X_test
print(perceptron.predict(X_test))
print(Y_test)

#Evaluate
MSE=perceptron.evaluate(X_test,Y_test)
print(MSE)