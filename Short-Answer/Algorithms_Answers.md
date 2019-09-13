#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): Amount of time while loop will run is proportional to the size of n.


b) O(n^3): has to loop 2 times , plus find if j is even


c) O(n): runs on time per each bunny


## Exercise II
 Binary search is my answer:
   1) Create a list of floors up to n.
   2) Find mid_floor by creating low_floor = mid_floor-1  and high_floor = mid-floor+1
   3)drop the an egg from mid_floor and check if it breaks
   4) if it did, repeat step (2)and step (5) on low_floor list if not pass (5) repeat steps (2) and (5) on the high_floor list
   5)once you find the floor where it does break , but it didn't on the floor before, you found f.

