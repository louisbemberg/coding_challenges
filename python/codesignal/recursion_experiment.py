def recursion(count=0):
    count +=1
    if count == 10:
        return "Stop doing recursion after 10 loops :)"
    recursion(count)
    print(count)
    return count

print(recursion())
