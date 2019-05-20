#encoding=utf-8
import jieba
from jieba import posseg
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from numpy import *

def createVocabList(dataSet):
    vocabSet = set([])  #create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document) #union of the two sets
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: pass#print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def trainNB0(trainMatrix,trainCategory):#分为五类
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    A =0;B =0;C =0;D =0;E =0
    for i in trainCategory:
        if i == 1:
            A = A+1
        if i == 2:
            B = B+1
        if i == 3:
            C =C+1
        if i == 4:
            D = D+1
        if i == 5:
            E = E+1

    pAbusive = A/(float(numTrainDocs)) #标示符为1
    pBbusive = B/(float(numTrainDocs)) #标示符为2
    pCbusive = C/(float(numTrainDocs)) #标示符为3
    pDbusive = D/(float(numTrainDocs)) #标示符为4
    pEbusive = E/(float(numTrainDocs)) #标示符为5
    p1Num = ones(numWords); p2Num = ones(numWords); p3Num = ones(numWords);p4Num = ones(numWords);p5Num = ones(numWords)     #change to ones()
    p1Denom = 5.0; p2Denom = 5.0 ; p3Denom = 5.0;p4Denom = 5.0;p5Denom = 5.0                   #change to 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 2 :
            p2Num += trainMatrix[i]
            p2Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 3 :
            p3Num += trainMatrix[i]
            p3Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 4 :
            p4Num += trainMatrix[i]
            p4Denom += sum(trainMatrix[i])
        elif trainCategory[i] == 5 :
            p5Num += trainMatrix[i]
            p5Denom += sum(trainMatrix[i])
        else:
            pass
    p1Vect = log(p1Num/p1Denom)
    p2Vect = log(p2Num/p2Denom)
    p3Vect = log(p3Num/p3Denom)
    p4Vect = log(p4Num/p4Denom)          #change to log()
    p5Vect = log(p5Num/p5Denom)          #change to log()
    return p1Vect,p2Vect,p3Vect,p4Vect,p5Vect,pAbusive,pBbusive,pCbusive,pDbusive,pEbusive

def classifyNB(vec2Classify, p1Vec, p2Vec,p3Vec,p4Vec,p5Vec,pClass1,pClass2,pClass3,pClass4,pClass5):
    p5 = sum(vec2Classify * p5Vec) + log(pClass5)
    p4 = sum(vec2Classify * p4Vec) + log(pClass4)
    p3 = sum(vec2Classify * p3Vec) + log(pClass3)
    p2 = sum(vec2Classify * p2Vec) + log(pClass2)    #element-wise mult
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)
    max_num = max(p1,p2,p3,p4,p5)
    if max_num == p1:
        return 1
    if max_num == p2:
        return 2
    if max_num == p3:
        return 3
    if max_num == p4:
        return 4
    if max_num == p5:
        return 5
    return 0

def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
        else:pass# print "the word: %s is not in my Vocabulary!" % word
    return returnVec

def textParse(bigString):    #input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def calcMostFreq(vocabList,fullText,num):#获取高频词
    import operator
    freqDict = {}
    for token in vocabList:
        freqDict[token]=fullText.count(token)
    sortedFreq = sorted(freqDict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:num]

def localWords(feed1,feed0):
    import feedparser
    docList=[]; classList = []; fullText =[]
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1) #NY is class 1
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)#create vocabulary
    top30Words = calcMostFreq(vocabList,fullText)   #remove top 30 words
    for pairW in top30Words:
        if pairW[0] in vocabList: vocabList.remove(pairW[0])
    trainingSet = range(2*minLen); testSet=[]           #create test set
    for i in range(20):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:#train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0
    for docIndex in testSet:        #classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print 'the error rate is: ',float(errorCount)/len(testSet)
    return vocabList,p0V,p1V

def getTopWords(ny,sf):
    import operator
    vocabList,p0V,p1V=localWords(ny,sf)
    topNY=[]; topSF=[]
    for i in range(len(p0V)):
        if p0V[i] > -6.0 : topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -6.0 : topNY.append((vocabList[i],p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print "SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**"
    for item in sortedSF:
        print item[0]
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print "NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**"
    for item in sortedNY:
        print item[0]


def parse_str_to_list(string):
    string = string.decode("UTF-8","ignore").encode("UTF-8")
    string.replace('”','').replace('	','').replace('\n','').lstrip().rstrip()
    seg = jieba.cut(string,cut_all=False)
    str = "/".join(seg)
    list = str.split("/")
    return list
