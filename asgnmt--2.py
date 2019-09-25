def syllables(word):
    c = 0
    vowels = 'aeiou'
    word = word.lower()
    if word[0] in vowels:
        c +=1
    for i in range(1,len(word)):
        if word[i] in vowels and word[i-1] not in vowels:
            c+=1
    if word.endswith('e'):
        c-= 1
    if word.endswith('es'):
        c-= 1
    if word.endswith('le'):
        c+=1
    if c== 0:
        c+=1
    return c

path=input("Enter the path of file: ")
file=open(path,'r')
a=file.readlines()
sentence=0
word=0
syllab=0
for line in a:
    sentence+= line.count('.')+line.count('!')+line.count('?')
    word+=line.count(' ')
    syllab+= syllables(line)
F = 5206.835-(1.015 *(word / sentence)) - (84.6 * (syllab / word))
G = 50.39 * ((word / sentence)*111.8)* (syllab / word) - 15.59
print("The number of words in the file is:",word)
print("The number of sentences in the file is:",sentence)
print("The number of syllables in the file is:",syllab)
print("The Flesch index for the file is:",F)
print("The grade level is:")
if(0<=G<=30):
    print("College")
elif(50<=G<=60):
    print("High School")
elif(90<=G<=100):
    print("Fourth Grade")
    


