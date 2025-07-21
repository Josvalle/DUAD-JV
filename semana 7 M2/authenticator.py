import jwt


class JWT_Manager:
    def __init__(self):
        with open(r'C:\Users\Usuario\Desktop\devs\devs_te\private_key.pem', 'rb') as file:
            self.private_key = file.read()
            self.public_key = b"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwhvqCC+37A+UXgcvDl+7\nnbVjDI3QErdZBkI1VypVBMkKKWHMNLMdHk0bIKL+1aDYTRRsCKBy9ZmSSX1pwQlO\n/3+gRs/MWG27gdRNtf57uLk1+lQI6hBDozuyBR0YayQDIx6VsmpBn3Y8LS13p4pT\nBvirlsdX+jXrbOEaQphn0OdQo0WDoOwwsPCNCKoIMbUOtUCowvjesFXlWkwG1zeM\nzlD1aDDS478PDZdckPjT96ICzqe4O1Ok6fRGnor2UTmuPy0f1tI0F7Ol5DHAD6pZ\nbkhB70aTBuWDGLDR0iLenzyQecmD4aU19r1XC9AHsVbQzxHrP8FveZGlV/nJOBJw\nFwIDAQAB\n-----END PUBLIC KEY-----\n"
    
    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.private_key, algorithm="RS256")
            return encoded
        except Exception as e:
            print(f"Error: {e}")
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=["RS256"])
            return decoded
        except Exception as e:
            print(e)
            return None
    
    