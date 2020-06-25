with open('tables.text', 'w' ) as table_file:
    for i in range(1, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(i, j, i * j), file=table_file)
        print("**" * 25, file=table_file)