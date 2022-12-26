# Substrings and Sweets
Ramu, a small boy loves to eat sweets. Whenever he gets time, he goes to a local sweet shop and buys sweets, but his father is really worried about Ramu’s Health and wants to make sure that he doesn’t eat more sweets. So he indulged Ramu in an interesting game. Everyday he will give Ramu a word 'w' and a number 'k'. Ramu will be allowed to buy only the number of sweets equal to the number of substrings with 'k' vowels that he generates from the given word 'w' . Ramu wants to get the maximum number of possible sweets. But Ramu doesn’t know what a substring is and also do not know how to count numbers, fortunately, he knows that you are a good programmer, so he has given this task to you. Given the word 'w' and number 'k', write a code to print the number of sweets that Ramu can get.

Vowels: a,e,i,o,u

A substring is a contiguous sequence of characters within a string. For example, string apple all possible substrings of length greater than or equal to one are apple, appl, pple, app, ppl, ple, ap, pp, pl, le, a, p, p, l, e.
 

### Input Format:

There are two lines of input, 

The first line contains the word given by Ramu’s father and,

The second line contains the value of k.

### Output Format:

Print only one integer, containing the value of sweets that Ramu can buy.
```
Example:

abc

1

All substrings of abc are:

 a, ab, abc, b, bc, c

Out of all these substrings a, ab and abc have 1 vowel exactly. 

Hence the answer is 3.
```
