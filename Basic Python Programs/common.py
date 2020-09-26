str1=input()
str2=input()
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str1[i] != " " and str1[i] == str2[j]:
            print(str1[i],end="")
            flag=1
            break
print("")
if not flag:
    print("-1")
