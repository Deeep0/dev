def two_fer(name):
    person = ["Alice", "Bohdan", "Zaphod"]
    if name in person:
        print("one for " + name + ", one for me. ")
    else :
        print("one for you, one for me.")

two_fer("Alice")
two_fer("gian")