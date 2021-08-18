def swappingFile(file1, file2):
    file1Name = input("Enter File name: ")
    with open(file1, 'r') as a:
        data_a = a.read()
    file2name = input("Enter File name: ")
    with open(file2, 'r') as b:
        data_b = b.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)

swappingFile()