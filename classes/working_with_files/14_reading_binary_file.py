import pickle

with open("binary_f1.bin", "rb") as file:
    employee_data = pickle.load(file)
    print(employee_data)