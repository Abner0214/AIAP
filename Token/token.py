# Open the file for reading
with open("tokenizedsentences.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Count the total number of lines in the file
line_count = len(lines)

# Initialize a dictionary to store sub-strings and their corresponding points
substring_points = {}

# Loop through each line and extract 3-character sub-strings
for current_line, line in enumerate(lines, 1):
    line = line.strip()

    for j in range(len(line) - 2):
        sub_string = line[j:j+3]
        if sub_string not in substring_points:
            # Initialize a list with 26 zeros for each sub-string
            substring_points[sub_string] = [0] * 26

        if j < len(line) - 3:
            next_char = line[j + 3]
            if 'A' <= next_char <= 'Z':
                substring_points[sub_string][ord(next_char) - ord('A')] += line_count - current_line

# Function to find the character with the biggest point for a 3-character substring
def find_biggest_point_char(sub_string):
    max_point = -1
    biggest_char = ""
    for char, point in enumerate(substring_points[sub_string]):
        if point > max_point:
            max_point = point
            biggest_char = chr(char + ord('A'))
    return biggest_char

# Function to keep appending the biggest point character until 'U' is found
def find_until_U(sub_string):
    result = sub_string
    while True:
        biggest_char = find_biggest_point_char(result[-3:])
        if biggest_char == 'U':
            result += 'U'  # Append 'U' once it's found
            return result
        result += biggest_char

while True:
    print("\t\t\t[Choose functionality]")
    print("1. Show the point table")
    print("2. Enter a 3-character sub-string to get its points")
    print("3. Enter a 3-character sub-string to find and append the biggest point character until 'U'")
    print("4. Stop")
    print("/")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        # Print the point table
        print(f"{'Sub-string':<10}", end=' ')
        for char in range(26):
            print(f"{chr(char + ord('A')):<6}", end=' ')
        print()
        
        for sub_string, points in substring_points.items():
            print(f"{sub_string:<10}", end=' ')
            for point in points:
                print(f"{point:<6}", end=' ')
            print()
    elif choice == "2":
        input_substring = input("Enter a 3-character sub-string: ")
        if input_substring in substring_points:
            points = substring_points[input_substring]
            print(f"Points for {input_substring}:")
            for char, point in enumerate(points):
                print(f"{chr(char + ord('A'))}: {point}")
        else:
            print(f"Sub-string '{input_substring}' not found in the text.")
    elif choice == "3":
        input_substring = input("Enter a 3-character sub-string: ")
        if input_substring in substring_points:
            print(f"Appending the biggest point character until 'U':")
            result = find_until_U(input_substring)
            print(f"The final result: {result}")
        else:
            print(f"Sub-string '{input_substring}' not found in the text.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        

# Close the file
file.close()
