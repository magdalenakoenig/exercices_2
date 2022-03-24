# bsp 1
def count_integer(numbers, integer):
    x = 0
    for i in numbers:
        if (i == integer):
            x = x + 1
        else:
            x = x
        if integer not in numbers:
            x = 42
    return(x)
print(count_integer([2,3,5,3], 3))
print("\n")

# bsp 2
def list_func(numbers, integer):
    for i in range(len(numbers)):
        if numbers[i] == integer:
            numbers[i] = 6
            copy = numbers.copy()
            result = copy
            numbers.reverse()
            print(numbers)
        else:
            result = []
    return(result)
print(list_func([1, 2, 1, 4], 4))
print("\n")

# bsp 3
def compare_lists(list1, list2):
    result = [i for i in list1 if i in list2]
    return(result)
print(compare_lists([1,2,3,5],[4,3,5,2,6]))
print("\n")

# bsp 4
def remove_duplicates(lst):
    for i in lst:
        if lst.count(i) > 1:
            result = lst.remove(i)
        else:
            result = lst
    return(result)
print(remove_duplicates([1,2,3,4,2,1,6,3]))
print("\n")

# bsp 5
def dict_func(dictionary):
    dict = {"Type": "Laptop", "Brand": "Lenovo", "Price": "800"}
    dict.setdefault("Type", "unknown type")
    dict.setdefault("Brand", "unknown brand")
    dict.setdefault("Price", "unknown price")
    print("You have a "+ dict.get("Type") + " from " + dict.get("Brand") + " that costs: " + dict.get("Price"))
    dict.setdefault("OS", "Linux")
    return(dict)
print(dict_func(dict))