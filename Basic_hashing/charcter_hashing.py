import numpy as np
hsar=np.zeros(256,dtype=int)
instr=input("Enter the string => ")
for i in range(len(instr)):
    hsar[ord(instr[i])]=hsar[ord(instr[i])]+1
while True:
    a=input("Enter the character for get it frequency in that string for exit press 'No' = ")
    if a=='no' or a=='NO' or a=='No' or a=='nO':
        break
    print("The frequency of this character is ",hsar[ord(a)])