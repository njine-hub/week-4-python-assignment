# File Read & Write Challenge

# Read the original file
with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (make it uppercase)
modified_content = content.upper()

# Write to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print(" File has been read, modified, and saved as output.txt")
  


  # Error Handling Lab

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n File Contents:\n")
        print(content)
except FileNotFoundError:
    print(" Error: File not found. Please check the filename.")
except PermissionError:
    print(" Error: You don’t have permission to read this file.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")