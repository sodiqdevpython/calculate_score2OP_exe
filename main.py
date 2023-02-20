from tkinter import *
from tkinter import filedialog
import os
import pandas as pd
import numpy as np
from tkinter import messagebox

# validate funksiyasi faqat raqam yozadigan qiladi.
def validate(new_value):                                                  

    try:
        if new_value == "" or new_value == "-" or new_value == "+":
            return True
        _str = str(float(new_value))
        return True
    except:
        return False
        #   return new_value == "" or new_value.isnumeric() or new_value == "."
#        Functions

data1 = {1: [62, 60, 58, 56, 53, 50, 47, 44, 44, 41, 37, 34, 37, 33, 29, 26, 27, 22, 18, 15, 20, 16, 12, 10, 14, 11, 8, 7, 10, 8, 6, 4, 7, 5, 4, 3, 5, 4, 3, 2], 2: [63, 61, 59, 57, 54, 51, 48, 45, 46, 42, 39, 35, 38, 34, 30, 27, 28, 23, 19, 16, 21, 17, 13, 11, 15, 12, 9, 7, 11, 9, 6, 5, 8, 6, 4, 3, 6, 4, 3, 2], 3: [64, 62, 60, 58, 55, 52, 49, 47, 47, 43, 40, 36, 39, 35, 31, 28, 30, 24, 20, 16, 22, 18, 14, 11, 17, 13, 10, 8, 12, 9, 7, 5, 9, 7, 5, 4, 7, 5, 3, 2], 4: [65, 63, 61, 60, 57, 54, 51, 48, 48, 45, 41, 37, 41, 36, 32, 29, 31, 26, 21, 17, 24, 19, 15, 12, 18, 14, 11, 9, 14, 11, 8, 6, 10, 8, 6, 4, 8, 6, 4, 3]}
data2 = {1: [65, 63, 61, 59, 59, 56, 53, 50, 53, 49, 46, 42, 48, 43, 39, 34, 41, 34, 28, 23, 33, 27, 22, 17, 26, 21, 16, 13, 21, 16, 12, 9, 16, 12, 9, 7, 13, 9, 7, 5], 2: [66, 64, 62, 60, 60, 57, 54, 51, 55, 51, 47, 43, 49, 44, 40, 36, 42, 36, 30, 24, 35, 29, 23, 18, 28, 23, 18, 14, 23, 18, 13, 10, 18, 14, 10, 8, 15, 11, 8, 6], 3: [67, 65, 63, 61, 62, 59, 56, 53, 56, 52, 48, 44, 51, 46, 41, 37, 44, 37, 31, 26, 37, 30, 25, 20, 31, 24, 19, 15, 25, 19, 15, 11, 21, 15, 12, 9, 17, 12, 9, 6], 4: [68, 66, 65, 63, 63, 60, 57, 54, 58, 53, 49, 46, 52, 47, 43, 38, 46, 39, 33, 27, 39, 32, 26, 21, 33, 26, 21, 16, 28, 22, 17, 13, 23, 17, 13, 10, 19, 14, 10, 7]}
data3 = {1: [49, 48, 47, 46, 44, 42, 40, 38, 40, 37, 34, 31, 35, 32, 28, 25, 26, 22, 18, 15, 20, 17, 14, 11, 16, 13, 10, 8, 12, 10, 7, 6, 9, 7, 5, 4, 7, 5, 4, 3], 2: [54, 53, 52, 50, 48, 46, 43, 41, 42, 39, 36, 33, 37, 33, 30, 26, 28, 24, 20, 17, 23, 19, 15, 12, 18, 14, 11, 9, 14, 11, 9, 7, 11, 8, 6, 5, 9, 6, 5, 4], 3: [59, 58, 56, 55, 52, 49, 47, 45, 45, 42, 39, 36, 39, 35, 31, 28, 30, 26, 21, 18, 25, 20, 17, 14, 20, 16, 13, 10, 16, 13, 10, 8, 13, 10, 8, 6, 11, 8, 6, 4], 4: [64, 63, 61, 60, 56, 53, 51, 48, 48, 44, 41, 38, 40, 36, 33, 29, 32, 27, 23, 19, 27, 22, 18, 15, 23, 18, 15, 12, 19, 15, 12, 9, 16, 12, 9, 7, 13, 10, 7, 5]}
data4 = {1: [49, 48, 47, 46, 47, 45, 43, 40, 45, 42, 39, 36, 43, 39, 35, 31, 36, 31, 26, 22, 31, 25, 21, 17, 25, 21, 17, 13, 21, 17, 13, 10, 17, 13, 10, 8, 14, 11, 8, 6], 2: [54, 53, 52, 50, 51, 49, 46, 44, 48, 44, 41, 38, 45, 41, 36, 33, 39, 33, 28, 24, 33, 28, 23, 19, 28, 23, 19, 15, 24, 19, 15, 12, 20, 16, 12, 9, 17, 13, 10, 7], 3: [59, 58, 56, 55, 55, 52, 50, 48, 51, 47, 44, 41, 47, 42, 38, 34, 42, 36, 30, 26, 36, 31, 25, 21, 32, 26, 21, 17, 28, 22, 17, 14, 24, 18, 14, 11, 20, 16, 12, 9], 4: [64, 63, 61, 60, 59, 56, 54, 51, 54, 50, 47, 43, 49, 44, 40, 36, 44, 38, 33, 28, 40, 33, 28, 23, 35, 29, 24, 19, 31, 25, 20, 16, 28, 22, 17, 13, 24, 19, 14, 11]}

