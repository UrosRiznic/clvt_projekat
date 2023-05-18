
distribution = row["distribution"]
sample_size = row["sample_size"]
arg1 = row["arg1"]
arg2 = row["arg2"]

start_time = time.time()

distributions = {
    "poisson": "sample = np.random.poisson(arg1, size=sample_size)",
    "uniform": "sample = np.random.uniform(arg1, arg2, size=sample_size)",
    "weibull": "sample = np.random.weibull(arg1, size=sample_size)",
    "normal": "sample = np.random.normal(arg1, arg2, size=sample_size)"
}

if distribution in distributions:
    exec(distributions[distribution])

end_time = time.time()


# ////////////////////////////////////////////////////////////////

distribution = row["distribution"]
sample_size = row["sample_size"]
arg1 = row["arg1"]
arg2 = row["arg2"]
    
start_time = time.time()
if distribution == "poisson":
    sample = np.random.poisson(arg1, size=sample_size)
elif distribution == "uniform":
    sample = np.random.uniform(arg1, arg2, size=sample_size)
elif distribution == "weibull":
    sample = np.random.weibull(arg1, size=sample_size)
elif distribution == "normal":
    sample = np.random.normal(arg1, arg2, size=sample_size)
end_time = time.time()

# /////////////////////////////////////////////////////////// 
distribution = row["distribution"]
sample_size = row["sample_size"]
arg1 = row["arg1"]
arg2 = row["arg2"]

start_time = time.time()

final = f"sample = np.random.{distribution}({arg1}, {arg2}, size={sample_size})"
exec(final)

end_time = time.time()




