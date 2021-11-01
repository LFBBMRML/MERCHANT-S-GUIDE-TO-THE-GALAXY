#test_variable = "glob prok gold"
#test_variable = test_variable.lower()

class Converter:

    def __init__(self, intergalactic_currency):
        self.intergalactic_currency = intergalactic_currency

    def check_for_credit(self):
        currency_list = self.intergalactic_currency
        currency_list = currency_list.split(" ")
        metals = ["gold", "silver", "iron"]
        if any(i in currency_list for i in metals):
            currency_list = " ".join(currency_list) + " Credit"
        else:
            currency_list = " ".join(currency_list)
        return currency_list

#intercalactig_convertion = Converter(test_variable)
#print(intercalactig_convertion.check_for_credit())