from convert import *

class Converter:
    
    def __init__(self, intergalactic_currency):
        self.intergalactic_currency = intergalactic_currency
        self.input_text = False
        self.input_text_with_metal = False
        self.currency_list = self.intergalactic_currency
        self.currency_list = self.currency_list.split(" ")
        
    def check_for_valid_input(self):
        valid_input = ["gold", "silver", "iron", "glob", "prok", "pish", "tegj"]
        if set(self.currency_list).issubset(valid_input):
            self.input_text = True

    def check_for_credit(self):
        metals = ["gold", "silver", "iron"]
        if self.input_text:
            if any(i in self.currency_list for i in metals):
                self.input_text_with_metal = True


    def output(self):
        self.check_for_valid_input()
        self.check_for_credit()
        if self.input_text and self.input_text_with_metal:
            return str(convert_currency(self.currency_list)) + " Credits"
        elif self.input_text and not self.input_text_with_metal:
            return str(convert_currency(self.currency_list))
        else:
            return "No idea what you are talking about!"

if __name__ == "__main__":
    print("Please run GUI.py")
