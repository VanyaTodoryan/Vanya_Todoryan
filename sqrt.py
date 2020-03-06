from tkinter import *
import math
window=Tk()
window.resizable(False, False)
def get_kof():
    global a,b,c,D
    a = kof_a.get()
    b = kof_b.get()
    c = kof_c.get()
    D = (b*b)-4*a*c
    lb_v = Label(window,text="Відповідь: Рівняння не має дійсних коренів!                                ",font=("arial",18))
    lb_v1 = Label(window, text="",font=("arial",18))
    lb_v2= Label(window, text="",font=("arial",18))
    if D<0:
        lb_v.place(x=10, y=180)
    elif D==0:
        x = (-b - math.sqrt(D)) / ((a * 2))
        lb_v1.config(fg="black",text=("Відповідь: х="+str('%.3f' % x)+"                                                        "))
        lb_v1.place(x=10, y=180)
    else:
        x1 = (-b - math.sqrt(D)) / ((a * 2))
        x = (-b + math.sqrt(D)) / ((a * 2))
        lb_v2.config(fg="black", text=("Відповідь: х1 = " + str('%.3f' % x)+" x2 = ")+str('%.3f' % x1)+"                                        ")
        lb_v2.place(x=10, y=180)
kof_a=DoubleVar()
kof_b=DoubleVar()
kof_c=DoubleVar()
window.title("Квадратні рівняння")
window.geometry("500x260+500+150")
entry_a=Entry(window, width="5", font=("arial",20),textvariable=kof_a)
entry_a.place(x=30, y=15)
lb_x1=Label(window,text="*(x*x)+", font=("arial",20))
lb_x1.place(x=108,y=15)
entry_b=Entry(window, width="5", font=("arial",20),textvariable=kof_b)
entry_b.place(x=198,y=15)
lb_x2=Label(window,text="*x+", font=("arial",20))
lb_x2.place(x=278,y=15)
entry_c=Entry(window, width="5", font=("arial",20),textvariable=kof_c)
entry_c.place(x=328,y=15)
lb_zero=Label(window,text="= 0", font=("arial",20))
lb_zero.place(x=408,y=15)
button=Button(window,text="Вирішити!",font=("arial",12),width="13",command=get_kof)
button.place(x=470-300,y=100)
window.mainloop()