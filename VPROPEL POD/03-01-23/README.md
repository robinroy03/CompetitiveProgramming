# Tranformation of Three Digit Numbers
Dattatreya Ramchandra Kaprekar (1905–1986) was an Indian recreational mathematician who described several classes of natural numbers. He observed that any three digit number with at least two different digits gets transformed to 495 while the following steps are followed:
```
1) Arrange the digits of number ‘n’ in ascending and then in descending order to get two four-digit numbers, m1 and m2.
2) Compute the difference diff between m1 and m2
3) If diff is not 495 then go to Step 1.
```
Given a three digit number, write a code to check if the number can be transformed to 495 following above procedure. Print the number of steps for the transformation if the number can be transformed and print No otherwise.
```
Example 1

100

5

Explanation

100 is transformed to 495 in five steps as shown below

100 – 001 = 099
990 – 099 = 891
981 – 189 = 792
972 – 279 = 693
963 – 369 = 594
954 – 459 = 495

Example 2

222

No
```
### Input Format

First line contains the number n

### Output format

Print the number of steps taken for transformation or No
