import sys 
import os
import random 
import math

def make_temp(unit=None):
    if unit is None:
        unit = random.choice('CKF')
    K = random.uniform(0, 1000)
    if unit == 'C':
        return K - 273.15, unit
    elif unit == 'F':
        return (K-273.15) * 9/5 + 32, unit
    return K, unit

def make_temp_input(easy=False):
    e = random.randint(3, 5)
    N = random.randint(10**(e-1), 10**e)
    u = None
    if easy:
        u = random.choice('CKF')
    yield random.choice('CKF')
    yield str(N)
    for _ in range(N):
        yield ' '.join(map(str, make_temp(u)))
    

if __name__ == "__main__":
    os.makedirs('input', exist_ok=True)
    for i in range(20):
        with open(f'input/{i}.txt', 'w') as f:
            f.writelines((x + '\n' for x in make_temp_input(i < 6)))

