def arithmetic_arranger(problems, flag=False):
  # Initialize dictionaries to store different parts of the arranged problems
  arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}
  # Initialize a list to store error messages
  error_messages = []

  # Check if there are more than 5 problems
  if len(problems) > 5:
      return "Error: Too many problems."

  # Iterate through each problem in the list
  for problem in problems:
      # Split the problem into operands and operator
      operands = problem.split()
      operand1 = operands[0]
      operator = operands[1]
      operand2 = operands[2]

      # Validate operands
      if not operand1.isdigit() or not operand2.isdigit():
          error_messages.append("Error: Numbers must only contain digits.")
      # Validate operator
      elif operator not in ['+', '-']:
          error_messages.append("Error: Operator must be '+' or '-'.")
      # Validate the length of operands
      elif not len(operand1) <= 4 or not len(operand2) <= 4:
          error_messages.append("Error: Numbers cannot be more than four digits.")
      else:
          # Calculate the width needed for formatting
          width = max(len(operand1), len(operand2)) + 2
          # Add formatted operands and line to the respective lists
          arranged_problems["top"].append(operand1.rjust(width))
          arranged_problems["bottom"].append(operator + operand2.rjust(width - 1))
          arranged_problems["line"].append('-' * width)

          # If flag is True, calculate and add the result to the list
          if flag:
              result = str(eval(problem))
              arranged_problems["result"].append(result.rjust(width))

  # Check if there are any error messages, and return them if present
  if error_messages:
      return '\n'.join(error_messages)

  # Format the arranged problems for display
  formatted_problems = [
      '    '.join(arranged_problems["top"]),
      '    '.join(arranged_problems["bottom"]),
      '    '.join(arranged_problems["line"])
  ]

  # If flag is True, add the result line to the formatted problems
  if flag:
      formatted_problems.append('    '.join(arranged_problems["result"]))

  # Return the final formatted result as a string
  return '\n'.join(formatted_problems)
