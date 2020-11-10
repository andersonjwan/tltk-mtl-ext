import tltk_mtl as MTL
import tltk_mtl_ext as MTLE
import numpy as np

na1 = MTL.Predicate('pred1', float(1), float(-1.6))
na2 = MTL.Predicate('pred2', float(-1), float(1.4))
na3 = MTL.Predicate('pred3', float(-1), float(2.3))

predicates = {}
predicates['pred1'] = na1
predicates['pred2'] = na2
predicates['pred3'] = na3

# MTL PREDICATE FINAL
phi  = MTLE.parse_mtl('G_ts:(1, 5) pred1 || pred2 U_ts:(5, 10) pred3', predicates)

traces = {}
traces['pred1'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred2'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
traces['pred3'] = np.array([1,2,2,5,3], dtype=np.float64) # traces has to be 64
#print(traces['pred'].shape)

time_data = np.arange(1, 2, 0.2, dtype=np.float32)
#print(time_data.shape)

phi.eval_interval(traces, time_data)
print(phi.robustness)
