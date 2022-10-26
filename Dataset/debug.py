import pdb
 
def CONCAT(a, b):
    fin = a + b
    return fin
 
pdb.set_trace()
sentence = input("Enter Sentence : ")
reason = input("Enter Reason : ")
 
Concatenate = CONCAT(sentence,reason)
print(Concatenate)
