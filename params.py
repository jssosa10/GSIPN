default_params = {
	'lambda_d': 0.0007,
	'lambda_dd': 0.1,
	'lambda_du': 0.1,
	'lambda_sd': 0.1,
	'lambda_su': 0.1,
	'lambda_de': 0.00001,
	'mu_dd': 0.1,
	'mu_du': 0.1,
	'mmu_sd': 0.1,
	'mu_su': 0.1,
	'mu_de': 0.1,
	'tao': 8760,
	'DC': 0.6,
	'SFF': 0.61,
	'beta': 0.1,
	'mttr_du': 8,
	'mttr_dd': 8,
	'mdd': 0.0001
}
def create_parameters(type,param):
	params = default_params.copy()
	params[type]=param
	params = recalculate(params)
	return params

def recalculate(params):
	params['mu_de'] = 1.0/float(params['mdd'])
	params['mu_dd'] = 1.0/float(params['mttr_dd'])
	params['mu_du'] = 1.0/(float(params['tao'])/2.0+float(params['mttr_du']))
	params['lambda_dd'] = float(params['DC'])*float(params['lambda_d'])
	params['lambda_du'] = float(1.0-params['DC'])*float(params['lambda_d'])
	return params