# глассные (a,e,i,o,u)
slovo = input ("Введите слово ")
eg=slovo.count('e')
ag=slovo.count('a')
ig=slovo.count('i')
og=slovo.count('o')
ug=slovo.count('u')
summaglas=eg+ag+ig+og+ug
print("Всего глассных:",summaglas)
print("Всего согласных",len(slovo)-summaglas)
if(eg==0):
    print("e=False")
else:
    print("e=", eg)
if(ag==0):
    print("a=False")
else:
    print("a=", ag)
if(ig==0):
    print("i=False")
else:
    print("i=", ig)
if(og==0):
    print("o=False")
else:
    print("o=", og)
if(ug==0):
    print("u=False")
else:
    print("u=", ug)