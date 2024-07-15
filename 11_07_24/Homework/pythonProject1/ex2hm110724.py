#For all the conditions in front of you, solve whether it will return true or false: For example for 9 < 4 will return true

if 4 < 9:
#Answer:/ Its true as 4 is indeed smaller than 9.
    print("True");
else:
    print("False");

if (2 * 3 + 4) * (7 + 7):
#Answer:/ It's true because in python values different of 0 are consider true on an operation.
    print("True");
else:
    print("False");

if 18 + 18:
#Answer:/ It's true because in python values different of 0 are consider true on an operation.
    print("True");
else:
    print("False");

if 10 == 10:
#Answer:/ It's true because indeed 10 = to 10, so the condition is fullfilled.
    print("True");
else:
    print("False");

if 10 == 10 and 20 == 30:
#Answer:/ It's false because the second condition after the "and" is not fullfilled, even when 10 == 10.
    print("True");
else:
    print("False");

if 10 == 10 or 20 == 30:
#Answer:/ It's true because once python evaluates the first condition this one takes priority and will return a True statement.
    print("True");
else:
    print("False");

if 20 == 30 or 10 == 10:
#Answer:/ The stament is true because after python evaluates the first condition as false will move to check on the second one because of the word "or".
# As the whole statement only requires for one of the conditions to be true.
    print("True");
else:
    print("False");

if not 3:
#Answer:/ Is false because the operator "not" in python turns values into false.
    print("True");
else:
    print("False");

if 3:
#Answer:/ The statement is true because in python any number different from zero is assigned as true.
    print("True");
else:
    print("False");

if (33 > 20) and (2 < 12) and 10:
#Answer:/ All the conditions on the statement are correct, due to this is true.
    print("True");
else:
    print("False");

#if True and True: ?
#Answer:/ The statement is true, because "and" checks both sides of the statement and as both are true. This makes it true.

#if True and False: ?
#Answer:/ The statement is false, because "and" checks both sides of the statement and the second is false. Therefore, the statement is false.

#if True or False: ?
#Answer:/ The statement is true, because when using "or" if one of the parts is true, the statement will be true.

#if False or True: ?
#Answer:/ same case here one of the sides of the statement is true, so it makes it true.

if (not 10) and (10):
#Answer:/ Statement is false because of the operator "not".
    print("True");
else:
    print("False");

if (not 10) and (not 10):
# Answer:/ Statement is false because of the operator "not".
    print("True");
else:
    print("False");

if 5 != 5 and 5 == 5:
#Answer:/ The statement is false because on the first section 5 is not diferent from 5 and even when the second section is true, the "and" will check both since the first one is false.
    print("True");
else:
    print("False");

if 2 == 2 or 3 == 3:
#Answer:/ Both parts of the statement are true. Because the operator "or" will check for a minimun of one to be true. Therefore the result will be "True".
    print("True");
else:
    print("False");

if 2 == 2 and 3 == 3:
#Answer:/ Both parts of the statement are true. Which fullfils the action of the operator "and".
    print("True");
else:
    print("False");

if 40 == 30 and 1 >= 4:
#Answer: Even when the second part of the atatement (1 >=4) is true, the first one is not, Therefore the operator "and" cannot return a true result, because needs both sections to be true.
    print("True");
else:
    print("False");

if 13 >= 3 or 47 >= 5:
#Answer:/ In this example the condition is fullfill in both cases, which makes the result as true. 
    print("True");
else:
    print("False");