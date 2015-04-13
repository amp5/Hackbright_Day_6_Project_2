# put your code here.

open_text = open('test.txt')

def word_count():
    word_dict = {}
    all_words = []
    for line in open_text:
        words_on_line = line.rstrip(). split(" ")
        for word in words_on_line:
            all_words.append(word)
            if word not in word_dict:
                word_dict[word] = 0
    print word_dict
    print "    "
    print all_words


            #d([key] = value




word_count()