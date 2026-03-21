source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")
try:
    with open(source_file, 'r') as f:
        content = f.read()
    upper_content = content.upper()
    with open(destination_file, 'w') as f:
        f.write(upper_content)
    print("\nFile converted to uppercase and saved successfully!")
    print("\n--- Original Content ---")
    print(content)
    print("\n--- Uppercase Content ---")
    print(upper_content)
except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("Error:", e)