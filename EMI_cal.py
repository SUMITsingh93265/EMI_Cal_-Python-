# Important note :- E = P x R x (1+r)^n/ ((1+r)^N – 1

print()
print("**************************************************************")
print("*********************** EMI Calculator ***********************")
print("**************************************************************")
loan_type = input("Loan type = ")
principal_amount = float(input("Enter the principal amount : "))
year = float(input("Enter the tenure period/(Year) : "))
interest_rate = float(input("Enter the interest rate (% P.A.) = "))

monthly_interst = interest_rate / (12 * 100)
monthly_period = year * 12
emi = (principal_amount * monthly_interst *
       (1 + monthly_interst)**monthly_period) / (
           (1 + monthly_interst)**monthly_period - 1)
total_payable_amount = emi * monthly_period
total_interest = total_payable_amount - principal_amount
print()
print("**************************************************************")
print("                        View Details.")
print("**************************************************************")
print(f"                     Your {loan_type} EMI.")
print("**************************************************************")
print()
print("**************************************************************")
print(f"Monthly {loan_type} EMI")
print(f"₹ {round(emi)}\-")
print("**************************************************************")
print()
print("**************************************************************")
print("Principal Amount")
print(f"₹ {round(principal_amount)}\-")
print("Interest Amount")
print(f"₹ {round(total_interest)}\-")
print("**************************************************************")
print("Total Amount Payable")
print(f"₹ {round(total_payable_amount)}\-")
print("**************************************************************")
