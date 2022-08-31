def findMissing(n):
    print(n)
    output = []
    for i in range(1, n[-1]):
        if i not in n:
            output.append(i)
    return output

list_of_number = [1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 13]
print(findMissing(list_of_number))