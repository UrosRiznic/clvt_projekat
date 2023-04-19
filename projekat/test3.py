print("radi")

distributions = {'poisson': np.random.poisson, 'uniform': np.random.uniform, 'weibull': np.random.weibull, 'normal': np.random.normal}
sample = distributions[distribution](*([arg1, arg2][:len(inspect.signature(distributions[distribution]).parameters)-2]), size=sample_size)
