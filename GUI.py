import tkinter
from tkinter.constants import LEFT
import tkinter.font as tkFont

def updated_output():
    pass


fenster = tkinter.Tk()


fenster.title("intergalactic transactions")
fenster.configure(bg="lightblue")
fenster.geometry("1000x250")


headline_font = tkFont.Font(size=16, weight="bold")
label_font = tkFont.Font(size=12, weight="bold")
button_font = tkFont.Font(size=12, weight="bold")
output_font = tkFont.Font(size=12, slant="italic")
information_font = tkFont.Font(size=12, weight="bold")

headline = tkinter.Label(fenster, text="MERCHANT'S GUIDE TO THE GALAXY", background="lightblue")
headline.config(font=headline_font)

information_field = tkinter.Label(fenster, text="conversion table \n Glob: I \n Prok: V \n Pish: X \n Tegj: L \n Ragi: C \n Legg: D \n Mili: M", background="lightblue")
information_field.config(font=information_font)

input_field = tkinter.Entry(fenster, bd=3, width=50)


output_field = tkinter.Label(fenster)
output_field.config(font=output_font)

convert_button = tkinter.Button(fenster, text="convert", command=updated_output)
convert_button.config(font=button_font)

exit_button = tkinter.Button(fenster, text="Beenden", command=fenster.destroy)
exit_button.config(font=button_font)


headline.place(x=500, y=30, anchor="center")
information_field.place()
input_field.place(x=350, y=100, anchor="center")
output_field.place(x=750, y=100, anchor="center")
convert_button.place(x=550, y=100, anchor="center")
exit_button.place(x=920, y=220, anchor="center")


fenster.mainloop()