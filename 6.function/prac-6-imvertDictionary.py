# invert a dictionary means to swap keys and values.
# For example,
# if you have a dictionary d = {'a': 1, 'b': 2, 'c': 3}, then invert it to {'1': 'a', '2': 'b', '3': 'c'}.

def invertDict(d):
    d={values:keys for keys,values in d.items()}
    return d
print(invertDict({'a': 1, 'b': 2, 'c': 3})) # {'1': 'a', '2': 'b', '3': 'c'}
