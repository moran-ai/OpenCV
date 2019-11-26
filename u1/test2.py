# 实例1
# import numpy as np
# a = np.arange(24)
# # a只有一个维度
# print(a)
# print(a.ndim)
# # 调整大小
# # b有三个维度
# b = a.reshape(3,4,2)
# print(b.ndim)
#
# # 实例2
# import numpy as np
#
# a = np.array([[1, 2, 3],[4, 5, 6]])
# print(a.shape)
# print(a.itemsize)
# print(a.size)
# print(a.dtype)

# 实例3
import numpy as np

x = np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)

y = np.array([1,2,3,4,5],dtype=np.float64)
print(y.itemsize)  # 字节
print(y.shape)  # 维度
print(y.ndim)  # 维度的数量

