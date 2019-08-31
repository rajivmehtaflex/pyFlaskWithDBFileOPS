import base64

def ping():
    print(__name__)

def convert_and_save(b64_string,filename):
    print(b64_string)
    with open(filename, "wb") as fh:
        fh.write(base64.decodebytes(b64_string.encode()))    