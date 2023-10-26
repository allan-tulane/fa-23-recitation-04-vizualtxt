import random
import time

import tabulate


def qsort(a, pivot_fn):

  if len(a) == 0 or len(a) == 1:
    return a
  p = pivot_fn(a)
  left = list(filter(lambda x: x<p, a))
  right  = list(filter(lambda x: x>p, a))

  (sL, sR) = (qsort(left, pivot_fn), qsort(right, pivot_fn))
  
  return sL + [p] + sR

  pass

def ssort(L):
  for i in range(len(L)):
      #print(L)
      m = L.index(min(L[i:]))
      L[i], L[m] = L[m], L[i]
  return L

def time_search(sort_fn, mylist):
  """
  Return the number of milliseconds to run this
  sort function on this list.

  Note 1: `sort_fn` parameter is a function.
  Note 2: time.time() returns the current time in seconds. 
  You'll have to multiple by 1000 to get milliseconds.

  Params:
    sort_fn.....the search function
    mylist......the list to search
    key.........the search key 

  Returns:
    the number of milliseconds it takes to run this
    search function on this input.
  """
  timeArr = []
  for i in range(10):
    start = time.time()
    sort_fn(mylist)
    runt = (time.time() - start) * 1000
    timeArr.append(runt)
  return (sum(timeArr)/len(timeArr))


  ###

def compare_sort(sizes=[10, 100, 200, 300, 400, 500, 1000, 2000, 5000, 10000]):
  """
  Compare the running time of different sorting algorithms.

  Returns:
    A list of tuples of the form
    (n, linear_search_time, binary_search_time)
    indicating the number of milliseconds it takes
    for each method to run on each value of n
  """
  ### TODO - sorting algorithms for comparison
  def qsort_fixed_pivot(a):
    return qsort(a, lambda x: x[0])
  def qsort_random_pivot(a):
    return qsort(a, random.choice)
  tim_sort = sorted
  result = []
  for size in sizes:
      # create list in ascending order
      mylist = list(range(size))
      # shuffles list if needed
      random.shuffle(mylist)
    
      result.append([
          len(mylist),
          time_search(qsort_fixed_pivot, mylist),
          time_search(qsort_random_pivot, mylist),
          time_search(tim_sort, mylist),
      ])
  return result
  ###

def print_results(results):
  """ change as needed for comparisons """
  print(tabulate.tabulate(results,
                          headers=['n', 'qsort-fixed-pivot', 
                                   'qsort-random-pivot', 
                                   'timsort'],
                          floatfmt=".3f",
                          tablefmt="github"))

def test_print():
  print_results(compare_sort())

random.seed()
test_print()
