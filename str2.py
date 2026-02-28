def capitalize_lines():
    print("Enter lines of text (type 'END' to stop):")
    while True:
        line = input()
        if line == "END":
            break
        print(line.upper())
capitalize_lines()