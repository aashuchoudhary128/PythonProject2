numbers = input("Enter a series of integers separated by spaces: ")
num_tuple = tuple(map(int, numbers.split()))
print("Total number of items:", len(num_tuple))
if len(num_tuple) > 0:
    print("Last item:", num_tuple[-1])
else:
    print("Tuple is empty.")
print("Tuple in reverse order:", num_tuple[::-1])
if 5 in num_tuple:
    print("Yes")
else:
    print("No")
if len(num_tuple) > 2:
    remaining = num_tuple[1:-1]      
    sorted_remaining = tuple(sorted(remaining))
    print("Sorted remaining elements:", sorted_remaining)
else:
    print("Not enough elements to remove first and last.")