print("WELCOME")

x = 0
y = 0

playq= input("""
DO YOU WANT TO PLAY QUİZ GAME

YES OR NO 
""")


if playq != "YES":
    quit()



print( "OK SHOW ME WHAT YOU GOT")

answer1 = input(" Street artist Banksy is originally associated with which British city?")

if answer1 == "Bristol":
     print ("CORRECT")
     x+=1
else:
      print("INCORRECT")
      y += 1


answer2 = input("What was the Turkish city of Istanbul called before 1930?")

if answer2 == "Constantinople":
     print ("CORRECT")
     x += 1
else:
      print("INCORRECT")
      y += 1



answer3 = input("What is the smallest planet in our solar system?")

if answer3 == "Mercury":
     print ("CORRECT")
     x += 1
else:
      print("INCORRECT")
      y += 1

answer4 = input("Which legendary surrealist artist is famous for painting melting clocks?")
if answer4 == "Salvador Dali":
     print ("CORRECT")
     x += 1
else:
      print("INCORRECT")
      y += 1

answer5 = input(" Name the Coffee shop in US sitcom Friends.")
if answer5 == "Central Perk":
     print ("CORRECT")
     x += 1
else:
      print("INCORRECT")
      y += 1

print("CORRECT {} AND INCORRECT {}".format(x,y))
