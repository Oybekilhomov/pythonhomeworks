
##List Tasks
##num1

def count_occurrences(lst, element):
    return lst.count(element)

my_list = [1, 2, 3, 4, 2, 2, 5]
element_to_count = 2
print(count_occurrences(my_list, element_to_count))  


##num2

def sum_of_elements(lst):
    return sum(lst)

my_list = [1, 2, 3, 4, 5]
print(sum_of_elements(my_list)) 


##num3

def max_element(lst):
    return max(lst)

my_list = [3, 1, 2, 8, 4]
print(max_element(my_list)) 


##num4

def min_element(lst):
    return min(lst)

my_list = [3, 1, 2, 11, 5]
print(min_element(my_list))  


##num5

def check_element(lst, element):
    return element in lst

my_list = [1, 3, 5, 7]
print(check_element(my_list, 5))  
print(check_element(my_list, 2))  


##num6

def first_element(lst):
    if lst:
        return lst[0]
    else:
        return None  
print(first_element([10, 20, 30])) 
print(first_element([]))          

    

##num7

def last_element(lst):
    if lst:
        return lst[-1]
    else:
        return None  
print(last_element([10, 20, 30]))  
print(last_element([]))           


##num8


def first_three_elements(lst):
    return lst[:3]
print(first_three_elements([10, 20, 30, 40, 50]))  
print(first_three_elements([5]))                 
print(first_three_elements([]))                   


##num9

def reverse_list(lst):
    return list(reversed(lst))
print(reverse_list([1, 2, 3, 4]))  
print(reverse_list([]))           


##num10

def sort_list(lst):
    return sorted(lst)
print(sort_list([5, 2, 9, 1]))  
print(sort_list([]))              
print(sort_list(["b", "a", "c"])) 


##num11

def remove_duplicates(lst):
    unique = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique
print(remove_duplicates([1, 2, 2, 3, 1, 4]))  
print(remove_duplicates([]))               


##num12

def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst
my_list = [1, 2, 4, 5]
print(insert_element(my_list, 3, 2))  


##num13

