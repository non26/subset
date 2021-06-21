`This code's looking for all sub set of the given list of float number' `
if we have a list, [1,2,3,4], so the index of that list is [0,1,2,3], so the length is 4

in case of  2 element:

+[0, 1]<br>
+[0, 2]<br>
+[0, 3]<br>
-[0, 4]<br> you will see that the value at the last index is 4, but the list don't have 4th index,
so this is where we change the first index to 0+1=1,
+[1,2]<br>
+[1,3]<br>
-[1,4]<br> again, we don't the 4th index, so increase the first value to 1+1=2
-[2,3]<br>
-[2,4]<br>
-[3,4]<br>
-[4,5]<br>at this set we'll see that the first index holding the value of 4, which is the
length of the super set, so this is the end of the subset where 2 element in the sub set being considering.

so the index of sub set that we use here is the list which prefix with +