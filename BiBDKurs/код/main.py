import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import psycopg2
from functools import partial
from materials import *

conn = psycopg2.connect(
    user="postgres",
    password="SQLGD2525",
    host="127.0.0.1",
    port=5432,
    database="ARM"
)
conn.autocommit = True


class progrload(tk.Frame):
    def __init__(self, win):
        super().__init__(win)
        self.progbar()

    def progbar(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200

        win.title('АРМ')
        win.geometry('500x400+{}+{}'.format(w, h))
        win.resizable(False, False)
        self.frame = tk.Frame(win, bg= "#4d4f4c")
        self.frame.place(relwidth=1, relheight=1)

        value_var = IntVar()
        value = 10

        #img = Image.open("logo2.png")
        #self.tkimage = ImageTk.PhotoImage(img)
        #self.l3 = tk.Label(self.frame, image=self.tkimage, bg="#4d4f4c")
        #self.l3.pack(expand=1)

        self.progressbar = ttk.Progressbar(orient="horizontal", variable=value_var, maximum=100)
        self.progressbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.label = ttk.Label(self.frame, textvariable=value_var)
        self.progressbar.start()

        while True:
            self.frame.update()
            if value_var.get() == 11:
                self.progressbar.stop()
                loginSystem(win)
                break


class loginSystem(tk.Frame):
    def __init__(self, logWin):
        super().__init__(logWin)
        self.loginSystem()

    def loginSystem(self):

        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w=(w//2)-200
        h=(h//2)-200

        win.title('Авторизация')
        win.geometry('260x140+{}+{}'.format(w, h))
        win.resizable(False, False)

        self.frame = tk.Frame(win)
        self.frame.place(relwidth=1, relheight=1)

        self.lab_Login = tk.Label(self.frame, text="Логин", font=10)
        self.lab_Login.place(x=100, y=0)

        self.lab_Password = tk.Label(self.frame, text="Пароль", font=15)
        self.lab_Password.place(x=94, y=46)

        self.inputLogin = ttk.Entry(self.frame, width=40)
        self.inputLogin.place(x=8, y=28)

        self.inputPassword = ttk.Entry(self.frame, width=40, show="*")
        self.inputPassword.place(x=8, y=74)

        self.connButton = tk.Button(self.frame, text="Войти",
                                    fg="black", bg="orange", width=10, font=('', 12),
                                    command=self.checkLogin)
        self.connButton.place(x=80, y=105)

    def checkLogin(self):
        Polzovatel = self.inputLogin.get()
        if Polzovatel == "admin" and self.inputPassword.get() == "admin":
            self.destroy()
            self.frame.destroy()
            Main(win)
        else:

            w = win.winfo_screenwidth()
            h = win.winfo_screenheight()
            w = (w // 2) - 200
            h = (h // 2) - 200
            errorWindow = tk.Toplevel(self)
            errorWindow.title("Ошибка входа")
            errorWindow.geometry('300x150+{}+{}'.format(w, h))
            errorWindow.resizable(False, False)

            self.errorWindowFrame= tk.Frame(errorWindow)
            self.errorWindowFrame.place(relwidth=1, relheight=1)

            self.errorLabel = tk.Label(self.errorWindowFrame, text="Неверный логин или пароль!\nПовторите попытку снова", font=('', 14))
            self.errorLabel.pack(expand=1, pady=35)

            self.repeatButton=tk.Button(self.errorWindowFrame, text="Повторить",
                                        fg="black", bg="orange", width=20, font=('', 12),
                                        command=errorWindow.destroy)
            self.repeatButton.pack(side=tk.BOTTOM, pady=5)


class Main(tk.Frame):
    def __init__(self, win):
        super().__init__(win)
        self.startMain()

    def startMain(self):

        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        win.title('АРМ бухгалтер')
        win.geometry('800x600+{}+{}'.format(w, h))
        win.resizable(False, False)

        self.frameMain = tk.Frame(win)
        self.frameMain.place(relwidth=1, relheight=1)

        self.mainLabel = tk.Label(self.frameMain, text="ГЛАВНОЕ МЕНЮ", font=('', 26))
        self.mainLabel.place(x=255, y=90)

        self.spiskiButton = tk.Button(self.frameMain, text="Справочные документы",
                                      fg="black", bg="orange", width=40, font=('', 18),
                                      command=self.spiskiApp)
        self.spiskiButton.place(x=115, y=165)

        self.docButton = tk.Button(self.frameMain, text="Оперативные документы",
                                   fg="black", bg="orange", width=40, font=('', 18),
                                   command=self.docApp)
        self.docButton.place(x=115, y=240)

        self.othetButton = tk.Button(self.frameMain, text="Отчётные документы",
                                     fg="black", bg="orange", width=40, font=('', 18),
                                     command=self.othWindowSp)
        self.othetButton.place(x=115, y=315)

        self.rebornButton = tk.Button(self.frameMain, text="Восстановление базы данных",
                                    fg="black", bg="orange", width=40, font=('', 18),
                                    command=self.d)
        self.rebornButton.place(x=115, y=390)

        self.closeApp = tk.Button(self.frameMain, text="Выход",
                                  fg="black", bg="orange", width=40, font=('', 18),
                                  command=self.closeApp)
        self.closeApp.place(x=115, y=465)

    def spiskiApp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        spiskiAppWindow = tk.Toplevel(self)
        spiskiAppWindow.title('Справочные документы')
        spiskiAppWindow.geometry('800x600+{}+{}'.format(w, h))
        spiskiAppWindow.resizable(False, False)

        self.spiskiFrame = tk.Frame(spiskiAppWindow)
        self.spiskiFrame.place(relwidth=1, relheight=1)

        self.spiskiLabel = tk.Label(self.spiskiFrame, text="МЕНЮ СПРАВОЧНЫХ ДОКУМЕНТОВ", font=('', 26))
        self.spiskiLabel.place(x=88, y=53)

        self.spiskButton1 = tk.Button(self.spiskiFrame, text="Список бригад",
                                      fg="black", bg="orange", width=40, font=('', 18),
                                      command=partial(self.viewDB, spisok_brigad, "SB", "Список бригад"))
        self.spiskButton1.place(x=115, y=128)

        self.spiskButton2 = tk.Button(self.spiskiFrame, text="Положение по премированию",
                                      fg="black", bg="orange", width=40, font=('', 18),
                                      command=partial(self.viewDB, spisok_premii, "PP", "Положение по премированию"))
        self.spiskButton2.place(x=115, y=203)

        self.spiskButton3 = tk.Button(self.spiskiFrame, text="Список сотрудников",
                                      fg="black", bg="orange", width=40, font=('', 18),
                                      command=partial(self.viewDB, spisok_sotrudnikov, "SSB", "Список сотрудников"))
        self.spiskButton3.place(x=115, y=278)

        self.spiskButton4 = tk.Button(self.spiskiFrame, text="Список разрядов",
                                      fg="black", bg="orange", width=40, font=('', 18),
                                      command=partial(self.viewDB, spisok_razradow, "SR", "Список разрядов"))
        self.spiskButton4.place(x=115, y=353)

        self.spiskButton4 = tk.Button(self.spiskiFrame, text="Список сеток",
                                      fg="black", bg="orange", width=40, font=('', 18),
                                      command=partial(self.viewDB, spisok_setok, "SS", "Список сеток"))
        self.spiskButton4.place(x=115, y=427)

        self.closeA = tk.Button(self.spiskiFrame, text='Назад',
                                fg="black", bg="orange", width=40, font=('', 18),
                                command=spiskiAppWindow.destroy)
        self.closeA.place(x=115, y=503)

    def docApp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        docAppWindow = tk.Toplevel(self)
        docAppWindow.title('Оперативные документы')
        docAppWindow.geometry('800x600+{}+{}'.format(w, h))
        docAppWindow.resizable(False, False)

        self.docFrame = tk.Frame(docAppWindow)
        self.docFrame.place(relwidth=1, relheight=1)

        self.docLabel = tk.Label(self.docFrame, text="МЕНЮ ОПЕРАТИВНЫХ ДОКУМЕНТОВ", font=('', 26))
        self.docLabel.place(x=75, y=128)

        self.docButton1 = tk.Button(self.docFrame, text='Наряд на сдельную работу',
                                    fg="black", bg="orange", width=40, font=('', 18),
                                    command=partial(self.viewDB, oper_narad, "NSR", "Наряд на сдельную работу"))
        self.docButton1.place(x=115, y=203)

        self.docButton2 = tk.Button(self.docFrame, text='Табель учёта фактически отработанного времени',
                                    fg="black", bg="orange", width=40, font=('', 18),
                                    command=partial(self.viewDB, oper_tabel, "TFOW", "Табель учёта фиктически отработанного времени"))
        self.docButton2.place(x=115, y=277)

        self.docButton3 = tk.Button(self.docFrame, text='Протокол совета бригад',
                                    fg="black", bg="orange", width=40, font=('', 18),
                                    command=partial(self.viewDB, oper_protokol, "PSB", "Протокол совета бригад"))
        self.docButton3.place(x=115, y=352)

        self.closeB = tk.Button(self.docFrame, text='Закрыть',
                                fg="black", bg="orange", width=40, font=('', 18),
                                command=docAppWindow.destroy)
        self.closeB.place(x=115, y=427)

    def othWindowSp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 400
        h = (h // 2) - 400

        othWind = tk.Toplevel(self)
        othWind.title("Отчётные документы")
        othWind.geometry("800x600+{}+{}".format(w, h))
        othWind.resizable(False, False)

        self.othWindow = tk.Frame(othWind)
        self.othWindow.place(relheight=1,relwidth=1)

        self.othetLabel = tk.Label(self.othWindow, text="МЕНЮ ОТЧЁТНЫХ ДОКУМЕНТОВ", font=('', 26))
        self.othetLabel.place(x=113, y=128)

        self.otButton1 = tk.Button(self.othWindow, text="Сводная ведомость ЗП бригад",
                                   fg="black", bg="orange", width=48, font=('', 18),
                                   command=partial(self.tempO, "O1"))
        self.otButton1.place(x=60, y=203)

        self.otButton2 = tk.Button(self.othWindow, text="Сводная ведомость премии бригад",
                                   fg="black", bg="orange", width=48, font=('', 18),
                                   command=partial(self.tempO, "O2"))
        self.otButton2.place(x=60, y=277)

        self.otButton3 = tk.Button(self.othWindow, text='Ведомость распределения ЗП и премии работникам бригад',
                                   fg="black", bg="orange", width=48, font=('', 18),
                                   command=partial(self.tempO, "O3"))
        self.otButton3.place(x=60, y=352)

        self.closeC = tk.Button(self.othWindow, text='Закрыть',
                                fg="black", bg="orange", width=48, font=('', 18),
                                command=othWind.destroy)
        self.closeC.place(x=60, y=427)

    def tempO(self, ot):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200

        self.topO = tk.Toplevel(self)
        self.topO.title("Выбор отчёта")
        self.topO.geometry("260x140+{}+{}".format(w, h))
        self.topO.resizable(False, False)

        self.Oframe = tk.Frame(self.topO)

        self.lab_brigade = tk.Label(self.topO, text="Бригада", font=10)
        self.lab_brigade.place(x=89, y=0)

        self.lab_mounth = tk.Label(self.topO, text="Месяц", font=15)
        self.lab_mounth.place(x=97, y=46)

        self.inputbrigade = ttk.Entry(self.topO, width=40)
        self.inputbrigade.place(x=8, y=28)

        self.inputmounth = ttk.Entry(self.topO, width=40)
        self.inputmounth.place(x=8, y=74)

        self.late = tk.Button(self.topO, text="Расчёт",
                                    fg="black", bg="orange", width=10, font=('', 12),
                                    command=partial(self.checkdata, ot))
        self.late.place(x=80, y=105)

    def checkdata(self, ot):
        if self.inputbrigade.get() != "" and self.inputmounth.get() != "":
            brigade = self.inputbrigade.get()
            mounth = self.inputmounth.get()
            self.topO.destroy()
            if ot == "O1":
                self.create_O1(brigade, mounth)
            elif ot == "O2":
                self.create_O2(brigade, mounth)
            elif ot == "O3":
                self.create_O3(brigade, mounth)
        else:
            self.warning()

    def create_O1(self, brigade, mounth):
        self.topO1table = tk.Toplevel(self)
        self.topO1table.title(f"Сводная ведомость распределения заработной платы бригады")
        screen_width = self.topO1table.winfo_screenwidth()
        screen_height = self.topO1table.winfo_screenheight()
        self.topO1table.geometry(f'{screen_width}x{screen_height}')
        self.topO1table.rowconfigure(index=0, weight=1)
        self.topO1table.columnconfigure(index=0, weight=1)
        self.topO1table.resizable(False, False)

        nsr_data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "NSR" WHERE brigade_code='{brigade}' AND mounth='{mounth}' """)
                nsr_data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            self.warning()

        pp_data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "PP" WHERE brigade_code='{brigade}' """)
                pp_data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            self.warning()

        print(pp_data)

        svod_zp = 0
        data = []
        for pp in pp_data:
            temp = [f'{pp[1]}', 0, '', 0]
            for nsr in nsr_data:
                temp[1] = nsr[5]
                temp[2] = nsr[6]
                if (nsr[4] == pp[1]):
                    temp[3] = temp[3] + nsr[12]
            svod_zp = svod_zp + temp[3]
            data.append(tuple(temp))
        svod_zp = round(svod_zp * 100) / 100

        self._viewO1 = tk.Frame(self.topO1table)
        self._viewO1.place(relwidth=1, relheight=1)

        self.tableLableO1 = tk.Label(self._viewO1, text='СВОДНАЯ ВЕДОМОСТЬ ЗП БРИГАДЫ', font=('', 26))
        self.tableLableO1.pack(pady=10)

        column_names = ot_sved_zp
        self.treeO1 = ttk.Treeview(self._viewO1, height=25, columns=column_names, show="headings")
        self.treeO1.pack(fill=X)

        total_width = 0
        for i in column_names:
            self.treeO1.heading(f"{i}", text=f"{i}")
            if i == '№':
                self.treeO1.column(f"{i}", stretch=False)
                self.treeO1.column(f"{i}", width=50)
                total_width += 50
            else:
                column_width = screen_width // len(column_names)
                self.treeO1.column(f"{i}", width=column_width, stretch=True)
                total_width += column_width

        for row in data:
            self.treeO1.insert('', tk.END, values=tuple(row))
            for i, value in enumerate(row):
                max_width = max([len(str(val)) for j, val in enumerate(row)] + [len(column_names[i])])
                column_width = screen_width // len(column_names)
                self.treeO1.column(column_names[i], width=max_width + 20, anchor=CENTER)

        self.svod_zp_L = tk.Label(self._viewO1, text=f"Итоговая Заработная плата = {svod_zp} рублей",
                           bd=0, justify=RIGHT, font=('', 18))
        self.svod_zp_L.place(x=10, y=610)

        self.closeO1 = tk.Button(self._viewO1, text='Закрыть',
                                fg="black", bg="orange", width=56, font=('', 18),
                                command=self.topO1table.destroy)
        self.closeO1.place(x=379, y=700)

    def create_O2(self, brigade, mounth):
        self.topO2table = tk.Toplevel(self)
        self.topO2table.title(f"Сводная ведомость распределения заработной платы бригады")
        screen_width = self.topO2table.winfo_screenwidth()
        screen_height = self.topO2table.winfo_screenheight()
        self.topO2table.geometry(f'{screen_width}x{screen_height}')
        self.topO2table.rowconfigure(index=0, weight=1)
        self.topO2table.columnconfigure(index=0, weight=1)
        self.topO2table.resizable(False, False)

        nsr_data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "NSR" WHERE brigade_code='{brigade}' AND mounth='{mounth}' """)
                nsr_data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            self.warning()

        pp_data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "PP" WHERE brigade_code='{brigade}' """)
                pp_data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            self.warning()

        svod_prem = 0
        data = []
        for pp in pp_data:
            temp = [f'{pp[1]}', 0, '', 0, 0, 0]
            for nsr in nsr_data:
                temp[1] = nsr[5]
                temp[2] = nsr[6]
                if (nsr[4] == pp[1]):
                    temp[3] = temp[3] + nsr[12]
            temp[4] = pp[3]
            temp[5] = round(float(temp[4]) * float(temp[3])) / 100
            svod_prem = svod_prem + temp[5]
            data.append(tuple(temp))
        svod_prem = round(svod_prem * 100) / 100

        self._viewO2 = tk.Frame(self.topO2table)
        self._viewO2.place(relwidth=1, relheight=1)

        self.tableLableO2 = tk.Label(self._viewO2, text='СВОДНАЯ ВЕДОМОСТЬ ПРЕМИИ БРИГАДЫ', font=('', 26))
        self.tableLableO2.pack(pady=10)

        column_names = ot_sved_prem
        self.treeO2 = ttk.Treeview(self._viewO2, height=25, columns=column_names, show="headings")
        self.treeO2.pack(fill=X)

        total_width = 0
        for i in column_names:
            self.treeO2.heading(f"{i}", text=f"{i}")
            if i == '№':
                self.treeO2.column(f"{i}", stretch=False)
                self.treeO2.column(f"{i}", width=50)
                total_width += 50
            else:
                column_width = screen_width // len(column_names)
                self.treeO2.column(f"{i}", width=column_width, stretch=True)
                total_width += column_width

        for row in data:
            self.treeO2.insert('', tk.END, values=tuple(row))
            for i, value in enumerate(row):
                max_width = max([len(str(val)) for j, val in enumerate(row)] + [len(column_names[i])])
                column_width = screen_width // len(column_names)
                self.treeO2.column(column_names[i], width=max_width + 20, anchor=CENTER)

        self.svod_prem_L = tk.Label(self._viewO2, text=f"Итоговая Премия = {svod_prem} рублей",
                           bd=0, justify=RIGHT, font=('', 18))
        self.svod_prem_L.place(x=10, y=610)

        self.closeO2 = tk.Button(self._viewO2, text='Закрыть',
                                fg="black", bg="orange", width=56, font=('', 18),
                                command=self.topO2table.destroy)
        self.closeO2.place(x=379, y=700)

    def create_O3(self, brigade, mounth):
        self.topO3table = tk.Toplevel(self)
        self.topO3table.title(f"Сводная ведомость распределения заработной платы бригады")
        screen_width = self.topO3table.winfo_screenwidth()
        screen_height = self.topO3table.winfo_screenheight()
        self.topO3table.geometry(f'{screen_width}x{screen_height}')
        self.topO3table.rowconfigure(index=0, weight=1)
        self.topO3table.columnconfigure(index=0, weight=1)
        self.topO3table.resizable(False, False)

        psb_data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "PSB" WHERE brigade_code='{brigade}' AND mounth='{mounth}' """)
                psb_data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            self.warning()

        nsr_data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "NSR" WHERE brigade_code='{brigade}' AND mounth='{mounth}' """)
                nsr_data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            self.warning()

        pp_data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "PP" WHERE brigade_code='{brigade}' """)
                pp_data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            self.warning()

        sum_prem = 0
        data = []
        for pp in pp_data:
            for nsr in nsr_data:
                if (nsr[4] == pp[1]):
                    sum_prem = sum_prem + round(nsr[12] * pp[3]) / 100
        sum_prem = round(sum_prem * 100) / 100

        sum_nsr = 0
        for nsr in nsr_data:
            sum_nsr = sum_nsr + nsr[12]

        Sb = 300
        Br = 22.5
        Tr = 8.4
        S0 = float(Sb) / Br / Tr
        tdata = []
        for psb in psb_data:
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM "SS" WHERE grid='{psb[6]}' """)
                    grid_r = [row for row in cursor.fetchall()]
            except Exception as _ex:
                self.warning()
            grid_ratio = grid_r[0][1]

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM "SR" WHERE rank={psb[5]} """)
                    rank_r = [row for row in cursor.fetchall()]
            except Exception as _ex:
                self.warning()
            rank_ratio = rank_r[0][1]

            Tar = round((S0 * grid_ratio * rank_ratio * psb[8]) * 100) / 100
            temp = [f'{psb[2]}', f'{psb[3]}', f'{psb[4]}', psb[5], f'{psb[6]}', psb[7], '-', psb[8], 0, Tar, 0, 0]

            tdata.append(temp)

        sum_Tar = 0
        for datum in tdata:
            sum_Tar = sum_Tar + datum[9]
        oPrir = round((sum_nsr - sum_Tar) * 100) / 100

        p = 0
        for datum in tdata:
            p = p + datum[5] * datum[9]
        p = oPrir / p

        sum_Prir = 0
        if oPrir < 0:
            self.warning()
        elif oPrir > 0:
            for datum in tdata:
                datum[8] = p * datum[5] * datum[9]
                datum[8] = round(datum[8] * 100) / 100
                sum_Prir = sum_Prir + datum[8]
        elif oPrir == 0:
            for datum in tdata:
                datum[8] = 0
        sum_Prir = round(sum_Prir * 100) / 100

        if oPrir - sum_Prir > 0:
            max_ktu = 0
            for i in range(0, len(tdata)):
                if tdata[i][5] > max_ktu:
                    max_ktu = tdata[i][5]
            best_men = []
            for i in range(0, len(tdata)):
                if tdata[i][5] == max_ktu:
                    best_men.append(i)
            out = True
            while out:
                for i in best_men:
                    tdata[i][8] = tdata[i][8] + 0.01
                    tdata[i][8] = round(tdata[i][8] * 100) / 100
                    sum_Prir = round((sum_Prir + 0.01) * 100) /100
                    if oPrir - sum_Prir == 0:
                        out = False
                        break
        elif oPrir - sum_Prir < 0:
            min_ktu = 9999
            for i in range(0, len(tdata)):
                if tdata[i][5] < min_ktu:
                    min_ktu = tdata[i][5]
            worse_men = []
            for i in range(0, len(tdata)):
                if tdata[i][5] == min_ktu:
                    worse_men.append(i)
            out = True
            while out:
                for i in worse_men:
                    tdata[i][8] = tdata[i][8] - 0.01
                    tdata[i][8] = round(tdata[i][8] * 100) / 100
                    sum_Prir = round((sum_Prir - 0.01) * 100) /100
                    if oPrir - sum_Prir == 0:
                        out = False
                        break

        all_zp = 0
        all_prem = 0
        for datum in tdata:
            datum[10] = datum[8] + datum[9]
            datum[10] = round(datum[10] * 100) / 100
            pp = []
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM "PP" WHERE brigade_code='{brigade}' AND profession_code='{datum[2]}' """)
                    pp = [row for row in cursor.fetchall()]
            except Exception as _ex:
                self.warning()
            datum[11] = round(datum[10] * pp[0][3])
            datum[11] = datum[11] / 100
            all_zp = all_zp + datum[10]
            all_prem = all_prem + datum[11]
        all_zp = round(all_zp * 100) / 100
        all_prem = round(all_prem * 100) / 100

        if sum_prem - all_prem > 0:
            max_ktu = 0
            for i in range(0, len(tdata)):
                if tdata[i][5] > max_ktu:
                    max_ktu = tdata[i][5]
            best_men = []
            for i in range(0, len(tdata)):
                if tdata[i][5] == max_ktu:
                    best_men.append(i)
            out = True
            while out:
                for i in best_men:
                    tdata[i][11] = tdata[i][11] + 0.01
                    tdata[i][11] = round(tdata[i][11] * 100) / 100
                    all_prem = round((all_prem + 0.01) * 100) / 100
                    if sum_prem - all_prem == 0:
                        out = False
                        break
        elif sum_prem - all_prem < 0:
            min_ktu = 9999
            for i in range(0, len(tdata)):
                if tdata[i][5] < min_ktu:
                    min_ktu = tdata[i][5]
            worse_men = []
            for i in range(0, len(tdata)):
                if tdata[i][5] == min_ktu:
                    worse_men.append(i)
            out = True
            while out:
                for i in worse_men:
                    tdata[i][11] = tdata[i][11] - 0.01
                    tdata[i][11] = round(tdata[i][11] * 100) / 100
                    all_prem = round((all_prem - 0.01) * 100) / 100
                    if sum_prem - all_prem == 0:
                        out = False
                        break

        data = []
        for datum in tdata:
            data.append(tuple(datum))

        self._viewO3 = tk.Frame(self.topO3table)
        self._viewO3.place(relwidth=1, relheight=1)

        self.tableLableO3 = tk.Label(self._viewO3, text='ВЕДОМОСТЬ РАСПРЕДЕЛЕНИЯ ЗП И ПРЕМИИ СОТРУДНИКАМ БРИГАД', font=('', 26))
        self.tableLableO3.pack(pady=10)

        column_names = ot_ved
        self.treeO3 = ttk.Treeview(self._viewO3, height=21, columns=column_names, show="headings")
        self.treeO3.pack(fill=X)

        total_width = 0
        for i in column_names:
            self.treeO3.heading(f"{i}", text=f"{i}")
            if i == '№':
                self.treeO3.column(f"{i}", stretch=False)
                self.treeO3.column(f"{i}", width=50)
                total_width += 50
            else:
                column_width = screen_width // len(column_names)
                self.treeO3.column(f"{i}", width=column_width, stretch=True)
                total_width += column_width

        for row in data:
            self.treeO3.insert('', tk.END, values=tuple(row))
            for i, value in enumerate(row):
                max_width = max([len(str(val)) for j, val in enumerate(row)] + [len(column_names[i])])
                column_width = screen_width // len(column_names)
                self.treeO3.column(column_names[i], width=max_width + 20, anchor=CENTER)

        self.itog_zp = tk.Label(self._viewO3, text=f"Итоговая Заработная плата = {all_zp} рублей",
                           bd=0, justify=RIGHT, font=('', 18))
        self.itog_zp.place(x=10, y=560)

        self.itog_prem = tk.Label(self._viewO3, text=f"Итоговая Премия = {all_prem} рублей",
                           bd=0, justify=RIGHT, font=('', 18))
        self.itog_prem.place(x=10, y=610)

        self.closeO3 = tk.Button(self._viewO3, text='Закрыть',
                                fg="black", bg="orange", width=56, font=('', 18),
                                command=self.topO3table.destroy)
        self.closeO3.place(x=379, y=700)

    def warning(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200

        errorWindow = tk.Toplevel(self)
        errorWindow.title("Ошибка ввода")
        errorWindow.geometry('300x150+{}+{}'.format(w, h))
        errorWindow.resizable(False, False)

        self.errorWindowFrame = tk.Frame(errorWindow)
        self.errorWindowFrame.place(relwidth=1, relheight=1)

        self.errorLabel = tk.Label(self.errorWindowFrame,
                                   text="Некорректные данные!", font=('', 14))
        self.errorLabel.pack(expand=1, pady=35)

        self.repeatButton = tk.Button(self.errorWindowFrame, text="Повторить",
                                      fg="black", bg="orange", width=20, font=('', 12),
                                      command=errorWindow.destroy)
        self.repeatButton.pack(side=tk.BOTTOM, pady=5)

    def viewDB(self, column_names, tablename, tablenamerus):
        self.viewTableDataBases = tk.Toplevel(self)
        self.viewTableDataBases.title(f"{tablenamerus}")
        screen_width = self.viewTableDataBases.winfo_screenwidth()
        screen_height = self.viewTableDataBases.winfo_screenheight()
        self.viewTableDataBases.geometry(f'{screen_width}x{screen_height}')
        self.viewTableDataBases.rowconfigure(index=0, weight=1)
        self.viewTableDataBases.columnconfigure(index=0, weight=1)
        self.viewTableDataBases.resizable(False, False)

        self._viewDB = tk.Frame(self.viewTableDataBases)
        self._viewDB.place(relwidth=1, relheight=1)

        data = []
        try:
            with conn.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM "{tablename}" """)
                data = [row for row in cursor.fetchall()]
        except Exception as _ex:
            print("ТАБЛИЦА НЕ ПОДТЯНУЛАСЬ")

        tabletitle = ''
        if tablename == 'SB':
            tabletitle = 'СПИСОК БРИГАД'
        elif tablename == 'SSB':
            tabletitle = 'СПИСОК СОТРУДНИКОВ БРИГАДЫ'
        elif tablename == 'PP':
            tabletitle = 'ПОЛОЖЕНИЕ ПО ПРЕМИРОВАНИЯ'
        elif tablename == 'SS':
            tabletitle = 'СПИСОК СЕТОК'
        elif tablename == 'SR':
            tabletitle = 'СПИСОК РАЗРЯДОВ'
        elif tablename == 'NSR':
            tabletitle = 'НАРЯД НА СДЕЛЬНУЮ РАБОТУ'
        elif tablename == 'PSB':
            tabletitle = 'ПРОТОКОЛ СОВЕТА БРИГАД'
        elif tablename == 'TFOW':
            tabletitle = 'ТАБЕЛЬ УЧЁТА ФАКТИЧЕСКИ ОТРАБОТАННОГО ВРЕМЕНИ'

        self.tableLable = tk.Label(self._viewDB, text=f'{tabletitle}', font=('', 26))
        self.tableLable.pack(pady=10)

        self.tree = ttk.Treeview(self._viewDB, height=30, columns=column_names, show="headings")
        self.tree.pack(fill=X, pady=5)

        total_width = 0
        for i in column_names:
            self.tree.heading(f"{i}", text=f"{i}")
            if i == '№':
                self.tree.column(f"{i}", stretch=False)
                self.tree.column(f"{i}", width=50)
                total_width += 50
            else:
                column_width = screen_width // len(column_names)
                self.tree.column(f"{i}", width=column_width, stretch=True)
                total_width += column_width

        data.reverse()
        for row in data:
            self.tree.insert('', tk.END, values=tuple(row))
            for i, value in enumerate(row):
                max_width = max([len(str(val)) for j, val in enumerate(row)] + [len(column_names[i])])
                column_width = screen_width // len(column_names)
                self.tree.column(column_names[i], width=max_width + 20, anchor=CENTER)

        self.inputButton = tk.Button(self._viewDB, text="Добавить",
                                     fg="black", bg="orange", width=15, font=('', 18),
                                     command=partial(self.inputTableWindows, column_names, tablename, tablenamerus))
        self.inputButton.place(x=100, y=740)
        if tablename == "SR":
            self.inputButton["state"] = "disable"
            self.inputButton["bg"] = "gray"

        self.changeButton = tk.Button(self._viewDB, text="Изменить",
                                      fg="black", bg="orange", width=15, font=('', 18),
                                      command=partial(self.inputTableWindows, column_names, tablename, tablenamerus, 'CHANGE'))
        self.changeButton.place(x=379, y=740)
        if tablename == "SR" or tablename == "SS"\
                or tablename == "NSR" or tablename == "TFOW" or tablename == "PSB":
            self.changeButton["state"] = "disable"
            self.changeButton["bg"] = "gray"

        self.deleteButton = tk.Button(self._viewDB, text="Удаление",
                                      fg="black", bg="orange", width=15, font=('', 18),
                                      command=partial(self.DELButton, column_names, tablename, tablenamerus))
        self.deleteButton.place(x=658, y=740)
        if tablename == "SR" or tablename == "SS":
            self.deleteButton["state"] = "disable"
            self.deleteButton["bg"] = "gray"

        self.searchButton = tk.Button(self._viewDB, text="Поиск",
                                      fg="black", bg="orange", width=15, font=('', 18),
                                      command=self.d)
        self.searchButton.place(x=938, y=740)

        self.closeButton = tk.Button(self._viewDB, text="Закрыть",
                                      fg="black", bg="orange", width=15, font=('', 18),
                                      command=self.viewTableDataBases.destroy)
        self.closeButton.place(x=1215, y=740)

    def inputTableWindows(self, column_names, tablename, tablenamerus, mode="INPUT"):
        selection = ''
        if mode == 'CHANGE':
            selection = self.tree.selection()

        inputTableWin = tk.Toplevel(self)
        inputTableWin.resizable(False, False)

        self.inTable = tk.Frame(inputTableWin)
        self.inTable.place(relwidth=1, relheight=1)

        if tablename == "SS":
            inputTableWin.title("Добавление в CC")
            inputTableWin.geometry('400x302')

            buflist = spisok_setok

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)

            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)

            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

        elif tablename == "PP":
            if mode == "CHANGE":
                inputTableWin.title("Изменение записи ПП")
            else:
                inputTableWin.title("Добавление в ПП")
            inputTableWin.geometry('400x460')

            buflist = spisok_premii

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)

            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)

            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)

            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)

            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            if mode == 'CHANGE':
                t = self.tree.item(selection[0], "values")[0]
                self.l1e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[1]
                self.l2e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[2]
                self.l3e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[3]
                self.l4e.insert(0, f"{t}")

        elif tablename == "SB":
            if mode == "CHANGE":
                inputTableWin.title("Изменение записи Сб")
            else:
                inputTableWin.title("Добавление в СБ")
            inputTableWin.geometry('400x375')

            buflist = spisok_brigad

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)

            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)

            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)

            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            if mode == 'CHANGE':
                t = self.tree.item(selection[0], "values")[0]
                self.l1e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[1]
                self.l2e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[2]
                self.l3e.insert(0, f"{t}")

        elif tablename == "SSB":
            if mode == "CHANGE":
                inputTableWin.title("Изменение записи ССБ")
            else:
                inputTableWin.title("Добавление в ССБ")
            inputTableWin.geometry('400x605')

            buflist = spisok_sotrudnikov

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)

            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)

            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)

            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)

            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[4]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)

            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"{buflist[5]}",
                               bd=0, justify=CENTER, height=2, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)

            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            if mode == 'CHANGE':
                t = self.tree.item(selection[0], "values")[0]
                self.l1e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[1]
                self.l2e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[2]
                self.l3e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[3]
                self.l4e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[4]
                self.l5e.insert(0, f"{t}")
                t = self.tree.item(selection[0], "values")[5]
                self.l6e.insert(0, f"{t}")

        elif tablename == "NSR":
            inputTableWin.title("Добавление в НСР")
            inputTableWin.geometry('400x740')

            buflist = oper_narad

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)

            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)

            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)

            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)

            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[4]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)

            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"{buflist[5]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)

            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.l7 = tk.Label(self.inTable, text=f"{buflist[6]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l7.pack(side=tk.TOP, fill=tk.X)

            self.l7e = ttk.Entry(self.inTable, width=15)
            self.l7e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"{buflist[7]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)

            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)

            self.l9 = tk.Label(self.inTable, text=f"{buflist[8]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l9.pack(side=tk.TOP, fill=tk.X)

            self.l9e = ttk.Entry(self.inTable, width=15)
            self.l9e.pack(fill=tk.X)

            self.l10 = tk.Label(self.inTable, text=f"{buflist[10]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l10.pack(side=tk.TOP, fill=tk.X)

            self.l10e = ttk.Entry(self.inTable, width=15)
            self.l10e.pack(fill=tk.X)

            self.l11 = tk.Label(self.inTable, text=f"{buflist[11]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l11.pack(side=tk.TOP, fill=tk.X)

            self.l11e = ttk.Entry(self.inTable, width=15)
            self.l11e.pack(fill=tk.X)

            self.l12 = tk.Label(self.inTable, text=f"{buflist[13]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l12.pack(side=tk.TOP, fill=tk.X)

            self.l12e = ttk.Entry(self.inTable, width=15)
            self.l12e.pack(fill=tk.X)

        elif tablename == "PSB":
            inputTableWin.title("Добавление в ПСБ")
            inputTableWin.geometry('400x590')

            buflist = oper_protokol

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)

            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)

            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)

            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)

            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[4]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)

            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"{buflist[5]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)

            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.l7 = tk.Label(self.inTable, text=f"{buflist[6]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l7.pack(side=tk.TOP, fill=tk.X)

            self.l7e = ttk.Entry(self.inTable, width=15)
            self.l7e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"{buflist[7]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)

            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)

            self.l9 = tk.Label(self.inTable, text=f"{buflist[8]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l9.pack(side=tk.TOP, fill=tk.X)

            self.l9e = ttk.Entry(self.inTable, width=15)
            self.l9e.pack(fill=tk.X)

        elif tablename == "TFOW":
            inputTableWin.title("Добавление в ТФОВ")
            inputTableWin.geometry('400x640')

            buflist = oper_tabel

            self.l1 = tk.Label(self.inTable, text=f"{buflist[0]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l1.pack(side=tk.TOP, fill=tk.X)

            self.l1e = ttk.Entry(self.inTable, width=15)
            self.l1e.pack(fill=tk.X)

            self.l2 = tk.Label(self.inTable, text=f"{buflist[1]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l2.pack(side=tk.TOP, fill=tk.X)

            self.l2e = ttk.Entry(self.inTable, width=15)
            self.l2e.pack(fill=tk.X)

            self.l3 = tk.Label(self.inTable, text=f"{buflist[2]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l3.pack(side=tk.TOP, fill=tk.X)

            self.l3e = ttk.Entry(self.inTable, width=15)
            self.l3e.pack(fill=tk.X)

            self.l4 = tk.Label(self.inTable, text=f"{buflist[3]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l4.pack(side=tk.TOP, fill=tk.X)

            self.l4e = ttk.Entry(self.inTable, width=15)
            self.l4e.pack(fill=tk.X)

            self.l5 = tk.Label(self.inTable, text=f"{buflist[4]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l5.pack(side=tk.TOP, fill=tk.X)

            self.l5e = ttk.Entry(self.inTable, width=15)
            self.l5e.pack(fill=tk.X)

            self.l6 = tk.Label(self.inTable, text=f"{buflist[5]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l6.pack(side=tk.TOP, fill=tk.X)

            self.l6e = ttk.Entry(self.inTable, width=15)
            self.l6e.pack(fill=tk.X)

            self.l7 = tk.Label(self.inTable, text=f"{buflist[6]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l7.pack(side=tk.TOP, fill=tk.X)

            self.l7e = ttk.Entry(self.inTable, width=15)
            self.l7e.pack(fill=tk.X)

            self.l8 = tk.Label(self.inTable, text=f"{buflist[7]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l8.pack(side=tk.TOP, fill=tk.X)

            self.l8e = ttk.Entry(self.inTable, width=15)
            self.l8e.pack(fill=tk.X)

            self.l9 = tk.Label(self.inTable, text=f"{buflist[8]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l9.pack(side=tk.TOP, fill=tk.X)

            self.l9e = ttk.Entry(self.inTable, width=15)
            self.l9e.pack(fill=tk.X)

            self.l10 = tk.Label(self.inTable, text=f"{buflist[9]}",
                               bd=0, justify=CENTER, height=1, font=('', 18))
            self.l10.pack(side=tk.TOP, fill=tk.X)

            self.l10e = ttk.Entry(self.inTable, width=15)
            self.l10e.pack(fill=tk.X)

        if mode == 'CHANGE':
            self.changeButton = tk.Button(self.inTable, text="Изменить",
                                         fg="black", bg="orange", width=18, font=('', 15),
                                         command=partial(self.change, selection, column_names, tablename, tablenamerus))
            self.changeButton.pack(pady=20)
        else:
            self.inputButton = tk.Button(self.inTable, text="Добавить",
                                         fg="black", bg="orange", width=18, font=('', 15),
                                         command=partial(self.inputTableSQL, column_names, tablename, tablenamerus))
            self.inputButton.pack(pady=20)

        self.closeB = tk.Button(self.inTable, text='Закрыть',
                                fg="black", bg="orange", width=18, font=('', 15),
                                command=inputTableWin.destroy)
        self.closeB.pack()

    def inputTableSQL(self, column_names, tablename, tablenamerus):
        if tablename == "SS":
            value1 = self.l1e.get()
            value2 = float(self.l2e.get())
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "grid", "grid_ratio") VALUES 
               	                            ('{value1}', {value2}) """)

                    self.refresh(column_names, tablename, tablenamerus)

            except Exception as _ex:
                self.errorWindows("Ошибка ввода", "Некорректные данные")

        if tablename == "PP":
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = int(self.l3e.get())
            value4 = int(self.l4e.get())
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "brigade_code", "profession_code", "percent_per_type_null", "percent_per_type_one") VALUES 
               	                            ('{value1}', '{value2}', {value3}, {value4}) """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка ввода", "Некорректные данные")

        if tablename == "SB":
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = int(self.l3e.get())
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "brigade_code", "sn_in_brigadier", "person_quantity") VALUES 
               	                            ('{value1}', '{value2}', {value3}) """)

                    self.refresh(column_names, tablename, tablenamerus)

            except Exception as _ex:
                self.errorWindows("Ошибка ввода", "Некорректные данные")

        if tablename == "SSB":
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = int(self.l5e.get())
            value6 = self.l6e.get()
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "brigade_code", "service_number", "profession_code", "sn_in", "rank", "grid") VALUES 
               	                            ('{value1}', '{value2}', '{value3}', '{value4}', {value5}, '{value6}') """)

                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка ввода", "Некорректные данные")

        if tablename == 'NSR':
            value1 = int(self.l1e.get())
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = self.l5e.get()
            value6 = int(self.l6e.get())
            value7 = self.l7e.get()
            value8 = int(self.l8e.get())
            value9 = float(self.l9e.get())

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM "SS" WHERE grid='{value7}' """)
                    grid_r = [row for row in cursor.fetchall()]
            except Exception as _ex:
                self.warning()
            grid_ratio = grid_r[0][1]

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM "SR" WHERE rank={value6} """)
                    rank_r = [row for row in cursor.fetchall()]
            except Exception as _ex:
                self.warning()
            rank_ratio = rank_r[0][1]

            value10 = round(grid_ratio * rank_ratio * value9 * 100) / 100
            value11 = int(self.l10e.get())
            value12 = int(self.l11e.get())
            value13 = round(float(value10 * value11) * 100 / value8) / 100
            value14 = self.l12e.get()

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "number", "brigade_code", "detail", "operation_number", "profession_code", "rank", "grid", "meter", "hours", "price", "out_detail_quantity", "in_detail_quantity", "total_sum", "mounth") VALUES 
               	                            ({value1}, '{value2}', '{value3}', '{value4}', '{value5}', {value6}, '{value7}', {value8}, {value9}, {value10}, {value11}, {value12}, {value13}, '{value14}') """)

                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка ввода", "Некорректные данные")

        if tablename == "PSB":
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = self.l5e.get()
            value6 = int(self.l6e.get())
            value7 = self.l7e.get()
            value8 = float(self.l8e.get())
            value9 = float(self.l9e.get())

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "mounth", "brigade_code", "service_number", "sn_in" ,"profession_code", "rank", "grid", "KTU", "work_time_hours") VALUES 
               	                            ('{value1}', '{value2}', '{value3}', '{value4}', '{value5}', {value6}, '{value7}', {value8}, {value9}) """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка ввода", "Некорректные данные")

        if tablename == "TFOW":
            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = self.l5e.get()
            value6 = int(self.l6e.get())
            value7 = self.l7e.get()
            value8 = self.l8e.get()
            value9 = self.l9e.get()
            value10 = float(self.l10e.get())
            work_day_time = 8.4
            value11 = value10 / work_day_time

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "mounth", "brigade_code", "service_number", "sn_in" ,"profession_code", "rank", "grid", "oklad", "graph_code", "work_time_hours", "work_time_days") VALUES 
               	                            ('{value1}', '{value2}', '{value3}', '{value4}', '{value5}', {value6}, '{value7}', '{value8}', '{value9}', {value10}, {value11}) """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка ввода", "Некорректные данные")

    def refresh(self, column_names, tablename, tablenamerus):
        self.viewTableDataBases.destroy()
        self.viewDB(column_names, tablename, tablenamerus)

    def errorWindows(self, msg1, msg2):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200
        errorWindow = tk.Toplevel(self)
        errorWindow.title(f"{msg1}")
        errorWindow.geometry('300x150+{}+{}'.format(w, h))
        errorWindow.resizable(False, False)

        self.errorWindowFrame = tk.Frame(errorWindow)
        self.errorWindowFrame.place(relwidth=1, relheight=1)

        self.errorLabel = tk.Label(self.errorWindowFrame, text=f"{msg2}",
                                   font=('', 14))
        self.errorLabel.pack(expand=1, pady=35)

        self.repeatButton = tk.Button(self.errorWindowFrame, text="Повторить", width=20, font=('', 12),
                                      command=errorWindow.destroy)
        self.repeatButton.pack(side=tk.BOTTOM, pady=5)

    def DELButton(self, column_names, tablename, tablenamerus):
        selection = self.tree.selection()

        if tablename == "PP":
            for item in selection:
                delValue1 = self.tree.item(item, "values")[0]
                delValue2 = self.tree.item(item, "values")[1]
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""DELETE FROM public."PP" WHERE brigade_code='{delValue1}' AND profession_code='{delValue2}' """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка удаления", "Невозможно удалить запись")

        if tablename == "SB":
            for item in selection:
                delValue1 = self.tree.item(item, "values")[0]
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""DELETE FROM public."SB" WHERE brigade_code='{delValue1}' """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка удаления", "Невозможно удалить запись")

        if tablename == "SSB":
            for item in selection:
                delValue1 = self.tree.item(item, "values")[0]
                delValue2 = self.tree.item(item, "values")[1]
                delValue3 = self.tree.item(item, "values")[2]
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""DELETE FROM public."SSB" WHERE brigade_code='{delValue1}' AND service_number='{delValue2}' AND profession_code='{delValue3}' """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка удаления", "Невозможно удалить запись")

        if tablename == "NSR":
            for item in selection:
                delValue1 = self.tree.item(item, "values")[0]
                delValue2 = self.tree.item(item, "values")[1]
                delValue3 = self.tree.item(item, "values")[4]
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""DELETE FROM public."NSR" WHERE number='{delValue1}' AND brigade_code='{delValue2}' AND profession_code='{delValue3}' """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка удаления", "Невозможно удалить запись")

        if tablename == "PSB":
            for item in selection:
                delValue1 = self.tree.item(item, "values")[0]
                delValue2 = self.tree.item(item, "values")[1]
                delValue3 = self.tree.item(item, "values")[2]
                delValue4 = self.tree.item(item, "values")[4]
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""DELETE FROM public."PSB" WHERE mounth='{delValue1}' AND brigade_code='{delValue2}' AND service_number='{delValue3}' AND profession_code='{delValue4}' """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка удаления", "Невозможно удалить запись")

        if tablename == "TFOW":
            for item in selection:
                delValue1 = self.tree.item(item, "values")[0]
                delValue2 = self.tree.item(item, "values")[1]
                delValue3 = self.tree.item(item, "values")[2]
                delValue4 = self.tree.item(item, "values")[4]
            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""DELETE FROM public."TFOW" WHERE mounth='{delValue1}' AND brigade_code='{delValue2}' AND service_number='{delValue3}' AND profession_code='{delValue4}' """)
                    self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка удаления", "Невозможно удалить запись")

    def change(self, selection, column_names, tablename, tablenamerus,):
        if tablename == "SSB":
            old_data = [0, 0, 0, 0, 0, 0]

            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = self.l3e.get()
            value4 = self.l4e.get()
            value5 = int(self.l5e.get())
            value6 = self.l6e.get()

            old_data[0] = self.tree.item(selection[0], "values")[0]
            old_data[1] = self.tree.item(selection[0], "values")[1]
            old_data[2] = self.tree.item(selection[0], "values")[2]
            old_data[3] = self.tree.item(selection[0], "values")[3]
            old_data[4] = self.tree.item(selection[0], "values")[4]
            old_data[5] = self.tree.item(selection[0], "values")[5]

            with conn.cursor() as cursor:
                cursor.execute(f"""DELETE FROM public."SSB" WHERE brigade_code='{old_data[0]}' AND service_number='{old_data[1]}' AND profession_code='{old_data[2]}' """)

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
               	                            "brigade_code", "service_number", "profession_code", "sn_in", "rank", "grid") VALUES 
               	                            ('{value1}', '{value2}', '{value3}', '{value4}', {value5}, '{value6}') """)
                self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка изменения", "Невозможно изменить данные!")
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
                              	                            "brigade_code", "service_number", "profession_code", "sn_in", "rank", "grid") VALUES 
                              	                            ('{old_data[0]}', '{old_data[1]}', '{old_data[2]}', '{old_data[3]}', {old_data[4]}, '{old_data[5]}') """)
                self.refresh(column_names, tablename, tablenamerus)

        elif tablename == "SB":
            old_data = [0, 0, 0]

            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = int(self.l3e.get())

            old_data[0] = self.tree.item(selection[0], "values")[0]
            old_data[1] = self.tree.item(selection[0], "values")[1]
            old_data[2] = self.tree.item(selection[0], "values")[2]

            with conn.cursor() as cursor:
                cursor.execute(f"""DELETE FROM public."SB" WHERE brigade_code='{old_data[0]}' """)

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"( "brigade_code", "sn_in_brigadier", "person_quantity") VALUES 
                               	                            ('{value1}', '{value2}', {value3}) """)
                self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка изменения", "Невозможно изменить данные!")
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"( "brigade_code", "sn_in_brigadier", "person_quantity") VALUES 
                               	                            ('{old_data[0]}', '{old_data[1]}', {old_data[2]}) """)
                self.refresh(column_names, tablename, tablenamerus)

        elif tablename == "PP":
            old_data = [0, 0, 0, 0]

            value1 = self.l1e.get()
            value2 = self.l2e.get()
            value3 = int(self.l3e.get())
            value4 = int(self.l4e.get())

            old_data[0] = self.tree.item(selection[0], "values")[0]
            old_data[1] = self.tree.item(selection[0], "values")[1]
            old_data[2] = self.tree.item(selection[0], "values")[2]
            old_data[3] = self.tree.item(selection[0], "values")[3]

            with conn.cursor() as cursor:
                 cursor.execute(
                    f"""DELETE FROM public."PP" WHERE brigade_code='{old_data[0]}' AND profession_code='{old_data[1]}' """)

            try:
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
                            	                            "brigade_code", "profession_code", "percent_per_type_null", "percent_per_type_one") VALUES 
                               	                            ('{value1}', '{value2}', {value3}, {value4}) """)
                self.refresh(column_names, tablename, tablenamerus)
            except Exception as _ex:
                self.errorWindows("Ошибка изменения", "Невозможно изменить данные!")
                with conn.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO "{tablename}"(
                                           	                    "brigade_code", "profession_code", "percent_per_type_null", "percent_per_type_one") VALUES 
                                              	                ('{old_data[0]}', '{old_data[1]}', {old_data[2]}, {old_data[3]}) """)
                self.refresh(column_names, tablename, tablenamerus)

    def closeApp(self):
        w = win.winfo_screenwidth()
        h = win.winfo_screenheight()
        w = (w // 2) - 200
        h = (h // 2) - 200

        clWin = tk.Toplevel(self)
        clWin.title("Выход из АРМ")
        clWin.geometry('320x150+{}+{}'.format(w, h))
        clWin.resizable(False, False)

        self.closeWindow = tk.Frame(clWin)
        self.closeWindow.place(relwidth=1, relheight=1)

        self.textCloseWindow = tk.Label(self.closeWindow, text="Вы дейтвительно хотите выйти?", font=('', 14))
        self.textCloseWindow.place(x=15, y=30)

        self.yesButton = tk.Button(self.closeWindow, text="Да",
                                   fg="black", bg="red", width=10, font=('', 12),
                                   command=self.d)
        self.yesButton.place(x=35, y=85)

        self.noButton = tk.Button(self.closeWindow, text="Нет",
                                  fg="black", bg="green", width=10, font=('', 12),
                                  command=clWin.destroy)
        self.noButton.place(x=185, y=85)

    def d(self):
        pass


if __name__ == "__main__":
    win = tk.Tk()
    start = loginSystem(win)
    start.pack()
    win.mainloop()
