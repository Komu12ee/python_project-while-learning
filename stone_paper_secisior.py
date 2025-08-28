import random
user=input(">>select 0 of stone,1 for paper,2 for secissors")
computer=random.randint(1,3)
user.lower()
if user=="stone":
    user=1
elif user=="paper":
    user=2
else:
    user=3
    
print("computer chooses:-",computer)  
