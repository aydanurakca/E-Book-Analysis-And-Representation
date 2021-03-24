import requests
from bs4 import BeautifulSoup 

def main(): 
    print("E-BOOK ANALYSIS AND REPRESENTATION\n")
    choice = 0
    
    while choice != "Q" or choice != "q":
        print("\nPress 1 to analyze an e-book.\nPress 2 to analyze 2 e-books and compare them.\nPress Q to quit.")
        choice = input("Your Choice: ")
        if choice == "Q" or choice == "q":
            print("The program has finished. Take Care!")
            break
        while choice != "1" and choice != "2":
            choice = input("Wrong entry. Please enter your choice correctly: ")
        if(choice == "1"):
            book = input("Please enter the name of e-book: ")
            num = input("Please enter the number of words that you want to list: ")
            if(num == ""): #if number is not given
                print("Number is taken 20 as a default value.")
                num = "20"
            num = int(num) #
            book = book.rstrip() #if there is a whitespace in input (which makes input wrong)
            result = createBook(book)
            if(result == ""):
                continue
            file = open("book1.txt", "w", encoding='utf-8')
            file.write(book + "\n" + result)   
            file.close()
            
            file = open('book1.txt','r', encoding='utf-8')
            dictionary = clearText(file)
            file.close()
            
            print("BOOK 1: {0}\n".format(book))
            print("{0:3}\t{1:12}\t{2:8}".format("NO", "WORD", "FREQ_1"))
            for i in range(num): #comparing the keys' values and finding the max value
                maximum = 0
                word = ""
                for key in dictionary:
                    if maximum < int(dictionary[key]):
                        maximum = dictionary[key]
                        word = key        
                print("{0:3}\t{1:12}\t{2:8}".format(i+1, word, maximum))
                dictionary[word] = -1
                
        elif(choice == "2"):
            book1 = input("Please enter the name of the first e-book:")
            book1 = book1.rstrip()
            result = createBook(book1)
            if(result == ""):
                continue
            file1 = open("book1.txt", "w", encoding='utf-8')
            file1.write(book1 + "\n" + result)
            file1.close()
            
            book2 = input("Please enter the name of the second e-book:")
            book2 = book2.rstrip()
            result2 = createBook(book2)
            if(result2 == ""):
                continue
            file2 = open("book2.txt", "w", encoding='utf-8')
            file2.write(book2+ "\n" + result2)
            file2.close()
            
            file1 = open('book1.txt','r', encoding='utf-8') 
            dict1 = clearText(file1)
            file1.close()
            
            file2 = open('book2.txt','r', encoding='utf-8')
            dict2 = clearText(file2)
            file2.close()
            
            num = input("Please enter the number of words that you want to list: ")
            if(num == ""):
                print("Number is taken 20 as a default value.")
                num = "20"
            num = int(num)
            
            common = findCommonWords(dict1, dict2)
            print("\nBOOK 1: {0}".format(book1))
            print("BOOK 2: {0}".format(book2))
            print("COMMON WORDS")
            print("{0:3}\t{1:12}\t{2:8}\t{3:8}\t{4:8}".format("NO", "WORD", "FREQ_1", "FREQ_2", "FREQ_SUM"))
            for i in range(num): #comparing the keys' values and finding the max value
                maximum = 0
                word = ""
                for key in common:
                    if maximum < int(common[key]):
                        maximum = common[key]
                        word = key        
                print("{0:3}\t{1:12}\t{2:8}\t{3:8}\t{4:8}".format(i+1, word, dict1[word], dict2[word], maximum))
                common[word] = -1
                     
            dict1_distincts = findDistinctWords(dict1, common)
            dict2_distincts = findDistinctWords(dict2, common)
            
            print("\nBOOK 1: {0}\n".format(book1))
            print("DISTINCT WORDS\n")
            print("{0:3}\t{1:12}\t{2:8}".format("NO", "WORD", "FREQ_1"))
            
            for i in range(num): #comparing the keys' values and finding the max value
                maximum = 0
                word = ""
                for key in dict1_distincts:
                    if maximum < int(dict1_distincts[key]):
                        maximum = dict1_distincts[key]
                        word = key        
                print("{0:3}\t{1:12}\t{2:8}".format(i+1, word, maximum))
                dict1_distincts[word] = -1
        
            print("\nBOOK 2: {0}\n".format(book2))
            print("DISTINCT WORDS\n")
            print("{0:3}\t{1:12}\t{2:8}".format("NO", "WORD", "FREQ_2"))
            for i in range(num): #comparing the keys' values and finding the max value
                maximum = 0
                word = ""
                for key in dict2_distincts:
                    if maximum < int(dict2_distincts[key]):
                        maximum = dict2_distincts[key]
                        word = key        
                print("{0:3}\t{1:12}\t{2:8}".format(i+1, word, maximum))
                dict2_distincts[word] = -1
            
            
