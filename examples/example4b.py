import tltk_mtl as MTL
import tltk_mtl_ext as MTLE
import numpy as np

na0 = MTL.Predicate('pred0', float(25), float(30))
na1 = MTL.Predicate('pred1', float(1), float(-1.6))
na2 = MTL.Predicate('pred2', float(-1), float(1.4))
na3 = MTL.Predicate('pred3', float(-1), float(2.3))

predicates = {}
predicates['pred0'] = na0
predicates['pred1'] = na1
predicates['pred2'] = na2
predicates['pred3'] = na3

phi  = MTLE.parse_mtl('G_ts:(0, inf) (pred0) && G_ts:(0, inf)((pred1 && (X pred2)) -> (X (pred3))) && F_ts:(0, 7) (pred1 && X pred2)', predicates)

traces = {}
traces['pred0'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred1'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred2'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred3'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64

time_data = np.arange(1, 2, 0.2, dtype=np.float32)

phi.eval_interval(traces, time_data)
print(phi.robustness)