def index_of_element(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1  
my_list = [5, 3, 7, 3, 9]
print(index_of_element(my_list, 3))  
print(index_of_element(my_list, 10))


##num14

def is_list_empty(lst):
    return len(lst) == 0
print(is_list_empty([]))       
print(is_list_empty([1, 2, 3])) 


##num15

def count_even_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count
print(count_even_numbers([1, 2, 3, 4, 5, 6]))  
print(count_even_numbers([]))                


##num16

def count_odd_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 != 0:
            count += 1
    return count
print(count_odd_numbers([1, 2, 3, 4, 5, 6])) 
print(count_odd_numbers([]))                 


##num17

def concatenate_lists(list1, list2):
    result = list1.copy()
    result.extend(list2)
    return result
a = [1, 2, 3]
b = [4, 5, 6]
print(concatenate_lists(a, b))  


##num18

def is_sublist(lst, sub):
    if not sub:
        return True 
    sub_len = len(sub)
    for i in range(len(lst) - sub_len + 1):
        if lst[i:i + sub_len] == sub:
            return True
    return False
print(is_sublist([1, 2, 3, 4, 5], [2, 3]))    
print(is_sublist([1, 2, 3, 4, 5], [3, 5]))    
print(is_sublist([1, 2, 3], []))            


##num19

def replace_first_occurrence(lst, old, new):
    try:
        index = lst.index(old)
        lst[index] = new
    except ValueError:
        pass  
    return lst
my_list = [1, 2, 3, 2, 4]
print(replace_first_occurrence(my_list, 2, 99)) 

my_list = [1, 2, 3]
print(replace_first_occurrence(my_list, 5, 99))  


##num20

def second_largest(lst):
    unique = list(set(lst))
    if len(unique) < 2:
        return None 
    unique.sort(reverse=True)
    return unique[1]
print(second_largest([10, 20, 30, 40]))   
print(second_largest([5, 5, 5]))         
print(second_largest([100]))              


##num21

def second_smallest(lst):
    first = second = float('inf')
    for num in lst:
        if num < first:
            second, first = first, num
        elif first < num < second:
            second = num
    return second if second != float('inf') else None
print(second_smallest([3, 1, 4, 1, 5])) 
print(second_smallest([7]))          
print(second_smallest([2, 2, 2]))       


##num22

def filter_even_numbers(lst):
    return list(filter(lambda x: x % 2 == 0, lst))
print(filter_even_numbers([1, 2, 3, 4, 5, 6])) 
print(filter_even_numbers([]))  


##num23

def filter_odd_numbers(lst):
    return list(filter(lambda x: x % 2 != 0, lst))
print(filter_odd_numbers([1, 2, 3, 4, 5, 6])) 
print(filter_odd_numbers([])) 


##num24

def list_length(lst):
    return len(lst)
print(list_length([1, 2, 3, 4])) 
print(list_length([])) 


##num25

def copy_list(lst):
    return list(lst)
original = [1, 2, 3]
copy = copy_list(original)

print(copy) 
print(copy is original)


##num26

def get_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None 
    mid = n // 2
    if n % 2 == 0:
        return [lst[mid - 1], lst[mid]]
    else:
        return lst[mid]
print(get_middle_element([1, 2, 3]))
print(get_middle_element([1, 2, 3, 4]))
print(get_middle_element([]))


##num27

def max_of_sublist(lst, start, end):
    sublist = lst[start:end] 
    if not sublist:
        return None 
    return max(sublist)
numbers = [3, 8, 1, 9, 2, 7]
print(max_of_sublist(numbers, 1, 4))
print(max_of_sublist(numbers, 3, 3)) 


##num28

def min_of_sublist(lst, start, end):
    sublist = lst[start:end] 
    if not sublist:
        return None 
    return min(sublist)
numbers = [5, 8, 2, 9, 1, 6]
print(min_of_sublist(numbers, 1, 4))
print(min_of_sublist(numbers, 4, 4))


##num29

def remove_element_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst
print(remove_element_by_index([10, 20, 30, 40], 2)) 
print(remove_element_by_index([10, 20, 30], 5))


##num30

def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True
print(is_sorted([1, 2, 3, 4])) 
print(is_sorted([1, 3, 2])) 
print(is_sorted([]))
print(is_sorted([5]))


##num31

def repeat_elements(lst, times):
    return [item for item in lst for _ in range(times)]
print(repeat_elements([1, 2, 3], 2))
print(repeat_elements(['a', 'b'], 3))
print(repeat_elements([1, 2], 0))


##num32

def merge_and_sort(list1, list2):
    return sorted(list1 + list2)
print(merge_and_sort([3, 1, 4], [2, 5]))
print(merge_and_sort([], [7, 6]))
print(merge_and_sort([], []))


##num33

def find_all_indices(lst, element):
    return [i for i, val in enumerate(lst) if val == element]
print(find_all_indices([1, 2, 3, 2, 4, 2], 2))
print(find_all_indices(['a', 'b', 'a'], 'a'))
print(find_all_indices([1, 2, 3], 5))


##num34

def rotate_list(lst, k=1):
    if not lst:
        return []
    k = k % len(lst) 
    return lst[-k:] + lst[:-k]
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3], 1)) 
print(rotate_list([], 3))


##num35

def create_range_list(start, end, step=1):
    return list(range(start, end + 1, step)) if step > 0 else list(range(start, end - 1, step))
print(create_range_list(1, 10))
print(create_range_list(5, 15, 2))
print(create_range_list(10, 1, -3))


##num36

def sum_of_positive_numbers(lst):
    return sum(num for num in lst if num > 0)
print(sum_of_positive_numbers([1, -2, 3, 4, -5]))
print(sum_of_positive_numbers([-1, -2, -3]))
print(sum_of_positive_numbers([]))


##num37

def sum_of_negative_numbers(lst):
    return sum(num for num in lst if num < 0)
print(sum_of_negative_numbers([1, -2, 3, -4, -5]))
print(sum_of_negative_numbers([1, 2, 3]))
print(sum_of_negative_numbers([]))


##num38

def is_palindrome(lst):
    return lst == lst[::-1]
print(is_palindrome([1, 2, 3, 2, 1]))
print(is_palindrome(['a', 'b', 'a']))
print(is_palindrome([1, 2, 3]))
print(is_palindrome([]))


