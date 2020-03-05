import time

global start, end, thetime

def anagram_checker(word1, word2):
    start = time.clock()
    anagram_status = True
    if len(word1) == len(word2):
        for character in word1:
            if character not in word2:
                anagram_status = False
    else:
        anagram_status = False  
    
    end = time.clock()
    thetime = end-start
    print("it took me ", thetime)
    return anagram_status


result = anagram_checker("basiparachromatin", "marsipobranchiata")
if result == True:
    print ("it is anagram")
else:
    print ("not anagram")

