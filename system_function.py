from math import exp, modf
class System_function():
    def __init__(self, settings, r):
        self.settings = settings
        self.r = r

    def white_noise(self):
        A = self.settings.A
        M = self.settings.M
        for k in range(1, 252):
            kasi = 0

    def response(self, u):
        Np = self.settings.Np
        T0 = self.settings.T0
        T1 = self.settings.T1
        T2 = self.settings.T2
        K = self.settings.K
        k1 = K / T0 / T1
        c = []
        y = []
        for k in range(2, Np * (self.r +1)):
            c[k] = exp(-T0/T1) * c[k-1] + T1 * k1 * (1 - exp(-T0/T1)) * u[k-1]
            + T1 * k1 * (T1 * (exp(-T0/T1)-1)+T0) * (u[k]-u[k-1])/T0
            y[k] = exp(-T0 / T2) * y[k - 1] + T2 * (1 - exp(-T0 / T2)) * c[k - 1]
            + T1 * (T2 * (exp(-T0 / T2) - 1) + T0) * (c[k] - c[k - 1]) / T0
        return y

    def m_sequence(self):
        a = self.settings.a
        p = self.settings.p
        m = self.settings.m
        u = []
        for k in range(1, 252):
            m[0] = m[1] + m[2]
            if m[0] == 2:
                m[0] == 0
            for j in range(p, -1, 0):
                m[j] = m[j-1]
            if m[0] == 0:
                u[k] = a
            if m[0] == 1:
                u[k] = -a
        return u





