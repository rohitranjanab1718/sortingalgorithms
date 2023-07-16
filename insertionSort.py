# 12 11 13 5 6
# 1st pass
# 11 12 13 5 6
# 2nd pass
# 11 12 13 5 6
# 3rd pass
# 11 12 5 13 6
# 11 5 12 13 6
# 5 11 12 13 6
# 4th pass
# 5 11 12 6 13
# 5 11 6 12 13
# 5 6 11 12 13

def insertion_sort(li):
    for i in range(1, len(li)):
        key = li[i]
        j = i-1
        while j >= 0 and key < li[j]:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = key
    return li


arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))

