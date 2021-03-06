import tltk_mtl as MTL
import numpy as np

na1 = MTL.Predicate('pred1', float(1), float(-1.6))
na2 = MTL.Predicate('pred2', float(-1), float(1.4))
na3 = MTL.Predicate('pred3', float(-1), float(2.3))

na12 = MTL.Or(na1, na2)
phi = MTL.Or(na12, na3)

traces = {}
traces['pred1'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred2'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred3'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64

time_data = np.arange(1, 2, 0.2, dtype=np.float32)

phi.eval_interval(traces, time_data)
print(phi.robustness)
