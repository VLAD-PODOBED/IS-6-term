import matplotlib.pyplot as plt
import numpy as np
from rsa import *
from elgamal import *

# -----------------------1-----------------------------
a = 5
prime_nums = get_prime(10**3, 10**5)
X = np.random.choice(prime_nums, 5, replace=False)
n = random.getrandbits(1024)
Y = []
start_time = time.time()
for x in X:
    y = (a ** x) % n
    calculation_time = time.time() - start_time
    Y.append(calculation_time)
    start_time = time.time()
calculation_time = time.time() - start_time
plt.plot(X, Y, '-ro')
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Зависимость времени вычисления от параметров')
plt.show()

#-----------------------2-----------------------------
# message = 'cG9kb2JlZCB2bGFkaXNsYXYgZ2VvcmdpZXZpY2g=' #base64
message = 'podobed vladislav georgievich' #ASCII

print('\n--RSA--')
rsa(message)
print('\n--Эль-Гамаля--')
elgamal(message)