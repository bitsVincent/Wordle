import random
import stardict
checklib = stardict.DictCsv("master5dict.csv")
testlib = stardict.DictCsv("test5dict.csv")

def gettestword() ->dict :
    return testlib.query(random.randint(1,testlib.count()-1))

def checkvaild(word):
    if(checklib.query(word)==None):
        return False
    else:
        return True