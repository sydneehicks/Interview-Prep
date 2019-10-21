
#find the first element in a lit that does not repeat
def first_ele(list_1):
  for i in range(len(list_1)-1):
    if list_1[i] != list_1[i + 1]:
      return True
  return False    
list = [1, 1, 3, 3, 5, 6, 6]
list_1 = [2,2,2,2]
print(first_ele(list))
print(first_ele(list_1))
#taking in a string of open and close parentheses and check to see if they match
def parent_func(match):
  open = 0 
  close = 0
  for i in range(len(match)-1):
    if match[i] == '(':
     open += 1
    else:
      close +=1
    if open < close:
      return False
  if open == close:
    return True
  else: 
    return False
print(parent_func('(((()))'))
def  func(n):
  if n %2 == 0:
    while n > 0:
      print('bar')
      n -= 1
  else:
    while n > 0:
      print('bar')
      n -= 2
# if n is even, keep printing bar until n is less than 0 while decrementing n. if it isn't even it would print out 'foo' n - 2
def func_1(n):
  x = ''
  for i in range(n):
    x += str(n+1)
  return (x)
print(func_1(4))
#take in a number, add that number to one, and print that n+1 n times
#count the occurences of a num in a sorted array
def occur(list, num):
  count = 0
  for number in list:
    if number == num:
      count += 1
  return count
#write a function which takes in 2 strings and return true if they are anagrams
def anagram(string_one, string_two):
  dict_one = {}
  dict_two = {}
  for char in string_one:
    if char in dict_one:
      dict_one[char] += 1
    else:
      dict_one[char] = 1
  for char in string_two:
    if char in dict_two:
      dict_two[char] += 1
    else:
      dict_two[char] = 1
  if dict_one == dict_two:
    return True
#implement the exponent func. (exp(x,y))
def exp(num,expo):
  new_num = 1
  while expo > 0: 
    new_num *= num

#reverse a string without using the reverse() function or strinf[::-1]

def reverse(string_1):
  def bar(lst):
    x = lst[0]
    for i in range (len(lst)):
      if x > lst[i]:
        x = lst[i]
  return x
# write a function that takes in a list that contains 3 numbers and sorts them in ascending order. 
def three_ascend(list_1):
  list_3 = []
  if list_1[0] > list_1[1]:
    list_1[1] == list_1[0]
  elif list_1[2] > list_1[3]:
    list 
  return list_1
list_2 = [2,3,1]
print(three_ascend(list_2))
# write a function that takes in a list that contains 3 numbers and sorts them in ascending order. Do no use the sort method
def  three_nums(list_a):
 min = list_a[0]
 max = list_a[0]
 mid = list_a[0]
 for number in list_a:
   if number > max:
     max = number
  elif number < min:
    min = number
  else:
    mid = number
  new_list = [min, mid, max]
  return new_list
  
#Write a function that returns whether any two numbers in list add up to 10 (e.g [8, 7, 5, 2] -> True [9, 3, 2, 9])
def any_10(list_b):
  for i in range(len(list_b)):
    for j in range(len(list_b)):
      if list_b[i] + list_b[j] == 10:
        return True
    if list_b[i] == list_b[j]:
        return False
list_2 = [4,5,9,6]
print(any_10(list_2))
list_3 = [7,5,5,0]
print(any_10(list_3))

#given 2 lists of ints, write a function that finds all pairs that add up to 10 where one number comes from each list. (e.g. [8,7,5,2,11] and [3,-1,5,12] -> [(7,3), (5,5), (11,-1)])
def pairs_10(list_c, list_d):
  list_e = []
  for i in range(len(list_c)):
    for j in range(len(list_d)):
      if list_c[i] + list_d[j] == 10:
        list_e.append(list_c[i])
        list_e.append(list_d[j])
  return list_e
list_3 = [4,-4,6,7]
list_4 = [6,5,4,3]
print(pairs_10(list_3,list_4))

#implement a binary search on a sorted list. Return index of target value or -1 if it isn't in the list
def binary_search(list_f, num):
  i = len(list_f)//2
  if len(list_f) == 0:
    return -1
  if list_f[i] == num:
    return i
  if list_f[i] > num:
    result = binary_search(list_f[:i], num)
    return result
  else:
    return i + binary_search(list_f[i:], num)
  
#given a rectangular 2D list, return the sum of the edges of the list. (e.g[[1,1,1],[1,99,1],[1,1,1] -> 8])
def edges_list(list_g):
  for row in range(len(list_g)-1):
    for column in row:

#write a function which gives the median value in a list. Do not use the median() function. You may use sorted() or arr.sort()
def median(med_list):
  sort = sorted(med_list)
  if len(sort) % 2 == 1:
    middle = len(sort)//2
    return sort[middle]
  else:
    upper = len(sort)/2
    lower = upper - 1
    add = sort[upper] + sort[lower]
    med = add/2
    return med
  
list_1 = [5, 6, 8, 1, 3, 10]
print(median(list_1))
