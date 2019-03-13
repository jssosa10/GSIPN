default_params = {
	'lambda_dd': 0.1,
	'lambda_du': 0.1,
	'lambda_sd': 0.1,
	'lambda_su': 0.1,
	'lambda_de': 0.1,
	'mu_dd': 0.1,
	'mu_du': 0.1,
	'mmu_sd': 0.1,
	'mu_su': 0.1,
	'mu_de': 0.1,
	'tao': 0.1,
	'DC': 0.1,
	'SFF': 0.1,
	'beta': 0.1,
	'mttr_du': 0.1,
	'mttr_dd': 0.1,
	'mdd': 0.1
}
def create_parameters(type,param):
	params = default_params
	params[type]=param
	params = recalculate(params)
	return params

def recalculate(params):
	return params