import tkinter as tk

# Створення вікна
window = tk.Tk()

# Робимо вікно на весь екран
window.attributes('-fullscreen', True)

# Назва вікна
window.title("Clicker game")

# Початковий баланс
click_count = 0

# Кількість списувань за натискання кнопки 
button1_cost = 10

# Кількість списувань за натискання кнопки
button2_cost = 45

# Кількість списувань за натискання кнопки 
button3_cost = 90

# Кількість списувань за натискання кнопки 
button4_cost = 190

# Кількість списувань за натискання кнопки 
button5_cost = 300

# Кількість списувань за натискання кнопки 
button6_cost = 750

# Кількість списувань за натискання кнопки 
button7_cost = 1650

# Кількість списувань за натискання кнопки 
button8_cost = 7500

# Кількість списань за кожне натискання кнопки 
button1_clicks = 0

# Кількість списань за кожне натискання кнопки 
button2_clicks = 0

# Кількість списань за кожне натискання кнопки 
button3_clicks = 0

# Кількість списань за кожне натискання кнопки 
button4_clicks = 0

# Кількість списань за кожне натискання кнопки 
button5_clicks = 0

# Кількість списань за кожне натискання кнопки 
button6_clicks = 0

# Кількість списань за кожне натискання кнопки 
button7_clicks = 0

# Кількість списань за кожне натискання кнопки 
button8_clicks = 0

# Коефіцієнт збільшення списань для кнопки 
button1_multiplier = 0.5 # 1% (половина відсотка)

# Коефіцієнт збільшення списань для кнопки 
button2_multiplier = 1 # 1% (половина відсотка)

# Коефіцієнт збільшення списань для кнопки 
button3_multiplier = 1.5 # 1% (половина відсотка)

# Коефіцієнт збільшення списань для кнопки 
button4_multiplier = 2.5 # 1% (половина відсотка)

# Коефіцієнт збільшення списань для кнопки 
button5_multiplier = 4.5 # 1% (половина відсотка)

# Коефіцієнт збільшення списань для кнопки 
button6_multiplier = 7.5 # 1% (половина відсотка)

# Коефіцієнт збільшення списань для кнопки 
button7_multiplier = 8.5 # 1% (половина відсотка)

# Коефіцієнт збільшення списань для кнопки 
button8_multiplier = 9.6 # 1% (половина відсотка)

# Функція для обробки натискання на кнопку "click"
def on_button_click():
    global click_count
    click_count += 1 +  button1_clicks * 2 + button2_clicks * 5 + button3_clicks * 8 + button4_clicks * 15 + button5_clicks * 22 + button6_clicks * 30 + button7_clicks * 45 + button8_clicks * 65
    label.config(text=f"Баланс: {click_count}")

