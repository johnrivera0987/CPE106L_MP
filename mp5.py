import random

class Doctor:
    hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")
    qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")
    replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours"}

    def reply(self,sentence): 
        probability = random.randint(1, 4) 
        if probability == 1:
            return random.choice(self.hedges) 
        else:
            return random.choice(self.qualifiers) + self.changePerson(sentence)
    def changePerson(self, sentence):  
        words = sentence.split() 
        replyWords = [] 
        for word in words:
            replyWords.append(self.replacements.get(word, word)) 
        return " ".join(replyWords)
    def greeting(self):
        print("Good morning, I hope you are well today.") 
        print("If you would like to exit the conversation just type: QUIT")
        print("What can I do for you?") 
    def signoff(self):
        print("Have a nice day!")
def main(): 
    Doc = Doctor()
    Doc.greeting()
    while True:
        sentence = input("\n>> ") 
        if sentence.upper() == "QUIT":
            Doc.signoff()
            break
        print(Doc.reply(sentence))
        

main()