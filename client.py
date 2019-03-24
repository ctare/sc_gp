from pylib.sc_util import *
import time
from tqdm import tqdm

#%%
def eval_f(value):
    # print("end", end=" ")
    for i in tqdm(range(10)):
        time.sleep(0.01)
        # print(i, end=" ")
    return len(value)


#%%
print("start")

while True:
    working(eval_f)
