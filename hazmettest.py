import cryptoHazmat

if __name__ == '__main__':
    keys = cryptoHazmat.CryptoHazmat("./adp")
    keys.createKeysfile()

    #print(keys.printkey())