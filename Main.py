# ============================================================================ #
# IMPORTS SECTIONS                                                             #
# ============================================================================ #

import eqsolver

def equation_solver():
    '''
    `BRIEF -> `MASTER method that simulates the equation solver using an infinite `while (True)` loop
    
    `PARAMS -> ` None
    `RETURN -> ` None
    '''
    
    print("\n")
    
    # display a loading bar
    eqsolver.progress_bar(20, "LOADING...", 0.6)
    
    # print the welcome user message and a basic user guide for the user
    eqsolver.welcome_user()
        
    # infinite loop to accept the input from the user
    while (True):
        
        # console object 
        console = eqsolver.Console()
        
        # print the main menu of the program
        console.print("MAIN - MENU", style=eqsolver.red_hex)
        console.print("1 -> solve equations", style=eqsolver.red_hex)
        console.print("2 -> EXIT", style=eqsolver.red_hex)
            
        # input the choice from the user
        choice = int(input("enter choice (1/2) : "))
            
        # edge case : INVALID CHOICE -> print a message
        if (choice != 1 and choice != 2):
            console.print("INVALID CHOICE", style=eqsolver.red_hex, justify="left")
            continue
        
        # case : if user wants to EXIT
        if (choice == 2):
            print()
            eqsolver.progress_bar(20, "EXITING", 1)
            print()
            console.print("EXIT", style=eqsolver.red_hex, justify="left")
            print()
            break
            
        # case : if user wants to calculate
        if (choice == 1):
            eqsolver.input_matrix()
            eqsolver.solve_equations()


if __name__ == '__main__':
    equation_solver()
    