##num39

def create_nested_list(lst, size):
    if size <= 0:
        return []
    return [lst[i:i+size] for i in range(0, len(lst), size)]
print(create_nested_list([1, 2, 3, 4, 5, 6, 7], 3))

print(create_nested_list([1, 2, 3, 4], 2))

print(create_nested_list([], 2))


##num40

def unique_in_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
print(unique_in_order([1, 2, 2, 3, 1, 4]))
print(unique_in_order(['a', 'b', 'a', 'c']))
print(unique_in_order([]))


##Tuple Tasks
##num1

my_tuple = (1, 2, 3, 2, 4, 1, 5)

element = 2

count = my_tuple.count(element)

print(f"The element {element} appears {count} times in the tuple.")


##num2

my_tuple = (11, 26, 4, 88, 43)

max_element = max(my_tuple)

print(f"The largest element in the tuple is {max_element}.")


###num3

my_tuple = (11, 26, 4, 88, 43)

min_element = min(my_tuple)

print(f"The smallest element in the tuple is {min_element}.")


##num4

my_tuple = (5, 10, 15, 20, 25)

element = 15

if element in my_tuple:
    print(f"The element {element} is present in the tuple.")
else:
    print(f"The element {element} is not present in the tuple.")


##num5

my_tuple = (33, 15, 8)

if my_tuple:
    first_element = my_tuple[0]
    print(f"The first element is {first_element}.")
else:
    print("The tuple is empty. No first element.")


##num6

my_tuple =(33, 15, 8) 

if my_tuple:
    last_element = my_tuple[-1]
    print(f"The last element is {last_element}.")
else:
    print("The tuple is empty. No last element.")


##num7

my_tuple = (5, 10, 15, 20)

length = len(my_tuple)

print(f"The tuple has {length} elements.")


##num8

my_tuple = (100, 200, 300, 400, 500)

first_three = my_tuple[:3]

print(f"The first three elements are: {first_three}")


##num9

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2

print(f"The combined tuple is: {combined}")


##num10

my_tuple = ()

if not my_tuple:
    print("The tuple is empty.")
else:
    print("The tuple is not empty.")


##num11

my_tuple = (1, 2, 3, 2, 4, 2, 5)

element = 2

indices = [index for index, value in enumerate(my_tuple) if value == element]

print(f"The element {element} appears at indices: {indices}")


##num12

my_tuple = (100, 200, 400, 300, 400, 200)

unique_sorted = sorted(set(my_tuple), reverse=True)

if len(unique_sorted) >= 2:
    second_largest = unique_sorted[1]
    print(f"The second largest element is {second_largest}.")
else:
    print("The tuple doesn't have enough unique elements to determine a second largest.")


##num13

my_tuple = (5, 1, 3, 1, 4, 2)

unique_sorted = sorted(set(my_tuple))

if len(unique_sorted) >= 2:
    second_smallest = unique_sorted[1]
    print(f"The second smallest element is {second_smallest}.")
else:
    print("The tuple doesn't have enough unique elements to determine a second smallest.")


##num14

element = 52

single_tuple = (element,)

print(f"The single-element tuple is: {single_tuple}")
print(f"Type: {type(single_tuple)}")


##num15

my_list = [3, 4, 5, 6, 7, 8, 9,]

my_tuple = tuple(my_list)

print(f"The tuple is: {my_tuple}")


##num16

my_tuple = (1, 2, 3, 4, 5)

is_sorted = my_tuple == tuple(sorted(my_tuple))

print(f"Is the tuple sorted in ascending order? {is_sorted}")


##num17

my_tuple = (10, 20, 5, 30, 25)

start = 1
end = 4

subtuple = my_tuple[start:end]

if subtuple:
    max_value = max(subtuple)
    print(f"The maximum element in the subtuple {subtuple} is {max_value}.")
else:
    print("The specified subtuple is empty.")


##num18

my_tuple = (12, 7, 25, 3, 18)

start = 1
end = 4

subtuple = my_tuple[start:end]

if subtuple:
    min_value = min(subtuple)
    print(f"The minimum element in the subtuple {subtuple} is {min_value}.")
