# E-Book-Analysis-And-Representation

# Introduction

E-books are getting more popular day by day. This project was about E-books. The frequencies of the words of the e-books on the wikibooks.org were examined and the most common words in the book were examined. While this study was being carried out, words that did not mean anything by themselves, called stop words, were not included in the study, as their amount could be really high. Later, two e-books were examined, and the multi-frequency words that were common in both and the distinct words found separately.

When the application is executed, a menu appears on the console screen from which the user decides whether they want to analyze a single book or two books. After the user gives the name of the book as input, the book, if available, is taken from the Wikibooks website and saved in a text file. Then, as a result of the necessary analysis, the requested information is displayed.

# Methodology 

The project starts with a menu on the console. This menu is inside a while loop unless “Q” for Quit operation is entered, the program continues. 

When 1 is entered, the program asks for the name of the e-book and the number of words that is wanted to be listed. The given book name is sent to a method called createBook(). createBook() method is used for getting each book from the website. It creates the content of the e-book. A popular web scraping library that is called Beautiful Soup is used to getting the text from the website. There are two possible URLs and if one is not working the other usually works. I use a try-except structure so that the program wouldn't stop suddenly. 

With beautiful soup library, I find the text as an HTML element and get its inner text with get_text() method. If the book is not valid or available, the program returns a message and it displays menu again. Here I used the “continue” keyword. That keyword is used to go back to where the iteration starts. So the program displays the menu. 

File operations are used to read and write on files. The result that we get from web scrapping (the content of the e-book) is then written into a file. After all file operations, we need to close the files.  encoding='utf-8' was important, because the result was only writeable to utf-8 files. 

For analysis, the stop words must have been discarded. clearText() method clears the text that has stop words. All stop words, numerals, punctuations and letters were discarded from the whole text. I added them into a list and if a key from the dictionary is on that list I marked them to not to use. The text becomes ready to analyze. The returned dictionary from clearText() method has no stop words and all the values are the amounts of the keys.

After that, with for loop, I compare all of the values in the dictionary and find the top ones. If there is a given amount, we take top X, but the default value for X is 20.

When the X most valued words are displayed in order, the program returns to the menu again. 

If 2 is entered, 2 book names are taken from the user and the books are created. The stop words are discarded as I mention above. 

Then, findCommonWords() method is used to compare dictionaries and finds common words. It finds the words that both books include. And as the reverse of findCommonWords(), findDistinctWords() method compares two dictionaries and finds distinct words. When these dictionaries are created, their values are compared like in the first option. The results are displayed.  

Dictionary data structure is mostly used. Dictionaries have key and value pairs. That feature of dictionaries helped me to store the amount of each word and made me reach them easily.

#LICENCE
MIT LICENCE
