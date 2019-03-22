from pylib.sc_util import *
from pylib.gp_util import *
from pylib.hgp import *

#%%
globals().update(load_data("jordan_ok/"))

#%%
GlobalStat.reset()
creator_init()
phase_init()

#%%
def eval_f(value):
    print("end", end=" ")
    for i in range(3):
        time.sleep(0.5)
        print(i, end=" ")
    # return value ** 2
    return len(value)
    # return eval_simple_tree(value)


#%%
print("start")

while True:
    working(eval_f)
