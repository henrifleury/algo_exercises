class MyLineReg:
    def __init__(self, n_iter=10, learning_rate=0.5, weights=None):
        self.n_iter = n_iter
        self.learning_rate = learning_rate
        self.weights = weights
    def __str__(self):
        return f"MyLineReg class: n_iter={self.n_iter}, learning_rate={self.learning_rate}"
    def fit(self, X, y, verbose=False):
        X=


print(MyLineReg())