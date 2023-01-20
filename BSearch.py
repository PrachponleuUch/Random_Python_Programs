def bSearch(OGlist, target):
    list = OGlist[:] # Copy list NOT BY REFERENCE
    list.sort()
    middle = 0
    start = 0
    end = len(list)
    steps=0
    
    while start <= end:
        print("Steps",steps,":", list[start:end+1])
        steps += 1
        middle = (start+end) // 2
        if target == list[middle]:
            return f"FOUND at location {middle}"
        elif target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    return "NOT FOUND"
    
list = [2,34,5,7,54,3,45,6,43,46,56,44]
target = int(input("Please enter a number to search: "))
print(bSearch(list, target))
print(list)
