card_id: int = int(input("Enter a card number (2-14): "));
#option1
match card_id:
    case 1:
        print(card_id);
    case 2:
        print(card_id);
    case 3:
        print(card_id);
    case 4:
        print(card_id);
    case 5:
        print(card_id);
    case 6:
        print(card_id);
    case 7:
        print(card_id);
    case 8:
        print(card_id);
    case 9:
        print(card_id);
    case 10:
        print(card_id);
    case 11:
        print("Jack");
    case 12:
        print("Queen");
    case 13:
        print("King");
    case 14:
        print("Ace");
    case 15:
        print("Joker");


## option2
if card_id >=2 and card_id <=10:
    print(card_id);
match card_id:
    case 11:
        print("Jack");
    case 12:
        print("Queen");
    case 13:
        print("King");
    case 14:
        print("Ace");
    case 15:
        print("Joker");
    case _:
        print("Invalid Card");

#option 3

    case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10:
        print(card_id);
    case 11:
        print("Jack");
    case 12:
        print("Queen");
    case 13:
        print("King");
    case 14:
        print("Ace");
    case 15:
        print("Joker");
    case _:
        print("Invalid Card");