from flask import Flask, request
from flask_restful import Resource, Api

##Change this if necessary
returnCensored = True
censorChar = "*"
diameter = "_" #Your call to the API must be formatted with space bars replaced with this.

##Api Variables:
PORT = "5555"
app = Flask(__name__)
api = Api(app)

#Censor Settings:
disallowed   = ["frick"]
disallowedOrder = []
replacements = {"!":"i"}

def compileDisallowedOrder():
    for word in disallowed:
        disallowedOrder.append(convertWordToCharacters(word))
        

def convertWordToCharacters(wordArg):
    word = ""
    previousLetter = ""
    for letter in list(wordArg.lower()):
        if letter != previousLetter:
            word += letter
        previousLetter = letter
    return word

#Alone this is not very thorough and is easily bypassed.
def isWordAllowed(word):
    if word.lower() in disallowed: 
        return False
    return True


def checkLetterOrder(word):
    wordLetterOrder = convertWordToCharacters(word)
    if wordLetterOrder in disallowedOrder:
        return False
    return True


def replaceAlternatives(word):
    output = ""
    for letter in list(word.lower()):
        if letter in replacements:
            output += replacements[letter]
            continue
        output += letter
    return output





##Much faster but more vulnerable to being evaded.
class quickCheck(Resource):
    def get(self, message):
        wprt = 0 #Word Ptr
        output = ""
        censored = False
        for word in message.split(diameter):
            wprt += 1
            if isWordAllowed(word) == False:
                censored = True
                output += f"{censorChar}" * len(word)

            else: output += word
            if wprt != len(message.split(diameter)): output += " "
        if returnCensored == True: return output
        else:
            if censored == True: return "Censored"
            return output

##Much slower but less vulnerable to being evaded.
class thoroughCheck(Resource):
    def get(self, message):
        wprt = 0 #Word Ptr
        output = ""
        censored = False
        for word in message.split(diameter):
            wprt += 1
            if isWordAllowed(replaceAlternatives((word))) == False: 
                censored = True
                output += f"{censorChar}" * len(word)

            else: output += word
            if wprt != len(message.split(diameter)): output += " "
        if returnCensored == True: return output
        else: 
            if censored == True: return "Censored"
            return output

##The slowest but most thorough.
class superCheck(Resource):
    def get(self, message):
        wprt = 0 #Word Ptr
        output = ""
        censored = False
        for word in message.split(diameter):
            wprt += 1
            if isWordAllowed(replaceAlternatives((word))) == False or checkLetterOrder(word) == False: 
                censored = True
                output += f"{censorChar}" * len(word)
            else: output += word
            if wprt < len(message.split(diameter)): output += " "
        if returnCensored == True: return output
        else: 
            if censored == True: return "Censored"
            return output




api.add_resource(quickCheck, "/QCheck/<message>")    #End Point -1
api.add_resource(thoroughCheck, "/TCheck/<message>") #End Point -2
api.add_resource(superCheck, "/SCheck/<message>") #End Point -3

if __name__ == "__main__":
    compileDisallowedOrder()
    print(f"Dissalowed Words: {disallowed}")
    print(f"Dissalowed Orders: {disallowedOrder}")
    app.run(port=PORT)
