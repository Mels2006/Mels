# 7. Tuple Exercise:
# Write a function that swaps the values of two tuples.
def swap_tuples(tuple1, tuple2):
    new_tuple = tuple1
    tuple1 = tuple2
    tuple2 = new_tuple
    return tuple1, tuple2


tuple_a = (1, 2, 3)
tuple_b = ('a', 'b', 'c')

print(f"Before swap: Tuple A = {tuple_a}, Tuple B = {tuple_b}")

tuple_a, tuple_b = swap_tuples(tuple_a, tuple_b)

print(f"After swap: Tuple A = {tuple_a}, Tuple B = {tuple_b}")


