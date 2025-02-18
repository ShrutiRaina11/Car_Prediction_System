import numpy as np
class MyModel:
  
  def __init__(self,alpha=0.001,max_iter=10000) -> None:
    self.alpha = alpha
    self.max_iter = max_iter
    self.m = 0
    self.n = 0
    self.weight = np.array([])
    self.bais = 0.

  def compute_gradient(self,X, y, w, b): 
    dz = np.dot(w,X) + b - y           # Calculate derivative for all samples
    dw = np.dot(dz,X.T)  / self.m     # Calculate gradient for weights
    db = np.sum(dz)   / self.m       # Calculate gradient for bias                                             
    return db, dw
  
  def fit(self, X, y):     
    X = X.T
    self.n,self.m = X.shape
    w = np.zeros((1,self.n))  #avoid modifying global w within function
    b = 0. #avoid modifying global b within function
    for i in range(self.max_iter):
      # Calculate the gradient and update the parameters
      db,dw = self.compute_gradient(X, y, w, b)   
      # Update Parameters using w, b, alpha and gradient
      w -= self.alpha * dw              
      b -= self.alpha * db                
    self.weight = w # final w
    self.bais = b # final b

  def predict(self,X): 
    X = X.T
    p = np.dot(self.weight, X) + self.bais     
    return p