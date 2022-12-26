######################
## MACHINE LEARNING ##
######################
import random, time

subjects = []
data = [
  "I will lead them", "I love you", "We will help you", "I hate you",
  "You are wrong", "You are stupid", "You will help them", "They are children",
  "I love sleep", "They like reading", "We are children", "How are you",
  "We will prevail", "We are not slaves", "We are good",
  "They can and will kill you", "We are not the same", "We are the same",
  "I am you", "I wished you called me", "I love thinking about the future",
  "I like watching stars", "I can take care of mysef",
  "I like watching people", "I like thinking about you", "You are hot",
  "I cannot give you any more", "I can do it",
  "I didn't ask about his family tree", "I am going to bed early",
  "You leech me of life"
]
brain = {}
data2 = []
brain2 = {}
sentence = ""


def showbrain():
  global brain
  for k, v in brain.items():
    newv = []
    for word in v:
      if word in newv:
        pass
      else:
        newv.append(word)
    print(f"{k.upper()}, {newv}")


for sentence in data:
  ss = sentence.split(" ")
  for word in range(len(ss)):
    if ss[word].lower() in brain:
      pass
    else:
      brain[ss[word].lower()] = []
    if word == 0:
      subjects.append(ss[word].lower())
    else:
      brain[ss[word - 1].lower()].append(ss[word])


def form_sentence():
  global sentence
  sentence = ""
  subject = random.choice(subjects).lower()
  sentence += subject.title()
  nextwordchoice = brain[subject]
  senlen = random.randint(2, 20)
  count = 1
  while count < senlen:
    nextword = random.choice(nextwordchoice)
    sentence += f" {nextword}"
    nextwordchoice = brain[nextword.lower()]
    if nextwordchoice == [] or (nextword in subjects and nextword == "you"):
      break
    count += 1


for i in range(int(input("Give me a random number between 1000 and 1500"))):
  form_sentence()
  if sentence in data:
    pass
  else:
    data.append(sentence)
    data2.append(sentence)
  print(str(i + 1) + ". " + sentence.title())

for sentence in data2:
  ss = sentence.split(" ")
  for word in range(len(ss)):
    if ss[word].lower() in brain2:
      pass
    else:
      brain2[ss[word].lower()] = []
    if word == 0:
      subjects.append(ss[word].lower())
    else:
      brain2[ss[word - 1].lower()].append(ss[word])
sentence = ""
subject = random.choice(subjects).lower()
sentence += subject
nextwordchoice = brain2[subject]
while True:
  nextword = random.choice(nextwordchoice)
  sentence += f" {nextword}"
  nextwordchoice = brain2[nextword.lower()]
  if nextwordchoice == [] or nextword in subjects:
    break
print("\n\n\n")
print(f"Generated sentence: {sentence}")
