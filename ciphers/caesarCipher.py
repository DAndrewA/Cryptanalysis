alph = "abcdefghijklmnopqrstuvwxyz"

# a function to perform a caesar shift on a given text by the given shift value over the given alphabet
# target: the target text to be enciphered
# shift: the value by which the caesar shift moves each character in the target
# alph: the alphabet for which the shift is performed on
# exceptions: a string containing characters that are to be left unaffected by the enciphering.
def caesarShift(target,shift,alph,exceptions="., -"):
    caesar = ""
    for c in target:
        if c not in exceptions:
            i = alph.index(c)+shift
            caesar += alph[i%len(alph)]
        else:
            caesar += c
    return caesar

'''
Examples

# an example of an extract taken from the national cipher challenge 2017
s1 = "DO DN BMZVO OJ CZVM AMJH TJP. RZ YDY KDXF PK NJHZ XCVOOZM V XJPKGZ JA HJIOCN VBJ VIY E RVN HZIODJIZY OCZMZ OJJ, NJ RZ VGMZVYT CVQZ V ADGZ JI CZM."
c1 = caesarShift(s1,5,alph.upper())
print(c1)
'''
