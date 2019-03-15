import gsipn_simulator as sm
taos =[2190,4380,8760,17520,35040,70080]
lambdas=[1/10000000.0,1/1000000.0,1/100000.0,1/10000.0]
mdd = [0.0001,0.001,0.01,0.1]
dc = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
beta = [0.001,0.01,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for x in ['1oo1','1oo2','2oo3']:
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