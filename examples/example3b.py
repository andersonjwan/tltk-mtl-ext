import sys
import os
import tltk_mtl as MTL
import tltk_mtl_ext as MTLE
import numpy as np
import time

import matplotlib.pyplot as plt

list_range = (2**i for i in range(10,15))

mode = 'cpu_threaded'

x_length = []
y_time = []

for i in list_range:
    Ar3 = -1
    br3 = -160

    Ar4 = 1
    br4 = 4500

    preds = {}
    preds['data1'] = MTL.Predicate('data1',Ar3,br3)

    traces = {'data1': np.ones(i,dtype=np.float32)*5}
    time_stamps = np.arange(1, i + 1,dtype=np.float32)

    root = MTLE.parse_mtl('!(F_ts:(0, inf) data1)', preds, mode)

    t0 = time.time()
    root.eval_interval(traces, time_stamps)
    t1 = time.time()

    x_length.append(i)
    y_time.append(t1-t0)

    print("TLTk" ,"| phi_b1","| Mode:" ,mode,'\t| Samples:', "{:,}".format(i), '\t| Time: ', '%.4f'%(t1 - t0), '    \t| robustness', root.robustness)
    del traces
    del time_stamps

fig = plt.scatter(x_length, y_time)
plt.xlabel('Trace Length')
plt.ylabel('Computation Time')
plt.savefig('phi_1b.pdf')
