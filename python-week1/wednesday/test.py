def convert(number):
    sounds = ["pling", "plang", "plong"]
    numbers = [3,5,7]
    sound = ""
    for soundnumber , s in zip(numbers, sounds):
        if number % soundnumber == 0:
            sound = sound + s
            
    return sound or str(number)



print(convert(3))