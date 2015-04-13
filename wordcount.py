# put your code here.

open_text = open('test.txt')

def word_count():
    unique_count = {}
    all_words = []
    for line in open_text:
        words_on_line = line.rstrip(). split(" ")
        for word in words_on_line:
            all_words.append(word)
            if word not in unique_count:
                unique_count[word] = 0

    print "Original Dictionary:"
    print unique_count    
    # tests passed:
    # print unique_count
    # print "    "
    # print all_words
    for word in all_words:
        if word in unique_count:
            unique_count[word] += 1

    print "\nThis is the new dictionary with count:"
    
    for word in unique_count:
        print word, unique_count[word]

    #d([key] = value




word_count()