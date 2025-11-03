# Smart Calculator with Search

## Features
- Basic arithmetic operations (+, -, *, /, ^)
- Equation solver using search algorithms
- Visualization of search process with step-by-step results
- Interactive menu system with emoji-enhanced interface

## How Search Works in This Calculator
The calculator uses a systematic linear search approach to solve equations. It explores potential values for x within a reasonable range (-100 to 100), calculating the result for each value to find one that satisfies the equation. While this brute-force method might not be the most efficient, it clearly demonstrates how search algorithms work by systematically trying different possibilities and keeping track of the best solution found.

## How to Run
1. Clone the repository
2. Run: `python calculator_with_search.py`
3. Follow the menu options

## Sample Equations to Try
- x + 5 = 10 (answer: 5)
- x * 3 = 21 (answer: 7)
- 100 - x = 75 (answer: 25)
- x ^ 2 = 16 (answer: 4)
- 50 / x = 10 (answer: 5)

## What I Learned About Search
Search algorithms are a powerful way to solve problems by systematically exploring possible solutions. In this calculator, I learned how even a simple linear search can effectively solve equations by trying different values and measuring how close each attempt comes to the desired result. This project demonstrates that while brute-force search might not be the most efficient method, it can be a reliable way to find solutions when the search space is reasonable.
