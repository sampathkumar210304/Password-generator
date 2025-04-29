"""Here first we have to ensure the word enter to the user is at least 8 characters and Enter the numbers 
   at least 4 digits .Here we combine the characters from the word,the digits from the number and combine the randomly selected characters
   After shuffle the all characters to make sure  randomnes,then we get the shuffled characters to from the strongest passwod""" 
import random

name=""
Number=0

name_list=[]#create a list of names
Num_list=[]#create a list of numbers
SP=["!", "@", "#", "$", "%", "^", "&", "*","(", ")", "~", "-", "_", "+", "="]#create a list of special characters

print("Welcome to the standard and strong password provider!")#print the statement
#write a while loop here
while(len(name)<=8):
     name=input("Enter any word more than or eqaual to 8 characters:")


while(len(str(Number))<=3):
     Number=input("Enter any number more than or equal to 4:")

#write a for loop here
for i in name:
    name_list.append(i)

for j in str(Number):
    Num_list.append(j)

for j in SP:
    Num_list.append(j)

#Then shuffle the all the lists    
random.shuffle(Num_list)
random.shuffle(name_list)
random.shuffle(SP)

      
 #And create a list and Zip them together     
list=[]

for i,j in zip(name_list,Num_list):
   list.append(i+j)

#And convert the list into a string
combine="".join(list)

print("Your Strong password is Here: " +combine)




    
