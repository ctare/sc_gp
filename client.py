from pylib.sc_util import *
from pylib.gp_util import *
from pylib.hgp import *
import json

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

#%%
load_data("jordan_ok/")

#%%
GlobalStat.reset()
creator_init()
phase_init()

#%%
def eval_f(value):
    # print("end", end=" ")
    # for i in range(3):
    #     time.sleep(0.01)
    #     print(i, end=" ")
    # # return value ** 2
    # return -len(value)
    print("learning...   model size ->", len(value))
    data = json.loads(value)
    tree = data["tree"]
    penalty = data["penalty"]
    loss_v = eval_simple_tree(tree)
    return float(np.mean(loss_v[-5:])) * penalty


#%%
print("start")

while True:
    working(eval_f)