def createBook(book1): #reading the html elements from urls with BS4
    URL1 = "https://en.wikibooks.org/wiki/" + book1 + "/print_version"
    URL2 = "https://en.wikibooks.org/wiki/" + book1 + "/Print_version"
    URL3 = "https://en.wikibooks.org/wiki/" + book1 + "/Print_Version"
  
    try:
        r = requests.get(URL1) 
        soup = BeautifulSoup(r.content, 'html5lib') 
        result = soup.find('div', {'class' :'mw-parser-output'}).get_text()
        try:
            delete_this = soup.find('table', {'class' :'metadata plainlinks ambox ambox-notice'}).get_text()
            result = result.replace(delete_this, '')
        except:
            try:
                delete_this = soup.find('div', {'class':'noprint PrettyTextBox'}).get_text()
                result = result.replace(delete_this, '')
            except:
                result = str(result)
    except AttributeError:
        try:
            r = requests.get(URL2) 
            soup = BeautifulSoup(r.content, 'html5lib') 
            result = soup.find('div', {'class' :'mw-parser-output'}).get_text()
            try:
                delete_this = soup.find('table', {'class' :'metadata plainlinks ambox ambox-notice'}).get_text()
                result = result.replace(delete_this, '')
            except:
                try:
                    delete_this = soup.find('div', {'class':'noprint PrettyTextBox'}).get_text()
                    result = result.replace(delete_this, '')
                except:
                        result = str(result)
        except AttributeError:
            try:
                r = requests.get(URL3) 
                soup = BeautifulSoup(r.content, 'html5lib') 
                result = soup.find('div', {'class' :'mw-parser-output'}).get_text()
                try:
                    delete_this = soup.find('table', {'class' :'metadata plainlinks ambox ambox-notice'}).get_text()
                    result = result.replace(delete_this, '')
                except:
                    try:
                        delete_this = soup.find('div', {'class':'noprint PrettyTextBox'}).get_text()
                        result = result.replace(delete_this, '')
                    except:
                            result = str(result)
            except:
                print("Book named {0} is cannot be found.".format(book1))
                result = ""  
 
    return result
    
def clearText(file): #to removing stop words and calculating the numbers of the keys
    dictionary = {}
    for line in file:
        line = " " + line + " "
        line = line.lower()
        if "\'" in line:
            line = line.replace("\'", "")
        for w in stopwords:
            line = line.replace(w," ")
        for word in line.split():             
            if word.lower() in dictionary:
                num = int(dictionary.get(word.lower()))
                num = num + 1
                dictionary[word.lower()]=num
            else:
                dictionary[word.lower()]=1
    
    for key in dictionary:
        if " "+key+" " in stopwords:
            dictionary[key] = -1
            
    return dictionary

def findCommonWords(dict1, dict2): # to find the common words and add them to a dictionary
    common = {}
    for key in dict1:
            if(key in dict2):
                common[key] = int(dict1[key]) + int(dict2[key])
    return common

def findDistinctWords(dict1, common): #to find the distict words and add them into a dictionary
    dict1_distincts = {}
    for key in dict1:
        if key not in common:
            dict1_distincts[key] = dict1[key]
    return dict1_distincts

#the stopwords that i think they has to be discarded.
stopwords = [".", ",", "?", ":", "*", "\"", "_", "#", "==", "=", "(", ")", " - ", "<","[", "]","{", "}","^", "−", " b ", " c ", ">>>", " 1 ", " 2 ", " 3 ",
             " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 0 ", " can ", " will ", "//", "$", "←", "/", "'s","’s", "'ve", "'d", "'ll", " a ", " about ", 
             " above ", " after ", " again ", " against ", " all ", " am ", " an ", " and ", " any ", " are ", " aren't ", " as ", " at ", " be ", 
             " because ", " been ", " before ", " being ", " below ", " between ", " both ", " but ", " by ", " can't ", " cannot ", " could ", 
             " couldn't ", " did ", " didn't ", " do ", " does ", " doesn't ", " doing ", " don't ", " down ", " during ", " each ", " few ", " for ", 
             " from ", " further ", " had ", " hadn't ", " has ", " hasn't ", " have ", " haven't ", " having ", " he ", " he'd ", " he'll ", " he's ", 
             " her ", " here ", " here's ", " hers ", " herself "," him ", " himself ", " his ", " how ", " how's ", " i ", " i'd ", " i'll ", " i'm ", 
             " i've ", " if ", " in ", " into ", " is ", " isn't ", " it ", " it's ", " its ", " itself ", " let's ", " me ", " more "," most ", " mustn't ", 
             " my ", " myself ", " no ", " nor ", " not ", " of ", " off ", " on ", " once ", " only ", " or ", " other ", " ought ", " our ", " ours ", 
             " ourselves ", " out ", " over ", " own ", " same ", " shan't ", " she ", " she'd ", " she'll ", " she's ", " should ", " shouldn't ", " so ", 
             " some ", " such ", " than ", " that ", " that's ", " the ", " their ", " theirs ", " them ", " themselves ", " then ", " there ", " there's ", 
             " these ", " they ", " they'd ", " they'll ", " they're ", " they've ", " this ", " those ", " through ", " to ", " too ", " under ", " until ", 
             " up ", " very ", " was ", " wasn't ", " we ", " we'd ", " we'll ", " we're ", " we've ", " were ", " weren't ", " what ", " what's ", " when ", 
             " when's ", " where ", " where's ", " which ", " while ", " who ", " who's ", " whom ", " why ", " why's ", " with ", " won't ", " would ", 
             " wouldn't ", " you "," you'd ", " you'll ", " you're ", " you've ", " your ", " yours ", " yourself ", " yourselves ", " within ", " k ", " s ",
             " d ", " e ", " f ", " g ", " h ", " j ", " l ", " m ", " n ", " o ", " p ", " q ", " r ", " t ", " u ", " v ", " w ", " x ", " y ", " z "]

if __name__ == "__main__":
    main()
