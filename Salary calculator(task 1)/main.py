# salary_calculator.py
# A simple Employee Salary Calculator.

def get_employee_info():
    """Ask the user for the employee details."""
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    allowance = float(input("Enter allowance: "))
    tax_rate = float(input("Enter tax rate (in %): "))
    return name, basic_salary, allowance, tax_rate


def calculate_gross_salary(basic_salary, allowance):
    """Gross salary = basic salary + allowance."""
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    """Tax amount = gross salary x (tax rate / 100)."""
    return gross_salary * tax_rate / 100


def calculate_net_salary(gross_salary, tax):
    """Net salary = gross salary - tax."""
    return gross_salary - tax


def show_salary_slip(name, gross_salary, tax, net_salary):
    """Print the final salary slip."""
    print()
    print("----- Salary Slip -----")
    print("Employee :", name)
    print("Gross    :", round(gross_salary, 2))
    print("Tax      :", round(tax, 2))
    print("Net      :", round(net_salary, 2))
    print("-----------------------")


def main():
    """Run the program step by step."""
    name, basic_salary, allowance, tax_rate = get_employee_info()

    gross_salary = calculate_gross_salary(basic_salary, allowance)
    tax = calculate_tax(gross_salary, tax_rate)
    net_salary = calculate_net_salary(gross_salary, tax)

    show_salary_slip(name, gross_salary, tax, net_salary)


main()