class Calculator:
    def __init__(self):
        """
        Initializes the calculator with:
        - sym_table: A dictionary to store variable mappings (A-Z to integer values).
        - running: A flag to control the main program loop.
        """
        self.sym_table = {}
        self.running = True
    
    def init_var(self):
        """
        Initializing a variable and adding characters to the table.
        Constraints:
        - Variable names must be a single letter (A-Z).
        - Values must be integers.
        - A maximum of 26 variables can be stored in the symbol table.
        """
        try:
            print("Available variable names: A-Z only!")
            var, num, op = input("Input var (e.g., A 3 =): ").split()
            if op == "=" and var.isalpha() and len(var) == 1 and 'A' <= var <= 'Z':
                if len(self.sym_table) >= 26:
                    print("Error: Symbol table is full (max: 26 variables).")
                    return
                if not num.isdigit():
                    print("Error: Value must be an integer.")
                    return
                self.sym_table[var] = int(num)
                print(f"ADDED INTO TABLE: {var} = {num}")
            else:
                print("Invalid input. Example: A 3 = (variable name: A-Z, operator: =)")
        except ValueError:
            print("Invalid input format. Example: A 3 =")
            
    def expression(self):
        """
        Processinf Postfix++ expression
        - Expression is evaluated using a stack:
        - Operands are pushed onto the stack.
        - Operators pop operands from the stack, perform the operation, and push the result back.
        """
        try:
            print("You can use nums or vars to create your expression.")
            print("Before you begin - introduce with available operations:")
            print("~ - unary minus — changes the sign\n" +
                  "# - cloning — return the value to the stack twice\n" +
                  "! - factorial\n" + 
                  "+ - addition\n" + 
                  "- - subtraction\n" + 
                  "* - multiplication\n" + 
                  "/ - division entirely\n" + 
                  "@ - returns the same three values to the stack, but in a different order: second, third, first\n")
            exp = input().split()
            stack = []
            uno = ['~', '#', '!']
            duo = ['+', '-', '*', '/']

            # function for processing input
            def resolve_value(value):
                value = str(value)
                if value.isalpha():
                    if value in self.sym_table:
                        return int(self.sym_table[value])
                    else:
                        raise ValueError(f"Invalid value. Symbol table does not have {value}!")
                return int(value)

            while exp:
                op = exp.pop(0)
                print(f"\nProcessing token: {op}")
                print(f"Stack before: {stack}")

                if op in uno:
                    # unary operations
                    a = resolve_value(stack.pop())
                    if op == '~':
                        stack.append(-a)
                    elif op == '!':
                        res = 1
                        for i in range(1, a + 1):
                            res *= i
                        stack.append(res)
                    elif op == '#':
                        stack.append(a)
                        stack.append(a)

                elif op in duo:
                    # binary operations
                    a = resolve_value(stack.pop())
                    b = resolve_value(stack.pop())
                    if op == '+':
                        stack.append(b + a)
                    elif op == '-':
                        stack.append(b - a)
                    elif op == '*':
                        stack.append(b * a)
                    elif op == '/':
                        if a == 0:
                            raise ZeroDivisionError("Division by zero is not allowed.")
                        stack.append(b // a)

                else:
                    stack.append(resolve_value(op))
                    print(f"Stack after: {stack}")

            print(f"ANSWER: {int(stack[-1])}")

        except ValueError as e:
            print(e)
        except IndexError:
            print("Invalid expression: not enough operands.")
        except ZeroDivisionError as e:
            print(e)

    def show_sym_table(self):
        """
        Displays the current symbol table.
        If the table is empty, informs the user.
        """
        if not self.sym_table:
            print("Symbol table is empty")
        else:
            for k, v in self.sym_table.items():
                print(f"{k} = {v}")

    def menu(self):
        """
        Provides a user interface for interacting with the calculator.
        """
        print("\nMenu:")
        print("1. Input expression")
        print("2. Initialize variable")
        print("3. View symbol table")
        print("0. Exit")
        
        try:
            user_input = int(input("Choose an option: "))
            match user_input:
                case 1:
                    self.expression()
                case 2:
                    self.init_var()
                case 3:
                    self.show_sym_table()
                case 0:
                    print("Exiting...")
                    self.running = False
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
            

    def run(self):
        """
        Starts the calculator.
        Continues running until the user selects the exit option.
        """
        while self.running:
            self.menu()

if __name__ == "__main__":
    """
    Entry point of the program.
    """
    calc = Calculator()
    calc.run()