#Using a loop to write multiple lines
with open("writefile2.txt", "w") as f:
    n = int(input("Enter the number of data you wanna enter:"))
    print("ENter multiple data of the user :")
    for i in range(n):
        data = list(input().split())
        a = ",".join(data)
        f.write(a + "\n")