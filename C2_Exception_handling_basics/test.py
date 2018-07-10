
class SalaryError(Exception):
    pass

# also an example for the use of finally in try and except block.
while True:
    try:
        salary = input("Please enter your salary: ")
        if not salary.isdigit():
            raise SalaryError()
        print(salary)
        break
    except SalaryError:
        print("Invalid salary amount, Please try again...")
    finally:
        print("this will get executed no matter what")