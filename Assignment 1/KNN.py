import numpy as np
from numpy.linalg import norm
class KNearestNeighbor(object):
    
    def __init__self(self):
        pass
    
    def train(self, X_train, Y_train,k):
        
        self.X = X_train
        self.Y = Y_train
        self.K = k
        
    def euclidean_distance(self, d1, d2):
        # measuring euclidean distance
        return norm(d1-d2)
    
    def closest_neighbor(self, x1, k=1):
        
        best_distance = self.euclidean_distance(x1, self.X[0])
        best_index = 0
        
        for i in range(self.K, len(self.X)):
            distance = self.euclidean_distance(x1, self.X[i])
            
            if distance < best_distance:
                best_distance = distance
                best_index = i
        return self.Y[best_index]
        
        
    
    def predict(self, X_test,k=1):
        
        y_predict = []
        
        for img in X_test:
            label = self.closest_neighbor(img,k)
            y_predict.append(label)
        return y_predict