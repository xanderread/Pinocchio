import numpy as np

#TODO: implement all the other methods for determining the liar value
#FIXME: clean up / comment code
# TODO: implement ai to determine the liar value calculations
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
    print("Evaluating.....")
    for f in methods:
        liarValue = f(initialTexts,lieTexts,liarValue)
        print("Current liar value: ",liarValue)
    print("The final liar value is: ",liarValue)
    
def responseTime(initialTexts,lieTexts,liarValue):
    #Must know how long they usually take to respond to use this
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
    initialSentences = len(sentences)
    sentences = []
    for sentence in lieTexts[:,0]:
        sentences.append(len(sentence.split('. ')))
    postSentences = len(sentences)
    if(postLength>initialLength or initialSentences > postSentences):
        return liarValue * 1.1 #TODO: how do we know to use these excat values? can use AI to get on this 
    else:
        return liarValue * 0.9 #TODO: how do we know to use these exact values? can use AI to get on this ECT




methods = [complicated,responseTime] #Order is in reverse order of importance
    
main(methods)