import tltk_mtl as MTL
import numpy as np

na0 = MTL.Predicate('pred0', float(25), float(30))
na1 = MTL.Predicate('pred1', float(1), float(-1.6))
na2 = MTL.Predicate('pred2', float(-1), float(1.4))
na3 = MTL.Predicate('pred3', float(-1), float(2.3))

req0 = MTL.Global(float(0), float('inf'), na0)
req1 = MTL.And(na1, MTL.Next(na2))
req2 = MTL.Or(MTL.Not(req1), MTL.Next(na3))
req3 = MTL.Finally(float(0), float(7), MTL.And(na1, MTL.Next(na2)))

req4 = MTL.And(req0, MTL.And(req2, req3))

phi = MTL.Global(float(0), float('inf'), req4)

traces = {}
traces['pred0'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred1'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred2'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred3'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64

time_data = np.arange(1, 2, 0.2, dtype=np.float32)

phi.eval_interval(traces, time_data)
print(phi.robustness)
