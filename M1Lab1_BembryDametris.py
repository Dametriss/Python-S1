#Dametris Bembry
#1-18-24
#M1Lab1 Decision structures,loops,and math

def calc_tax(annual_income):
    marginal = 0
    flat = 0 
    if annual_income >0 and annual_income <= 9875:
        marginal = annual_income *0.10
        
    if annual_income >=9876 and annual_income <= 40125:
        flat = 986
        marginal = (annual_income - 9875) * .12
        
    if annual_income >=40126 and annual_income <= 85525:
        flat = 4618
        marginal = (annual_income - 40125) * .22
        
    if annual_income >=85526 and annual_income <= 163300:
        flat = 14606
        marginal = (annual_income - 85525) * .24

           
    if annual_income >=163301 and annual_income <= 207350:
        flat = 33272
        marginal = (annual_income - 163300) * .32

    
    if annual_income >=207351 and annual_income <= 518400:
        flat = 47368
        marginal = (annual_income - 207350) * .35

    if annual_income >=518401:
        flat = 156235
        marginal = (annual_income - 518400) * .37

    # Calc total tax
    total_tax = flat + marginal

    return total_tax


        
def main():
    run_again = "yes"
    while run_again == "yes":
        status = input("Enter your marital status: ")
        if status == "single":
            #Get income
            income = int(input("Enter your annual income: "))
            #call the calc_tax function
            total_tax = calc_tax(income)
            print(f"For the income ${income}, the total tax is {total_tax:.2f}")
        else:
            print("This program is eligbable for a single person ")
        run_again = input("Would you like to run agian?")
    
    
if __name__ == "__main__":
    main()
