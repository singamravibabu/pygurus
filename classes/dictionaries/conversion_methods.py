states = [
    ["TG",'hyd'],
    ['AP','amr'],
    ["TN","che"],
    ["KA","blr"],
    ["KL",'tri'],
    ['MH','mum'],
]

# dict() function converts a list of lists to a dictionary
states_dict = dict(states)
print(states_dict)

# list() function converts 1D items to a list
keys_list = list(states_dict.keys())
print(keys_list)

values_list = list(states_dict.values())
print(values_list)

# tuple() function
keys_tuple = tuple(states_dict.keys())
print(keys_tuple)