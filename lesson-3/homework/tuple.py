# 1. Count Occurrences
def count_occurrences(tpl, element):
    return tpl.count(element)

# 2. Max Element
def max_element(tpl):
    return max(tpl) if tpl else None

# 3. Min Element
def min_element(tpl):
    return min(tpl) if tpl else None

# 4. Check Element
def check_element(tpl, element):
    return element in tpl

# 5. First Element
def first_element(tpl):
    return tpl[0] if tpl else None

# 6. Last Element
def last_element(tpl):
    return tpl[-1] if tpl else None

# 7. Tuple Length
def tuple_length(tpl):
    return len(tpl)

# 8. Slice Tuple (First 3 Elements)
def slice_tuple(tpl):
    return tpl[:3]

# 9. Concatenate Tuples
def concatenate_tuples(tpl1, tpl2):
    return tpl1 + tpl2

# 10. Check if Tuple is Empty
def is_empty_tuple(tpl):
    return len(tpl) == 0

# 11. Get All Indices of Element
def find_all_indices(tpl, element):
    return [i for i, x in enumerate(tpl) if x == element]

# 12. Find Second Largest
def second_largest(tpl):
    unique = sorted(set(tpl), reverse=True)
    return unique[1] if len(unique) > 1 else None

# 13. Find Second Smallest
def second_smallest(tpl):
    unique = sorted(set(tpl))
    return unique[1] if len(unique) > 1 else None

# 14. Create a Single Element Tuple
def single_element_tuple(element):
    return (element,)

# 15. Convert List to Tuple
def list_to_tuple(lst):
    return tuple(lst)

# 16. Check if Tuple is Sorted
def is_sorted_tuple(tpl):
    return tpl == tuple(sorted(tpl))

# 17. Find Maximum of Subtuple
def max_of_subtuple(tpl, start, end):
    return max(tpl[start:end]) if tpl[start:end] else None

# 18. Find Minimum of Subtuple
def min_of_subtuple(tpl, start, end):
    return min(tpl[start:end]) if tpl[start:end] else None

# 19. Remove Element by Value
def remove_element(tpl, element):
    lst = list(tpl)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

# 20. Create Nested Tuple
def create_nested_tuple(tpl, n):
    return tuple(tpl[i:i + n] for i in range(0, len(tpl), n))

# 21. Repeat Elements
def repeat_elements(tpl, n):
    return tuple(x for x in tpl for _ in range(n))

# 22. Create Range Tuple
def create_range_tuple(start, end):
    return tuple(range(start, end + 1))

# 23. Reverse Tuple
def reverse_tuple(tpl):
    return tpl[::-1]

# 24. Check Palindrome
def is_palindrome_tuple(tpl):
    return tpl == tpl[::-1]

# 25. Get Unique Elements (Maintaining Order)
def unique_elements_tuple(tpl):
    seen = set()
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))
numbers = (4, 2, 2, 5, 6, 5, 2, 9, 10)

print(count_occurrences(numbers, 2))  # Output: 3
print(max_element(numbers))           # Output: 10
print(min_element(numbers))           # Output: 2
print(check_element(numbers, 5))      # Output: True
print(first_element(numbers))         # Output: 4
print(last_element(numbers))          # Output: 10
print(tuple_length(numbers))          # Output: 9
print(slice_tuple(numbers))           # Output: (4, 2, 2)
print(concatenate_tuples((1, 2), (3, 4)))  # Output: (1, 2, 3, 4)
print(is_empty_tuple(()))             # Output: True
print(find_all_indices(numbers, 2))   # Output: [1, 2, 6]
print(second_largest(numbers))        # Output: 9
print(second_smallest(numbers))       # Output: 4
print(single_element_tuple(99))       # Output: (99,)
print(list_to_tuple([1, 2, 3]))       # Output: (1, 2, 3)
print(is_sorted_tuple(numbers))       # Output: False
print(remove_element(numbers, 5))     # Output: (4, 2, 2, 6, 5, 2, 9, 10)
print(reverse_tuple(numbers))         # Output: (10, 9, 2, 5, 6, 5, 2, 2, 4)
print(is_palindrome_tuple((1, 2, 3, 2, 1))) # Output: True
print(unique_elements_tuple(numbers)) # Output: (4, 2, 5, 6, 9, 10)
