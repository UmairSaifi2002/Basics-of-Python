# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

# # by me
# def count_word_frequency(words):
#     output = {word : words.count(word) for word in words }
#     return output

# # by sir
# # def count_word_frequency(words):
# #     word_count = {}
# #     for word in words:
# #         word_count[word] = word_count.get(word, 0) + 1
# #     return word_count

# print(count_word_frequency(words))

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------

# Common Keys
# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

# Example:

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}

# def merge_dicts(dict1, dict2):
    # by sir
    # result = dict1.copy()
    # for key, value in dict2.items():
    #     result[key] = result.get(key, 0) + value
    # return result

    # by me
#     output = {key:value for key,value in dict1.items()}
#     for key in dict2:
#         if key in dict1:
#             total = dict1[key] + dict2[key]
#             output[key] = total
#         else:
#             output[key] = dict2[key]
#     return output
        
# print(merge_dicts(dict1,dict2)) # {'a': 1, 'b': 5, 'c': 7, 'd': 5}

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

# Example:

# my_dict = {'a': 5, 'b': 9, 'c': 2}

# def max_value_key(my_dict):
    # by me
    # maxKey = ''
    # curr = 0
    # for key,value in my_dict.items():
    #     if curr < value :
    #         # print(curr)
    #         curr = value
    #         # print(curr)
    #         maxKey = key
    # return maxKey
    # by sir
#     return max(my_dict, key=my_dict.get)

# print(max_value_key(my_dict))

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Reverse Key-Value Pairs
# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

# Example:

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# def reverse_dict(my_dict):
#     # BY ME
#     key = list(my_dict.values())
#     value = list(my_dict.keys())
#     my_dict.clear()
#     for i in range(len(key)):
#         my_dict[key[i]] = value[i]
#     return my_dict
        # BY SIR
    #   return {v: k for k, v in my_dict.items()}

# print(reverse_dict(my_dict))

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

# Example:

# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# def filter_dict(my_dict, condition):
#     return {k:v for k,v in my_dict.items() if condition(k,v)}

# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
# print(filtered_dict)

# # ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ---------- X ----------
# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

# Example:

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

# def check_same_frequency(list1, list2):
#    

# print(check_same_frequency(list1, list2))
