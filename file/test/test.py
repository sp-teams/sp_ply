
import tkinter as tki
window = tki.Tk()
window.geometry('500x420')
window.title('test')
ary=[0]*5
ary[0]='s0.png'
ary[1]='s0.png'
ary[2]='s0.png'
ary[3]='s0.png'
k=0
p=tki.PhotoImage(file=ary[k])
gh=IntVar()
window.mainloop()