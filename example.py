import gsipn as pn
import numpy as np
net = pn.GSIPN()
net.add_place('w',1)
net.add_place('d',0)
net.add_place('r',0)
net.add_place('A',1)
net.add_place('U',0)
net.add_transition('t0',t_class='exp',rate=0.0000022,assertion='c = not c')
net.add_transition('t1',predicate='r>0',assertion='r-=1')
net.add_transition('t2',t_class='exp',rate=0.0001,assertion='r+=1\nc = not c')
net.add_transition('t3',t_class='exp',rate=0.000001, predicate = 'not c')
net.add_transition('t4',t_class='exp',rate=0.0001,predicate = 'c')
net.add_inArc('w','t0')
net.add_outArc('d','t0')
net.add_inArc('d','t1')
net.add_outArc('r','t1')
net.add_inArc('r','t2')
net.add_outArc('w','t2')
net.add_inArc('A','t3')
net.add_outArc('U','t3')
net.add_inArc('U','t4')
net.add_outArc('A','t4')
net.add_varible('c',True)
net.add_varible('r',1)
res = []
for x in range(1000):
	marks = net.simulate(1000)
	z = 0
	for mark in marks:
		z+= mark['U']*1.0/len(marks)
	res.append(z)
print np.mean(res)
##print len(marks
##print net.global_varibles