from math import exp, modf, sqrt
import numpy
import matplotlib.pyplot as plt

class System_function():
    def __init__(self, settings):
        self.settings = settings

    def white_noise(self, lamb):
        A = self.settings.A
        M = self.settings.M
        x0 = self.settings.x0
        v = []
        for k in range(1, 253):
            sigma = 0
            for i in range(12):
                x1 = modf((A * x0), M)
                sigma = sigma + x1
                x0 = x1
            v[k] = lamb * (sigma - 6)
        return v

    def response(self, u):
        T0 = self.settings.T0
        T1 = self.settings.T1
        T2 = self.settings.T2
        K = self.settings.K
        k1 = K / T0 / T1
        e1 = exp(-T0 / T1)
        e2 = exp(-T0 / T2)
        c = []
        y = []
        for k in range(1, 253):
            c[k] = e1 * c[k-1] + T1 * k1 * (1 - e1) * u[k-1]
            + T1 * k1 * (T1 * (e1 - 1)+T0) * (u[k]-u[k-1])/T0
            y[k] = e2 * y[k - 1] + T2 * (1 - e2) * c[k - 1]
            + T1 * (T2 * (e2 - 1) + T0) * (c[k] - c[k - 1]) / T0
        return y

    def m_sequence(self):
        a = self.settings.a
        p = self.settings.p
        m = self.settings.m
        u = []
        for k in range(1, 253):
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

    def co_fuction(self, r, u, z):
        Np = self.settings.Np
        R_mz = []
        for k in range(1,Np+1):
            for i in range(Np+1, (r+1)*Np+1):
                s = s + u[i-k] * z[i]
            R_mz[k] = s/Np/r
        return R_mz

    def guji(self, R_mz):
        Np = self.settings.Np
        a = self.settings.a
        delta = self.settings.delta
        c = -R_mz[Np-1]
        xishu = Np/((Np+1)*a^2*delta)
        g = []
        for k in range(1, Np+1):
            g[k] = xishu * [R_mz[k] + c]
        return g

    def lilunzhi(self):
        K = self.settings.K
        T1 = self.settings.K1
        T2 = self.settings.T2
        Np = self.settings.Np
        delta = self.settings.delta
        xishu = K/(T1 - T2)
        g0 = []
        for k in range(1, Np+1):
            g0[k] = xishu*(exp(-k*delta/T1)-exp(-k*delta/T2))
        return g0

    def guji_error(self, g, g0):
        Np = self.settings.Np
        for i in range(1, Np+1):
            e = g0[i] - g[i]
            err = err + pow(e, e)
            s = s + g0[i]
        error = sqrt(err/s)
        return error

    def fangcha(self, data):
        fangcha = numpy.var(data)
        return fangcha















