
def tax_calc(GrossSalary: int, tax: int) -> float:
    return 0.12 * GrossSalary

def salarydeduc_calc(Tax: int, Loan: int, Insurance: int) -> float:
    return Insurance + Loan + Tax


# def Calc_Tax(GrossSalary: int):
#     return 0.12 * GrossSalary

# def Calc_SalaryDeduction(Tax: int, Loan: int, Insurance: int):
#     return Tax + Loan + Insurance