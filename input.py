def Text_1_answer(text, answer):
    print(text)
    while True:
        space = input("Input answer:")
        if space != answer:
            print("Wrong, input again!")
        else:
            print("Yes go!")
            break;


Text_1_answer("test","abc")