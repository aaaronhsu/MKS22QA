# homework
def sound():
    db = float(input("Input decibel level: "))

    if db < 40:
        print("Quiter than a quiet room")
    elif db == 40:
        print("Quiet room")
    elif db < 70:
        print("Louder than a quiet room but quieter than an alarm clock")
    elif db == 70:
        print("Alarm clock")
    elif db < 106:
        print("Louder than an alarm clock but quieter than a gas lawnmower")
    elif db == 106:
        print("Gas lawnmower")
    elif db < 130:
        print("Louder than a gas lawnmower but quieter than an jackhammer")
    elif db == 130:
        print("Jackhammer")
    else:
        print("Louder than a jackhammer")