ar1 = pd.DataFrame(data1)
ar2 = pd.DataFrame(data2)
ar3 = pd.DataFrame(data3)
ar4 = pd.DataFrame(data4)


def imt():
    rost = entry_5.get()
    rost = float(rost)
    massa = entry_6.get()
    massa = float(massa)
    global fla, fla_result
    fla = massa/(rost**2)
    fla = round(fla, 2)
    if fla >= 9 and fla <= 24.9:
        fla_result = 'Норма'
    elif fla >= 25 and fla <= 29.9:
        fla_result = 'Предожирение'
    elif fla >= 30 and fla <= 34.9:
        fla_result = 'Первая степень ожирения'
    elif fla >= 35 and fla <= 39.9:
        fla_result = 'Вторая степень ожирения'
    elif fla >= 40 and fla <= 44.9:
        fla_result = 'Третья степень ожирения'
    elif fla >= 45:
        fla_result = 'Четвертая степень ожирения'
    else:
        fla_result = 'Вы ввели недопустимое значение'
    lblr0.configure(text=f"{fla_result}")

def track_entry_change(*args):
    
    massa=float(massa_entry.get()) 
    rost=float(rost_entry.get())
    if massa==0 or rost==0:
        massa=0
        rost=1
        label_text.set(round(massa/(rost*rost),2))
    else:
        label_text.set(round(massa/(rost*rost),2))
      

def imt2():
    tali = float(entry_8.get())
    beder = float(entry_9.get())
    global tb, tbtext
    tb = (tali/beder)
    tb = round(tb, 2)
    jins = int(pol.get())
    if jins == 1:
        if tb >= 1:
            lblr3.configure(text=f"Абдоминально-висцерального ожирения") 
            tbtext="Абдоминально-висцерального ожирения"
        else:
            lblr3.configure(text=f"норме Абдоминально-висцерального ожирения нет") 
            tbtext="норме Абдоминально-висцерального ожирения нет"
    else:
        if tb >= 0.85:
            lblr3.configure(text=f"Абдоминально-висцерального ожирения") 
            tbtext="Абдоминально-висцерального ожирения"
        else:
            lblr3.configure(text=f"норме Абдоминально-висцерального ожирения нет")  
            tbtext="норме Абдоминально-висцерального ожирения нет" 
    
#       End of functions

def track_entry_change2(*args):
    tali=float(tali_entry.get()) 
    beder=float(beder_entry.get())
    if tali==0 or beder==0:
        tali=0
        beder=1
        label_text_tb.set(round(tali/(beder),3))
    else:
        label_text_tb.set(round(tali/(beder),3))
    

