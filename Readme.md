# Assignment 46
### Machine Learning
## Perceptron (Perception Neuron)


+ In this project we try to analyze three dataset with perceptron.


# _1- Employee's Salary_

In first problem I used make_regression to produce a dataset for Employee's salary.
After creating this dataset ,I could predict the salary from the given experience, because the relation between salary and experience is linear.

I write a perceptron class in the next step to use it for predicting salary from experience.

I also change the hyperparameter of perceptron class to fit the est line on my dataset.
I draw two diagram, one for data and the line that trough all data and other for loss.

I used MAE method to find loss in this problem.


learning rate Wieght= 0.0001      learning rate Bias= 0.1        epochs=4

<img src="Employee's_Salary\Evaluate.png" width="550">


learning rate Wieght= 0.0001      learning rate Bias= 0.1        epochs=25

<img src="Employee's_Salary\End_of_Train.png" width="550">




## How to Install
Run following commend :
```
pip install -r requirments.txt
```


## How to Run
execute this command in terminal:
Run following command :
```
python Employee's_salary.py
```
-----------------------------------------

# 2- Abalone 


* Abalone dataset is the second dataset that I used it to test my perceptron algorithm.
you can access this dataset from below link:

https://www.kaggle.com/datasets/rodolfomendes/abalone-dataset

LEFT diagram is shown abalone length and height data and the line that I find by using perceptron.
Right diagram is shown loss value that is claculated in each epochs wth MAE method.


learning rate Wieght= 0.001      learning rate Bias= 0.1        epochs=4

<img src="Abalone\start_of_train.png" width="550">


learning rate Wieght= 0.1      learning rate Bias= 0.1        epochs=25

<img src="Abalone\End_of_train.png" width="550">

## How to Install
Run following commend :
```
pip install -r requirments.txt
```

## How to Run
execute this command in terminal:
Run following command :
```
python abalone.py
```
-----------------------------------------

# 3- Boston House Price


+ In the third problem I survey the Boston house price again, but this time I use perceptron.
you can access this dataset from below link:

https://www.kaggle.com/datasets/vikrishnan/boston-house-prices

I find two features that are most related to price of houses and use them to create X_train and used price to create Y_train.

I fit train data to my perceptron algorithm and I also set hyperparameter, then I found out that below value are best for hyperparameter:
learning rate Wieght= 0.0001
learning rate Bias= 0.1
epochs=30




3D animation of Boston house price and the best plane that fit on these data.

learning rate Wieght= 0.0001      learning rate Bias= 0.1        epochs=30

I show from first step that perceptron started to run to final step that perceptron find the best plane that trough all data.
another 3D animation of the best plane that perceptron could find in 30 epochs.

![movie](Boston_House_Prices\boston_y_pred.gif)

-----------------------------------------

