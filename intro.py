introduction=input("write something about you")
characterCount=0
wordCount=1
print(introduction)
for i in introduction:
    characterCount=characterCount+1
    if(i==" "):
        wordCount=wordCount+1
print("no. words in the string")  
print(wordCount)
print("no. of characters in the paragraph")
print(characterCount)      
