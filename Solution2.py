l = input().split(',')
i1 = l.index('5')
i2 = l.index('8')

list1 = l[i1:i2+1]

list2 = [int(i) for i in l if i not in list1]

print(sum(list2) + int("".join(list1)))
