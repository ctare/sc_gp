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
evcnt = 0
def eval_f(value):
    global evcnt
    evcnt += 1
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

    print("loss_v", loss_v)
    individual = creator.Individual(parse_simple_tree(tree, GlobalStat.pset, GlobalStat.phase))
    edges, nodes, labels = get_graph(individual, GlobalStat.pset)
    g = nx.MultiDiGraph()
    for i, node in enumerate(nodes):
        # nodes[i] = (node, {"label": labels[node]})
        if type(labels[node]) == tuple:
            name, v = labels[node]
            nodes[i] = (node, {"label": name, **v})
        else:
            nodes[i] = (node, {"label": labels[node]})

    g.add_nodes_from(nodes)
    g.add_edges_from(edges)

    agraph = nx.nx_agraph.to_agraph(g)
    # agraph.node_attr["shape"] = "circle"
    agraph.node_attr["fontsize"] = "20"
    agraph.draw(f"/root/share/tree_{evcnt}.png", prog="dot", format="png")

    print("loss", float(np.mean(loss_v[-5:])), "penalty", penalty)
    return float(np.mean(loss_v[-5:])) * penalty


#%%
print("start")

while True:
    working(eval_f)
