with open("file1.txt","r") as f:
    current_position = f.tell()
    print(current_position)
    print(f.read(2))
    f.seek(4)
    print(f.tell())
    print(f.read(2))