def result():
    if (entry_3.get() and entry_4.get()) and smoke.get():
        global sad, dad, smokeResult
        sad = entry_3.get()
        sad = float(sad)
        dad = entry_4.get()
        dad = float(dad)
        smokeResult = smoke.get()
        score_math = []
        global numIntVar
        numIntVar = 0
        global lst
        lst2 = [var2, var3, var4, var5, var6, var7, var8]
        lst = [var1, var2, var3, var4, var5, var6,
               var7, var8, var9, var10, var11]
        for i in lst:
            score_math.append(i)
            numIntVar += i.get()
        global score
        if len(lst) == len(lst2) and lst == lst2:
            score = 0
        else:
            score = 1
    else:
        messagebox.showerror(
            'Ошибка', 'Обязательное для заполнения поле: Вредные привычки; САД ; ДАД; Пульс (ЧСС) ')
    jins = int(pol.get())
    if jins == 1:
        try:
            entr1 = float(entry_10.get())
        except:
            entr1 = 1
        if numIntVar >= 4:
            result = ('Очень высокий риск')
        elif (lst[8].get()) == 1 and entr1 >= 6.9 and numIntVar < 4:
            result = ('Высокий риск')
        elif numIntVar == 0 and smokeResult == 2:
            result = ('Низкий риск')
        elif numIntVar == 2:
            result = ('Умеренный риск')
        else:
            result = ('Высокий риск')
    else:
        try:
            entr1 = float(entry_10.get())
        except:
            entr1 = 1
        if numIntVar >= 4:
            result = ('группа очень высокого сердечно сосудистого риска')
        elif (lst[8].get()) == 1 and entr1 >= 5.1 and numIntVar < 4:
            result = ('группа высокого сердечно сосудистого риска')
        elif numIntVar == 0 and smokeResult == 2:
            result = ('группа низкого сердечно сосудистого риска')
        elif numIntVar == 2:
            result = ('группа умеренного сердечно сосудистого риска')
        else:
            result = ('группа высокого сердечно сосудистого риска ')
    #stepen АГ ni aniqlash 
    global kateg_step512
    if sad <= 120 and dad<=80 :
        kateg_step512 = ('Оптимальное артериальное давление ')
    elif sad <= 130 and dad<=85 :
        kateg_step512 = ('Нормальное артериальное давление ')
    elif (sad >= 130 and sad<=139 ) and (dad >=85 and dad<=89):
        kateg_step512 = ('Высокое нормальное артериальное давление ')
    elif (sad >= 140 and sad<=159 ) and (dad >=90 and dad<=99):
        kateg_step512 = ('Артериальная гипертензия 1 степени')
    elif (sad >= 160 and sad<=179 ) and (dad >=100 and dad<=109):
        kateg_step512 = ('Артериальная гипертензия 2 степени')
    elif (sad >= 180 and sad<=230 ) and (dad >=110 and dad<=180):
        kateg_step512 = ('Артериальная гипертензия 3 степени')
    else:
        kateg_step512 = ('Неправние САД или ДАД данные')

    
    
    
    #               Score 2 OP agar 70 dan baland bulsa
    if jins == 1:
        muj = True
        jen = False
    else:
        muj = False
        jen = True
    if smokeResult == 2:
        k = False
        nk = True
    else:
        k = True
        nk = False
    sad1 = int(sad)
    if 160 <= sad1 and sad1 <= 170:
        son1 = 0
    elif ((140 <= sad1) and (sad1 <= 159)):
        son1 = 1
    elif ((120 <= sad1) and (sad1 <= 139)):
        son1 = 2
    elif ((100 <= sad1) and (sad1 <= 119)):
        son1 = 3
    sonn = int(son1)
    # print(son)
    yosh1 = int(entry_2.get())
    if yosh1 >= 85 and yosh1 <= 89:
        s = 1
    elif yosh1 >= 80 and yosh1 <= 84:
        s = 5
    elif yosh1 >= 75 and yosh1 <= 79:
        s = 9
    elif yosh1 >= 70 and yosh1 <= 74:
        s = 13
    elif yosh1 >= 65 and yosh1 <= 69:
        s = 17
    elif yosh1 >= 60 and yosh1 <= 64:
        s = 21
    elif yosh1 >= 55 and yosh1 <= 59:
        s = 25
    elif yosh1 >= 50 and yosh1 <= 54:
        s = 29
    elif yosh1 >= 45 and yosh1 <= 49:
        s = 33
    elif yosh1 >= 40 and yosh1 <= 44:
        s = 37
    elif yosh1 >= 0 and yosh1 <= 40:
        s = 41
        # print('40 dan yuqori yosh bulishi kerak')
        # print(s)
    global s1
    s1 = (sonn) + (s) - (1)
    # print(s+1, 'satr')  # satr tartib raqami topildi
    # ustun tartib raqamini topamiz
    m = 0.0011*(float(entry_puls.get())) + 0.014*(sad) + 0.008*(dad) + 0.009 * (float(entry_6.get())) - 0.009 * (float(entry_5.get())) + 0.014*(float(entry_2.get()))-0.27
    ml = float(entry_15.get())
    if (m >= 3 and m <= 3.9) or (ml >= 100 and ml <= 150):
        u = 0
    elif (m >= 4 and m <= 4.9) or (ml >= 150 and ml <= 200):
        u = 1
    elif (m >= 5 and m <= 5.9) or (ml >= 200 and ml <= 250):
        u = 2
    elif (m >= 6 and m <= 6.9) or (ml > 250):
        u = 3
        # print(u+1, 'ustun')
        # ustun topildi
    global rost
    rost = float(entry_5.get())
    
    
    
    global tt
    
    if jen:
        if k:
            tt = ar1.iat[s, u]
            #print(tt)
        else:
            tt = ar2.iat[s, u]
            #print(tt)
    else:
        if k:
            tt = ar3.iat[s, u]
        else:
            tt = ar4.iat[s, u]
    if entry_15 and entry_13:
        ka = float(entry_13.get())-float(entry_15.get())
    else:
        messagebox.showerror(
            'Ошибка', 'ЛПВП  и  Общий холестерин обязательны')

    if jins == 1:
        #ЛПВП ni hisoblash
        if float(entry_15.get())>=0.9 and float(entry_15.get())<=1.7:
            addupt2 = ''
        elif float(entry_15.get())<0.9 :
            addupt2 = 'Низкий уровень ЛПВП'
        elif float(entry_15.get())>1.7:
            addupt2 = 'Высокие значения ХС ЛПВП'
        else:
            addupt2 = 'неправильный значения'
        #ЛПНП ni hisoblash
        if  float(entry_12.get())>=1.9 and float(entry_12.get())<=3.5:
            addupt3 = ''
        elif  float(entry_12.get())<1.9:
            addupt3 = 'Липопротеины низкой плотности (ЛПНП)'
        elif  float(entry_12.get())>3.5:
            addupt3 = 'Повышение ЛПНП '
        else:
            addupt3 = 'неправильный значения'
        # Креатинин
        if    float(entry_13.get())>=44 and float(entry_13.get())<=80:
            addupt4 = ''
        elif  float(entry_13.get())<44:
            addupt4 = 'Низкий уровень креатинина в крови'
        elif   float(entry_13.get())>80:
            addupt4 = 'Высокий уровень креатинина в крови'        
        else:
            addupt3 = 'неправильный значения'    
        #mochevoy
    
        if  float(entry_11.get())>=210 and float(entry_11.get())<=458:
            addupt5 = ''
        elif  float(entry_11.get())<210:
            addupt5 = 'Снижение уровня мочевой кислот в крови'
        elif float(entry_11.get())>458:
            addupt5 = 'Повышение уровня мочевой кислоты в крови'
        else:
            addupt5 = 'неправильный значения'            
            
    elif   jins != 1:
    #ЛПВП ni hisoblash
        if  float(entry_15.get())>=1.17 and float(entry_15.get())<=2.3:
            addupt2 = ''
        elif float(entry_15.get())<1.17:
            addupt2 = 'Низкий уровень ЛПВП'
        elif float(entry_15.get())>2.3:
            addupt2 = 'Высокие значения ХС ЛПВП '
        else:
            addupt2 = 'неправильный значения'
    #ЛПНП ni hisoblash
        if float(entry_12.get())>=2.2 and float(entry_12.get())<=3.38:
            addupt3 = ''
        elif float(entry_12.get())<2.2:
            addupt3 = 'Липопротеины низкой плотности (ЛПНП)'
        elif float(entry_12.get())>3.38:
            addupt3 = 'Повышение ЛПНП '  
        else:
            addupt3 = 'неправильный значения'
        # Креатинин
        if  float(entry_13.get())>=53 and float(entry_13.get())<=97:
            addupt4 = ''
        elif  float(entry_13.get())<53:
            addupt4 = 'Низкий уровень креатинина в крови'
        elif  float(entry_13.get())>97:
            addupt4 = 'Высокий уровень креатинина в крови'
        else:
            addupt4 = 'неправильный значения'
    #mochevoy
        if  float(entry_11.get())>=150 and float(entry_11.get())<=405:
            addupt5 = ''
        elif  float(entry_11.get())<150:
            addupt5 = 'Снижение уровня мочевой кислот в крови'
        elif  float(entry_11.get())>405:
            addupt5 = 'Повышение уровня мочевой кислоты в крови'
        else:
            addupt5 = 'неправильный значения'

    else: 
        messagebox.showerror(
                'Ошибка', 'Выберите пол')
    
    #xolestiren
    if float(entry_14.get())>=3.2 and float(entry_14.get())<=5.4:
        addupt1 = ''
    elif float(entry_14.get())<3.2:
        addupt1 = 'Низкий уровень холестерина'
    elif float(entry_14.get())>5.4:
        addupt1 = 'Высокий уровень холестерина'
    else:
        addupt1 = 'неправильный значения'
        

        #Глюкоза
    if float(entry_10.get())>=4.1 and float(entry_10.get())<=6.1:
        addupt6 = ''
    elif float(entry_10.get())<4.1:
        addupt6 = 'Гипогликемия '
    elif float(entry_10.get())>6.1:
        addupt6 = 'Гипергликемия '
    else:
        addupt6 = 'неправильный значения'
        
    
    # lst_addupts = [addupt1,addupt2,addupt3,addupt4,addupt5,addupt6]
    # num_addupt = 2
    # for i in lst_addupts:
    #     if len(i)>5:
    #         num_addupt+=1
    rost = entry_5.get()
    rost = float(rost)
    massa = entry_6.get()
    massa = float(massa)
    global fla, fla_result
    fla = massa/(rost**2)
    fla = round(fla, 2)
    if float(entry_2.get())>40 and float(entry_2.get())<70 or float(entry_2.get())<40:
        determine_score = 'SCORE2'
        qw = tt
        messagebox.showinfo(
            'Результат', f"SCORE2 : {qw} \n  \t{result}\t\n ИМТ - {fla}   {fla_result}\n Факторы риска \n 1. {kateg_step512} \n 2. {tbtext} \n {addupt1} \n {addupt2} \n {addupt3} \n {addupt4} \n {addupt5} \n {addupt6}") #Коэффицент атерогенности: {ka}\n
    else:
        qw = tt
        determine_score = 'SCORE2-OP'
        messagebox.showinfo(
            'Результат', f"SCORE2-OP : {qw} \n   \t{result}\t\n ИМТ - {fla}   {fla_result}\n Факторы риска \n 1. {kateg_step512} \n  2. {tbtext} \n {addupt1} \n {addupt2} \n {addupt3} \n {addupt4} \n {addupt5} \n {addupt6}") #Коэффицент атерогенности: {ka}\n
    
    view_result = f"Имя: {entry_1.get()} \t Возраст: {int(entry_2.get())} \n {determine_score}: {qw} \t{result}\t\n ИМТ - {fla}  {fla_result}\n Факторы риска \n 1. {kateg_step512} \n 2. {tbtext} \n {addupt1} \n {addupt2} \n {addupt3} \n {addupt4} \n {addupt5} \n {addupt6}"
    with open('result.txt', 'w+', encoding="utf-8") as result_file:
        result_file.write(view_result)

