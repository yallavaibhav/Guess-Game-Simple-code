secret = "JIMJAM"
guess = ""
limit = 3
mama = False
while guess != secret and not(mama):
  if(limit<=0):
    mama = True
  else:
    guess = input("enter the guessed name")
    
    limit -= 1  
    if limit == 0:
      print("No chances left")
    else:
       print("Still "+str(limit)+" chances left")
    

if mama == True:
   print("Sorry try again")  
else:
  print("You have "+str(limit)+ " chance left, but YOU WONNN")  