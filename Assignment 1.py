
def calculate_monthly_installment(principle_loan_amount, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_payment = loan_term_years * 12 
    monthly_installment = (principle_loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) *total_payment / ((1 + monthly_interest_rate) *total_payment  - 1))
    return monthly_installment

def calculate_total_payable(monthly_installment, total_year):
    total_payable = monthly_installment * total_year 
    return total_payable

def calculate_dsr(housing_loan, gross_monthly_income, monthly_commitment):
    dsr = ((housing_loan + monthly_commitment) / gross_monthly_income) * 100
    return dsr

def main():
    loan_calculations = []  # List to store previous loan calculations

    while True:
        # Menu
        print("\nMenu:")
        print("1. Calculate a new loan")
        print("2. Display all previous loan calculations")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            # Get user inputs
            principle_loan_amount = float(input("Enter the principle loan amount: "))
            annual_interest_rate = float(input("Enter the annual interest rate (%): "))
            loan_term_years = int(input("Enter the loan term in years: "))
            gross_monthly_income = float(input("Enter the gross monthly income: "))
            other_monthly_commitment = float(input("Enter the total of other monthly commitment: "))
    
            # Calculate the monthly instalment for the housing loan
            monthly_installment = calculate_monthly_installment(principle_loan_amount, annual_interest_rate, loan_term_years)
    
            # Calculate the total monthly commitment payments
            total_monthly_commitment_payments = monthly_installment + other_monthly_commitment
    
            # Calculate the Debt Service Ratio (DSR)
            dsr = calculate_dsr(principle_loan_amount, gross_monthly_income, total_monthly_commitment_payments)
    
            # Specify the DSR threshold for eligibility
            dsr_threshold = 70  # You can adjust this threshold as needed
    
            # Determine eligibility
            if dsr <= dsr_threshold:
                eligibility = "Loan applicant is eligible."
            else:
                eligibility = "Loan applicant is not eligible."
    
            # Display results
            print("\nMonthly Instalment: ${:.2f}".format(monthly_installment))
            print("Debt Service Ratio (DSR): {:.2f}%".format(dsr))
            print(eligibility)
    
            # Store loan calculation details
            loan_details = {
                "Loan Amount": principle_loan_amount,
                "Interest Rate": annual_interest_rate,
                "Total Monthly commitment": total_monthly_commitment_payments,
                "Gross Monthly Income": gross_monthly_income,
                "DSR": dsr,
                "Monthly Installment": monthly_installment,
                "Eligibility": eligibility 
            }
            loan_calculations.append(loan_details)

        elif choice == "2":
            # Display all previous loan calculations
            print("\nPrevious Loan Calculations:")
            for idx, calculation in enumerate(loan_calculations, 1):
                print(f"\nCalculation {idx}:")
                for key, value in calculation.items():
                    print(f"{key}: {value}")

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else: 
            print("Invalid choice. Please enter 1, 2, or 3.")


main()