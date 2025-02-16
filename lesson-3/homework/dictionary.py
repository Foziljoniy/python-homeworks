import random

# 1. Union of Sets
def union_sets(set1, set2):
    return set1 | set2  # Equivalent to set1.union(set2)

# 2. Intersection of Sets
def intersection_sets(set1, set2):
    return set1 & set2  # Equivalent to set1.intersection(set2)

# 3. Difference of Sets
def difference_sets(set1, set2):
    return set1 - set2  # Elements in set1 but not in set2

# 4. Check Subset
def is_subset(set1, set2):
    return set1.issubset(set2)

# 5. Check Element in Set
def check_element(set1, element):
    return element in set1

# 6. Set Length
def set_length(set1):
    return len(set1)

# 7. Convert List to Set
def list_to_set(lst):
    return set(lst)

# 8. Remove Element from Set
def remove_element(set1, element):
    set1.discard(element)  # Discard avoids errors if element doesn't exist
    return set1

# 9. Clear Set
def clear_set(set1):
    return set()  # Returns a new empty set

# 10. Check if Set is Empty
def is_empty_set(set1):
    return len(set1) == 0

# 11. Symmetric Difference
def symmetric_difference_sets(set1, set2):
    return set1 ^ set2  # Equivalent to set1.symmetric_difference(set2)

# 12. Add Element to Set
def add_element(set1, element):
    set1.add(element)
    return set1

# 13. Pop Element from Set
def pop_element(set1):
    return set1.pop() if set1 else None  # Pops an arbitrary element

# 14. Find Maximum in Set
def max_in_set(set1):
    return max(set1) if set1 else None

# 15. Find Minimum in Set
def min_in_set(set1):
    return min(set1) if set1 else None

# 16. Filter Even Numbers
def filter_even_numbers(set1):
    return {x for x in set1 if x % 2 == 0}

# 17. Filter Odd Numbers
def filter_odd_numbers(set1):
    return {x for x in set1 if x % 2 != 0}

# 18. Create a Set of a Range
def create_range_set(start, end):
    return set(range(start, end + 1))

# 19. Merge and Deduplicate Lists
def merge_lists_to_set(list1, list2):
    return set(list1 + list2)

# 20. Check Disjoint Sets
def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)

# 21. Remove Duplicates from List
def remove_duplicates(lst):
    return list(set(lst))

# 22. Count Unique Elements in List
def count_unique_elements(lst):
    return len(set(lst))

# 23. Generate Random Set
def generate_random_set(size, start, end):
    return {random.randint(start, end) for _ in range(size)}


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
num_list = [1, 2, 2, 3, 4, 4, 5, 5]

print(union_sets(set1, set2))               # {1, 2, 3, 4, 5, 6, 7, 8}
print(intersection_sets(set1, set2))        # {4, 5}
print(difference_sets(set1, set2))          # {1, 2, 3}
print(is_subset({1, 2}, set1))              # True
print(check_element(set1, 3))               # True
print(set_length(set1))                     # 5
print(list_to_set(num_list))                # {1, 2, 3, 4, 5}
print(remove_element(set1, 4))              # {1, 2, 3, 5}
print(clear_set(set1))                      # set()
print(is_empty_set(set()))                  # True
print(symmetric_difference_sets(set1, set2)) # {1, 2, 3, 6, 7, 8}
print(add_element(set1, 10))                # {1, 2, 3, 5, 10}
print(pop_element(set1))                    # Removes an arbitrary element
print(max_in_set(set1))                     # 5
print(min_in_set(set1))                     # 1
print(filter_even_numbers(set1))            # {2, 4}
print(filter_odd_numbers(set1))             # {1, 3, 5}
print(create_range_set(1, 10))              # {1, 2, 3, ..., 10}
print(merge_lists_to_set([1, 2], [2, 3]))   # {1, 2, 3}
print(check_disjoint_sets(set1, {6, 7}))    # True
print(remove_duplicates(num_list))          # [1, 2, 3, 4, 5]
print(count_unique_elements(num_list))      # 5
print(generate_random_set(5, 1, 50))        # Random set of 5 numbers
