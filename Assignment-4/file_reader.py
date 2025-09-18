try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print("Error: sample.txt not found")   

# rstrip() is used to remove any trailing whitespace characters (like newline characters) from the end of each line before printing.