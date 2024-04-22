# users
userOne = lambda : {
    "name": "Medeiros",
    "password": "654321",
    "cpf": "987654321",
    "credit_limit": 2000,
    "money": 300,
    "transactions_status": "No transaction yet",
}

userTwo = lambda : {
    "name": "Lucas",
    "password": "859306",
    "cpf": "111222333",
    "credit_limit": 3000,
    "money": 200,
    "transactions_status" : "No transaction yet",
}

usersArray = lambda : [userOne(), userTwo()]

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

def fundTransfierCurring(nameToTransefer, password, amount, nameToReceive):
    user1 = login(nameToTransefer, password)
    user2 = userByName(nameToReceive)
    create_transaction(user1)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")
    fundTransfer(user1, user2, amount)
    print(f"User to transfer -> \n{user1}\n")
    print(f"User to receive -> \n{user2}\n")

def creditCurrign(name, password, amount):
    user = login(name, password)
    create_transaction(user)
    print(f"Credit user -> \n{user}\n")
    removeCredit(user, amount)
    print(f"Credit executed for user -> \n{user}\n")
    complete_transaction(user)
    print(f"Credit completed for user -> \n{user}\n")

# COMENTE AS FUNÇÕES QUE NÃO SERÃO TESTADAS QUNADO FOR RODAR O PROGRAMA

#Functions to test

cashCurrign("Medeiros", "654321", 100)
# fundTransfierCurring("Medeiros", "654321", 100, "Lucas")
# creditCurrign("Medeiros", "654321", 100)
