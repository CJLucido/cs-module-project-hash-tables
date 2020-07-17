"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

# list(map(f, q))

cache = {}
value_cache ={}
value_numerical_cache = {}

def capture_io(v):
    listed_tuple = list(v)
    for i in listed_tuple:
        cache[i] = f(i)
    print(cache)

capture_io(q)

def find_value_each_set(c):
    for item in c:
        # find the value of that item plus or minus another or the same
        for item2 in cache:
            value_cache[f"f({item}) + f({item2})"] = c[item] + c[item2]
            value_cache[f"f({item}) - f({item2})"] = c[item] - c[item2]
            value_numerical_cache[f"{c[item]} + {c[item2]}"] = c[item] + c[item2]
            value_numerical_cache[f"{c[item]} - {c[item2]}"] = c[item] - c[item2]

    # pass

find_value_each_set(cache)

def compare_values(c2):
    for item in c2:
        for item2 in c2:
            if c2[item] == c2[item2]:
                print(f"{item} = {item2}")
            else:
                pass

# def compare_values_numerical(c2):
#     for item in c2:
#         for item2 in value_numerical_cache:
#             if c2[item] == value_numerical_cache[item2]:
#                 print(f"{item} = {item2}")
#             else:
#                 pass

def compare_values_twice(c2, c3):
    functional_output = []
    numerical_output = []
    for item in c2:
        for item2 in c2:
            if c2[item] == c2[item2]:
                functional_output.append(f"{item} = {item2}")
            else:
                pass

    for item in c3:
        for item2 in c3:
            if c3[item] == c3[item2]:
                numerical_output.append(f"{item} = {item2}")
            else:
                pass

    for i in range(len(functional_output)):       
        print(f'{functional_output[i]}  {numerical_output[i]}')

compare_values(value_cache)
compare_values(value_numerical_cache)
compare_values_twice(value_cache, value_numerical_cache)