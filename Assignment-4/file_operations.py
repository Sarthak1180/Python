# Get user input and write to file
user_input = input("Enter text to write to file: ")
with open('output.txt', 'w') as file:
    file.write(user_input)

# Append additional data
additional_data = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write('\n' + additional_data)

# Read and display final content
with open('output.txt', 'r') as file:
    print("\nFinal file content:")
    print(file.read())