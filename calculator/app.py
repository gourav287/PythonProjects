def evaluate():
     while True:
          # Input the relevant mathematical expression
          expr = input('\nEnter a valid mathematical expression: ')

          try:
               # Evaluate the expression and print the result
               # We are using Python's inbuilt eval function for the same
               print('\nThe result of the expression {} is {}.'.format(expr, eval(expr)))
               break
          except:
               # In case of invalid input, confirm with the user and take informed decision
               print('\nInvalid Input')
               while True:
                    invalid_inp = input('\nDo you wish to continue? Press \'Y\' for Yes, press any other key for No: ')
                    if invalid_inp == 'Y':
                         break 
                    else:
                         return

def main():               
     print('\nWelcome to the Calculator')

     # Invoking the evaluate function
     evaluate()

     print('\nThanks for stopping by. Hope it helped.')

if __name__ == "__main__":
     #Invoking the main function
     main()