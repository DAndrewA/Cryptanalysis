alph = "abcdefghijklmnopqrstuvwxyz"
from caesarCipher import caesarShift

# a function for performing a vigenere encipherment on a given target text
# mode: 0 for enciphering, 1 for deciphering
# target: the target text
# key: a string used to determine what the encipherment of each character should be
# alph: the alphabet the encipherment is being done accross
# exceptions: a string containing all the characters that are to be ignored in the encipherment
def vigenereCipher(mode,target,key,alph,exceptions="., -"):
    vigenere = ""
    for i in range(len(target)):
        if target[i] not in exceptions:
            shift = alph.index(key[i%len(key)])*(1-2*mode)
            c = caesarShift(target[i],shift,alph,exceptions)
            vigenere += c
        else:
            vigenere += target[i]
    return vigenere

'''
Examples

s1 = "IT IS GREAT TO HEAR FROM YOU. WE DID PICK UP SOME CHATTER A COUPLE OF MONTHS AGO AND J WAS MENTIONED THERE TOO, SO WE ALREADY HAVE A FILE ON HER. HER NAME IS JODIE AND SHE WORKS AS LIAISON BETWEEN THE BRITISH LIBRARY AND THE BRITISH MUSEUM, RESEARCHING LINKS BETWEEN ARTEFACTS AND IMPERIAL ROMAN TEXTS, SO THAT TIES IN WITH THE INTELLIGENCE YOU HAVE BEEN RECEIVING. NOTHING SUGGESTS THAT SHE HAS BEEN INVOLVED IN ANYTHING SHADY AND SHE HAS HELPED WITH SEVERAL INSURANCE FRAUD CASES. SHE HAS AN INTERESTING BACKGROUND. SHE DID A PHD ON HUMAN MIGRATION STUDIES, MAINLY MATHEMATICAL MODELLING, THEN MOVED ON TO STUDY KNOWLEDGE MIGRATION WHICH GOT HER INTO THE BIBLIOPHILE CIRCUIT. AFTER GRADUATING SHE SPENT SOME TIME WITH ONE OF THE LONDON AUCTION HOUSES WORKING ON PROVENANCE BEFORE TAKING HER CURRENT POSITION WITH THE LIBRARY. THERE REALLY IS NOTHING SUSPICIOUS IN HER BACKGROUND AND I WAS INCLINED TO WRITE HER OFF AS A LEAD, BUT WHEN I GOT YOUR MESSAGE I DECIDED I WANTED TO MEET HER. I TRIED TO SET THAT UP ONLY TO BE TOLD THAT SHE IS OUT OF COUNTRY FOR A WHILE. IN CAIRO."
k1 = "NATIONALCIPHERCHALLENEGE"
v1 = vigenereCipher(0,s1,k1,alph.upper())
print(v1)
v2 = vigenereCipher(1,v1,k1,alph.upper())
print(v2)
'''

while True:
    target = input("What text do you want to encipher? ")
    key = input("Whats the key? ")
    mode = int(input("0 for encipher, 1 for decipher: "))
    print(vigenereCipher(mode,target,key,alph.upper()))
