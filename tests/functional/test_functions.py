import pytest

def test_read_csv():
    data = pd.read_csv("data.csv")
    assert len(data) == 10  # proveravamo da li ima 10 redova u CSV datoteci
    assert "distribution" in data.columns  # proveravamo da li postoji kolona "distribution"
    assert "sample_size" in data.columns  # proveravamo da li postoji kolona "sample_size"
    assert "arg1" in data.columns  # proveravamo da li postoji kolona "arg1"
    assert "arg2" in data.columns  # proveravamo da li postoji kolona "arg2"


def test_generate_samples():
    data = pd.read_csv("data.csv")
    for index, row in data.iterrows():
        distribution = row["distribution"]
        sample_size = row["sample_size"]
        arg1 = row["arg1"]
        arg2 = row["arg2"]
        if distribution == "poisson":
            sample = np.random.poisson(arg1, size=sample_size)
        elif distribution == "uniform":
            sample = np.random.uniform(arg1, arg2, size=sample_size)
        elif distribution == "weibull":
            sample = np.random.weibull(arg1, size=sample_size)
        elif distribution == "normal":
            sample = np.random.normal(arg1, arg2, size=sample_size)
        assert len(sample) == sample_size  # proveravamo da li je veličina uzorka ispravna


def test_calculate_statistics():
    data = pd.read_csv("data.csv")
    for index, row in data.iterrows():
        distribution = row["distribution"]
        sample_size = row["sample_size"]
        arg1 = row["arg1"]
        arg2 = row["arg2"]
        if distribution == "poisson":
            sample = np.random.poisson(arg1, size=sample_size)
        elif distribution == "uniform":
            sample = np.random.uniform(arg1, arg2, size=sample_size)
        elif distribution == "weibull":
            sample = np.random.weibull(arg1, size=sample_size)
        elif distribution == "normal":
            sample = np.random.normal(arg1, arg2, size=sample_size)
        std = np.std(sample)
        mean = np.mean(sample)
        assert isinstance(std, float) and isinstance(mean, float)  # proveravamo da li su standardna devijacija i srednja vrednost brojevi
