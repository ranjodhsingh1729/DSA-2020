import collections


# Check Off Approach
# Big-O = O(n^2)
def anagram1(word1, word2):
    array = list(word2)
    ok = True
    pos1 = 0
    while pos1 < len(word1) and ok:
        pos2 = 0
        faund = False
        while pos2 < len(array) and not faund:
            if word1[pos1] == array[pos2]:
                faund = True
            else:
                pos2 += 1
        if faund:
            array[pos2] = None
        else:
            ok = False
        pos1 += 1
    return ok


# Sort and Compare Approach
# Big-O = O(n^2)
def anagram2(word1, word2):
    word1, word2 = list(word1), list(word2)

    word1.sort(); word2.sort()

    if word1 == word2:
        return True
    else:
        return False
    

# Count and Compare Approach
# Big-O = O(n)
def anagram3(word1, word2):
    counter1 = collections.Counter()
    counter2 = collections.Counter()
    
    for char in word1:
        counter1[char] += 1
    
    for char in word2:
        counter2[char] += 1
    
    if counter1 == counter2:
        return True
    else:
        return False
