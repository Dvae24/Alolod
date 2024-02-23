import GrossSalary
from SalaryDeduction import tax_calc
from SalaryDeduction import salarydeduc_calc

name = input("Name:").title()
hour = int(input("How many hours are you working? "))
Loan = float(input("How much did you loan? "))
Insurance = int(input("Health Insurance: "))
Tax = tax_calc(Loan, Insurance)
print()

gs = GrossSalary.gs_comp(hour)
sd = salarydeduc_calc(Loan, Insurance, Tax)
salary = gs - sd


print(f"Name:{name} \nHours of Work:{hour}hrs \nLoan:{Loan}PHP \nInsurance:{Insurance}PHP \nTax:{Tax}PHP ")
print()
print(f"Gross Salary:{gs} PHP \nDeductions:{sd: .2f} PHP \nNet Salary:{salary: .2f}")
# print = SalaryDeduction.Calc_SalaryDeduction()
