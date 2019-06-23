S = input("Enter the String: ")
K = int(input("Enter the length: "))
temp = []
len_temp = 0
for item in S:
    len_temp += 1
    if item not in temp:
        temp.append(item)
    if len_temp == K:
        print(''.join(temp))
        len_temp = 0
        temp=[]