import sys
import os
import tltk_mtl as MTL
import tltk_mtl_ext as MTLE
import numpy as np
import time

mode = 'cpu_threaded'

preds = {}

Ar1 = -1
br1 = -160
preds['data1'] = MTL.Predicate('data1', Ar1, br1, mode)

Ar2 = -1
br2 = -4500
preds['data2'] = MTL.Predicate('data2', Ar2, br2, mode)

# root = F(data1 /\ data2)
root = MTLE.parse_mtl('!(F_ts:(0, inf)(data1 && data2))', preds, mode)

traces = {}
traces['data1'] = np.ones(10, dtype=np.float32) * 5
traces['data2'] = np.ones(10, dtype=np.float32) * 10

time_data = np.arange(1, 10 + 1, dtype=np.float32)

t0 = time.time()
root.eval_interval(traces, time_data)
t1 = time.time()

print("TLTk", "\t | Mode:", mode, '\t| Time: ', '%.4f'%(t1 - t0), '     \t| Robustness:', root.robustness)
