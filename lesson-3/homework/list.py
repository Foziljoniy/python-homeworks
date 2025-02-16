# 1. Count Occurrences
def count_occurrences(lst, element):
    return lst.count(element)

# 2. Sum of Elements
def sum_of_elements(lst):
    return sum(lst)

# 3. Max Element
def max_element(lst):
    return max(lst) if lst else None

# 4. Min Element
def min_element(lst):
    return min(lst) if lst else None

# 5. Check Element
def check_element(lst, element):
    return element in lst

# 6. First Element
def first_element(lst):
    return lst[0] if lst else None

# 7. Last Element
def last_element(lst):
    return lst[-1] if lst else None

# 8. Slice List (First 3 Elements)
def slice_list(lst):
    return lst[:3]

# 9. Reverse List
def reverse_list(lst):
    return lst[::-1]

# 10. Sort List
def sort_list(lst):
    return sorted(lst)

# 11. Remove Duplicates
def remove_duplicates(lst):
    return list(set(lst))

# 12. Insert Element
def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

# 13. Index of Element
def index_of_element(lst, element):
    return lst.index(element) if element in lst else -1

# 14. Check for Empty List
def is_empty(lst):
    return len(lst) == 0

# 15. Count Even Numbers
def count_even(lst):
    return sum(1 for x in lst if x % 2 == 0)

# 16. Count Odd Numbers
def count_odd(lst):
    return sum(1 for x in lst if x % 2 != 0)

# 17. Concatenate Lists
def concatenate_lists(lst1, lst2):
    return lst1 + lst2

# 18. Find Sublist
def find_sublist(lst, sublist):
    return str(sublist) in str(lst)

# 19. Replace Element
def replace_element(lst, old, new):
    if old in lst:
        lst[lst.index(old)] = new
    return lst

# 20. Find Second Largest
def second_largest(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) > 1 else None

# 21. Find Second Smallest
def second_smallest(lst):
    unique = sorted(set(lst))
    return unique[1] if len(unique) > 1 else None

# 22. Filter Even Numbers
def filter_even(lst):
    return [x for x in lst if x % 2 == 0]

# 23. Filter Odd Numbers
def filter_odd(lst):
    return [x for x in lst if x % 2 != 0]

# 24. List Length
def list_length(lst):
    return len(lst)

# 25. Create a Copy
def copy_list(lst):
    return lst[:]

# 26. Get Middle Element
def middle_element(lst):
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]
    else:
        return lst[n // 2 - 1:n // 2 + 1]

# 27. Find Maximum of Sublist
def max_of_sublist(lst, start, end):
    return max(lst[start:end]) if lst[start:end] else None

# 28. Find Minimum of Sublist
def min_of_sublist(lst, start, end):
    return min(lst[start:end]) if lst[start:end] else None

# 29. Remove Element by Index
def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst

# 30. Check if List is Sorted
def is_sorted(lst):
    return lst == sorted(lst)

# 31. Repeat Elements
def repeat_elements(lst, n):
    return [x for x in lst for _ in range(n)]

# 32. Merge and Sort
def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)

# 33. Find All Indices
def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

# 34. Rotate List
def rotate_list(lst, k):
    k = k % len(lst) if lst else 0
    return lst[-k:] + lst[:-k]

# 35. Create Range List
def create_range_list(start, end):
    return list(range(start, end + 1))

# 36. Sum of Positive Numbers
def sum_positive(lst):
    return sum(x for x in lst if x > 0)

# 37. Sum of Negative Numbers
def sum_negative(lst):
    return sum(x for x in lst if x < 0)

# 38. Check Palindrome
def is_palindrome(lst):
    return lst == lst[::-1]

# 39. Create Nested List
def create_nested_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

# 40. Get Unique Elements in Order
def unique_elements_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
numbers = [4, 2, 2, 5, 6, 5, 2, 9, 10]

print(count_occurrences(numbers, 2))  # Output: 3
print(sum_of_elements(numbers))       # Output: 45
print(max_element(numbers))           # Output: 10
print(min_element(numbers))           # Output: 2
print(check_element(numbers, 5))      # Output: True
print(first_element(numbers))         # Output: 4
print(last_element(numbers))          # Output: 10
print(slice_list(numbers))            # Output: [4, 2, 2]
print(reverse_list(numbers))          # Output: [10, 9, 2, 5, 6, 5, 2, 2, 4]
print(sort_list(numbers))             # Output: [2, 2, 2, 4, 5, 5, 6, 9, 10]
print(remove_duplicates(numbers))     # Output: [2, 4, 5, 6, 9, 10]
print(insert_element(numbers, 99, 3)) # Output: [..., 99, ...]
print(index_of_element(numbers, 5))   # Output: First index of 5
print(is_empty(numbers))              # Output: False
print(count_even(numbers))            # Output: 5
print(count_odd(numbers))             # Output: 4
print(concatenate_lists([1, 2], [3, 4])) # Output: [1, 2, 3, 4]
print(replace_element(numbers, 5, 100))  # Replaces first 5 with 100
print(second_largest(numbers))        # Output: 9
print(filter_even(numbers))           # Output: [4, 2, 2, 6, 2, 10]
print(find_all_indices(numbers, 2))   # Output: [1, 2, 6]
print(rotate_list(numbers, 3))        # Output: Rotated list

