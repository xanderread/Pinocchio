import numpy as np
import re

#TODO: implement all the other methods for determining the liar value
#FIXME: clean up / comment code
#TODO: implement ai to determine the liar value calculations -> Use outcome of methods to determine whether the person is a liar
#TODO: tie program to ai

def logTexts():
    responses = []
    uncomplete = True
    while uncomplete:
        #Needs implemented as a GUI
        print("-----------------------------------")
        print("Type \"q\" to complete this section")
        print("-----------------------------------")
        text = input("Enter the persons next message:    ")
        if(text == "q"):
            uncomplete = False
        else:
            #Must look for outliers as some people may just be slow repliers
            responseTime = int(input("How much time, in seconds, did it take for the person to respond? "))
            newText = [text,responseTime]
            responses.append(newText)
    return np.array(responses)


def main(methods):
    liarValue = int(50) #AI could determine the liar value
    #Each potential sign will increase or decrease this value before it is evaluated at the end
    print("Enter the initial conversation (introducing the game and themselves) below:")
    initialTexts = logTexts()
    print("Enter the conversation after the lie has been mentioned below:")
    lieTexts = logTexts()
#     initialTexts = np.array([["Hello", 10],["I'm doing good thank you",20],["This. is just a normal conversation yea",50]])
#     lieTexts = np.array([["I disagree with that",40],["No your lying to me. I didnt say that. Why dont you believe me",50],["I dont want to respond anymore. Loser head.",80]])
#     print("\n\n\n\n -----------------------------")
    endEarly = input("Did the person abruptly leave, or attempt to abruptly leave, the conversation? Y/N")
    if(endEarly == "Y"):
        liarValue = liarValue * 1.1
    print("Evaluating.....")
    for f in methods:
        liarValue = f(initialTexts,lieTexts,liarValue)
        print("Current liar value: ",liarValue)
    print("The final liar value is: ",liarValue)
    
def responseTime(initialTexts,lieTexts,liarValue):
    justTimesInitial = np.array(initialTexts[:,1], dtype=np.uint32)
    justTimesPost = np.array(lieTexts[:,1], dtype=np.uint32)
    initialTextResponseTime = np.average(justTimesInitial)
    postTextReponseTime = np.average(justTimesPost)
    if(1.1*(initialTextResponseTime) <= (postTextReponseTime)): #Greater than 10% as suggested in wikiHow
        return liarValue * 1.1
    else:
        return liarValue * 0.9

def complicated(initialTexts,lieTexts,liarValue):
    mylen = np.vectorize(len)
    initialLength = np.mean(mylen(initialTexts[:, 0]))
    postLength = np.mean(mylen(lieTexts[:,0]))
    sentences = []
    for sentence in initialTexts[:,0]:
        sentences.append(len(sentence.split('. ')))
    initialSentences = np.mean(np.array(sentences))
    sentences = []
    for sentence in lieTexts[:,0]:
        sentences.append(len(sentence.split('. ')))
    postSentences = np.mean(np.array(sentences))
    if(postLength>initialLength or initialSentences > postSentences):
        return liarValue * 1.1 #TODO: how do we know to use these excat values? can use AI to get on this
    else:
        return liarValue * 0.9 #TODO: how do we know to use these exact values? can use AI to get on this ECT

def personalPronouns(initialTexts,lieTexts,liarValue):
    #Must assess whether the liar has removed personal pronouns
    pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
    pronouns = []
    for sentence in initialTexts[:,0]:
        pronouns.append(len(pronounRegex.findall(sentence)))
    initialPronouns = np.mean(np.array(pronouns)) #TODO: Should use np implementation throughout
    pronouns = []
    for sentence in lieTexts[:,0]:
        pronouns.append(len(pronounRegex.findall(sentence)))
    liePronouns = np.mean(np.array(pronouns))
    if(initialPronouns > 1.2*liePronouns): #TODO: Must find how much it should change by to be flagged
        return liarValue * 1.1 #Could instead return how much its increased / decreased by and use that to determine whether they are a liar
    else:
        return liarValue * 0.9

def tenseHopping(initialTexts,lieTexts,liarValue):
    #Must assess whether the liar has started tense hopping
    return liarValue

def thirdPersonPronouns(initialTexts,lieTexts,liarValue):
    #Must assess whether the liar has used more third person pronouns
    return liarValue

def exclusiveWords(initialTexts,lieTexts,liarValue):
    #Must assess whether the liar has used fewer exclusive words
    return liarValue

def negativeEmotion(initialTexts,lieTexts,liarValue):
    #Must assess whether the liar has used more negative emotion words
    return liarValue

def motionVerbs(initialTexts,lieTexts,liarValue):
    #Must assess whether the liar has used more motionVerbs
    return liarValue

methods = [complicated,responseTime] #Order is in reverse order of importance
    
main(methods)