import numpy as np

np.random.seed(0) # псевдослучайные числа образуют одну и ту же последовательность (при каждом запуске)
x = np.arange(-1.0, 1.0, 0.1) # аргумент [-1; 1] с шагом 0,1


model_a = lambda xx, ww: (ww[0] + ww[1] * xx) # модель
Y = -5.2 + 0.7 * x + np.random.normal(0, 0.1, len(x))

X = (np.vstack((np.ones(len(x)), x))).T

w = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(Y))

print(w[0])