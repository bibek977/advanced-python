def file_opener(filename):
    try:
        with open(filename,'r') as f:
            print(f.read())

    except FileNotFoundError:
        # print(f"file {filename} not found")
        print(f"filename {filename[5:10]} not found")

file_opener("text/text1.txt")
file_opener("text/text2.txt")
file_opener("text/text3.txt")

file_opener("text/text4.txt")