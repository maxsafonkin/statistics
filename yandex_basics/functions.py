from collections import Counter

def mean(X: list[float]) -> float:
    return sum(X)/len(X)

def median(X: list[float]) -> float:
    X_len = len(X)
    X_sorted = sorted(X)
    if X_len % 2 == 0:
        return (X_sorted[X_len//2 - 1] + X_sorted[X_len//2]) / 2
    else:
        return X_sorted[X_len//2]

def var(X: list[float]) -> float:
    X_len = len(X)
    m = mean(X)
    sq_err = sum([(x-m)**2 for x in X])
    return 1 / (X_len - 1) * sq_err

def std(X: list[float]) -> float:
    return var(X) ** (1/2)

def covar(X: list[float], Y: list[float]) -> float:
    X_len = len(X)
    assert X_len == len(Y), "Sets should contain same amount of samples"

    X_mean, Y_mean = mean(X), mean(Y)
    sum_of_centered_products = sum([(X[i] - X_mean)*(Y[i] - Y_mean) for i in range(X_len)])
    return 1 / (X_len - 1) * sum_of_centered_products

def corr(X: list[float], Y: list[float]) -> float:
    return covar(X, Y) / (std(X) * std(Y))

def F(X: list[int | float | str], decimal: int = 2) -> dict[int | float | str, float]:
    count_values = Counter(X)
    total = sum(count_values.values())
    probabilities = {
        value: round(freq / total, decimal) for (value, freq) in count_values.items()
    }
    return probabilities