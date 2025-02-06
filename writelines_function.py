# This creates lines in a file 
with open("writefile.txt","w") as f:
    write = ["1\n","line2\n","line3\n"]
    f.writelines(write)
