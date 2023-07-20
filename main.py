import random
import wordlewordlist
import interface

def entry():
    gp = wordlewordlist.guessingprocess("master5dict.csv","test5dict.csv")
    word=gp.getword()
    length=len(word)
    #Start Attemptation
    while(gp.getattemptcount()<=gp.getmaxattemptcount()):
        guessword=input().lower()
        #Check Vaildation, if failed continue and restart the attempt
        wordvaildmsg=gp.checkword(guessword)
        if(wordvaildmsg!=""):
           interface.attempterrormsg(wordvaildmsg)
           continue
        interface.printresult(guessword,gp.compare(guessword,word))
    interface.gamesummary(gp.getwinflag(),gp.getwordinfo())

entry()
    
