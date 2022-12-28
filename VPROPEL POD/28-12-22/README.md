# Selection of lucky winner
In a cinema theatre named 'w', with `n' seats, whenever the theatre is full (i.e., when all the seats are occupied), theatre administartion will be gifting a viewer with a surprise gift and the lucky viewer will be chosen through the following process, called as the  'Character allottment process'.

Character allotment process :

1. Starting from the first seat, allot a character  of "w" ( starting from the first character) to each seat.  That is, allot the first character of w to the seat no.1, allot the second character of  `w' to the seat no.2 and so on.

2. If all the characters of "w" are allotted, then continue the allotment from the first symbol of "w" again.

3. After allotting a character to the last seat, continue the allotment process by allotting the next character (character,  next to the character allotted to the last seat earlier) from the last seat 

4. Continue allotting the characters  till the first seat.

5. In the process, all the seats would have two characters allotted to each seat, one character during the forward allottment process  (when the characters are allotted from the first seat to the last seat) and another during the backward allottement process. (when the characters are allotted from the last seat to the first seat)

6. The first seat which gets the same character during both the forward allottment process and the backward allottment process is the lucky seat.

7. The person occupying the luck seat is given the surprise gift.

For eg, Name of the theatre : good.  Total number of seats : 10  During the forward allottment, seats are allotted as : 1-g, 2-o, 3-o, 4-d,5-g, 6-o, 7-o, 8-d, 9-g, 10-o

and during reverse allotment process 10-o, 9-d, 8-g, 7-o, 6-o, 5-d, 4-g, 3-o, 2-o, 1-d. The first seat to get the same characters in both the allottment is the seat no : 10.  The person who occupied the seat no. 10 is the lucky winner.

Given the name of the theatre `w', the total number of seats in the theatre, write an algorithm and the code to identify the lucky seat. Print -1 if no seat number could get the same letters.

### Input format :

Name of the theatre: w

Total number of  seats in the theatre: n

### Output format :

The seat number of the lucky seat.
