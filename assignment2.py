import socket;
class Assignment2:

    #Task 1 (Constructor)
    def __init__(self, year):
        self.year = year

    #Task 2 (Age)
    def tellAge(self, currentYear):
        print("Your age is %d" % (currentYear - self.year))

    #Task 3 (List)
    def listAnniversaries(self):
        currentYear = 2022
        anniversaries = [(year - self.year) for year in range(self.year + 10, currentYear, 10)]
        return anniversaries

    #Task 4 (String Manipulation)
    def modifyYear(self, n):
        year_str = str(self.year)
        first_two = year_str[:2] * n
        odd_chars = year_str[1::2] * n
        return first_two + odd_chars

    
    #Task 5 (Loop and Conditional statements)
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower():
            return False
        digit_count = sum(1 for char in string if char.isdigit())
        if digit_count != 1:
            return False
        return True
    
    #Task 6 (Socket)
    def connectTcp(host, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.close()
            return True
        except Exception as e:
            print("Error:", e)
            return False
    