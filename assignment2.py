import socket


class Assignment2:
    year = 0

    #Task 1
    def __init__(self, year):
        self.year = year

    #Task 2
    def tellAge(self, currentYear):
        age = currentYear - self.year

        print(f"Your age is {age}")

    #Task 3
    def listAnniversaries(self):
        totalYears = 2022 - self.year
        anniversaries = []

        for year in range(totalYears):
            if year == 0:
                continue
            elif year % 10 == 0:
                anniversaries.append(year)

        return anniversaries

    #Task 4
    def modifyYear(self, n):
        yearString = f"{self.year}"
        firstTwo = ""
        yearMultiplied = f"{self.year * n}"
        oddPositions = ""

        for item in range(n):
            firstTwo += yearString[0:2]

        for item in range(len(yearMultiplied)):
            if item % 2 != 0:
                oddPositions += yearMultiplied[item-1]


        return f"{firstTwo + oddPositions}"

    #Task 5
    @staticmethod
    def checkGoodString(string):
        numbers = 0

        for item in string:
            if item.isnumeric():
                numbers += 1

        if 0 < numbers < 2 and len(string) > 9 and string[0].islower():
            return True
        else:
            return False

    #Task 6
    @staticmethod
    def connectTcp(host, port):
        try:
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((host, port))
            return True
        except Exception as e:
            return False