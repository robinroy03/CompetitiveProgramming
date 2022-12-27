f = open("input7.txt",'r')
l = f.readlines()
f.close()

file=dict()             # key as file directory, value as size
current_directory=[]    # to identify the current directory
file_location=[]        # to store all file location similar to "file" dictionary
directories=[]          # to store all directory locations
directory_size=dict()   # key as directory name, value as size

for i in l:
    i=i.rstrip()
    if i.startswith("$ cd "):
        if i[5:]=="..":
            current_directory.pop()
        else:
            current_directory.append(i[5:])
            directories.append("/".join(current_directory))
    elif i[0].isdigit():
        size,name=i.split()
        file["/".join(current_directory)+"/"+name]=size
        file_location.append("/".join(current_directory)+"/"+name)

sum_=0      # sum for part 1

for directory in directories:
    size=0
    for files in file_location:
        if files.startswith(directory):
            size+=int(file[files])
    directory_size[directory]=size
    if size<=100000:
        sum_+=size

print(sum_)  # part 1 solution 

to_delete=30000000-(70000000-directory_size["slash"])   # a directory of size >= this size to be deleted
list_=[]                                                # list to store size of all those directories

for k,v in directory_size.items():
    if v>=to_delete:
        list_.append(v)

list_.sort()
print(list_[0]) # part 2 solution