else:
    print("The specified subtuple is empty.")


##num19

my_tuple = (10, 20, 30, 20, 40)
element_to_remove = 20

temp_list = list(my_tuple)

if element_to_remove in temp_list:
    temp_list.remove(element_to_remove)
    new_tuple = tuple(temp_list)
    print(f"New tuple after removing {element_to_remove}: {new_tuple}")
else:
    print(f"Element {element_to_remove} not found in the tuple.")


##num20

original_tuple = (1, 2, 3, 4, 5, 6)

group_size = 2

nested = tuple(original_tuple[i:i+group_size] for i in range(0, len(original_tuple), group_size))

print(f"Nested tuple: {nested}")


##num21

original_tuple = (3, 4, 5)
repeat_count = 3

repeated_tuple = tuple(elem for elem in original_tuple for _ in range(repeat_count))

print(f"Repeated tuple: {repeated_tuple}")


##num22

start = 3
end = 15

range_tuple = tuple(range(start, end + 1))

print(f"Range tuple: {range_tuple}")


##num23

original_tuple = (1, 2, 3, 4, 5)

reversed_tuple = original_tuple[::-1]

print(f"Reversed tuple: {reversed_tuple}")


##num24

my_tuple = (1, 2, 3, 2, 1)

is_palindrome = my_tuple == my_tuple[::-1]

print(f"Is the tuple a palindrome? {is_palindrome}")


##num25

original_tuple = (1, 2, 2, 3, 1, 4, 3)

seen = set()
unique_elements = []

for item in original_tuple:
    if item not in seen:
        seen.add(item)
        unique_elements.append(item)

unique_tuple = tuple(unique_elements)

print(f"Unique elements tuple: {unique_tuple}")


##Set Tasks
##num1

set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b

print("Union of A and B:", union_set)


##num2

set_a = {1, 2, 3}
set_b = {2, 3, 4}

intersection_set = set_a & set_b

print("Intersection of A and B:", intersection_set)


##num3

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}

difference_set = set_a - set_b

print("Difference of A and B (A - B):", difference_set)


##num4

set_a = {1, 2}
set_b = {1, 2, 3, 4}

is_subset = set_a.issubset(set_b)

print("Is A a subset of B?", is_subset)


##num5

my_set = {1, 2, 3}

element = 2

if element in my_set:
    print(f"{element} is in the set.")
else:
    print(f"{element} is not in the set.")


##num6

my_set = {1, 2, 2, 3, 4, 4, 5}

unique_count = len(my_set)

print("Number of unique elements:", unique_count)


##num7

my_list = [1, 2, 2, 3, 4, 4, 5]

unique_set = set(my_list)

print("Unique elements:", unique_set)


##num8

my_set = {1, 2, 3, 4}

element = 3

my_set.discard(element)

print("Updated set:", my_set)


##num9

my_set = {1, 2, 3, 4, 5}

my_set.clear()

print("Cleared set:", my_set)


##num10

my_set = set()

if not my_set:
    print("The set is empty.")
else:
    print("The set is not empty.")


##num11

set_a = {1, 2, 3}
set_b = {3, 4, 5}

sym_diff = set_a ^ set_b

print("Symmetric Difference:", sym_diff)


##num12

my_set = {1, 2, 3}

element = 4

my_set.add(element)

print("Updated set:", my_set)


##num13

my_set = {10, 20, 30}

removed_element = my_set.pop()

print("Removed element:", removed_element)
print("Updated set:", my_set)


##num14

num_set = {10, 25, 3, 42, 18}

max_value = max(num_set)

print("Maximum element:", max_value)


##num15

num_set = {10, 25, 3, 42, 18}

min_value = min(num_set)

print("Minimum element:", min_value)


##num16

num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

even_set = {num for num in num_set if num % 2 == 0}

print("Even numbers:", even_set)


##num17

num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

odd_set = {num for num in num_set if num % 2 != 0}

print("Odd numbers:", odd_set)


##num18

num_set = set(range(1, 11))

print("Set from 1 to 10:", num_set)


##num19

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged_set = set(list1) | set(list2)


print("Merged set with unique elements:", merged_set)


##num20

set_a = {1, 2, 3}
set_b = {4, 5, 6}

