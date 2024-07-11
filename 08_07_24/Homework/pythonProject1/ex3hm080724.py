#3. A description of the volume level must be displayed for an audio system. Receive from the user a volume level (int) and print feedback as follows(hint - use  match case):
#a. For 0 print: "Mute"
#b. For 1 print: "Very Quiet!"
#c. For 2 print: "Very Quiet!"
#d. For 3 print: "Quiet!"
#e. For 4 print: "Moderately Quiet!"
#f. For 5 print: "Medium!"
#g. For 6 print: "Moderately loud!"
#h. For 7 print: "Loud!"
#i. For 8 print: "Very Loud!"
#j. For 9 print: "Extremely Loud!"
#k. For 10 print: "Extremely Loud!"
#Start
volume: int = int(input("Please enter the current volume level on a scale from 0 - 10: "));

match volume:
    case 0:
        print("The volume is currently mute")
    case 1 | 2:
        print("Volume is currently very quiet!")
    case 3:
        print("Volume is quiet!")
    case 4:
        print("The volume is on a moderately quiet level!")
    case 5:
        print("The volume level is at the moment: Medium!")
    case 6:
        print("Volume is moderately loud!")
    case 7:
        print("Precaution! The volume is loud!")
    case 8:
        print("Warning!! The volume is Very Loud!")
    case 9 | 10:
        print("CAUTION!!! The volume is extremely loud!")
    #end