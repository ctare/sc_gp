from pylib.sc_util import *

#%%
def eval_f(value):
    print("end", end=" ")
    for i in range(3):
        time.sleep(1)
        print(i, end=" ")
    return len(value)


#%%
print("start")

while True:
    working(eval_f)
