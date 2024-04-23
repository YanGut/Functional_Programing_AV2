from q1_YanMendonca import *
import threading

# Descomente as funções de teste que deseja executar

# Tests===========================================================================================

# assert("completed" in cashCurrign("Medeiros", "654321", 100))

assert("completed" in fundTransfierCurring("Rodrigo", "859306", 100, "Rodrigues"))

# assert("completed" in creditCurrign("Lara", "859306", 100))

# Threads===========================================================================================

# Cash ----------------------------------------------------------------------------------------
# pbranchesCash = 100
# threadsCash = []
# for i in range(pbranchesCash):
#     t = threading.Thread(target=cashCurrign, args=("Medeiros", "654321", 1))
#     threadsCash.append(t)
#     t.start()
# for t in threadsCash:
#     t.join()

# Fund ----------------------------------------------------------------------------------------
# pbranchesFund = 100
# threadsFund = []
# for i in range(pbranchesFund):
#     t = threading.Thread(target=fundTransfierCurring, args=("Medeiros", "654321", 1, "Lucas"))
#     threadsFund.append(t)
#     t.start()
# for t in threadsFund:
#     t.join()

# Credit ----------------------------------------------------------------------------------------
pbranchesCredit = 100
threadsCredit = []
for i in range(pbranchesCredit):
    t = threading.Thread(target=creditCurrign, args=("Medeiros", "654321", 1))
    threadsCredit.append(t)
    t.start()
for t in threadsCredit:
    t.join()