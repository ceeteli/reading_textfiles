# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as f:
        story_content = f.read()
        f.close()
    return story_content

story_text = read_file_content('story.txt')


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_list = {}
    word_count = text.split()

    for word in word_count:
        if word in word_list.keys():
            word_list[word] += 1
        else:
            word_list[word] = 1
    return word_list


print(count_words())
