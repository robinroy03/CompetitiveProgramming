# Maximum Number of Applicants from NGOs
An MNC has a foundation which wants to provide seed fund for few Non-Governmental Organizations (NGO) committed to improve educational quality across the country. They make a call for this and circulate an online application. More than one member from a NGO can apply for the seed fund. A column in the online application ask for the number of applicants (NOA) excluding himself applying for the seed fund from the NGO to which the applicant belongs. Given ‘m’ random values of NOA column of the online application taken from few applicants of ‘k’ NGOs (where m>=k), write a code to find the maximum number of applicants from these ‘k’ NGOs.
```
Example 1

Input

5

7

2 3 3 3 3 1 1

Output

17

Explanation

We need to take five out of seven given values. Each different value should be belong to different NGOs, so 1,2,3 should be taken. And two more 3’s are taken. Value written in the form excludes the person who writes it so have to add 1 for each value taken

Example 2

Input

3

6

2 3 3 2 1 1

Output

9

Explanation

We need to take three out of six given values. Each different value should be belong to different NGOs, so 1,2,3 should be taken.

Example 3

Input

6

12

4 3 3 2 2 2 2 2 1 1 1 1

Output

19

Explanation

We need to take six values out of twelve given values. Each different value should be belong to different NGOs, so 1,2,3,4 should be taken. When we look at number of 1’s it is 4, for value of 1, only two enteries can be from same NGO. Therefore one more 1 that is two 1’s in total should be taken. When we look at number of 2’s it is 5, only three 2’s can be written from people of same NGO. Therefore we need to take one more 2 that is two 2’s in total. So the six values chosen are 1, 1, 2, 2, 3, 4 and one more value for each NGO should be added therefore maximum number of applicants will be 19.
```
### Input Format

First line contains the number of NGO’s, k

Next line contains the number of applicants considered, m

Next line contains the NOA values written by the m applicants separated by a space

### Output Format

Print the maximum number of applicants from k NGOs
