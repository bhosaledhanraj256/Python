class Student:
    def __init__(self, Company, CarName,Model):
        self.Company = Company
        self.CarName = CarName
        self.Model = Model

s  = Student(" Mahindra", "Scorpio "," 2017")
s2 = Student(" Mahindra", "Thar.   "," 2022")
s3 = Student(" Mahindra", "TharROXX"," 2025")
s4 = Student(" Mahindra", "ScorpioN"," 2024")
print(s.Company, s.CarName,s.Model)
print(s2.Company, s2.CarName,s2.Model)
print(s3.Company, s3.CarName,s3.Model)
print(s4.Company, s4.CarName,s4.Model)