def reset(text):
    entry_lst = [entry_1, entry_2, entry_3, entry_4, entry_5, entry_6, entry_8,
                 entry_9, entry_10, entry_11, entry_12, entry_13, entry_14, entry_15,entry_puls]
    chek_lst = [var1, var2, var3, var4, var5, var6,  var7, var8, var9, var10, var11]

    
    
    for i in entry_lst:
        i.delete(0, END)

    for j in chek_lst:
        j.set(0)
   
    lblr3.configure(text=f"")
    lblr0.configure(text=f"")
    lblr2.configure(text=f"")
    lblr.configure(text=f"")
    entry_8.insert(0, text)
    entry_9.insert(0, text)
    entry_5.insert(0, text)
    entry_6.insert(0, text)
    
    pol.set(None)
    smoke.set(None)

def print_result():
    try:
        file_path = "result.txt"
        if os.name == 'nt':
            commandf = f'notepad /p "{file_path}"'
        else:
            commandf = f'lpr "{file_path}"'
        os.system(commandf)
    except:
        messagebox.showerror('Xato', 'Пожалуйста, введите все формы !')
        pass
window = Tk()
window.title(
    'Программа для определения групп коронарного риска при первичной профилактике сердечно-сосудистых заболеваний')
window.geometry("1030x605")



