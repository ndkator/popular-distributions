from tkinter import *
import matplotlib.pyplot as plt
import random as rnd
import time
from scipy.stats import trapz

root = Tk()
root.title('МОДЕЛИРОВАНИЕ ИС. ПРАКТИКА.')
root.geometry('550x325+400+150')  # Первоначальный размер окна
root.configure(background='red')
root.resizable(False, False)

USERchoice = StringVar() # Переменная для выбора необходимого распределения

def enjoy(): # Функция перехода из первоначальной формы в последующую

    def histwork(massiv): # Функция работы с гистограммой

        clr = ['crimson', 'burlywood', 'chartreuse', 'darkmagenta',
               'darkviolet', 'green', 'gold', 'indigo', 'khaki']
        y = massiv
        plt.hist(y, int(INTERV.get()), color=[rnd.choice(clr)], histtype='bar', rwidth=0.8)
        plt.xlabel('Интервалы')
        plt.ylabel('Значения')
        plt.title('Гистограмма')
        print('\nПостроение выполнено успешно!')

    def valuesoutput(massiv, t1, t2): # Функция вывода тайминга и срезов из массива
        if int(N1.get()) < 100:
            infolbl.delete('1.0', END)
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX')
            infolbl.insert('1.0', '\n')
            infolbl.insert('1.0', massiv)
            infolbl.insert('1.0', 'Исходный массив: ' + '\n')
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX' + '\n')
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX' + '\n' * 2)
            infolbl.insert('1.0', '\n')
            infolbl.insert('1.0', t2 - t1)
            infolbl.insert('1.0', 'Время выполнения (сек): ' + '\n')
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX' + '\n')
        else:
            infolbl.delete('1.0', END)
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX')
            infolbl.insert('1.0', '\n')
            infolbl.insert('1.0', massiv[-15:])
            infolbl.insert('1.0', '\n')
            infolbl.insert('1.0', massiv[:15])
            infolbl.insert('1.0', 'Исходный массив: ' + '\n')
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX' + '\n')
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX' + '\n' * 2)
            infolbl.insert('1.0', '\n')
            infolbl.insert('1.0', t2 - t1)
            infolbl.insert('1.0', 'Время выполнения (сек): ' + '\n')
            infolbl.insert('1.0', 'XXXXXXXXXXXXXXXXXX' + '\n')

    def create(): # Равномерное распределение
        t1 = time.time() # старт таймера
        massiv = []
        i = 0
        while i < int(N1.get()):
            massiv.append(rnd.uniform(int(LEFTZ.get()), int(RightZ.get())))
            i += 1
        massiv.sort()  # на выходе - отсортированные по возрастанию значения
        histwork(massiv) # передаём переменную massiv в функцию работы с гистограммой
        t2 = time.time() # остановка таймера
        valuesoutput(massiv, t1, t2) # вывод тайминга и срезов
        plt.show() # вывод графика

    def expocreate(): # Экспоненциальное распределение
        t1 = time.time()
        massiv = []
        i = 0
        while i < int(N1.get()):
            massiv.append(rnd.expovariate(int(LAMBDD.get())))
            i += 1
        massiv.sort()
        histwork(massiv)
        t2 = time.time()
        valuesoutput(massiv, t1, t2)
        plt.show()

    def simpsoncreate(): # Треугольное распределение
        t1 = time.time()
        massiv = []
        i = 0
        while i < int(N1.get()):
            massiv.append(rnd.triangular(int(LOWW.get()), int(HIGHH.get())))
            i += 1
        massiv.sort()
        histwork(massiv)
        t2 = time.time()
        valuesoutput(massiv, t1, t2)
        plt.show()

    def normalcreate(): # Нормальное распределение
        t1 = time.time()
        massiv = []
        i = 0
        while i < int(N1.get()):
            massiv.append(rnd.normalvariate(int(MUU.get()), int(SIGMAA.get())))
            i += 1
        massiv.sort()
        histwork(massiv)
        t2 = time.time()
        valuesoutput(massiv, t1, t2)
        plt.show()

    def trapzcreate(): # Трапецеидальное распределение
        '''c, d = 0.5, 0.6 # моменты'''
        r = trapz.rvs(float(CE.get()), float(DE.get()), int(loc.get()), int(scale.get()) - int(loc.get()),
                      size=int(N1.get()))

        t1 = time.time()
        histwork(r)
        t2 = time.time()
        valuesoutput(r, t1, t2)
        plt.show()


    # ОПРЕДЕЛЕНИЕ ВИДА РАСПРЕДЕЛЕНИЯ
    if USERchoice.get() == '1':
        #################### РАВНОМЕРНОЕ РАСПРЕДЕЛЕНИЕ ####################
        zoot = Tk()
        zoot.title('Равномерное распределение')
        zoot.geometry('550x325+400+150')
        zoot.configure(background='crimson')
        zoot.resizable(False, False)

        lbl1 = Label(zoot, text='Количество чисел в массиве:', font='20',
                     background='crimson', fg='white')
        lbl1.place(x=25, y=25)

        lbl2 = Label(zoot, text='Количество интервалов:', font='20',
                     background='crimson', fg='white')
        lbl2.place(x=25, y=75)

        lbl3 = Label(zoot, text='Граница интервала слева:', font='20',
                     background='crimson', fg='white')
        lbl3.place(x=25, y=125)

        lbl4 = Label(zoot, text='Граница интервала справа:', font='20',
                     background='crimson', fg='white')
        lbl4.place(x=25, y=175)

        N1 = Entry(zoot, width=10, bg='white', fg='black')
        N1.place(x=250, y=25)

        INTERV = Entry(zoot, width=10, bg='white', fg='black')
        INTERV.place(x=250, y=75)

        LEFTZ = Entry(zoot, width=10, bg='white', fg='black')
        LEFTZ.place(x=250, y=125)

        RightZ = Entry(zoot, width=10, bg='white', fg='black')
        RightZ.place(x=250, y=175)

        infolbl = Text(zoot, height=12, width=25, font='Arial 8', wrap=WORD,
                       bg='black', fg='white')
        infolbl.place(x=350, y=25)
        infolbl.insert('1.0', 'В данном блоке будет выведен полученный массив')
        scrollbar = Scrollbar(zoot)
        scrollbar.place(x=504, y=25)
        scrollbar['command'] = infolbl.yview
        infolbl['yscrollcommand'] = scrollbar.set

        btn1 = Button(zoot, text='CLICK ME',
                      background='Black',  # фоновый цвет кнопки
                      foreground='White',  # цвет текста
                      activeforeground='Black',
                      activebackground='White',  # цвет кнопки, когда она находится в нажатом состоянии
                      bd=4,
                      padx=2,
                      pady=4,
                      width=26,
                      font='15',
                      command=create)
        btn1.place(x=275, y=225)
        zoot.mainloop()


    elif USERchoice.get() == '2':
        ################# ЭКСПОНЕНЦИАЛЬНОЕ РАСПРЕДЕЛЕНИЕ #################
        xoot = Tk()
        xoot.title('Экспоненциальное распределение')
        xoot.geometry('550x325+400+150')
        xoot.configure(background='darkviolet')
        xoot.resizable(False, False)

        lbl1 = Label(xoot, text='Количество чисел в массиве: ', font='20',
                     bg='darkviolet', fg='white')
        lbl1.place(x=25, y=25)

        lbl2 = Label(xoot, text='Количество интервалов: ', font='20',
                     bg='darkviolet', fg='white')
        lbl2.place(x=25, y=75)

        lbl3 = Label(xoot, text='Значение лямбда: ', font='20',
                     bg='darkviolet', fg='white')
        lbl3.place(x=25, y=125)

        N1 = Entry(xoot, width=10, bg='black', fg='white')
        N1.place(x=250, y=25)

        INTERV = Entry(xoot, width=10, bg='black', fg='white')
        INTERV.place(x=250, y=75)

        LAMBDD = Entry(xoot, width=10, bg='black', fg='white')
        LAMBDD.place(x=250, y=125)

        infolbl = Text(xoot, height=12, width=25, font='Arial 8', wrap=WORD,
                       bg='black', fg='white')
        infolbl.place(x=350, y=25)
        infolbl.insert('1.0', 'В данном блоке будет выведен полученный массив')
        scrollbar = Scrollbar(xoot)
        scrollbar.place(x=504, y=25)
        scrollbar['command'] = infolbl.yview
        infolbl['yscrollcommand'] = scrollbar.set

        btn1 = Button(xoot, text='CLICK ME',
                      background='Black',  # фоновый цвет кнопки
                      foreground='White',  # цвет текста
                      activeforeground='Black',
                      activebackground='White',  # цвет кнопки, когда она находится в нажатом состоянии
                      bd=4,
                      padx=2,
                      pady=4,
                      width=26,
                      font='15',
                      command=expocreate)
        btn1.place(x=275, y=225)
        xoot.mainloop()


    elif USERchoice.get() == '3':
        #################### ТРЕУГОЛЬНОЕ РАСПРЕДЕЛЕНИЕ ####################
        coot = Tk()
        coot.title('Треугольное распределение')
        coot.geometry('550x325+400+150')
        coot.configure(background='green')
        coot.resizable(False, False)

        lbl1 = Label(coot, text='Количество чисел в массиве: ', font='20',
                     bg='green', fg='white')
        lbl1.place(x=25, y=25)

        lbl2 = Label(coot, text='Количество интервалов: ', font='20',
                     bg='green', fg='white')
        lbl2.place(x=25, y=75)

        lbl3 = Label(coot, text='Граница интервала слева: ', font='20',
                     bg='green', fg='white')
        lbl3.place(x=25, y=125)

        lbl4 = Label(coot, text='Граница интервала справа: ', font='20',
                     bg='green', fg='white')
        lbl4.place(x=25, y=175)

        N1 = Entry(coot, width=10)
        N1.place(x=250, y=25)

        INTERV = Entry(coot, width=10)
        INTERV.place(x=250, y=75)

        LOWW = Entry(coot, width=10)
        LOWW.place(x=250, y=125)

        HIGHH = Entry(coot, width=10)
        HIGHH.place(x=250, y=175)

        infolbl = Text(coot, height=12, width=25, font='Arial 8', wrap=WORD,
                       bg='black', fg='white')
        infolbl.place(x=350, y=25)
        infolbl.insert('1.0', 'В данном блоке будет выведен полученный массив')

        scrollbar = Scrollbar(coot)
        scrollbar.place(x=504, y=25)
        scrollbar['command'] = infolbl.yview
        infolbl['yscrollcommand'] = scrollbar.set

        btn2 = Button(coot, text='CLICK ME',
                      background='Black',  # фоновый цвет кнопки
                      foreground='White',  # цвет текста
                      activeforeground='Black',
                      activebackground='White',  # цвет кнопки, когда она находится в нажатом состоянии
                      bd=4,
                      padx=2,
                      pady=4,
                      width=26,
                      font='15',
                      command=simpsoncreate)
        btn2.place(x=275, y=225)
        coot.mainloop()


    elif USERchoice.get() == '4':
        ################# НОРМАЛЬНОЕ РАСПРЕДЕЛЕНИЕ #################
        voot = Tk()
        voot.title('Нормальное распределение')
        voot.geometry('550x325+400+150')
        voot.configure(background='yellow')
        voot.resizable(False, False)

        lbl1 = Label(voot, text='Количество чисел в массиве: ', font='20',
                     bg='yellow')
        lbl1.place(x=25, y=25)

        lbl2 = Label(voot, text='Количество интервалов: ', font='20',
                     bg='yellow')
        lbl2.place(x=25, y=75)

        lbl3 = Label(voot, text='Значение Mu: ', font='20',
                     bg='yellow')
        lbl3.place(x=25, y=125)

        lbl4 = Label(voot, text='Значение Sigma: ', font='20',
                     bg='yellow')
        lbl4.place(x=25, y=175)

        N1 = Entry(voot, width=10)
        N1.place(x=250, y=25)

        INTERV = Entry(voot, width=10)
        INTERV.place(x=250, y=75)

        MUU = Entry(voot, width=10)
        MUU.place(x=250, y=125)

        SIGMAA = Entry(voot, width=10)
        SIGMAA.place(x=250, y=175)

        infolbl = Text(voot, height=12, width=25, font='Arial 8', wrap=WORD,
                       bg='white', fg='black')
        infolbl.place(x=350, y=25)
        infolbl.insert('1.0', 'В данном блоке будет выведен полученный массив')

        scrollbar = Scrollbar(voot)
        scrollbar.place(x=504, y=25)
        scrollbar['command'] = infolbl.yview
        infolbl['yscrollcommand'] = scrollbar.set

        btn3 = Button(voot, text='CLICK ME',
                      background='Black',  # фоновый цвет кнопки
                      foreground='White',  # цвет текста
                      activeforeground='Black',
                      activebackground='White',  # цвет кнопки, когда она находится в нажатом состоянии
                      bd=4,
                      padx=2,
                      pady=4,
                      width=26,
                      font='15',
                      command=normalcreate)
        btn3.place(x=275, y=225)
        voot.mainloop()


    elif USERchoice.get() == '5':
        ################# ТРАПЕЦЕИДАЛЬНОЕ РАСПРЕДЕЛЕНИЕ #################
        boot = Tk()
        boot.title('Трапецеидальное распределение')
        boot.geometry('550x325+400+150')
        boot.configure(background='purple')
        boot.resizable(False, False)

        lbl1 = Label(boot, text='Количество чисел в массиве: ', font='20',
                     bg='purple', fg='white')
        lbl1.place(x=25, y=25)

        lbl2 = Label(boot, text='Количество интервалов: ', font='20',
                     bg='purple', fg='white')
        lbl2.place(x=25, y=75)

        lbl3 = Label(boot, text='Граница слева: ', font='20',
                     bg='purple', fg='white')
        lbl3.place(x=25, y=125)

        lbl4 = Label(boot, text='Граница справа: ', font='20',
                     bg='purple', fg='white')
        lbl4.place(x=25, y=175)

        lbl5 = Label(boot, text='Значение c: ', font='20',
                     bg='purple', fg='white')
        lbl5.place(x=350, y=25)

        lbl6 = Label(boot, text='Значение d: ', font='20',
                     bg='purple', fg='white')
        lbl6.place(x=350, y=75)

        N1 = Entry(boot, width=10)
        N1.place(x=250, y=25)

        INTERV = Entry(boot, width=10)
        INTERV.place(x=250, y=75)

        loc = Entry(boot, width=10)
        loc.place(x=250, y=125)

        scale = Entry(boot, width=10)
        scale.place(x=250, y=175)

        infolbl = Text(boot, height=6, width=25, font='Arial 8', wrap=WORD,
                       bg='black', fg='white')
        infolbl.place(x=350, y=125)
        infolbl.insert('1.0', 'В данном блоке будет выведен полученный массив')

        scrollbar = Scrollbar(boot)
        scrollbar.place(x=504, y=125)
        scrollbar['command'] = infolbl.yview
        infolbl['yscrollcommand'] = scrollbar.set

        CE = Entry(boot, width=10)
        CE.place(x=450, y=25)

        DE = Entry(boot, width=10)
        DE.place(x=450, y=75)

        btn4 = Button(boot, text='CLICK ME',
                      background='Black',  # фоновый цвет кнопки
                      foreground='White',  # цвет текста
                      activeforeground='Black',
                      activebackground='White',  # цвет кнопки, когда она находится в нажатом состоянии
                      bd=4,
                      padx=2,
                      pady=4,
                      width=26,
                      font='15',
                      command=trapzcreate)
        btn4.place(x=275, y=225)
        boot.mainloop()


