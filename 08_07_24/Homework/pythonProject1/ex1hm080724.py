#Write a Python program that receives from the user his id as a string, his first name as a string, the his last name as a string, his height as a decimal (float), the year of birth as an integer (int)
#Now print the details using ("..."f(print in the following format:
#id: 1 name: cohen , danny height: 1.87 year-of-birth: 2001
#-- In the example you see the printout after entering id, 1 first name danny, last name cohen, Height 1.87 and year of birth 2001
#-- Where it is highlighted this is the input that came from the user (hint: we will use } {), the rest of the text is fixed text
#Start
idn: str = str(input("Please enter your ID number: "));
fname: str = str(input("Please provide your First Name: "));
lname: str = str(input("Please provide your First Name: "));
height: float = float(input("What's your height? "));
yob: int = int(input("What's your Year of birth? "));
print(f"The user registered with ID number {idn} under the name {fname} {lname}, poses a height of {height}, and was born on the year {yob}.");
#End