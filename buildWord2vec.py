
import word2vec
import sys
import numpy as np

if(len(sys.argv) != 3):
    print "Wrong # of argvs"
    sys.exit(0)

print "Making phrase file"
word2vec.word2phrase(sys.argv[1], sys.argv[1]+"-phrase", verbose = True)

print "Making bin file"
word2vec.word2vec(sys.argv[1]+"-phrase", sys.argv[1]+".bin", size = 100, verbose = True)

print "Loading word2vec model"
model = word2vec.load(sys.argv[1]+".bin")

scoreList = []

print "Calculating score"
counter = 0
with open(sys.argv[2], 'r') as f:
    lines = f.readlines()
    for line in lines:
        if counter % 1000 == 0:
            print "# " + str(counter)
        chars = line.split()
        currentVec = 1
        for c in chars:
            decodedC = c.decode("utf-8")
            if decodedC in model.vocab:
                currentVec *= model[decodedC]
        scoreList.append(np.linalg.norm(currentVec))
        counter += 1

print "Making score tmp"
with open("tmpList.txt", 'w') as f:
    for score in scoreList:
        f.write(repr(score)+'\n')

print "Making prediction"
startPoint = 261955
numberOfEmoji = 40
counter = 0
writeList = ['Id,Emoticon']
while (counter + 1)* numberOfEmoji < len(scoreList):
    subList = scoreList[counter * numberOfEmoji: (counter+1) * numberOfEmoji]
    sortSubIndex = sorted(range(len(subList)), key=lambda k : subList[k])
    myId = startPoint + counter
    emotRank = ''
    for emotionIndex in sortSubIndex:
        emotRank += str(emotionIndex+1) + ' '
    writeList.append(str(myId)+ ', ' + emotRank)
    counter += 1

with open('prediction.csv', 'w') as f:
    for line in writeList:
        f.write(line+'\n')
