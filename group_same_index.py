input_lists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
output_lists = []
index = 0

for li in range(len(input_lists[0])):
    output_lists.append([])
    for j in range(len(input_lists)):
        output_lists[index].append(input_lists[j][index])
    index += 1
    
print(output_lists)
