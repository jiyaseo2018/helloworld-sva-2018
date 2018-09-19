
# let the user know what's going on
print ("Welcome to MadStories!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
name1 = raw_input("Enter you name: ")
number1 = raw_input("Enter your favorite number from 1 to 9: ")
show1 = raw_input("What is your favorite tv show or a film?: ")
occupation1 = raw_input("Name your dream job: ")
object1 = raw_input("Most valuable thing you own right now: ")
famousPerson1 = raw_input("A famous historical person you wanna meet: ")
word1 = raw_input("Enter a word you say the most: ")
hobby1 = raw_input("Enter your hobby: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "  " + name1 + "'s story..." \
" When I was " + number1 + " years old, I used to watch " + show1 + ". " \
"It inspired me to become " + occupation1 + ", " + "because it means I can have " + object1 + " when I grow up." \
" " + famousPerson1 + " once said, " + "'If you don't give up, good things happen.' " \
"So I did " + hobby1 + " everyday, saying " + "'" + word1 + "'" + " to myself constantly. " \
"I truly believed in " + famousPerson1 + " and desperately wanted to be a " + occupation1 + ". " \
"Here I am now, still doing " + hobby1 + " and saying " + "'" + word1 + "'" + " everyday. " \
"Thanks to you, " + famousPerson1 + ", good things do happen."

# finally we print the story
print (story)