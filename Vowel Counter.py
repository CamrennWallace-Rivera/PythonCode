#Camrenn Wallace-Rivera
def vowels(string):
    count=0
    for i in range(len(string)):
        if(string[i] in "aeiou"):
            count+=1
    return count

def consonants(string):
    count=0
    for i in range(len(string)):
        if(string[i] not in "aeiou"):
            count+=1
    return count
string=input("Enter String: ")
print("Vowels: ",vowels(string))
print("Consonants: ",consonants(string))
print("Vowels: ",vowels(string))
print("Consonants: ",consonants(string))

