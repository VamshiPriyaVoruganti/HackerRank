def product(fracs):
    t = reduce(lambda x, y : x * y,[z for z in fracs])
    return t.numerator, t.denominator