vcmd = (window.register(validate), '%P')

errmsg = StringVar()

lbl1 = Label(window, text='Программа для определения групп коронарного риска при первичной профилактике сердечно-сосудистых заболеваний', font=('Arial  13 bold italic underline')).place(x=0, y=0)

vir_canvas = Canvas(window,background='black')
vir_canvas.place(x=0, y=0, width=1020,height=6)

vir_canvas1 = Canvas(window,background='black')
vir_canvas1.place(x=0, y=47, width=1020,height=5)

vir_canvas2 = Canvas(window,background='black')
vir_canvas2.place(x=0, y=295, width=1020,height=5)

vir_canvas3 = Canvas(window,background='black')
vir_canvas3.place(x=0, y=352, width=1020,height=5)

vir_canvas4 = Canvas(window,background='black')
vir_canvas4.place(x=0, y=440, width=1020,height=5)

hor_canvas = Canvas(window,background='black')
hor_canvas.place(x=475, y=297, width=5,height=58)



lbl2 = Label(window, text='Ф.И.О.', font=('Helvetica 10')).place(x=5, y=25)
entry_1 = Entry(window)
entry_1.place(x=57, y=25, width=200, height=22)

lbl3 = Label(window, text='Возраст:', font=('Helvetica 10')).place(x=260, y=25)
entry_2 = Entry(window, validate='key', validatecommand=vcmd)
entry_2.place(x=320, y=25, width=30, height=22)

