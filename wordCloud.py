import wordcloud

file=open("YOUR FILE PATH GOES HERE ",'r')
words=file.read()
file.close()

"""
#THIS IS JUST ANOTHER WAY TO PARSE THE WORDS IN YOUR FILE
#ex: Hello!! There  removes '!!' from Hello

words=words.split()
for i in range(len(words)):
    word=""
    if not words[i].isalpha():
        for j in range(len(words[i])):
            if words[i][j].isalpha():
                word+=words[i][j]
        words[i]=word

print(words)
                
"""
#
print(words)
i=0
while i<len(words):
    if not words[i].isalpha() and not words[i]==' ' :
        words=words[:i]+words[i+1:]
        i-=1
    i+=1
words=words.split()


worddict={}
for word in words:
    if len(word)>3:#discarding all words having length less than 3 remove this line if you want all words
        if word not in worddict.keys():
            worddict[word]=1
        elif word in worddict.keys():
            worddict[word]+=1
        else:
            print("Somethings Fishy Here")

print(worddict)

cloud=wordcloud.WordCloud()
cloud.generate_from_frequencies(worddict)
cloud.to_file("myfile.jpg")#name of your image file
