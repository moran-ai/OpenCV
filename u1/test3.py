# 实例6
import numpy as np

# 默认浮点数
x = np.ones(5)
print(x)
print(x.dtype)

# 自定义类型
x = np.ones([2,2], dtype=int)
print(x)

# 实列7
import numpy as np

# 默认为浮点数
x = np.zeros(5)
print(x)

# 设置类型为整数
y = np.zeros((5,),dtype=int)
print(y)

# 自定义类型
z = np.zeros((2,2),dtype=[("x","i4"),("y","i4")])
print(z)
