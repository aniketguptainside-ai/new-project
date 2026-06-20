import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("choose 1 to 100 bitween no. ")

    while True:
        try:
            guess = int(input("Guess please"))
            attempts += 1
            
            if guess < secret_number:
                print("बहुत छोटा नंबर! थोड़ा बड़ा नंबर चुनें।")
            elif guess > secret_number:
                print("बहुत बड़ा नंबर! थोड़ा छोटा नंबर चुनें।")
            else:
                print(f"बधाई हो! आपने {attempts} प्रयासों में गुप्त नंबर खोज लिया।")
                break
        except ValueError:
            print("कृपया एक वैध (valid) संख्या दर्ज करें।")

number_guessing_game()





