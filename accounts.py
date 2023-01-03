class Account():

    def __init__(self, name, pw):
        self.__Name = name
        
class PWHashes():
    def __init__(self):
        self.__PWHashes = dict()
    
    def addNewAcc(self, un: str, pwH: int):
        self.__PWHashes.update({un: pwH})
    
    def Hash(self, pw: str):
        num = 0
        for i in range(len(pw)):
            num += ((ord(pw[i]) - 20) * i)
            num = num ** 50 - i
            num = num % 4294967296
        return num

if __name__ == "__main__":
    pw = input()
    ht = PWHashes()
    print(ht.Hash(pw))
