import random

def guess_the_number():
    print("Selamat Datang Di Permainan Guess the Number Game!")
    print("Saya memikirkan angka 1 sampai 100.")
    print("Apakah kamu bisa menebak angka tersebut?")

    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            user_guess = int(input("Masukkan Tebakanmu: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Terlalu rendah! Coba lagi.")
            elif user_guess > number_to_guess:
                print("Terlalu Tinggi! Coba Lagi.")
            else:
                print(f"Selamat! Kamu menebak angkanya {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Masukan salah. Tolong masukkan lagi angka dari 1 sampai 100 .")

if __name__ == "__main__":
    guess_the_number()
