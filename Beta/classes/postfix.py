class Calculator:
    def __init__(self):
        self.sym_table = {}
        self.running = True

    def init_var(self):
        try:
            var, num, op = input("Input var (e.g., A 3 =): ").split()
            if op == "=":
                self.sym_table[var] = num
                print(f"{var} = {num}")
            else:
                print("Invalid operator. Example input: V 5 =")
        except ValueError:
            print("Invalid input format. Example: A 3 =")

    def expression(self):
        print("Expression evaluation: coming soon!")

    def show_sym_table(self):
        if not self.sym_table:
            print("Symbol table is empty")
        else:
            for k, v in self.sym_table.items():
                print(f"{k} = {v}")

    def menu(self):
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
        while self.running:
            self.menu()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
