import random
crack= ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
ques = int(input("Kaç haneli?"))
passw=""
for i in range(ques):
    uga = random.choice(crack)
    passw += uga
print(passw)
