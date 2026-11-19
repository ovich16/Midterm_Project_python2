import message

def welcome_message():
    while True:
        message.msg1()
        try:
            diff_choice = int(input('ENTER A NUMBER BETWEEN 1 and 3: '))
            if 4 > diff_choice > 0:
                message.msg2()
                input()
                break
            else:
                message.msg3()
                input()
        except:
            message.msg4()
            input()
    return diff_choice

welcome_message()