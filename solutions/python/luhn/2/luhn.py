class Luhn:
    def __init__(self, card_num):
        self.stripped_card_num = card_num.replace(" ", "")
        self.doubled_numbers = []
        
        for index, number in enumerate(self.stripped_card_num[-1::-1]):
            if not number.isdigit():
                break
            if index % 2 == 0:
                self.doubled_numbers.append(int(number))
            else:
                if int(number) * 2 > 9:
                    self.doubled_numbers.append(int(number) * 2 - 9)
                else:    
                    self.doubled_numbers.append(int(number) * 2)
                


    def valid(self):
        if len(self.doubled_numbers) < 2 or len(self.doubled_numbers) < len(self.stripped_card_num):
            return False
        
        if sum(self.doubled_numbers) % 10:
            return False
        return True