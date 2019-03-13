import numpy as np
import nets as nn
import params as pm

nets = {}

nets['1oo1'] = nn.create1oo1
nets['1oo2'] = nn.create1oo2
nets['2oo3'] = nn.create2oo3


def simulate(net):
	res = []
	for x in range(1000):
		marks = net.simulate(1000)
		z = 0
		for mark in marks:
			z+= mark['U']*1.0/len(marks)
		res.append(z)
	return np.mean(res)

def create_net(netID,params):
	return nets[netID](params);

def create_net_fixed(new_parameter,type,netID):
	params = pm.create_parameters(type,new_parameter)
	return create_net(netID, params)

def generate_results(new_parameters,type,netID):
	return [simulate(create_net_fixed(new_parameter,type,netID)) for new_parameter in new_parameters]

for x,y in create_net_fixed(0.1,'mttr_du','2oo3').transitions.items():
	print x,y