file = open("text.txt","r+")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for item in wordcount.items():
    print("{}\t{}".format(*item))
    print("{}\t{}".format(*item),file=open("text.txt", "a"))
file.close();
