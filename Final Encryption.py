# Final Encryption


import string 
import random
alphabet=string.printable
print(alphabet)
#print(len(alphabet))
key='qwerty'#to be more general
#key=alphabet.find(key)/ #comment this if using random.randint

newmessage=''
newmessage2=''

message=input('enter a new message : ')

'''for character in message:
    for i in key:
        a=key.index(i)
        b=message.index(character)
        if a==b:
            
            newkey=alphabet.find(i)
            #print(newkey)
            position=alphabet.find(character)
           # print(position)
            newposition=(position+newkey)%len(alphabet)
            #print(newposition)
            newcharacter=alphabet[newposition]
            #print(newcharacter)
            newmessage+=newcharacter
        #else:'''
           
for character, num in zip(message, range(len(message))):
    i=key[(num%len(key))]
    #a=key.index(i)
    #print(a)
    #a=a%len(key)
    #print(a)
    newkey=alphabet.find(i)
    position=alphabet.find(character)
    newposition=(position+newkey)%len(alphabet)
    newcharacter=alphabet[newposition]
    newmessage+=newcharacter
print("Encrypted message : ", newmessage)
#print("Decryption key : ", key)
