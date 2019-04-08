from pylib.sc_util import *
from pylib.gp_util import *
from pylib.hgp import *
import json

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import time

#%%
load_data("jordan_ok/")

#%%
GlobalStat.reset()
creator_init()
phase_init()

#%%
evcnt = 0
def eval_f(value):
    global evcnt
    evcnt += 1
    print("learning...   model size ->", len(value))
    data = json.loads(value)
    tree = data["tree"]
    penalty = data["penalty"]

    # with open("/root/share/tree_test.txt", "w") as f:
    #     f.write(json.dumps(tree))
    # individual = creator.Individual(parse_simple_tree(tree, GlobalStat.pset, GlobalStat.phase))
    # edges, nodes, labels = get_graph(individual, GlobalStat.pset)
    # g = nx.MultiDiGraph()
    # for i, node in enumerate(nodes):
    #     # nodes[i] = (node, {"label": labels[node]})
    #     if type(labels[node]) == tuple:
    #         name, v = labels[node]
    #         nodes[i] = (node, {"label": name, **v})
    #     else:
    #         nodes[i] = (node, {"label": labels[node]})
    #
    # g.add_nodes_from(nodes)
    # g.add_edges_from(edges)
    #
    # agraph = nx.nx_agraph.to_agraph(g)
    # # agraph.node_attr["shape"] = "circle"
    # agraph.node_attr["fontsize"] = "20"
    # agraph.draw(f"/root/share/tree_{evcnt}.png", prog="dot", format="png")

    # try:
    start_time = time.time()
    # loss_v = eval_simple_tree(tree)
    individual = creator.Individual(parse_simple_tree(tree, GlobalStat.pset, GlobalStat.phase))
    loss_v = [len(str(individual))] * 5
    end_time = time.time()
    with open("/root/share/learning_time.txt", "a") as f:
        f.write(str(end_time - start_time) + "\n")

    with open("/root/share/timestamp.txt", "a") as f:
        f.write(str(start_time) + "\n")
    # except:
    #     print("exception!!!!")
    #     loss_v = [1000] * 5

    print("loss", float(np.mean(loss_v[-5:])), "penalty", penalty)
    return float(np.mean(loss_v[-5:])) * penalty


#%%
print("start")

while True:
    working(eval_f)
