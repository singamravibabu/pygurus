import pickle

emp_data = [
    [1001, "Raju", "d_01", 35000.0, 45],
    [1002, "Kiran", "d_03", 58000.0, 34],
    [1004, "Uday", "d_-1", 44000.0, 49],
]

with open("binary_f1.bin", "wb") as file:
    pickle.dump(emp_data, file)