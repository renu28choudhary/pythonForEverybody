# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Prompt the user for the file name
fname = input("Enter file name: ")

try:
    # Open the file
    fh = open(fname, 'r')

    count = 0  # Counter for matching lines
    total = 0  # To accumulate the floating-point values

    for line in fh:
        # Check if the line starts with the target text
        if line.startswith("X-DSPAM-Confidence:"):
            count += 1  # Increment the count
            
            # Extract the floating-point value from the line
            colon_pos = line.find(':')  # Find the position of the colon
            value = float(line[colon_pos + 1:].strip())  # Convert the substring to float
            
            # Add the extracted value to the total
            total += value
    
    fh.close()  # Close the file

    # Compute and print the average
    if count > 0:
        average = total / count
        print(f"Average spam confidence: {average}")
    else:
        print("No matching lines found.")

except FileNotFoundError:
    print(f"Error: The file '{fname}' was not found.")
except ValueError as e:
    print(f"Error processing the file: {e}")
