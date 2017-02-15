def open_test():
    fp = open(r"C:\Users\Administrator\AppData\Local\Temp\2\RIDErsjhih.d\argfile.txt", "r")
    print fp
    content = fp.readlines()
    print content
open_test()