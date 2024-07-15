#Thus, one should choose appropriate values for each exercise length – once for a true result and once for a false result.
# Of course, in each condition, values should be chosen independently for d, c, b, a so that they lead once to true and then to appropriate values to result in false
#(each exercise's values are independent of the previous exercise).
#It is recommended to create one code file where all answers are true, and one where all answers are false. Note that for some exercises there is no solution.
# For example, for an exercise of type 'True or a if', it will always evaluate to true regardless of what we put in 'a', so there won't be an answer that returns false for this section.

#1
a = 1
b = 1
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

#2
a = 2
b = 2
c = 2
d = 2
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

#3
a = 0
b = 0
c = 0
d = 0
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

#4
a = 0
b = 0
c = 0
d = 0
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

#5
a = 0
b = 0
c = 0
d = 0
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

#6
a = 6
b = 6
c = 6
d = 6
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

#7
a = 1
b = 0
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

#8
a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

#9
a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

#10
a = 4
b = 2
c = 5
d = 4
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")