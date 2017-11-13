



# Finding the maximum element using the reduce transformation

elements = [34,67,45,98,23,44,67,88]
maximum_element = lambda first,second: first if (first > second) else second
print(reduce(maximum_element, elements))