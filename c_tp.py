def print_hollow_diamond(n):
    # Print upper triangle
    for rows in range(1, n + 1):
        print(" " * (n - rows), end="")
        print("*", end="")
        if rows > 1:
            print(" " * ((rows - 1) * 2 - 1), end="")
            print("*", end="")
        print()

    # Print lower triangle
    for rows in range(n - 1, 0, -1):
        print(" " * (n - rows), end="")
        print("*", end="")
        if rows > 1:
            print(" " * ((rows - 1) * 2 - 1), end="")
            print("*", end="")
        print()

n = 5
print_hollow_diamond(n)

