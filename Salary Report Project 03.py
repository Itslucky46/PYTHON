import calendar

# nsban=calendar.nsban[Month]
# sads=f"{nsban}/{Year}"

Emp_Name=input("Enter your Name : ")
Emp_ID=input("Enter Your EMP ID : ")
Monthly_Salary=float(input("Enter Your Monthly Salary : "))
Tds_Percentage=float(input("Emp TDS % (Cut) : "))
Emp_Leave=int(input("Enter your leave days : "))
Month=int(input("Enter Month [1-12] : "))
Year=int(input("Enter Year : "))
Emp_Bonus=float(input("Emp Bonus : "))


# calculate Yearly Salary
Yearly_Salary= Monthly_Salary*12


# Function to calculate TDS amount
def TDS(Monthly_Salary, tds_Percentage):
    return (Monthly_Salary * Tds_Percentage) / 100

# Tds_Percent=(Monthly_Salary*Tds_Percentage)/100


# Calculate leave amount
Leave_Amount = (Monthly_Salary / calendar.monthrange(Year, Month)[1]) * Emp_Leave
# Leave_Amount=(Monthly_Salary/30)*Emp_Leave  

# Calculate TDS amount
Tds_Amount = TDS(Monthly_Salary, Tds_Percentage)
    
# Calculate final salary
Net_Salary = (Monthly_Salary + Emp_Bonus) - (Leave_Amount + Tds_Amount)

# Format the month and year
month_name = calendar.month_name[Month]
formatted_date = f"{month_name}/{Year}"



print("---------------------------------------")
print("Date              : ",formatted_date)
print("---------------------------------------")
print("Employee Name     : ",Emp_Name)
print("Employee ID       : ",Emp_ID)
print("Monthly Salary    : ",Monthly_Salary)
print("Yearly Salary     : ",Yearly_Salary)
print("Leave Amount      : ",Leave_Amount)
print("TDS Amount        : ",Tds_Amount )
print("Bonus             : ",Emp_Bonus)
print("Net Salary        : ",Net_Salary)
print("---------------------------------------")




