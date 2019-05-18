import gsipn_simulator as sm
taos =[4380,8760,17520,87600]
lambdas=[1.0/x for x in taos]
mdd = [0.0001,0.001,0.01,0.1]
dc = [0.0,0.6,0.9,0.99]
beta = [0.01,0.05,0.1]
for x in ['242']:
	res = sm.generate_results(taos,'tao',x)
	print x,'tao',res
	res = sm.generate_results(lambdas,'lambda_de',x)
	print x,'lambda_de',res
	res = sm.generate_results(mdd,'mdd',x)
	print x,'mdd',res
	res = sm.generate_results(dc,'DC',x)
	print x,'DC',res
	res = sm.generate_results(beta,'beta',x)
	print x,'beta',res