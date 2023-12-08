def step_up_amt(sip_amt, last_year, interest):
    # Input the % of increase in investment per year
    step_up_percent = int(input('\nPlease enter yearly step-up percent: '))

    # Calculate monthly SIP amount per year based on investment step up percent
    yearly_sip = [sip_amt]
    for i in range(1, last_year):
        yearly_sip.append(round(yearly_sip[i-1]*(1 + step_up_percent/100), 2))
    
    # Output the monthly SIP per year
    print('\nYour monthly SIPs for the next {} years will be:'.format(last_year))
    for i in range(last_year):
        print('Year-{}'.format(i+1), yearly_sip[i], sep = '  |  ')
    
    # Invoke the SIP Calculator to calculate and output the relevant amounts
    sip_calc(sip_amt, last_year, interest, yearly_sip)

def sip_calc(sip_amt, last_year, interest, yearly_sip=None):
    # Declaring relevant variables
    total_months = last_year * 12
    total_investment, final_amt, total_returns = 0, 0, 0

    if yearly_sip == None:
        yearly_sip = [sip_amt]*last_year
    
    # Calculating total investment amount in n years
    total_investment = sum(yearly_sip)*12

    # Calculating total amount generated in n years
    for i in range (total_months):
        sip_amt = yearly_sip[i//12]
        final_amt += sip_amt * (1+interest) ** (total_months-i)
    
    # Calculating total returns to be generated in n years
    total_returns = final_amt - total_investment

    # Output the relevant amounts (total investment, final amount and returns)
    print('\nTotal amount invested in last {} years: {}'.format(last_year, sum(yearly_sip)*12))
    print('Final Amount at the end of {}th year will be: {}'.format(last_year, round(final_amt, 2)))
    print('Total returns in {} years: {}'.format(last_year, round(total_returns, 2)))

def main():
    print('Welcome to the SIP calculator.\n')

    # Inout the relevant values for calculation
    sip_amt = int(input("Please enter monthly SIP amount: "))
    last_year = int(input("Please enter the time period (in years): "))
    interest = int(input('Please enter expected rate of interest: '))/1200

    print('\nPlease enter the relevant operation number:')
    while True:
        inp = int(input('''1: Calculate normal SIP returns.
2: Calculate Step-Up SIP returns.
'''))
        if inp not in [1, 2]:
            print('\nInvalid input. Please try again.')
        else:
            break

    # Invoke relevant function based on selection of the option
    if inp == 1:
        sip_calc(sip_amt, last_year, interest)
    else:
        step_up_amt(sip_amt, last_year, interest)
    
    print('\nThanks for stopping by. Have a great day ahead.')

if __name__ == '__main__':
    # Invoking the main function
    main()
