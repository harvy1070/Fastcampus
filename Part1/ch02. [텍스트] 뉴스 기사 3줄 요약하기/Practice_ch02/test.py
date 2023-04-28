import base64

string = 'Life too short, We need Python!'
encoded = base64.b64encode(string)

bstring = string.encode