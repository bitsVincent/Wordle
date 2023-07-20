import random
import wordlewordlist
import interface

def entry():
    gp = wordlewordlist.guessingprocess("master5dict.csv","test5dict.csv")
    ifc = interface.consoleinterface()
    ifc.gamestart()
    #Start Attemptation
    while(gp.getattemptcount()<=gp.getmaxattemptcount()):
        ifc.attemptmsg(gp.getattemptcount(),gp.getmaxattemptcount())
        guessword=input().lower()
        #Check Vaildation, if failed continue and restart the attempt
        wordvaildmsg=gp.checkword(guessword)
        if(wordvaildmsg!=""):
           ifc.attempterrormsg(wordvaildmsg)
           continue
        ifc.printresult(guessword,gp.compare(guessword))
        if(gp.getwinflag()): break
    ifc.gamesummary(gp.getwinflag(),gp.getwordinfo())

entry()
    
