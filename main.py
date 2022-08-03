name=input(" name ")
char=[]
for  i in name:
    if i not in char:
        char.append(i)
    else:
        continue
if len(char)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM !")

