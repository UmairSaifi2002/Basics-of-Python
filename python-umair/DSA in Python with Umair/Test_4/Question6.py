# What will be the output of the following code block?

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)

'''
Here's a step-by-step explanation of the code block:

fruit_list1 is defined with four fruit names.

fruit_list2 is assigned the reference of fruit_list1, so both lists now point to the same memory location. Any changes made to either of them will be reflected in the other.

fruit_list3 is assigned a slice of fruit_list1 that includes all elements. This creates a new, shallow copy of the list, so changes made to fruit_list3 won't affect fruit_list1 or fruit_list2.

The first element of fruit_list2 is changed to 'Guava'. Since fruit_list1 and fruit_list2 refer to the same list, the first element of fruit_list1 is also changed to 'Guava'.

The second element of fruit_list3 is changed to 'Kiwi'. This does not affect fruit_list1 or fruit_list2.

A variable sum is initialized with the value 0.

A for loop iterates over a tuple containing fruit_list1, fruit_list2, and fruit_list3.

If the first element of the current list is 'Guava', sum is incremented by 1.

If the second element of the current list is 'Kiwi', sum is incremented by 20.

The final value of sum is printed.

After the modifications, the lists are as follows:

fruit_list1: ['Guava', 'Berry', 'Cherry', 'Papaya']

fruit_list2: ['Guava', 'Berry', 'Cherry', 'Papaya'] (same as fruit_list1)

fruit_list3: ['Apple', 'Kiwi', 'Cherry', 'Papaya']

Now let's calculate the sum:

For fruit_list1: sum += 1 (first element is 'Guava') = 1

For fruit_list2: sum += 1 (first element is 'Guava') = 2

For fruit_list3: sum += 20 (second element is 'Kiwi') = 22

So, the output of the code block will be:

22
'''