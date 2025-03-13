import random 
r="rock"
p="paper"
s="scissors"
o=["rock","paper","scissors"]
print("1.rock\n2.paper\n3.scissor\n")
you=int(input("enter the choice in 1-3 :"))
c=random.choice(o)
if you==1:
   you="rock"
   print("your choice is : rock")
elif you==2:
   you="paper"
   print("your choice is : paper")
elif you==3:
   you="scissors"
   print("your choice is : scissors")
else:
   print("plz enter valid choice")

print("opponent choice is :",c)

if you==c:
   print("result : tie")
elif (you=="rock" and c=="scissors" ) or (you=="scissors"and c=="paper") or (you=="paper"and c=="rock"):
     print("yay 😍 ! ,you won......")
else:
   print("oops 😒 ! you lose......")
   


