# calculator_with_search.py
# Smart Calculator with Equation Solver
# Uses search concepts from Chapter 3
import operator
import math

class SmartCalculator:
    """
    A calculator that can solve simple equations using search
    """
    def __init__(self):
        # Create a dictionary of basic math operations
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        }

    def basic_calculate(self, num1, op, num2):
        """
        Perform basic calculation with the given numbers and operation.
        
        Args:
            num1 (float): First number in the calculation
            op (str): Operation to perform (+, -, *, /, ^)
            num2 (float): Second number in the calculation
            
        Returns:
            float: Result of the calculation
            str: Error message if calculation fails
        
        Examples:
            >>> calc = SmartCalculator()
            >>> calc.basic_calculate(5, '+', 3)
            8.0
            >>> calc.basic_calculate(10, '/', 2)
            5.0
        """
        # Check if operation is valid and perform calculation
        if op in self.operations:
            try:
                return self.operations[op](float(num1), float(num2))
            except ZeroDivisionError:
                return "Error: Division by zero"
            except ValueError:
                return "Error: Invalid numbers"
        return "Error: Invalid operation"

    def solve_for_x(self, target, operation, known_value, x_position='left'):
        """
        Solve simple equations like: x + 5 = 10 or 3 * x = 15
        Uses a simple search approach to find x
        
        Args:
            target (float): The desired result of the equation
            operation (str): The mathematical operation (+, -, *, /, ^)
            known_value (float): The non-x value in the equation
            x_position (str): Whether x is on the 'left' or 'right' of the operation
            
        Returns:
            float: The value of x that satisfies the equation
            
        Examples:
            >>> calc = SmartCalculator()
            >>> calc.solve_for_x(10, '+', 5, 'left')  # x + 5 = 10
            5.0
            >>> calc.solve_for_x(15, '*', 3, 'right')  # 3 * x = 15
            5.0
        """
        # This demonstrates a brute-force search
        # We'll try different values of x until we find the answer
        # Search range
        min_x = -100
        max_x = 100
        step = 0.1

        # Search for x value that satisfies the equation
        current_x = min_x
        best_x = None
        best_difference = float('inf')

        while current_x <= max_x:
            # Calculate result with current x
            if x_position == 'left':
                result = self.operations[operation](current_x, known_value)
            else:
                result = self.operations[operation](known_value, current_x)

            # Check if we found exact answer
            difference = abs(result - target)
            if difference < 0.0001:  # Close enough!
                return current_x

            # Track best answer so far
            if difference < best_difference:
                best_difference = difference
                best_x = current_x

            current_x += step

        return best_x

    def visualize_search(self, target, operation, known_value, x_position='left'):
        """
        Show the search process step by step
        This helps understand how search algorithms explore possibilities
        """
        print("\n🔍 SEARCHING FOR SOLUTION...")
        print(f"Goal: Find x where ", end="")
        if x_position == 'left':
            print(f"x {operation} {known_value} = {target}")
        else:
            print(f"{known_value} {operation} x = {target}")

        # Show first few search steps
        test_values = [-10, -5, 0, 5, 10, 15, 20]
        print("\nTesting values:")
        print("-" * 40)
        for x in test_values:
            if x_position == 'left':
                result = self.operations[operation](x, known_value)
            else:
                result = self.operations[operation](known_value, x)
            distance = abs(result - target)
            if distance < 0.0001:
                print(f"✅ x = {x:6.1f} → Result = {result:6.1f} [FOUND IT!]")
                return x
            else:
                print(f" x = {x:6.1f} → Result = {result:6.1f} [off by {distance:.1f}]")

        print("\n...continuing detailed search...")
        # Now do the full search
        return self.solve_for_x(target, operation, known_value, x_position)

    def equation_solver_menu(self):
        """
        Interactive menu for equation solving
        """
        print("\n" + "="*50)
        print("EQUATION SOLVER (using search)")
        print("="*50)
        print("I can solve equations like:")
        print(" x + 5 = 10")
        print(" x * 3 = 15")
        print(" 10 - x = 7")
        print(" 20 / x = 4")

        # Get equation parts from user
        while True:
            try:
                print("\nEnter equation parts:")
                x_left = input("Is x on left side? (y/n): ").lower().startswith('y')
                if x_left:
                    print("Enter in format: x op num = result")
                    op = input("Operation (+,-,*,/,^): ").strip()
                    known = float(input("Number after operation: "))
                    target = float(input("Desired result (after =): "))
                else:
                    print("Enter in format: num op x = result")
                    known = float(input("Number before operation: "))
                    op = input("Operation (+,-,*,/,^): ").strip()
                    target = float(input("Desired result (after =): "))

                if op not in self.operations:
                    print("Invalid operation!")
                    continue

                # Solve the equation with visualization
                result = self.visualize_search(target, op, known, 'left' if x_left else 'right')
                
                if result is not None:
                    print(f"\nSolution: x = {result:.4f}")
                    # Verify the solution
                    if x_left:
                        verification = self.basic_calculate(result, op, known)
                    else:
                        verification = self.basic_calculate(known, op, result)
                    print(f"Verification: {verification:.4f} {'≈' if abs(verification - target) < 0.0001 else '≠'} {target}")
                else:
                    print("\nNo solution found in the search range")

            except ValueError as e:
                print("Error: Please enter valid numbers")
            
            # Ask if user wants to solve another equation
            if not input("\nSolve another equation? (y/n): ").lower().startswith('y'):
                break

