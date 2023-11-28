# This project was inspired while learning number system in School
# NAME: Moirangthem Henthoiba
# SCHOOL: CSA (Competitive Success Academy)
# CLASS: 11 - Section A
# ROLL NO: 38
# Year: Nov-2023

# NOTE:
    # Each number system ranges

    # binary (2) -> 0 & 1
    # decimal (10) -> 0-9
    # octal (8) -> 0-7
    # hexadcemial (16) -> 0-9 & A-F

# GOAL:
    # binary -> other [o] (Forgot the time)
    # decimal -> other [o] (Forgot the time)
    # octal -> other [o] 26/11/2023 (9:35 AM)
    # hexadecimal -> other [o 29/11/2023 (12:46 AM)

hexa_dict = {
    # Making a dictionary just to convert a number to alphabet which is absolutely neccessary for converting to hexadecimal number system
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

class Binary():
    def _value(self, raw: int):
        self.raw = raw

    def _converter(self):
        exp = 0
        _sum = 0
        while self.raw != 0:
            _sum = _sum + ((self.raw % 10) * (2 ** exp))
            self.raw = self.raw // 10
            exp += 1
        return _sum

    def _decimal(self): # -> Issue: Can input integers other than 0 and 1
        # Todo -> Need to contain only 0 or 1 in the user input
        final_result = f"Decimal: {b._converter()}"
        return final_result

    def _octal(self):
        _sum = b._converter()
        result = []
        string = ""
        if _sum == 0:
            string = "0"
        while _sum > 0:
            result.append(_sum % 8)
            _sum = _sum // 8
        for r in result:
            string += str(r)
        final_result = f"Octal: {string[::-1]}"
        return final_result

    def _hexa(self):
        _sum = b._converter()
        result = []
        string = ""
        if _sum == 0:
            string = "0"
        while _sum > 0:
            result.append(_sum % 16)
            _sum = _sum // 16
        for r in result:
            for x in hexa_dict:
                if r == x:
                    r = hexa_dict[x]
            string += str(r)
        final_result = f"Hexadecimal: {string[::-1]}"
        return final_result
        
class Decimal:
    def _value(self, raw: int):
        self.raw = raw

    def _binary(self):
        result = [] # empty list created just to use later in the code
        string = "" # and empty string created just to use later in the code
        if self.raw == 0:
            string = "0" # if self.raw is 0 then it will print out 0
        while self.raw > 0: # if self.raw is greater than 0 then it will go inside the while loop
            result.append(self.raw % 2) # appending on the empty list variable `result`
            self.raw = self.raw // 2 # making the self.raw value to self.raw // 2 (which will give quotient in integers only not decimal)
        for r in result: # looping the appended list `result`
            string += str(r)
        final_result = f"Binary: {string[::-1]}" # converting the elements in the list `result` to string type and adding it on the empty string variable `string`
        return final_result  # finally returnin out the value of the variable `string` using string slicing and reversing it with the -1 step

    def _octal(self):
        # same comments as _binary function one which is above the _octal function so need to do double explanation
        result = []
        string = ""
        if self.raw == 0:
            string = "0"
        while self.raw > 0:
            result.append(self.raw % 8)
            self.raw = self.raw // 8
        for r in result:
            string += str(r)
        final_result = f"Octal: {string[::-1]}"
        return final_result

    def _hexa(self):
        result = []
        string = ""
        if self.raw == 0:
            string = "0"
        while self.raw > 0:
            result.append(self.raw % 16)
            self.raw = self.raw // 16
        for r in result:
            for x in hexa_dict:
                if r == x:
                    r = hexa_dict[x]
            string += str(r)
        final_result = f"Hexadecimal: {string[::-1]}"
        return final_result

class Octal:
    def _value(self, raw: int):
        self.raw = raw
    
    def _converter(self):
        exp = 0
        _sum = 0
        for _ in str(self.raw):
            while self.raw != 0:
                _sum = _sum + ((self.raw % 10) * (8 ** exp))
                self.raw = self.raw // 10
                exp += 1
            break
        return _sum

    def _binary(self):
        result = []
        string = ""
        _sum = o._converter()
        if _sum == 0:
            string = "0"
        while _sum > 0:
            result.append(_sum % 2)
            _sum = _sum // 2
        for r in result:
            string += str(r)
        final_result = f"Binary: {string[::-1]}"
        return final_result

    def _decimal(self):
        final_result = f"Decimal: {o._converter()}"
        return final_result
    
    def _hexa(self):
        result = []
        string = ""
        _sum = o._converter()
        if _sum == 0:
            string = "0"
        while _sum > 0:
            result.append(_sum % 16)
            _sum = _sum // 16
        for r in result:
            for x in hexa_dict:
                if r == x:
                    r = hexa_dict[x]
            string += str(r)
        final_result = f"Hexadecimal: {string[::-1]}"
        return final_result
    
class Hexa:
    def _value(self, raw: str):
        self.raw = raw

    def _converter(self):
        result = []
        exp = 0
        _sum = 0
        for item in self.raw:
            for i in hexa_dict:
                if item == hexa_dict[i]:
                    item = i
            item = int(item)
            result.append(item)
        for x in result[::-1]:
            _sum = _sum + (x * (16 ** exp))
            exp += 1
        return _sum
    
    def _binary(self):
        value = h._converter()
        string = ""
        result = []
        
        while value > 0:
            result.append(value % 2)
            value = value // 2
        for i in result:
            string += str(i)
        final_result = f"Binary: {string[::-1]}"
        return final_result

    def _decimal(self):
        final_result = f"Decimal: {h._converter()}"
        return final_result
    
    def _octal(self):
        value = h._converter()
        string = ""
        result = []
        
        while value > 0:
            result.append(value % 8)
            value = value // 8
        for i in result:
            string += str(i)
        final_result = f"Octal: {string[::-1]}"
        return final_result

d = Decimal()
b = Binary()
o = Octal()
h = Hexa()

_option = input('''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[?] Choose what number system you want to input

[1] Binary
[2] Decimal
[3] Octal
[4] Hexadecimal
                
[#] Choose: ''')
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

if __name__ == "__main__":
    if _option == "1":
        number = int(input("Enter a binary number: "))
        b._value(number)
        option = input('''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] Binary -> Decimal
[2] Binary -> Octal
[3] Binary -> Hexadecimal
                       
[#] Choose: ''')
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if option == "1":
            print(b._decimal())
        elif option == "2":
            print(b._octal())
        elif option == "3":
            print(b._hexa())

    elif _option == "2":
        number = int(input("Enter a decimal number: "))
        d._value(number)
        option = input('''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] Decimal -> Binary
[2] Decimal -> Octal
[3] Decimal -> Hexadecimal
                       
[#] Choose: ''')
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if option == "1":
            print(d._binary())
        elif option == "2":
            print(d._octal())
        elif option == "3":
            print(d._hexa())
    
    elif _option == "3":
        number = int(input("Enter a Octal number: "))
        o._value(number)
        option = input('''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] Octal -> Binary
[2] Octal -> Decimal
[3] Octal -> Hexadecimal
                       
[#] Choose: ''')
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if option == "1":
            print(o._binary())
        elif option == "2":
            print(o._decimal())
        elif option == "3":
            print(o._hexa())

    elif _option == "4":
        number = input("Enter a Hexa number: ")
        h._value(number)
        option = input('''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] Hexadecimal -> Binary
[2] Hexadecimal -> Decimal
[3] Hexadecimal -> Octal
                       
[#] Choose: ''')
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        if option == "1":
            print(h._binary())
        elif option == "2":
            print(h._decimal())
        elif option == "3":
            print(h._octal())