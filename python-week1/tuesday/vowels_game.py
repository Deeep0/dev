words = input ("enter the word .")

vowels = ["a","e","i","o","u"]

translation = ""
for word in words:
    if word in vowels:
        translation = translation + "g"
    else :
         translation = translation + word 
print(translation)