def main():
    """
    Main program loop
    """
    calc = SmartCalculator()
    while True:
        print("\n" + "="*50)
        print("🤖 SMART CALCULATOR WITH AI ASSISTANCE")
        print("="*50)
        print("1. Basic Calculation")
        print("2. Solve Equation (using search)")
        print("3. See Search Visualization")
        print("4. About Search Algorithms")
        print("5. Exit")
        
        choice = input("\nChoose option (1-5): ")
        
        if choice == '1':
            # Get two numbers and operation from user, then calculate
            try:
                # Enhanced input validation for numbers
                while True:
                    try:
                        num1 = float(input("Enter first number: "))
                        break
                    except ValueError:
                        print("⚠️ Please enter a valid number!")
                
                # Enhanced operation validation
                valid_ops = ['+', '-', '*', '/', '^']
                while True:
                    op = input("Enter operation (+, -, *, /, ^): ").strip()
                    if op in valid_ops:
                        break
                    print(f"⚠️ Invalid operation! Please choose from: {', '.join(valid_ops)}")
                
                while True:
                    try:
                        num2 = float(input("Enter second number: "))
                        if op == '/' and num2 == 0:
                            print("⚠️ Cannot divide by zero! Please enter another number.")
                            continue
                        break
                    except ValueError:
                        print("⚠️ Please enter a valid number!")
                
                result = calc.basic_calculate(num1, op, num2)
                print(f"\n🎯 Result: {result}")
            except KeyboardInterrupt:
                print("\n\nCalculation cancelled by user.")
                continue
                
        elif choice == '2':
            # Equation solver
            calc.equation_solver_menu()
            
        elif choice == '3':
            # Visualization demo
            print("\nLet's solve: x + 5 = 12")
            result = calc.visualize_search(12, '+', 5, 'left')
            print(f"\nSolution: x = {result}")
            
        elif choice == '4':
            print("\n📚 ABOUT SEARCH ALGORITHMS")
            print("-" * 40)
            print("This calculator uses a simple linear search:")
            print("• It tries different values of x")
            print("• Checks if each value solves the equation")
            print("• Keeps track of the best answer")
            print("• This is similar to 'brute force' search")
            print("\nReal search algorithms (Chapter 3) are smarter:")
            print("• BFS: Explores all possibilities level by level")
            print("• DFS: Explores one path deeply before trying others")
            print("• A*: Uses heuristics to search more efficiently")
            
        elif choice == '5':
            print("\nThanks for using Smart Calculator! 👋")
            break

if __name__ == "__main__":
    main()
