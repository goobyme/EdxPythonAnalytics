def word_count(test_string):
    word_dic = {}
    word_list = test_string.split(' ')
    for word in word_list:
        if not word[0].isalpha():
            word = word[1:]
        if not word[len(word)-1]:
            word = word[:len(word)-1]

        if word.lower() not in list(word_dic.keys()):
            word_dic[word.lower()] = 1
        else:
            word_dic[word.lower()] += 1

    return word_dic


def main():
    word_count('abc')


if __name__ == '__main__':
    main()

