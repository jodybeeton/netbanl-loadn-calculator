# Nedbank Loan Calculator
print("---Welcome To Nedbank Loan Console Calculator---")

loan_amount = int(input("Please enter loan amount: "))
interest_rate = float(input("Please enter your interest rate without a percentage sign: "))
_number_of_months = 12  # how long it would take you to repay the loan.

total_repayment = loan_amount + (loan_amount * interest_rate)
monthly_installment = total_repayment / _number_of_months

print('Total Repayment:', total_repayment)
print("Monthly Installment:", monthly_installment)
print("Please go tto the nearest Nedbank branch with your bank statement, ID and proof of residence.")

if interest_rate <7:
    print("The interest rate is less than 7")
if interest_rate >24.5:
    print("The interest rate is greater than 24.5")

if interest_rate >= 7 and interest_rate <= 24.5:
    print("Total Repayment and Monthly Installment")

