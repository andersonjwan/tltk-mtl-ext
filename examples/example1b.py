import sys
import tltk_mtl as MTL
import tltk_mtl_ext as MTLE
import numpy as np

Ar3 = -1
br3 = -160

Ar4 = 1
br4 = 4500

preds = {}
preds['speed'] = MTL.Predicate('speed', Ar3, br3)
preds['rpm']   = MTL.Predicate('rpm', Ar4, br4)

root = MTLE.parse_mtl('!(F_ts:(0, 100) (speed && rpm))', preds)

traces = {}
traces['speed'] = np.array([10,20,30,40,50], dtype=np.float64)
traces['rpm']   = np.array([10,20,30,40,50], dtype=np.float64)

time_data = np.arange(1, 10, 2, dtype=np.float32)

root.eval_interval(traces, time_data)
print(root.robustness)
