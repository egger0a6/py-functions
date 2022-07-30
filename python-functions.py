def sum_to(n):
  '''-----------------------------------------------------------------------------
  #  function sum_to
  #
  #  purpose: recursive function that accepts a single integer and returns the
  #   sum of the integers from 1 to n
  #
  #  @param n : int 
  #
  #  returns: int
  -----------------------------------------------------------------------------'''
  return 1 if (n <= 1) else n + sum_to(n - 1)


def largest(numList):
  '''-----------------------------------------------------------------------------
  #  function largest
  #
  #  purpose: recursive function that accepts a list of integers and returns the
  #   largest number in that list
  #
  #  @param numList : list of integers
  #
  #  returns: int
  -----------------------------------------------------------------------------'''
  def largest_helper(numList, max):
    if numList[-1] > max: max = numList[-1]
    if len(numList) <= 1: return max
    numList.pop()
    return largest_helper(numList, max)
  
  return largest_helper(numList, numList[-1])


def occurences(str1, str2):
  '''-----------------------------------------------------------------------------
  #  function occurences
  #
  #  purpose: recursive function that takes 2 string arguments and counts the 
  #   number of occurences of the second string inside the first
  #
  #  @param str1 : string
  #  @param str2 : string
  #
  #  returns: int
  -----------------------------------------------------------------------------'''
  def occurance_count(str1, str2):
    if (str1.find(str2) == -1 or len(str1) < len(str2)): return 0
    index = str1.find(str2)
    return 1 + occurance_count(str1[index+1:], str2)
  
  return occurance_count(str1, str2)


def product(*nums):
  '''-----------------------------------------------------------------------------
  #  function product
  #
  #  purpose: recursive function that accepts arbitrary amount of numbers and 
  #   returns the product of them all multiplied together
  #
  #  @param *nums : arbitrary number of numbers
  #
  #  returns: int or float
  -----------------------------------------------------------------------------'''
  def product_with_index(nums, idx):
    if (idx == len(nums)): return 1
    return nums[idx] * product_with_index(nums, idx+1)
  
  return product_with_index(nums, 0)