lbl4 = Label(window, text='Пол:').place(x=370, y=25)

pol = IntVar()
Radiobutton(window, variable=pol, text='Мужской',
            value=1).place(x=410, y=22)
Radiobutton(window, variable=pol, text='Женский',
            value=2).place(x=490, y=22)


var1 = IntVar()
chek1 = Checkbutton(window, takefocus=0, text='А. Гипертоническая болезнь',onvalue = 1, offvalue = 0,
            variable=var1).place(x=10, y=74)

var2 = IntVar()
chek2 = Checkbutton(window, takefocus=0, text='В.Ишемическая болезнь сердца. Стабильная стенокардия нарушения',onvalue = 1, offvalue = 0,
            variable=var2).place(x=10, y=110)

var3 = IntVar()
chek3 = Checkbutton(window, takefocus=0, text='С.В анамнезе перенесенный им',onvalue = 1, offvalue = 0,
            variable=var3).place(x=10, y=146)

var4 = IntVar()
chek4 = Checkbutton(window, takefocus=0, text='D.В анамнезе перенесенный ОНМК, ТИА',onvalue = 1, offvalue = 0,
            variable=var4).place(x=10, y=182)

var5 = IntVar()
chek5 = Checkbutton(window, takefocus=0, text='E.XCH',onvalue = 1, offvalue = 0,
            variable=var5).place(x=10, y=218)

