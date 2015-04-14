# put your code here.

open_text = open('test.txt')

def word_count():
    unique_count = {} # initializing empty dictionary to keep track of each unique occurence of a word
    all_words = [] # initializing empty list of all of the words
    for line in open_text:
        words_on_line = line.rstrip().split(" ") # pulling all the words out of a line and putting them in a list, assigned to variable
        for word in words_on_line:
            all_words.append(word) # this adds each word from the line list to the all_words list.
                # I wonder if there is any way to consolidate this idea with line.rstrip().split
            if word not in unique_count: # this adds new words to the dictionary, ignoring duplicates
                unique_count[word] = 0 #d[key] = value, this is syntax for adding a key to a dictionary

    print "Original Dictionary:"
    print unique_count # the unique_count dictionary has been compiled by the above for loop!
    
    for word in all_words: # now go through all occurences of every word in text
        if word in unique_count: # maybe don't need this -- every word is definitely in unique
            unique_count[word] += 1 # shorthand += for increasing a value by 1 

    print "\nThis is the new dictionary with count:"
    
    for word in unique_count:
        print word, unique_count[word]
        # just for printng the list in the same way as the example output

    




word_count()