#As chamadas das funcoes estao la embaixo, descomente as que deseja testar

# users
userCashOne = lambda : {
    "name": "Medeiros",
    "password": "654321",
    "credit_limit": 2000,
    "money": 300,
    "transactions_status": "No transaction yet",
}

userCashTwo = lambda : {
    "name": "Lucas",
    "password": "859306",
    "credit_limit": 3000,
    "money": 200,
    "transactions_status" : "No transaction yet",
}

userFundOne = lambda : {
    "name": "Rodrigo",
    "password": "859306",
    "credit_limit": 3000,
    "money": 200,
    "transactions_status" : "No transaction yet",
}

userFundTwo = lambda : {
    "name": "Rodrigues",
    "password": "859306",
    "credit_limit": 3000,
    "money": 200,
    "transactions_status" : "No transaction yet",
}

userCreditOne = lambda : {
    "name": "Matheus",
    "password": "859306",
    "credit_limit": 3000,
    "money": 200,
    "transactions_status" : "No transaction yet",
}

userCreditTwo = lambda : {
    "name": "Lara",
    "password": "859306",
    "credit_limit": 3000,
    "money": 200,
    "transactions_status" : "No transaction yet",
}

usersArray = lambda : [userCashOne(), userCashTwo(), userFundOne(), userFundTwo(), userCreditOne(), userCreditTwo()]

login = users = lambda name, password: [user for user in usersArray() if user["name"] == name and user["password"] == password][0]

userByName = lambda name: [user for user in usersArray() if user["name"] == name][0]

create_transaction = lambda user: user.update({"transactions_status": "created"})

removeMoney = lambda user, amount: user.update({"money": user["money"] - amount, "transactions_status" : "transaction executed"}) if user["money"] >= amount else user.update({"transactions_status" : "transaction failed, not money enough"})

addMoney = lambda user, amount: user.update({"money": user["money"] + amount, "transactions_status" : "transaction executed"})

# ===================================================== top ======================================================

cash = lambda amount : amount

receive_cash = lambda user, amount: removeMoney(user, amount)

print_payment_receipt = lambda user: print(f"Payment receipt printed for transaction by {user['name']}\n")

return_payment_receipt = lambda user: f"Payment receipt returned for transaction by {user['name']}"

complete_transaction = lambda user: user.update({"transactions_status": "completed"})

# ===================================================== middle ======================================================

def fundTransfer(user1, user2, amount):
    removeMoney(user1, amount)
    addMoney(user2, amount)

# ===================================================== bottom ======================================================

removeCredit = lambda user, amount: user.update({"credit_limit": user["credit_limit"] - amount, "transactions_status" : "transaction in credit executed"}) if user["credit_limit"] >= amount else user.update({"transactions_status" : "transaction failed, not credit enough"})

# ===================================================== test ======================================================
def cashCurrign(name, password, amount):
    user = login(name, password)
    create_transaction(user)
    print(f"Cash user -> \n{user}\n")
    cashTest =  cash(amount)
    receive_cash(user, cashTest)
    print(f"Cash executed for user -> \n{user}\n")
    print_payment_receipt(user)
    return_payment_receipt(user)
    complete_transaction(user)
    print(f"Cash completed for user -> \n{user}\n")
    return user["transactions_status"]

def fundTransfierCurring(nameToTransefer, password, amount, nameToReceive):
    user1 = login(nameToTransefer, password)
    user2 = userByName(nameToReceive)
    create_transaction(user1)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")
    fundTransfer(user1, user2, amount)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")
    complete_transaction(user1)
    complete_transaction(user2)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")
    return user1["transactions_status"]

def creditCurrign(name, password, amount):
    user = login(name, password)
    create_transaction(user)
    print(f"Credit user -> \n{user}\n")
    removeCredit(user, amount)
    print(f"Credit executed for user -> \n{user}\n")
    complete_transaction(user)
    print(f"Credit completed for user -> \n{user}\n")
    return user["transactions_status"]

# COMENTE AS FUNÇÕES QUE NÃO SERÃO TESTADAS QUNADO FOR RODAR O PROGRAMA==================================================

#Functions to test

cashCurrign("Medeiros", "654321", 100)
# fundTransfierCurring("Rodrigo", "859306", 100, "Rodrigues")
# creditCurrign("Lara", "859306", 100)