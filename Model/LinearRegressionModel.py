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
    dj_dw = np.zeros((self.n,))
    dj_db = 0.

    errors = np.dot(X, w) + b - y  # Calculate errors for all samples
    dj_dw = np.dot(errors, X)      # Calculate gradient for weights
    dj_db = np.sum(errors)         # Calculate gradient for bias             
    dj_dw = dj_dw / self.m                                
    dj_db = dj_db / self.m                                
        
    return dj_db, dj_dw
  
  def fit(self, X, y): 
    
    self.m,self.n = X.shape
    w = np.zeros(self.n)  #avoid modifying global w within function
    b = 0.
    for i in range(self.max_iter):

      # Calculate the gradient and update the parameters
      dj_db,dj_dw = self.compute_gradient(X, y, w, b)   

      # Update Parameters using w, b, alpha and gradient
      w -= self.alpha * dj_dw              
      b -= self.alpha * dj_db            
    
    self.weight = w # final w
    self.bais = b # final b

  def predict(self,x): 
    p = np.dot(x, self.weight) + self.bais     
    return p