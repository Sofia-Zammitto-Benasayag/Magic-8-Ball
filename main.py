import random

#variables 
name = "Lucy"
question = "Will it rain today?"
answer = ""

random_number = random.randint(1,15) 

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."  
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now." 
elif random_number == 7:
  answer = "My sources say no."  
elif random_number == 8:
  answer = "Outlook not so good."   
elif random_number == 9:
  answer = "Very doubtful." 
elif random_number == 10:
  answer = "Who can tell?" 
elif random_number == 11:
  answer = "Very positive."
elif random_number == 12:
  answer = "Very negative."
elif random_number == 13:
  answer = "Who knows?" 
elif random_number == 14:
  answer = "Yes." 
elif random_number == 15:
  answer = "No."         
else: answer = "Error" 

print("Lucy asks: " + question)
print("Magic 8 says: " + answer)