# Example variable argument:
# this is actually variable length argument
# this is of two types one of the dictionary type and another is of tuple type
def aver(*numbers):
    for i in numbers:
        c =c+ i
        avg = c/len(numbers)
    print(avg)
aver(1,2,3,4,4,5,5,6)

    
