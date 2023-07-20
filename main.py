import random
import wordlewordlist
import interface

def checkwordvaildation(word,length):
    if(len(word)!=length): return "Word length incorrect."
    if(not wordlewordlist.checkvaild(word)): return "Not a vaild word."
    return ""
def compare(guessword,word):
    result=""
    for i in range(0,len(guessword)):
        if word[i] == guessword[i]:
            result+="1"
        elif guessword[i] in word:
            result+="2"
        else:
            result+="0"
    return result


def entry():
    print("Start with a five letter word.")
    answord=wordlewordlist.gettestword()
    word=answord.get('word')
    length=len(word)
    flag=False
    #Start Attemptation
    i=0
    guesslist=[]
    while(i<=length):
        print("Attempt "+str(i+1)+"/"+str(length+1)+":",end="")
        guessword=input().lower()
        #Check Vaildation, if failed continue and restart the attempt
        wordvaildmsg=checkwordvaildation(guessword,length)
        if(wordvaildmsg!=""):
           print(wordvaildmsg)
           continue
        if(guessword in guesslist):
            print("You've already guessed that.")
            continue
        guesslist.append(guessword)
        result=compare(guessword,word)
        interface.printresult(guessword,result)
        if(result==("1"*length)):
            flag=True
            break
        i=i+1
    interface.gamesummary(flag,answord)

entry()
    
