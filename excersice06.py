# Define a function which takes 2 numberic list as an input
# and find the common element in the list

numberList1 = [1,23,7]
numberList2 = [2,4,1,6,12,22,23,12]

def findCommonNum(numberList1,numberList2):
    newList = []
    for item1 in numberList1:
        # for item2 in numberList2:
        #     if(item2 == item1):
        #         newList.append(item2)
        #         break
        if item1 in numberList2:
            newList.append(item1)
    return newList

print(findCommonNum(numberList1,numberList2))
print("file edited")