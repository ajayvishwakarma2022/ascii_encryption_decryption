# reg.no.21MEI10049
# name-ajay vishwakarma final lab exam
# this code for a create a file --->take input--> convert the text into encrypted text and save in the file
createfile = input("enter file location:\n")


def creatfile():
    file = open(createfile, 'x')
    add_text = input("enter the data :\n")
    file.write(add_text)
    file.close()


creatfile()

key = int(input("enter the key in integer number:"))


def encryption():
    global encrypt_data
    encrypt_data = ""
    a = open(createfile, "r")
    data = a.read()
    for i in data:
        encrypt_data += chr(ord(i) - key)
        with open(createfile,"a") as a:
            a.write(encrypt_data)
        print("encryption using ASCII is:", encrypt_data)


encryption()


