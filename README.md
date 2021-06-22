## Subset
if we have the set (Math's term) of integer (list, in python) such as [1,2,3,4] called **super set**, the number of subset will be 2<sup>len([1,2,3,4])</sup>, and each subset will have either 1, 2, 3, or 4 elements, and each element is ele
## Idea of finding sub set
we'll use the index of super set instead of its value to find all sub set and then match back to the value of super set
- in case of 2 element ( the other n elements will use the same idea)
	1. find the initial index of sub set
		> here, in case of 2 elements : [0, 1]
		>  if 3 element will be [0,1,2]
	
	2. increase the value of the last index of the initial sub set
	3. when increase the last value of initial sub set and get value equal to  the length of super set, we'll create a new initial sub set like,
	
	
	> initial index of sub set : [0,1] increase the last index will get [0,2], ?>  	[0,3], [0,4] we will notice the index 4 in sub set can not match to the index of super set, so in this we'll create the new initial sub set as [1, 2]
	
	4. when continue increasing and find that the first index of the initial sub set be like [4, N] we'll notice that the first index is 4 and can not match to the index of super set , in the case show that can not continue with the 2 element of sub set.

| 1 st index | last index  |
|--|--|
| 0 |1  |
|0	|	2( 1+1)|
|0	|3 (2+1)	|
| 0|4 this can't be, increase the value prior this index|
|1|2|
|1|3|
|1|<span style="color:red">4</span>|
|2|3|
|2|<span style="color:red">4</span>|
|3|<span style="color:red">4</span>|
|<span style="color:red">4</span>  the case of 2 elements end herer|5|

