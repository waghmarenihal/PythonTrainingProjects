sentence = input("> ")
length_sentence= len(sentence)
i=0
word_count=0
words=[]
word_starting=0
j=0
total_words=0
vowels_count=0
highest_len_count=0
highest_len_word=""
duplicate_word_count=0

while i!=length_sentence:

    #Word Count Logic
    if sentence[i]==" ":
        word_count= word_count+1

    #Vowel Checking Logic
    if sentence[i]=="A" or sentence[i]=="a" or sentence[i]=="E" or sentence[i]=="e" or sentence[i]=="I" or sentence[i]=="i" or sentence[i] == "O" or sentence[i]=="o" or sentence[i]=="U" or sentence[i]=="u":
        vowels_count=vowels_count+1

    #Fecting words from sentence
    if sentence[i]==" ":
        words.append(sentence[word_starting:i])
        total_words=total_words+1
        word_starting=i+1

    i=i+1

words.append(sentence[word_starting:length_sentence])
total_words=total_words+1

while j!=total_words:
    check_me=words[j]
    # Biggest Word Logic
    if highest_len_count<len(check_me):
        highest_len_count=len(check_me)
        highest_len_word=check_me

    #Duplicate Word Logic
    k=0
    while k!=total_words:
        if check_me==words[k] and k!=j:
            duplicate_word_count=duplicate_word_count+1
        k=k+1

    j=j+1


#Displaying outputs
word_count=word_count+1
print("We found "+str(word_count)+" words in above sentence.")
print("We found "+str(vowels_count)+" vowels in above sentence.")
print("We found "+str(duplicate_word_count)+" duplicate words in above sentence.")
print("'"+highest_len_word+"' is the biggest word with "+str(highest_len_count) + " alphabets.")