############# ВИЗУАЛИЗАЦИЯ ПЕРВОНАЧАЛЬНОЙ ФОРМЫ #############
lbl0 = Label(text='Укажите вид распределения: ', font='20',
             background='red', fg='white')
lbl0.place(x=185, y=25)

RAVNOMER = Radiobutton(text="Равномерное распределение", value=1,
                       variable=USERchoice, padx=15, pady=10, indicatoron=0,
                       width=30)
RAVNOMER.place(x=25, y=75)

EXPONENC = Radiobutton(text="Экспоненциальное распределение", value=2,
                       variable=USERchoice, padx=15, pady=10, indicatoron=0,
                       width=30)
EXPONENC.place(x=25, y=150)

TREUGOL = Radiobutton(text="Треугольное распределение", value=3,
                      variable=USERchoice, padx=15, pady=10, indicatoron=0,
                      width=30)
TREUGOL.place(x=25, y=225)

NORMAL = Radiobutton(text="Нормальное распределение", value=4,
                     variable=USERchoice, padx=15, pady=10, indicatoron=0,
                     width=30)
NORMAL.place(x=275, y=75)

ERLAN = Radiobutton(text="Трапецеидальное распределение", value=5,
                    variable=USERchoice, padx=15, pady=10, indicatoron=0,
                    width=30)
ERLAN.place(x=275, y=150)

btn0 = Button(root, text='CLICK ME',
              background='Black',  # фоновый цвет кнопки
              foreground='White',  # цвет текста
              activeforeground='Black',
              activebackground='White',  # цвет кнопки, когда она находится в нажатом состоянии
              bd=4,
              padx=2,
              pady=4,
              width=26,
              font='15',
              command=enjoy)
btn0.place(x=275, y=225)
root.mainloop() # Фиксация первоначального окна
