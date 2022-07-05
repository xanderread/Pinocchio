import numpy as np
import re

#TODO: implement all the other methods for determining the liar value
#FIXME: clean up / comment code
#TODO: implement ai to determine the liar value calculations -> Use outcome of methods to determine whether the person is a liar
#TODO: tie program to ai

#The AI will use the different charactersitic changes to determine whether the person is a liar
#The AI will be provided with the following array:
# [post length, # sentences, personal pronouns, tensehopping, third person pronouns, avg word length, leaving fast]

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
            #Response time isn't currently being used in the model
            #responseTime = int(input("How much time, in seconds, did it take for the person to respond? "))
            #newText = [text,responseTime]
            responses.append(text)
    return np.array(responses)


def main(methods):
    liarValue = 0
    print("Enter the initial conversation (introducing the game and themselves) below:")
    initialTexts = logTexts()
    print("Enter the conversation after the lie has been mentioned below:")
    lieTexts = logTexts()
    endEarly = input("Did the person abruptly leave, or attempt to abruptly leave, the conversation? Y/N")
    if(endEarly == "Y"):
        liarValue = 1
    print("Evaluating.....")
    for f in methods:
        liarArray = [0,0,0,0,0,0,0,0,liarValue]
        f(initialTexts,lieTexts)
        print("Current liar array: ",liarArray)
        #The liar array is then put into the trained AI which will be trained to determine whether the person is lieing or telling the truth based upon these characteristics
    
# def responseTime(initialTexts,lieTexts,liarValue): #Not provided in dataset however can be used to skew the results after applying the AI
#     justTimesInitial = np.array(initialTexts[:,1], dtype=np.uint32)
#     justTimesPost = np.array(lieTexts[:,1], dtype=np.uint32)
#     initialTextResponseTime = np.average(justTimesInitial)
#     postTextReponseTime = np.average(justTimesPost)
#     if(1.1*(initialTextResponseTime) <= (postTextReponseTime)): #Greater than 10% as suggested in wikiHow
#         return liarValue * 1.1
#     else:
#         return liarValue * 0.9

def complicated(initialTexts,lieTexts):
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
    liarArray[0] = postLength / initialLength
    liarArray[1] = postSentences / initialSentences

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
    lieArray[2]=liePronouns / initialPronouns

def tenseHopping(initialTexts,lieTexts,liarValue):
    #Must assess whether the liar has started tense hopping (Google docs contains a Stack overflow post which should help this be solved easily -> Check if tenses are changed between sentences more or less regularly
    return liarValue

def thirdPersonPronouns(initialTexts,lieTexts):
    #Must assess whether the liar has used more third person pronouns
    pronounRegex = re.compile(r'\b(he|him|his|himself|she|her|hers|herself|it|its|itself|they|them|their|theirs|themselves)\b',re.I)
    pronouns = []
    for sentence in initialTexts[:,0]:
        pronouns.append(len(pronounRegex.findall(sentence)))
    initialPronouns = np.mean(np.array(pronouns)) #TODO: Should use np implementation throughout with additional time
    pronouns = []
    for sentence in lieTexts[:,0]:
        pronouns.append(len(pronounRegex.findall(sentence)))
    liePronouns = np.mean(np.array(pronouns))
    lieArray[4]= liePronouns / initialPronouns
    
def avgWordLength(intialTexts,lieTexts):
    return None

# def exclusiveWords(initialTexts,lieTexts,liarValue):
#     #Must assess whether the liar has used fewer exclusive words
#     return liarValue

# def negativeEmotion(initialTexts,lieTexts,liarValue):
#     #Must assess whether the liar has used more negative emotion words
#     return liarValue

# def motionVerbs(initialTexts,lieTexts,liarValue):
#     #Must assess whether the liar has used more motionVerbs
#     return liarValue

def AIdetection():
    #Before developing this method, the data must be scraped from the document found and 200+ cases should be made to determine whether someone is a liar or not a liar based on past texts and future texts
    return None

methods = [complicated,personalPronouns,thirdPersonPronouns,avgWordLength,tenseHopping] #Order is irrelevant
    
main(methods)