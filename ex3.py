def fact(n):
    assert n >= 1
    return {0: 1}.get(n, n * fact(n-1))