import cryptoHazmat

if __name__ == '__main__':
    keys = cryptoHazmat.CryptoHazmat("./sajad")
    keys.createKeysfile()
    #print(keys.printkey())