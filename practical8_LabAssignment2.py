source_file = input("Enter source Python file name: ")
destination_file = input("Enter destination file name: ")
try:
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        lines = src.readlines()
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#") or stripped == "":
                continue
            if "#" in line:
                line = line.split("#")[0] + "\n"
            dest.write(line)
    print("\nFile copied without comments successfully!")
    print("\n--- Source File Content ---")
    with open(source_file, 'r') as f:
        print(f.read())
    print("\n--- Destination File Content (No Comments) ---")
    with open(destination_file, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("Error:", e)