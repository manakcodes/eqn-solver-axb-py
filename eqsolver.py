# ============================================================================ #
# IMPORTS SECTIONS                                                             #
# ============================================================================ #

from numpy import matmul, zeros, float64
from numpy.linalg import det, inv
from rich.console import Console
from time import sleep, localtime, strftime
from rich.progress import Progress

# ============================================================================ #
# GLOBAL SECTION                                                               #
# ============================================================================ #

# matrix objects 
matrix_A = None
matrix_X = None
matrix_B = None
n = None

# ============================================================================ #
# COLOR CODES FOR THE COLORED TERMINAL OUTPUT                                  #
# ============================================================================ #

# crimson
red_hex = "#DC143C"

# dark green
green_hex = "#006400"

# royal blue
blue_hex = "#4169E1"

# rebecca purple
purple_hex = "#663399"

# hot pink
pink_hex = "#B10A5E"


# ============================================================================ #
# FUNCTION BODIES                                                              #
# ============================================================================ #

def welcome_user():
    '''
    `BRIEF -> ` PRINTS a well detailed border using '=' and prints the info about the project
    
    `PARAMS -> ` None 
    
    `RETURN -> ` None
    '''
    
    # Console object
    console = Console()

    # print the info about the project
    
    console.print("=" * 60, style=green_hex)
    console.print("Welcome to the Linear Equation Solver using Python".center(60), style=blue_hex)
    
    full_timestamp = strftime("%A, %d %B %Y %H:%M:%S", localtime())

    console.print(full_timestamp.center(60), style=blue_hex)

    console.print("=" * 60, style=green_hex)

    console.print("This interactive program helps you solve a system of linear equations", style=blue_hex)
    
    console.print(f"Using matrix algebra in the form : \n[bold][{red_hex}]AX = B[/{red_hex}][/bold]\n", style=blue_hex)

    console.print("Here’s what each part represents :", style=blue_hex)
    console.print("  [bold]A[/bold] → coefficient matrix (your equation's left-hand side)", style=red_hex)
    console.print("  [bold]X[/bold] → variables to be solved (e.g., x, y, z...)", style=red_hex)
    console.print("  [bold]B[/bold] → constants (your equation's right-hand side)", style=red_hex)

    console.print("\nThe system is solved using : ", style=red_hex)
    console.print("  [bold]X = A⁻¹ × B[/bold]", style=red_hex)

    console.print("\nthis tool automatically checks whether your system has : ", style=blue_hex)
    console.print("  - [bold]A UNIQUE SOLUTION[/bold]]", style=red_hex)
    console.print("  - [bold]INFINITE SOLUTIONS[/bold]]", style=red_hex)
    console.print("  - [bold]NO SOLUTIONS[/bold]]", style=red_hex)

    console.print("\njust follow the prompts to enter your matrix data.", style=blue_hex)
    console.print("make sure matrix A is square (same number of equations and variables).\n", style=blue_hex)

    console.print("=" * 60, style=green_hex)
    console.print()
    
    
def input_matrix():
    '''
    `BRIEF -> ` INPUTS the number of equations and number of variables from the user then asks the user to enter matrix A, matrix B, and then matrix X, then prints a message once the user enters the matrix, 
    (IF `no_of_equations != no_of_variables` then it `EXITS` the program)
    
    `PARAMS -> ` None 
    
    `RETURN -> ` None
    '''

    # to handle global variables
    global matrix_A, matrix_X, matrix_B, n
    
    # Console object
    console = Console()
    
    # input number of equations and number of variables from the user
    no_of_equations = int(input("enter the number of equations : "))
    no_of_unknowns = int(input("enter the number of unknowns  : "))
    
    # CASE : no_of_equations != no_of_variables -> print a message and EXIT
    if (no_of_equations != no_of_unknowns):
        console.print("THE NUMBER OF EQUATIONS MUST BE EQUAL TO THE NUMBER OF VARIABLES", style=red_hex, justify="left")
        exit()
        
    # define n
    n = no_of_equations

    # create the matrix A
    matrix_A = zeros(shape=(n , n), dtype=float64)

    # input the matrix from the use
    print("enter the matrix A below : ")

    for i in range(n):
        for j in range(n):
            matrix_A[i][j] = float(input(f"enter element A[{i + 1}][{j + 1}] : "))
            
    # print message for matrix A
    print("\nmatrix A completed successfully\n")

    # create a row matrix B of size (n x 1) to hold the constants
    matrix_B = zeros(shape=(n, 1), dtype=float64)

    # input the rows matrix B from the user
    ColIndex = 0
    for i in range(n):
        matrix_B[i][ColIndex] = float(input(f"enter element B[{i + 1}][{ColIndex + 1}] : "))
        
    # print message for matrix B
    print("\nmatrix B completed successfully\n")

    matrix_X = zeros(shape=(n, 1), dtype=str)

    # input the matrix X from the user (variable matrix)
    ColIndex = 0
    for i in range(n):
        matrix_X[i] = input(f"enter element X[{i + 1}][{ColIndex + 1}] : ")
        
    # print message for matrix X
    print("\nmatrix X completed successfully\n")


