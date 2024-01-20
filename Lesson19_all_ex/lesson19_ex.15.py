# 15. Multiple Exceptions:
# Write a function that performs the following tasks:
# Accepts a list and an index as input.
# Attempts to access the element at the given index in the list.
# Handles both IndexError
# Uses a finally block to print "Task completed" regardless of whether an exception
# occurred or not.
def access_element(my_list, index):
    try:
        element = my_list[index]
        print(f"Element of index {index}: {element}")
    except IndexError:
        print(f"IndexError: Index {index} is out of range.")
    finally:
        print("Task completed")


my_list = [1, 2, 3, 4, 5]


access_element(my_list, 2)


access_element(my_list, 7)
