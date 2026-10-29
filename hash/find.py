from storage import Byte

class Find:
    def finding(n):
        val = Byte.byte
        match val:
            #SHA
            case val if val <= 1:
                print("not a valid hash")
            case val if val == 20:
                print("SHA-1")
            case val if val == 28:
                print("SHA-224")
            case val if val == 32:
                print("SHA-256 or SHA3-256")
            case val if val ==  48:
                print("SHA-384")
            case val if val == 64:
                print("SHA-512")
            #MD
            case val if val == 16:
                ("MD4 or MD5")