var6 = IntVar()
chek6 = Checkbutton(window, takefocus=0, justify=LEFT, text='F.Атеросклероз периферический многососудистый со стенозой и/или\n эндоартерэктомии в анамнезе, аневризма аорты',onvalue = 1, offvalue = 0,
            variable=var6).place(x=10, y=254)

var7 = IntVar()
chek7 = Checkbutton(window, takefocus=0, text='G.Перенесенные операции на сердце и сосудах', onvalue = 1, offvalue = 0,
            variable=var7).place(x=500, y=74)

var8 = IntVar()
chek8 = Checkbutton(window, takefocus=0, justify=LEFT, text='H.Нарушения ритма: (экстросистолия желудочковая, Экстрасистолия \n наджелудочковая, Пароксизмальная наджелудочковая тахикардия, \n Полная блокада правой ножки пучка Гисса, Полная блокада левой ножки пучка\n Гисса,Фибрилляция предсердий Другие нарушения ритма)',onvalue = 1, offvalue = 0,
            variable=var8).place(x=500, y=110)

var9 = IntVar()
chek9 = Checkbutton(window, takefocus=0, text='I.Сахарный диабет без осложнений',onvalue = 1, offvalue = 0,
            variable=var9).place(x=500, y=185)

var10 = IntVar()
chek10 = Checkbutton(window, takefocus=0, text='J.Сахарный диабет с осложнениями',onvalue = 1, offvalue = 0,
            variable=var10).place(x=500, y=215)

var11 = IntVar()
chek11 = Checkbutton(window, takefocus=0, text='К.Нарушение толерантности к глюкозе',onvalue = 1, offvalue = 0,
            variable=var11).place(x=500, y=250)


lbl5 = Label(window, text='Сопутствующие заболевания (отметить):',
             font=('Helvetica 12 bold')).place(x=0, y=50)

lbl6 = Label(window, text='Вредные привычки',
             font=('Helvetica 12 bold')).place(x=0, y=300)
lbl7 = Label(window, text='Гемодинамические показатели и показатели объективного статуса', font=(
    'Helvetica 12 bold')).place(x=482, y=300)

lbl8 = Label(window, text='Курение (отметить):',
             font=('Helvetica 10')).place(x=0, y=330)
vcmd = (window.register(validate), '%P')


smoke = IntVar()
Radiobutton(window, variable=smoke, text='Да',
            value=1).place(x=160, y=328)
Radiobutton(window, variable=smoke, text='Heт',
            value=2).place(x=212, y=328)
Radiobutton(window, variable=smoke, text='Курил в прошлом',
            value=3).place(x=270, y=328)

lblsad = Label(window, text='САД (мм.рт.ст)', font=('Helvetica 10')).place(x=500, y=330)
lbldad = Label(window, text='ДАД (мм.рт.ст)').place(x=650, y=330)
lblpuls = Label(window, text='Пульс (ЧСС уд.в мин)',font=('Helvetica 10')).place(x=800, y=330)


entry_3 = Entry(window, validate='key', validatecommand=vcmd)
entry_3.place(width=40, x=600, y=330)

entry_4 = Entry(window, validate='key', validatecommand=vcmd)
entry_4.place(width=40, x=740, y=330)

entry_puls = Entry(window, validate='key', validatecommand=vcmd)
entry_puls.place(width=40, x=950, y=330)


lbl8 = Label(window, text='Антропометрические данные и данные Tanita:',
             font=('Helvetica 12 bold')).place(x=0, y=357)
#eskisi
'''lbl9 = Label(window, text='Pост (м)').place(x=10, y=380)
entry_5 = Entry(window, validate='key', validatecommand=vcmd)
entry_5.place(x=90, y=380)
'''
#avtomatik hisoblashi uchun 
rost_entry = StringVar()
lbl9 = Label(window, text='Pост (м)').place(x=10, y=380)
entry_5 = Entry(window, textvariable=rost_entry, validate='key', validatecommand=vcmd)
entry_5.place(x=90, y=380)

