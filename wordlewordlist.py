import random
import stardict

class guessingprocess(object):
    checklib=None
    testlib=None
    answordinfo=None
    answord=""
    guesslist=[]
    attemptcount=0
    gamewinflag=False
    def __init__(self,checklibcsv,testlibcsv) -> None:
        self.checklib=stardict.DictCsv(checklibcsv)
        self.testlib=stardict.DictCsv(testlibcsv)
        self.answordinfo=self.testlib.query(random.randint(1,self.testlib.count()-1))
        self.answord=self.answordinfo.get('word')
        self.guesslist=[]
        self.attemptcount=1
        self.gamewinflag=False
        return
    
    def checkword(self,word) -> str:
        if(len(word)!=len(self.getword())): return "Word length incorrect."
        if(self.checklib.query(word)==None) : return "Not a vaild word"
        if(word in self.guesslist): return "You've already guessed that."
        #Passed checking, now move on
        self.guesslist.append(word)
        self.attemptcount=self.attemptcount+1;
        return ""
    
    def compare(self,word):
        # it returns a string with length of 5, 
        # 1 means correct, 
        # 2 means the letter exists in the word but the place is incorrect, 
        # 0 means the letter is incorrect and it doesn't exist in the word.
        
        result=""
        for i in range(0,len(word)):
            if self.answord[i] == word[i]:
                result+="1"
            elif self.answord[i] in word:
                result+="2"
            else:
                result+="0"
        if(result=="1"*len(self.answord)):
            self.gamewinflag=True
        return result
    def getword(self) -> str:
        return self.answord
    def getwordinfo(self) -> dict:
        return self.answordinfo
    def getattemptcount(self) ->int:
        return self.attemptcount
    def getmaxattemptcount(self)->int:
        return len(self.answord)+1
    def getwinflag(self) ->bool:
        return self.gamewinflag