def print_equations():
    '''
    `BRIEF -> ` PRINTS the equations in the form of `x1 + x2 + ..... + xn = constant` and also prints the determinant of the matrix A
    
    `PARAMS -> ` None 
    
    `RETURN -> ` None
    '''
    
    # to handle global variables
    global matrix_A, matrix_X, matrix_B, n
    
    # Console object
    console = Console()
    
    # print the equations in a formatted manner with coefficients, variables and constants
    for i in range(n):
        terms = []
        for j in range(n):
            term = f"{matrix_A[i][j]:.3f}{matrix_X[j][0]}"
            terms.append(term)
        equation = " + ".join(terms)
        equation += f" = {matrix_B[i][0]:.3f}"
        console.print(equation, style=purple_hex)
        print()


def solve_equations():
    '''
    `BRIEF -> `SOLVES the equations using `AX = B then X = A⁻¹B` method and prints the value of the variables in a formatted manner if `det(A) != 0`, otherwise prints a message that `EITHER INFINITE SOLUTIONS OR NO SOLUTIONS POSSIBLE`
    
    `PARAMS -> ` None 
    
    `RETURN -> ` None
    '''
    
    # to handle global variables
    global matrix_A, matrix_X, matrix_B, n
    
    # Console Object
    console = Console()
    
    # CASE : if determinant is no 0
    if ((det(matrix_A)) != 0):
        
        # loading simulation
        progress_bar(20, "CALCULATING DETERMINANT", 0.75)
        progress_bar(20, "MULTIPLYING MATRICES", 0.75)
        progress_bar(20, "SOLVING EQUATIONS", 0.5)
        
        print()
        
        # print equations
        console.print("[bold]EQUATIONS : [/bold]\n", style=green_hex)
        print_equations()
        
        print()
        
        # print the determinant
        console.print(f"[bold]DETERMINANT -> Δ(A) : {round(det(matrix_A), 4)}[/bold]\n", style=green_hex)
        
        # X = multiply_matrix(A⁻¹, B)
        sol = matmul(inv(matrix_A), matrix_B)
        
        console.print("\n[bold]SOLUTION : [/bold]\n", style=green_hex)
        
        # print the values of the corresponding variables
        for i in range(n):
            var = matrix_X[i][0]
            val = sol[i][0]
            console.print(f"{var} → {round(val, 4)}", style=blue_hex)
            
        print()
        
    # CASE : (det(A)) = 0 -> PRINT a message
    else:
        progress_bar(20, "HMM...", 1)
        progress_bar(20, "SOMETHING IS NOT RIGHT...", 1)
        progress_bar(20, "IT CAN'T BE...", 1)
        console.print("\n[bold]EITHER INFINITE SOLUTIONS OR NO SOLUTIONS[/bold]\n", style=red_hex, justify="left")
        console.print("[bold]EQUATIONS : [/bold]\n", style=green_hex)
        print_equations()
    

        
def progress_bar(total, description, speed):
    '''
    `BRIEF -> `shows a single progress bar using Python `Rich` Library, advancing at a given speed
    
    `PARAMS -> `
    -> `total (int)` : total progress steps
    -> `description (str)` : task description shown on the bar
    -> `speed (float)` : how much to advance on each update (controls speed)
    
    `RETURN -> ` None
    '''
    
    with Progress() as progress:
        task = progress.add_task(description, total=total)

        while (not progress.finished):
            progress.update(task, advance=speed)
            sleep(0.02)
 



