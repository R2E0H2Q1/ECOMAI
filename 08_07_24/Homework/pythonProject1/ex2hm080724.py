#2. Receive a test score from the user (int) and print feedback as follows: (hint - use else-elif-if)
#a. For a score between 0-40, print: "Try harder next time..."
#b. For a score between 41-60, print: "You're getting there, need some more work".
#c. For a score between: 61-80, print "Pretty good!"
#d. For a score between :81-95, print "Awesome!"
#e. For a score between: 96-100, print:"Excellent!!! You're a Star!"
#f. For a grade less than 0 or greater than 100, print: "Illegal grade"
#Start
score: int = int(input("Please enter your received score! "));
if score >= 0 and score <= 40:
    print("Try harder next time...");

elif score >= 41 and score <= 60:
    print("You're getting there, need some more work!");

elif score >= 61 and score <= 80:
    print("Pretty good!");

elif score >= 81 and score <= 95:
    print("Awesome!");

elif score >=96 and score <= 100:
    print("Excellent!!! You're a Star!");

else:
    print("Illegal grade");
#end