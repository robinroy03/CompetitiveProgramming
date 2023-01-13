# File System
A file system is a collection of files arranged in a particular order for easier access, search, editing etc. The Simple File System(SFS), has one root mount which is denoted using ‘/’.

Each file is a descendant of ‘/’. A directory is a special kind of file that can have other files organised within it. SFS also allows a user to move files from one location to another throughout the file system. SFS only allows a user to move files to a different directory only when there is no naming conflict.

For example: consider this:

 
[ image ]

Now consider if we have to move a file named a.txt from ‘/home/user/’ to ‘/opt/java’. We see that a file named a.txt already exists at the given location, so we cannot move it, however we can move ‘/usr/local/x.cpp’ to ‘/home/user/’ as there is no naming conflict. The names of all files are internally represented using IDs which are natural numbers. For example ‘/’ may have an id of 1, ‘home’ may have an id of 2 and ‘a.txt’ may have an id of 62 and so on.... each of these files have a corresponding ID. You will be asked various queries of the `<source> <destination> <filename>` and you have to tell ‘yes’ or ‘no’ (without quotes) if the files can be moved from source to destination or not.

```
Consider the above example:

Given the queries of the form:

/home/user /home a.txt

/home/user /opt/java a.txt

/lib/cpp /usr/local d.txt

 

For the first one we are moving a.txt from /home/user to /home which is possible as there is no naming conflict, so we say yes.

We are moving a.txt from /home/user to /opt/java . A file named a.txt already exists in the destination hence, we say no.

We are moving d.txt from /lib/cpp to /usr/local. As no file exists with the same name in destination we say yes.
```
 
```
Note:

(i) There are no duplicates in directory but duplicates are there in files

(ii) All file names have an extension separated by a dot '.' and directories do not have extensions

(iii) It is guaranteed that the path given will be valid and the files with given names in the queries will be present and source and destination will not be same.
```

### Input format:

First line contains a single integer denoting the number of files, N

Second line contains a single integer denoting the edges in the file system, M

Next M lines contain two natural numbers separated by a space denoting the ids of the files joined by the edge.

Next line contains N space separated strings and the names of all the files.

Next line contains a positive integer Q denoting the number of queries.

Next Q lines contain queries of the form <string> <destination> <filename>, each separated by a space.

### Output format:

Output Q lines each containing a single string ‘yes’ or ‘no’ (without quotes), if the file can be moved or not.

```
Example:

Input:

15

14

1 2

1 3

1 4

1 5

2 6

3 7

4 8

5 9

6 10

7 11

7 12

8 13

8 14

9 15

/ home opt lib usr user java cpp local a.txt a.txt b.txt d.txt e.txt x.cpp

3

/home/user /home a.txt

/home/user /opt/java a.txt

/lib/cpp /usr/local d.txt

Output:

yes

no

yes
```
 

Explanation:

IDs of the files are as:

/ - 1

home - 2

opt - 3 and so on

The rest of the explanation can be taken from the example given in the problem.