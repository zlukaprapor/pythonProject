def multiplication_table(rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(f"{i} * {j} = {i * j}", end="\t")
        print()