# Функція для обробки натискання на кнопку button1
def on_button1_click():
    global click_count, button1_clicks, button1_cost
    if click_count >= button1_cost:
        click_count -= button1_cost
        button1_clicks += 1
        button1_cost += int(button1_cost * button1_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button1.config(text=f"Нож (+1)| Вартість: {button1_cost} | Куплено: {button1_clicks}")
        on_button_click()  # Додаємо +2 до балансу

# Функція для обробки натискання на кнопку button2
def on_button2_click():
    global click_count, button2_clicks, button2_cost
    if click_count >= button2_cost:
        click_count -= button2_cost
        button2_clicks += 1
        button2_cost += int(button2_cost * button2_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button2.config(text=f"Гранатомет (+5)| Вартість: {button2_cost} | Куплено: {button2_clicks}")
        on_button_click()  # Додаємо +5 до балансу

# Функція для обробки натискання на кнопку button3
def on_button3_click():
    global click_count, button3_clicks, button3_cost
    if click_count >= button3_cost:
        click_count -= button3_cost
        button3_clicks += 1
        button3_cost += int(button3_cost * button3_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button3.config(text=f"Снайперка (+8)| Вартість: {button3_cost} | Куплено: {button3_clicks}")
        on_button_click()

        # Функція для обробки натискання на кнопку button3
def on_button4_click():
    global click_count, button4_clicks, button4_cost
    if click_count >= button4_cost:
        click_count -= button4_cost
        button4_clicks += 1
        button4_cost += int(button4_cost * button4_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button4.config(text=f"Автомат (+15)| Вартість: {button4_cost} | Куплено: {button4_clicks}")
        on_button_click()

# Функція для обробки натискання на кнопку button1
def on_button5_click():
    global click_count, button5_clicks, button5_cost
    if click_count >= button5_cost:
        click_count -= button5_cost
        button5_clicks += 1
        button5_cost += int(button5_cost * button5_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button5.config(text=f"Дробовик(+22)| Вартість: {button5_cost} | Куплено: {button5_clicks}")
        on_button_click()  

# Функція для обробки натискання на кнопку button1
def on_button6_click():
    global click_count, button6_clicks, button6_cost
    if click_count >= button6_cost:
        click_count -= button6_cost
        button6_clicks += 1
        button6_cost += int(button6_cost * button6_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button6.config(text=f"Пулемет (+30)| Вартість: {button6_cost} | Куплено: {button6_clicks}")
        on_button_click()  

# Функція для обробки натискання на кнопку button1
def on_button7_click():
    global click_count, button7_clicks, button7_cost
    if click_count >= button7_cost:
        click_count -= button7_cost
        button7_clicks += 1
        button7_cost += int(button7_cost * button7_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button7.config(text=f"Штурмова Винтовка (+45)| Вартість: {button7_cost} | Куплено: {button7_clicks}")
        on_button_click()  

        # Функція для обробки натискання на кнопку button1
def on_button8_click():
    global click_count, button8_clicks, button8_cost
    if click_count >= button8_cost:
        click_count -= button8_cost
        button8_clicks += 1
        button8_cost += int(button8_cost * button8_multiplier)
        label.config(text=f"Баланс: {click_count}")
        button8.config(text=f"Боевая Машина (+65)| Вартість: {button8_cost} | Куплено: {button8_clicks}")
        on_button_click()  

# Завантаження зображення для кнопки "click"
image10 = tk.PhotoImage(file="Зображення/Нож.png")

# Завантаження зображення для кнопки "click"
image2 = tk.PhotoImage(file="Зображення/Меч.png")

image3 = tk.PhotoImage(file="Зображення/Гранатомет.png")

image4 = tk.PhotoImage(file="Зображення/Снайперка.png")

image5 = tk.PhotoImage(file="Зображення/Автомат.png")

image6 = tk.PhotoImage(file="Зображення/Дробовик.png")

image7 = tk.PhotoImage(file="Зображення/Пулемет.png")

image8 = tk.PhotoImage(file="Зображення/Штурмова Винтовка.png")

image9 = tk.PhotoImage(file="Зображення/Боевая Машина.png")

# Створення фрейму для меню "Shop"
shop_frame = tk.Frame(window, bg="lightgray")

# Створення кнопок у фреймі "Shop"
button1 = tk.Button(shop_frame, image=image10, text=" Нож (+1) | Вартість: 10 | Куплено: 0", compound="top", command=on_button1_click, width=325)
button1.pack()

button2 = tk.Button(shop_frame, image=image3, text=" Гранатомет (+5) | Вартість: 45 | Куплено: 0", compound="top", command=on_button2_click, width=325)
button2.pack()

button3 = tk.Button(shop_frame, image=image4, text=" Снайперка (+8) | Вартість: 90 | Куплено: 0", compound="top", command=on_button3_click, width=325)
button3.pack()

button4 = tk.Button(shop_frame, image=image5, text=" Автомат (+15) | Вартість: 190 | Куплено: 0", compound="top", command=on_button4_click, width=325)
button4.pack()

button5 = tk.Button(shop_frame, image=image6, text=" Дробовик (+22) | Вартість: 300 | Куплено: 0", compound="top", command=on_button5_click, width=325)
button5.pack()

button6 = tk.Button(shop_frame, image=image7, text=" Пулемет (+30) | Вартість: 750 | Куплено: 0", compound="top", command=on_button6_click, width=325)
button6.pack()

button7 = tk.Button(shop_frame, image=image8, text=" Штурмова Винтовка (+45) | Вартість: 1650 | Куплено: 0", compound="top", command=on_button7_click, width=325)
button7.pack()

button8 = tk.Button(shop_frame, image=image9, text=" Боевая машина (+65) | Вартість: 7500 | Куплено: 0", compound="top", command=on_button8_click, width=325)
button8.pack()

def open_shop():
    shop_frame.pack(side="left", fill="both")
    shop_button.config(state=tk.DISABLED)  # Деактивуємо кнопку "Shop"

def close_shop():
    shop_frame.pack_forget()
    shop_button.config(state=tk.NORMAL)  # Активуємо кнопку "Shop"

# Створення кнопки "Меню"
shop_button = tk.Button(window, text="Shop", command=open_shop, width=7, height=2, fg="black")
shop_button.place(x=1210, y=5)

# Створення кнопки для закриття меню "Shop" (хрестик)
close_button = tk.Button(shop_frame, text="✖ Закрити Shop", command=close_shop, width=15, fg="black")
close_button.pack(side="right", anchor="n")

# Ви можете використовувати клавішу Escape для виходу з повноекранного режиму
def exit_fullscreen(event):
    window.attributes('-fullscreen', False)

window.bind("<Escape>", exit_fullscreen)

# Створення мітки для відображення балансу
label = tk.Label(window, text=f"Баланс: {click_count}")
label.place(x=600, y=1)

# Кнопка "click"
click_button = tk.Button(window, image=image2, text="click", command=on_button_click, width=200, height=200)
click_button.place(y=400, x=535)

# Запуск головного циклу Tkinter для відображення вікна
window.mainloop()