are_disjoint = set_a.isdisjoint(set_b)

print("Are the sets disjoint?", are_disjoint)


##num21

my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(my_list))

print("List without duplicates:", unique_list)


##num22

my_list = [1, 2, 2, 3, 4, 4, 5]

unique_count = len(set(my_list))

print("Number of unique elements:", unique_count)


##num23

import random

random_set = set(random.sample(range(1, 21), 5))

print("Random set:", random_set)


##Dictionary Tasks
##num1

my_dict = {'name': 'Jama', 'age': 17}

value = my_dict.get('name') 

value = my_dict.get('gender', 'Not specified')  


##num2

my_dict = {'name': 'Jama', 'age': 17}

if 'name' in my_dict:
    print("Key exists")
else:
    print("Key does not exist")


##num3

my_dict = {'name': 'Jama', 'age': 17, 'city': 'Xorazm'}

num_keys = len(my_dict)

print("Number of keys:", num_keys)


##num4

my_dict = {'name': 'Jama', 'age': 17, 'city': 'Xorazm'}

keys_list = list(my_dict.keys())

print(keys_list)


##num5

my_dict ={'name': 'Jama', 'age': 17, 'city': 'Xorazm'}

values_list = list(my_dict.values())

print(values_list) 


##num6

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = {**dict1, **dict2}

print(merged)


##num7

my_dict = {'a': 1, 'b': 2, 'c': 3}

removed_value = my_dict.pop('b', None)

print(my_dict)
print("Removed:", removed_value)


##num8

my_dict = {'a': 1, 'b': 2}

my_dict.clear()

print(my_dict) 

new_dict = {}


##num9

my_dict = {}

if not my_dict:
    print("Dictionary is empty")
else:
    print("Dictionary has elements")


##num10

my_dict = {'name': 'Jama', 'age': 17, 'city': 'Xorazm'}
key = 'age'

if key in my_dict:
    pair = (key, my_dict[key])
    print("Key-value pair:", pair)
else:
    print("Key not found")


##num11

my_dict = {'name': 'Jama', 'age': 17}

my_dict['age'] = 18

print(my_dict)


##num12

my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 1
}

target_value = 1

count = list(my_dict.values()).count(target_value)

print(f"{target_value} appears {count} times") 


##num13


my_dict = {'a': 1, 'b': 2, 'c': 3}

inverted = {v: k for k, v in my_dict.items()}

print(inverted) 


##num14


my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30}

target_value = 10

matching_keys = [k for k, v in my_dict.items() if v == target_value]

print(matching_keys) 


##num15

keys = ['a', 'b', 'c']
values = [1, 2, 3]

my_dict = dict(zip(keys, values))

print(my_dict) 


##num16

my_dict = {
    'a': 1,
    'b': {'nested': True},
    'c': [1, 2, 3]
}

has_nested = any(isinstance(v, dict) for v in my_dict.values())

print("Contains nested dictionary:", has_nested)  


##num17

my_dict = {
    'user': {
        'name': 'Jama',
        'age': 17
    },
    'location': 'Xorazm'
}

name = my_dict['user']['name']

print(name) 


##num18

from collections import defaultdict

my_dict = defaultdict(int)

my_dict['a'] += 1
my_dict['b'] += 1
my_dict['c'] += 5

print(my_dict) 


##num19

my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

unique_count = len(set(my_dict.values()))

print(unique_count) 


##num20

my_dict = {'b': 2, 'a': 1, 'c': 3}

sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}

print(sorted_dict) 


##num21

my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_by_value)


##num22

my_dict = {'a': 5, 'b': 15, 'c': 25, 'd': 7}

filtered = {k: v for k, v in my_dict.items() if v > 10}

print(filtered) 


##num23

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 9, 'b': 5, 'y': 7}

common_keys = set(dict1.keys()) & set(dict2.keys())

print(common_keys) 


##num24

pair_tuple = (('a', 1), ('b', 2), ('c', 3))

my_dict = dict(pair_tuple)

print(my_dict)


##num25

my_dict = {'a': 1, 'b': 2, 'c': 3}

first_pair = next(iter(my_dict.items()))

print(first_pair) 
