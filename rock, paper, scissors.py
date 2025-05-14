import random

def game():
    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Выберите: 1 - Камень 🪨, 2 - Ножницы ✂️, 3 - Бумага 📄")
    
    # Варианты и их представление
    choices = {1: "Камень 🪨", 2: "Ножницы ✂️", 3: "Бумага 📄"}
    
    while True:
        try:
            player_choice = int(input("Ваш выбор (1-3): "))
            if player_choice not in [1, 2, 3]:
                print("Пожалуйста, введите число от 1 до 3!")
                continue
            
            computer_choice = random.randint(1, 3)
            
            print(f"\nВы выбрали: {choices[player_choice]}")
            print(f"Компьютер выбрал: {choices[computer_choice]}")
            
            # Определение победителя
            if player_choice == computer_choice:
                print("Ничья! 🤝")
            elif (player_choice == 1 and computer_choice == 2) or \
                 (player_choice == 2 and computer_choice == 3) or \
                 (player_choice == 3 and computer_choice == 1):
                print("Вы победили! 🎉")
            else:
                print("Компьютер победил! 💻")
            
            # Предложение сыграть ещё
            play_again = input("\nХотите сыграть ещё? (да/нет): ").lower()
            if play_again != "да":
                print("Спасибо за игру! До встречи! 👋")
                break
        
        except ValueError:
            print("Ошибка! Введите число от 1 до 3.")

# Запуск игры
if __name__== "__main__":
    game()