import time
def anagram_finder (word1, word2):
    global possible_anagram
    global word_match
    start = time.clock()
    possible_anagram = True
    if len(word1) != len(word2):
        possible_anagram = False 
    
    word2_list = list(word2)
    character_position_1 = 0
    while character_position_1 < len(word1) and possible_anagram:        
        character_position_2 = 0
        word_match = False           
        while character_position_2 < len(word2_list) and not word_match:           
            if word1[character_position_1] == word2_list[character_position_2]:
                word_match = True               
            else:
                character_position_2 += 1
        
        if word_match:            
            word2_list[character_position_2] = None
        else:
            possible_anagram = False
        
        character_position_1 += 1
    end = time.clock()
    diff = end -start
    print("it took me", diff)
    return possible_anagram   
   

print(anagram_finder("basiparachromatinl", "marsipobranchiatak"))







