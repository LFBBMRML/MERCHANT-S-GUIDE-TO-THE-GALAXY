import tkinter
from tkinter.constants import LEFT
import tkinter.font as tkFont
from converter import Converter

def main():
    def updated_output():
        intergalactic_transactions = Converter(user_input.get().lower())
        #print(intergalactic_transactions.check_for_credit())
        output_text.set(intergalactic_transactions.output())


    fenster = tkinter.Tk()

    user_input = tkinter.StringVar(fenster)
    output_text = tkinter.StringVar()

    fenster.title("intergalactic transactions")
    fenster.configure(bg="lightblue")
    fenster.geometry("1000x250")


    headline_font = tkFont.Font(size=16, weight="bold")
    label_font = tkFont.Font(size=12, weight="bold")
    button_font = tkFont.Font(size=12, weight="bold")
    output_font = tkFont.Font(size=12, slant="italic")

    headline = tkinter.Label(fenster, text="MERCHANT'S GUIDE TO THE GALAXY", background="lightblue")
    headline.config(font=headline_font)


    input_field = tkinter.Entry(fenster, textvariable=user_input, bd=3, width=50)

    output_text.set("intercalary currency in arabic numeral")
    output_field = tkinter.Label(fenster, textvariable=output_text)
    output_field.config(font=output_font)

    convert_button = tkinter.Button(fenster, text="convert", command=updated_output)
    convert_button.config(font=button_font)

    exit_button = tkinter.Button(fenster, text="Exit", command=fenster.destroy)
    exit_button.config(font=button_font)


    headline.place(x=500, y=30, anchor="center")
    input_field.place(x=250, y=100, anchor="center")
    output_field.place(x=750, y=100, anchor="center")
    convert_button.place(x=500, y=100, anchor="center")
    exit_button.place(x=920, y=220, anchor="center")
    
    fenster.mainloop()

if __name__ == "__main__":
   main()
    