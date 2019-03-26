from pylib.sc_util import *
import time
from tqdm import tqdm
import json

#%%
def eval_f(value):
    # print("end", end=" ")
    data = json.loads(value)
    string = data["string"]
    phase = data["phase"]
    print("phase", phase)
    for i in tqdm(range(10)):
        time.sleep(0.01)
        # print(i, end=" ")
    # return len(string)
    return int(string) + 1


#%%
print("start")

while True:
    working(eval_f)
