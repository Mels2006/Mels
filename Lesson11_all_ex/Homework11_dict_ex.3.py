# Write a python function, which create a dictionary
# for given number N, where keys are numbers from
# 1 to N, and values are cubs of that numbers
def create_cubes_dict(N):
    cubes_dict = {i: i**3 for i in range(1, N)}
    return cubes_dict


N = 5
result_dict = create_cubes_dict(N)
print(result_dict)