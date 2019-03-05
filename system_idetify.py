from system_function import System_function
from math import sqrt

r = input("请输入周期")
lamb = input("请输入噪声标准差，0.0/0.1/0.5")
sf = System_function()
u = sf.m_sequence()
v = sf.white_noise(lamb)
y = sf.response(u)
z = v + y
R_mz = sf.co_fuction(r, u, z)
gujizhi = sf.guji(R_mz)
lilunzhi = sf.lilunzhi()
error = sf.guji_error(gujizhi, lilunzhi)
ov = sf.fangcha(v)
oy = sf.fangcha(y)
yita = sqrt(oy/ov)