def print_stats(name, **info):
    print(name, 'is:')
    for key, value in info.items():
        print(f'{key}: {value}')
print_stats(name ='John', age = 10, gender = 'm')
