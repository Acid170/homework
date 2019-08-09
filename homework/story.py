#Kofi is going to school
def myStory():
    input_noun = input("Please enter a noun: ")
    input_verb = input("Please enter a verb: ")
    input_place = input("Please enter the place: ")
    story = "{noun} is {verb} to {place}".format(noun=input_noun, verb=input_verb, place=input_place)
    print(story)

myStory()
