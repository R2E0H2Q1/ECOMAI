#Write a Python program that takes 2 strings and prints them with an asterisk between them and also with a minus between them.
#For example, if the following strings were received: "rocks" "python", will be printed:
#*python*rocks*
#-python-rocks-
#Start
str1: str = input("Please enter your city of residence!");
str2: str = input("Please enter the name of your street of residence!");
print("I live in ","*",str1,"*",str2,"*");
print("I live in ","-",str1,"-",str2,"-");
#End