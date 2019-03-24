from pylib.sc_util import *
import time

#%%
def eval_f(value):
    print("end", end=" ")
    for i in range(3):
        time.sleep(10)
        print(i, end=" ")
    return len(value)


#%%
print("start")

while True:
    working(eval_f)
