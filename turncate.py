with open("file1.txt","a") as f:
    f.truncate(6)
with open("file1.txt","r") as f:
    print(f.read())