#eskisi
'''lbl10 = Label(window, text='Macca тeлa (кг)').place(x=230, y=380)
entry_6 = Entry(window, validate='key', validatecommand=vcmd)
entry_6.place(x=340, y=380)
'''
#avtomatik hisoblashi uchun 
massa_entry = StringVar()
lbl10 = Label(window, text='Macca тeлa (кг)').place(x=230, y=380)
entry_6 = Entry(window, textvariable=massa_entry, validate='key', validatecommand=vcmd)
entry_6.place(x=340, y=380)

#
tali_entry = StringVar()
lbl11 = Label(window, text='Окружность талии (см)').place(x=495, y=380)
entry_8 = Entry(window, textvariable=tali_entry, validate='key', validatecommand=vcmd)
entry_8.place(x=630, y=380)

#
beder_entry = StringVar()
lbl12 = Label(window, text='Окружность бедер (см)').place(x=750, y=380)
entry_9 = Entry(window, textvariable=beder_entry, validate='key', validatecommand=vcmd)
entry_9.place(x=885, y=380)

# hisoblash uchun 
'''btn1 = Button(window, text='ИМТ', width=10, command=imt).place(x=40, y=410)
lblr = Label(window, text='MT/(P. m) 2')
lblr.place(x=140, y=410)
'''
#hisoblash
btn1 = Button(window, text='ИМТ', width=10, command=imt).place(x=40, y=410)
lblr0 = Label(window, text='кг/(м)^2')
lblr0.place(x=160, y=410)

label_text = StringVar()
lblr = Label(window,   textvariable=label_text)
lblr.place(x=130, y=410)


massa_entry.trace("w", track_entry_change)

beder_entry.trace("w", track_entry_change2)


btn2 = Button(window, text='Соотношение окружность', command=imt2).place(x=500, y=410)
lblr3 = Label(window, text='талии/бедер')
lblr3.place(x=720, y=410)

label_text_tb=StringVar()
lblr2 = Label(window, text='талии/бедер' ,   textvariable=label_text_tb)
lblr2.place(x=680, y=410)


lbl12 = Label(window, text='Лабораторные данные',
              font=('Helvetica 12 bold')).place(x=0, y=450)

lbl = Label(window, text='Глюкоза в крови, ммоль/л').place(x=10, y=480)
entry_10 = Entry(window, validate='key', validatecommand=vcmd)
entry_10.place(x=170, y=480)

lbl = Label(window, text='Мочевая кислота, мкмоль/л').place(x=300, y=480)
entry_11 = Entry(window, validate='key', validatecommand=vcmd)
entry_11.place(x=480, y=480)

lbl = Label(window, text='ЛПНП, ммоль/л').place(x=610, y=480)
entry_12 = Entry(window, validate='key', validatecommand=vcmd)
entry_12.place(x=720, y=480)

#

lbl = Label(window, text='Креатинин, мкмоль/л.').place(x=10, y=520)
entry_13 = Entry(window, validate='key', validatecommand=vcmd)
entry_13.place(x=170, y=520)

lbl = Label(window, text='Общий холестерин, ХС ммоль/л').place(x=300, y=520)
entry_14 = Entry(window, validate='key', validatecommand=vcmd)
entry_14.place(x=480, y=520)

lbl = Label(window, text='ЛПВП, ммоль/л').place(x=610, y=520)
entry_15 = Entry(window, validate='key', validatecommand=vcmd)
entry_15.place(x=720, y=520)

btn_result = Button(window, text='Результат', width=14, font=('Helvetica 12 bold'),
                    command=result).place(x=10, y=560)

btn_print = Button(window, text='Печатать', command=print_result).place(x=960, y=560)

btn_reset = Button(window, text='Сброс', command=lambda:reset("0")).place(x=900, y=560)

lbl5 = Label(window, text='', foreground="red", textvariable=errmsg).place(x=200, y=570)

window.mainloop()
