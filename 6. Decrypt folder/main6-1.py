import itertools
import zipfile

def un_zip(passwd_string, min_len, max_len, zFile) :
    for len in range(min_len, max_len):
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode())
                print(f'Password is: {passwd}')
                return 1
            except:
                pass

passwd_string = "0123456789ancdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
passwd_string = "0123456789"

zFile = zipfile.ZipFile(r'6. Decrypt folder\pass1234.zip')

min_len = 1
max_len = 5

un_zip_res = un_zip(passwd_string, min_len, max_len, zFile)