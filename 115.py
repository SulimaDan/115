# def product_of_list(lst):
#     product = 1
#     for num in lst:
#         product *= num
#     return product


# numbers = [1, 2, 3, 4, 5]
# result = product_of_list(numbers)
# print(result)  









# def find_minimum(lst):
#     if not lst: 
#         return None
#     minimum = lst[0]
#     for num in lst:
#         if num < minimum:
#             minimum = num
#     return minimum


# numbers = [3, 11, 19, 31, -5, 9, -62, 6, 10]
# result = find_minimum(numbers)
# print(result) 







# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def count_primes(lst):
#     return sum(1 for num in lst if is_prime(num))


# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# result = count_primes(numbers)
# print(result) 







# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True






# def count_primes(lst):
#     count = 0
#     for num in lst:
#         if is_prime(num):
#             count += 1
#     return count

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# result = count_primes(numbers)
# print(result)






# def remove_element(lst, element):
#     original_length = len(lst)
#     lst[:] = [x for x in lst if x != element]
#     new_length = len(lst)
#     return original_length - new_length

# numbers = [1, 2, 3, 4, 2, 5, 2, 6]
# element_to_remove = 2
# count_removed = remove_element(numbers, element_to_remove)
# print(count_removed) 
# print(numbers)  



def merge_lists(lst1, lst2):
    return lst1 + lst2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = merge_lists(list1, list2)
print(merged_list) 






