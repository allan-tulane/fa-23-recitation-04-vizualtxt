# CMPS 2200 Reciation 5
## Answers

**Name:** Ali Sulehria


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**
The table below lists the averages over ten runs of three sorting algorithms for various values of n. We can see that random pivot quicksort takes a similar, though slightly shorter, time to complete as compared to the fixed pivot. The selection short performs favorably for small lists, but grows much too quickly. 

|     n |   qsort-fixed-pivot |   qsort-random-pivot |    ssort |
|-------|---------------------|----------------------|----------|
|    10 |               0.020 |                0.026 |    0.008 |
|   100 |               0.203 |                0.328 |    0.211 |
|   200 |               0.764 |                0.721 |    1.376 |
|   300 |               3.845 |                2.518 |    2.160 |
|   400 |               1.112 |                5.418 |    6.109 |
|   500 |               6.890 |                9.872 |   20.209 |
|  1000 |              12.995 |                5.925 |   37.593 |
|  2000 |              12.079 |               19.113 |  138.135 |
|  5000 |              53.636 |               45.270 |  923.664 |
| 10000 |              99.795 |              111.526 | 3734.287 |

The random and fixed pivot, both being quicksort, are of the order O(n) = log^2(n), which holds for these recurrences. 

For the case where the input is in order, the quicksort algorithms performed similarly. This is likely because the quicksort algorithm's speed isn't very dependent on whether the list is sorted or not - the only way to change it would be by changing the pivot selection function and the inputs.

- **1c.**

|     n |   qsort-fixed-pivot |   qsort-random-pivot |   timsort |
|-------|---------------------|----------------------|-----------|
|    10 |               0.000 |                0.000 |     0.000 |
|   100 |               1.000 |                1.001 |     0.000 |
|   200 |               0.994 |                2.652 |     0.000 |
|   300 |               2.339 |                2.032 |     0.000 |
|   400 |               4.000 |                3.000 |     0.000 |
|   500 |               3.955 |                5.175 |     0.000 |
|  1000 |               8.958 |               11.113 |     0.281 |
|  2000 |              11.959 |               16.287 |     1.005 |
|  5000 |              42.298 |               46.584 |     0.809 |
| 10000 |              87.956 |               92.281 |     3.060 |

Tim blew my sorting algorithms out of the water and it's really not very fair. The algorithm is significantly faster at every value. wow!