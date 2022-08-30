from collections import defaultdict

def group_anagram(w):
    d = defaultdict(list)
    
    for i in w:
        sorted_i = ''.join(sorted(i))
        d[sorted_i].append(i)
    return d.values()
        


words = ["tea", "eat", "bat", "ate", "arc", "car" ]

print(group_anagram(words))
