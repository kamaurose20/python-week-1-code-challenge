def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value
            
    return dict1

dict1 = {'a': 12, 'b': 25, 'c': 9}
dict2 = {'a': 100, 'b': 200, 'c': 300}

result = merge_dicts(dict1, dict2)
print(result)
