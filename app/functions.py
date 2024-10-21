
#Grade Calculation Function
def calculate_grades(grades):
    # Calculate the average of the grades
    average = sum(grades) / len(grades)

    # Determine the letter grade based on the average
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def main():
    # Get the grades from the user
    grades_input = input("Enter the grades separated by spaces: ")

    # Convert the input string into a list of integers
    grades = [int(grade) for grade in grades_input.split()]

    # Calculate the letter grade
    letter_grade = calculate_grades(grades)

    # Output the result
    print(f"The average grade is {letter_grade}")


# Run the main function
if __name__ == "__main__":
    main()




#Loan Amortization Calculation Function
def calculate_loan_amortization(loan_amount, annual_interest_rate, loan_term_years):
    # Calculate monthly interest rate and total payments
    monthly_interest_rate = annual_interest_rate / 100 / 12
    total_payments = loan_term_years * 12

    # Calculate monthly payment using the amortization formula
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    remaining_balance = loan_amount

    # Create amortization schedule
    amortization_schedule = []

    for month in range(1, total_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        amortization_schedule.append({
            'month': month,
            'monthly_payment': round(monthly_payment, 2),
            'principal_payment': round(principal_payment, 2),
            'interest_payment': round(interest_payment, 2),
            'remaining_balance': round(remaining_balance, 2)
        })

    return monthly_payment, amortization_schedule

def main():
    # Ask the user for loan details
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    loan_term_years = int(input("Enter the loan term (in years): "))

    # Calculate the monthly payment and amortization schedule
    monthly_payment, amortization_schedule = calculate_loan_amortization(loan_amount, annual_interest_rate, loan_term_years)

    # Output the results
    print(f"Your monthly payment is: ${monthly_payment:.2f}")
    print("\nAmortization Schedule:")
    for entry in amortization_schedule:
        print(f"Month {entry['month']}: Payment: ${entry['monthly_payment']}, Principal: ${entry['principal_payment']}, "
              f"Interest: ${entry['interest_payment']}, Remaining Balance: ${entry['remaining_balance']}")

# Run the main function
if __name__ == "__main__":
    main()

# TEST CASES

# Test case for calculate_grades
sample_grades = [85, 90, 78, 92, 88]
grade_result = calculate_grades(sample_grades)
print(f"Test Case - Grades: {sample_grades}, Resulting Letter Grade: {grade_result}")

# Test case for calculate_loan_amortization
loan_amount = 20000  # Example loan amount
annual_interest_rate = 5  # Example annual interest rate
loan_term_years = 5  # Example loan term in years

monthly_payment, amortization_schedule = calculate_loan_amortization(loan_amount, annual_interest_rate, loan_term_years)
print(
    f"Test Case - Loan Amortization: Loan Amount: ${loan_amount}, Interest Rate: {annual_interest_rate}%, Loan Term: {loan_term_years} years")
print(f"Monthly Payment: ${monthly_payment:.2f}")
print("Amortization Schedule (First 3 months):")
for entry in amortization_schedule[:3]:  # Print only the first 3 months for brevity
    print(f"Month {entry['month']}: Payment: ${entry['monthly_payment']}, Principal: ${entry['principal_payment']}, "
          f"Interest: ${entry['interest_payment']}, Remaining Balance: ${entry['remaining_balance']}")