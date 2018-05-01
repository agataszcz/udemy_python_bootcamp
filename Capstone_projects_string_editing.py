'''
Capstone Mini Projects: String Editing
'''
def reverse(s):
    '''
    Input: string
    Output: reversed string
    '''
    return s[::-1]

def reverse_words(s):
	'''
	Input: string
	Output: string with words in a reversed order, without reversing words themselves. 
	'''
	return ' '.join(s.split()[::-1])

def count_vowels(s):
	'''
	A function for counting vowels in a string.
	'''
    a = s.lower().count('a')
    print("Total count of 'a' is {}".format(a))
    e = s.lower().count('e')
    print("Total count of 'e' is {}".format(e))
    i = s.lower().count('i')
    print("Total count of 'i' is {}".format(i))
    o = s.lower().count('o')
    print("Total count of 'o' is {}".format(o))
    u = s.lower().count('u')
    print("Total count of 'u' is {}".format(u))
    y = s.lower().count('y')
    print("Total count of 'y' is {}".format(y))
        
    return "Total number of vowels: {}".format(a+e+i+o+u+y)

def count_vowels2(s):
	'''
	Alternative function for counting vowels in a string and printing their respective totals (if they are greater than O).
	'''     
    a = s.lower().count('a')
    if a>0:
        print("Total count of 'a' is {}".format(a))
    e = s.lower().count('e')
    if e>0:
        print("Total count of 'e' is {}".format(e))
    i = s.lower().count('i')
    if i>0:
        print("Total count of 'i' is {}".format(i))
    o = s.lower().count('o')
    if o>0:
        print("Total count of 'o' is {}".format(o))
    u = s.lower().count('u')
    if u>0:
        print("Total count of 'u' is {}".format(u))
    y = s.lower().count('y')
    if y>0:
        print("Total count of 'y' is {}".format(y))
    
    return "Total number of vowels: {}".format(a+e+i+o+u+y)

def count_vowels3(s):
	'''
    Alternative function for counting vowels in a string.
	'''
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    count_y = 0
    
    for letter in s.lower():
        if letter =="a":
            count_a += 1
        if letter =="e":
            count_e += 1
        if letter =="i":
            count_i += 1
        if letter =="o":
            count_o += 1
        if letter =="u":
            count_u += 1
        if letter =="y":
            count_y += 1
    print("Number of 'a' letters: {}". format(count_a))
    print("Number of 'e' letters: {}". format(count_e))
    print("Number of 'i' letters: {}". format(count_i))
    print("Number of 'o' letters: {}". format(count_o))
    print("Number of 'u' letters: {}". format(count_u))
    print("Number of 'y' letters: {}". format(count_y))
    return "Total number of vowels: {}.".format(count_a + count_e + count_i + count_o + count_u + count_y)

def count_all_vowels(s):
	'''
	A function for counting all vowels in a string as one total.
	'''
    vowel_count = 0
    for letter in s.lower():
        #using lower() to avoid problems with uppercase letters
        if letter in "aeiouy":
            vowel_count += 1
    return vowel_count

def palindrome_check(s):
	'''
	A function for checking if a string is a palindrome. Palindromes read the same forwards and backwards (like “racecar”).
	Input: string
	Output: Boolean
	'''
    return s.lower() == s.lower()[::-1]

def count_words(s):
	'''
	A function for counting words in a string.
	'''
    return len(s.split())

def count_words_from_textfile(filepath):
	'''
	A function for counting words in a string from a .txt file. It opens the file in a reading mode, counts words inside, and closes the file.
	Filepath must appear in quotes.
	'''
    with open(filepath, 'r') as f:
        word_count = len(f.read().split())
    return "Number of words in the file: {}.".format(word_count)



