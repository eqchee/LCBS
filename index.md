# Longest Common Bitonic Subsequence Algorithm



## About The Project

Given 2 sequences A and B containing hexadecimals, this algorithm has been designed to find the length of the longest common bitonic subsequence. 

To enhance the efficiency of the algorithm, the hexadecimals that are common to both sequences are shortlisted first. Then, dynamic programming is used to tabulate the length of the longest increasing subsequence and longest decreasing subsequence. Both tables are added up to determine the longest bitonic subsequence, deducting 1 so as to account of the duplication during the addition. 



## Time Complexity

The time complexity of this algorithm would be O(nm), where n is the number of inputs in list A and m is the number of inputs in list B. In the worst case scenario where all the inputs in list A are common to all the inputs in list B, the search for the longest common bitonic subsequence would require the outer for-loop to be executed n times and for each execution of the outer for-loop, the inner for-loop would be executed m times. Thus, the total number of operations from the nested for-loops would be nm based on product rule and the time complexity would be O(nm).
