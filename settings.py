class Settings():
    #存储初始化数值的类
    def __init__(self):
        self.m = [0, 1, 0, 1, 1, 0]
        self.Np = 2^6 - 1
        self.a = 1
        self.p = 6
        self.K = 120
        self.T1 = 8.3
        self.T2 = 6.2
        self.T0 = 1
        #self.K1 = (self.K / self.T1 / self.T2)
        self.M = 32768
        self.A = 179
        self.x0 = 11