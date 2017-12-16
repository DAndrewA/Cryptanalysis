# gets the frequency of all substrings of a given length in the target text
def frequencyAnalysis(target,subLen):
    freqDict = {}
    for i in range(0,len(target)-subLen+1):
        try:
            freqDict[target[i:i+subLen]] += 1
        except:
            freqDict[target[i:i+subLen]] = 1
    return freqDict

# examples using the function
s1 = "abcdefghijklmnopqrstuvwxyz"
f1 = frequencyAnalysis(s1,1)
print(f1)

s2 = "aaaaaaabbabababaghbkjhahb"
f21 = frequencyAnalysis(s2,1)
f22 = frequencyAnalysis(s2,2)
f23 = frequencyAnalysis(s2,3)
print(f21,f22,f23)
