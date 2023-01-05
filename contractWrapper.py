from web3 import Web3

# connect to network node
web3 = Web3(Web3.HTTPProvider('https://data-seed-prebsc-1-s1.binance.org:8545/'))

# smart contract ABI
contractABI = '[{"inputs":[{"internalType":"string","name":"_chatTag","type":"string"},{"internalType":"string","name":"_newLink","type":"string"}],"name":"changeLink","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_chatTag","type":"string"},{"internalType":"uint256","name":"_newPrice","type":"uint256"}],"name":"changePrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_chatTag","type":"string"}],"name":"getLink","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_chatTag","type":"string"}],"name":"getPrice","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_chatID","type":"string"},{"internalType":"string","name":"_userID","type":"string"}],"name":"getSubStatus","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_chatTag","type":"string"},{"internalType":"string","name":"_chatID","type":"string"},{"internalType":"string","name":"_link","type":"string"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"initializeGroup","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_chatID","type":"string"}],"name":"isChatIdActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_chatTag","type":"string"}],"name":"isChatTagActive","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_chatTag","type":"string"},{"internalType":"string","name":"_userID","type":"string"}],"name":"subscribe","outputs":[],"stateMutability":"payable","type":"function"}]'
# deployed smart contract address
contractAddress = web3.toChecksumAddress("0x161c3192186103Ef42aD6cFD4F5D03B0BA5fDcEF")
# connect to smart contract
contract = web3.eth.contract(address=contractAddress, abi=contractABI)

# call getLink() from smart contract
def getLink(chatTag):
    return contract.functions.getLink(chatTag).call()

# call getPrice() from smart contract
def getPrice(chatTag):
    return float("{:.3f}".format(web3.fromWei(contract.functions.getPrice(chatTag).call(),'ether')))

# call getSubStatus() from smart contract
def getSubStatus(chatTag, userID):
    return contract.functions.getSubStatus(chatTag, userID).call()

# call isChatIdActive() from smart contract
def isChatIdActive(chatID):
    return contract.functions.isChatIdActive(chatID).call()

# call isChatTagActive() from smart contract
def isChatTagActive(chatTag):
    return contract.functions.isChatTagActive(chatTag).call()

# call changeLink() from smart contract
def changeLink(wallet, key, chatTag, newLink):
    try:
        wallet = web3.toChecksumAddress(wallet)
        nonce = web3.eth.get_transaction_count(wallet)
        txn = contract.functions.changeLink(chatTag, newLink).buildTransaction({
        'from': wallet,
        'gas': 50000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=key)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

        if (receipt['status'] == 1):
            return web3.toHex(txn_hash)
        else:
            return 1

    except:
        return 1

# call changePrice() from smart contract
def changePrice(wallet, key, chatTag, newPrice):
    try:
        wallet = web3.toChecksumAddress(wallet)
        nonce = web3.eth.get_transaction_count(wallet)
        txn = contract.functions.changePrice(chatTag, web3.toWei(newPrice ,'ether')).buildTransaction({
        'from': wallet,
        'gas': 50000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=key)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

        if (receipt['status'] == 1):
            return web3.toHex(txn_hash)
        else:
            return 1

    except:
        return 1

# call initializeGroup() from smart contract
def initializeGroup(wallet, key, chatTag, chatID, link, price):
    try:
        wallet = web3.toChecksumAddress(wallet)
        nonce = web3.eth.get_transaction_count(wallet)
        txn = contract.functions.initializeGroup(chatTag, chatID, link, web3.toWei(price ,'ether')).buildTransaction({
        'from': wallet,
        'gas': 200000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=key)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

        if (receipt['status'] == 1):
            return web3.toHex(txn_hash)
        else:
            return 1

    except:
        return 1

# call subscribe() from smart contract
def subscribe(wallet, key, chatTag, userID):
    try:
        wallet = web3.toChecksumAddress(wallet)
        nonce = web3.eth.get_transaction_count(wallet)
        txn = contract.functions.subscribe(chatTag, userID).buildTransaction({
        'from': wallet,
        'value': web3.toWei(getPrice(chatTag),'ether'),
        'gas': 100000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonce,
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=key)
        txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(txn_hash)

        if (receipt['status'] == 1):
            return web3.toHex(txn_hash)
        else:
            return 1

    except:
        return 1