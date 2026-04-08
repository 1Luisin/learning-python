import random 

class Perceptron:

    def __init__(self):
        self.weights = [random.uniform(-1,1), random.uniform(-1,1)]            

    def guess(self, inputs):
        total = sum(inputs[i] * self.weights[i] for i in range(len(self.weights)))
        return self._sign(total)
    
    def _sign(self,num):
        return 1 if num >= 0 else -1