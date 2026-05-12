import numpy as np

def linear_threshold_gate(dot, T):
    if dot >= T:
        return 1
    else:
        return 0

input_table = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

weights = np.array([1, 1])
T = 1
dot_products = input_table @ weights

for i in range(len(input_table)):
    activation = linear_threshold_gate(dot_products[i], T)
    print(f"Input {input_table[i]} -> Output {activation}")
