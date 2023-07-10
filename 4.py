n = int(input("Enter number of elements in list: "))
l = []
for i in range(n):
    e = int(input("Enter the value: "))
    l.append(e)

print("Original list: " + str(l))

flag = 0

l1 = l[:]
l1.sort()
if l1 == l:
    flag = 1

if flag:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
