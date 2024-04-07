def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f :
        file_contents = f.read()
        txd = text_to_dictionary(file_contents.lower())
        print(txd)
        txdl = dictionary_to_list(txd)
        print(txdl)

def text_to_dictionary(text , onlyletters=True) :
    char_count = {}
    for char in text :
        if onlyletters:
            if char.isalpha():
                if char in char_count :
                    char_count[char]+= 1
                else:
                    char_count[char] = 1
        else:
            if char in char_count :
                char_count[char]+= 1
            else:
                char_count[char] = 1
    return  char_count

def dictionary_to_list(dicct):
    char_list = [{'char' : key , 'count' :value } for key , value in dicct.items()]
    char_list.sort(key=lambda x : x['count'] , reverse=True)
    return char_list

main()
