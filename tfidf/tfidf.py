
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.cross_validation import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from datetime import datetime

fNumber = 250

with open(sys.argv[1], 'r') as f:
    print "Reaing training file"
    vec = TfidfVectorizer(min_df = 1 , max_df = 0.7, max_features = fNumber, ngram_range = (3,3))
    features = vec.fit_transform(f.readlines())
    print "Transforming sparse into dense matrix"
    dense = features.toarray()
    print "Reduce dense matrix"
    pca = PCA(n_components = fNumber/2)
    X_train = pca.fit_transform(np.array(dense))
    print X_train.shape

with open(sys.argv[2], 'r') as f:
    print "Reading test file"
    featuresTest = vec.transform(f.readlines())
    print "Transforming sparse into dense matrix"
    dense = featuresTest.toarray()
    # DO NOT Re-fit test data
    print "Reduce dense matrix"
    X_test = pca.transform(np.array(dense))
    print X_test.shape


bestModels = []
from sklearn.externals import joblib
for i in range(1, 41):
    print "Classifier ", i
    with open('../corpus/label/' + str(i) + '.txt', 'r') as f:
        Y_train = np.array(f.readlines())
    kf = KFold(X_train.shape[0], n_folds = 7, shuffle = True)
    fold = 0
    bestScore, bestModel = 0, 0
    for trainIndex, testIndex in kf:
        X_val_train, X_val_test = X_train[trainIndex], X_train[testIndex]
        Y_val_train, Y_val_test = Y_train[trainIndex], Y_train[testIndex]
        clf = LogisticRegression(C=1.0)
        clf.fit(X_val_train, Y_val_train)
        thisScore = clf.score(X_val_test, Y_val_test)
        print "fold # ", fold  , " score ", thisScore
        if thisScore > bestScore:
            bestModel = clf
        fold += 1

    bestModels.append(bestModel)

allTrainScore = []
print "Making train data precision"
for i in range(0, len(bestModels)):
    thisTrainScore = bestModels[i].predict_proba(X_train)
    tmp = []
    for s in thisTrainScore:
        tmp.append(s[1])
    allTrainScore.append(tmp)
allTrainScore = np.array(allTrainScore)
print allTrainScore.shape
with open('../corpus/label/allLabel.txt', 'r') as f:
   allLabel = f.readlines() 
predictionTrain = np.argsort(allTrainScore, axis=0)[::-1]
trainScore = 0
for labalIndex in range(len(allLabel)):
    if str(allLabel[labalIndex]) == str(predictionTrain[:, labalIndex][0]):
        trainScore += 1
    elif str(allLabel[labalIndex] == str(predictionTrain[:, labalIndex][1])):
        trainScore += .5
    elif str(allLabel[labalIndex] == str(predictionTrain[:, labalIndex][2])):
        trainScore += .33
print "Train score : ",trainScore / len(allLabel)

allTestScore  = []
for i in range(0, len(bestModels)):
    thisTestScore = bestModels[i].predict_proba(X_test)
    tmp = []
    for s in thisTestScore:
        tmp.append(s[1]) # Predict prob. to be true
    allTestScore.append(tmp)

print "Making prediction"
allTestScore = np.array(allTestScore)
print allTestScore.shape
startPoint = 261955
prefix = 'Id,Emoticon'
prediction = np.argsort(np.array(allTestScore), axis = 0)[::-1]
with open('prediction'+str(datetime.now())+'.csv', 'w') as f:
    f.write(prefix+'\n')
    for i in range(len(prediction[0])):
        prediction_i = prediction[:, i]
        newString = ''
        for index in prediction_i:
            newString += (str(index) + ' ')
        f.write(str(startPoint+i)+','+newString+'\n')

