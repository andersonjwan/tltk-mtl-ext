import sys
import tltk_mtl as MTL
import numpy as np

Ar3 = -1
br3 = -160

Ar4 = 1
br4 = 4500

pred3 = MTL.Predicate('speed', Ar3, br3)
pred4 = MTL.Predicate('rpm', Ar4, br4)

root = MTL.Not(MTL.Finally(0,100,MTL.And(pred3,pred4)))

traces = {}
traces['speed'] = np.array([10,20,30,40,50], dtype=np.float64)
traces['rpm']   = np.array([10,20,30,40,50], dtype=np.float64)

time_data = np.arange(1, 10, 2, dtype=np.float32)

root.eval_interval(traces, time_data)
print(root.robustness)
