"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    result = []
    for idx in items:
        if idx % 2 != 0:
            result.append(items[idx])
    
    return result


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print (f'{i}. {item}')

        i += 1
    
    return items


def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)
    return nums


def censor_vowels(word):
    chars = []
    vowels = "aeiou"

    for letter in word: 
        if letter in vowels:
            chars.append('*')
        else:
            chars.append(letter)  
    
    return chars.join('')


def snake_to_camel(string):
    words = string.split('_')
    camel_case = []
    first_word = words.pop(0)
    camel_case.append(first_word.lower())
    camelCase = ""

    for word in words:
        camel_case.append(word.title())

    for word in camel_case:
        camelCase += word    

    return camelCase



def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest



def truncate(string):
    result = ""

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result += char
        

    return result



def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens += 1

        elif char == ')':
            parens -= 1

    # if parens < 0:
    #     return false

    return parens == 0



def compress(string):
    pass  # TODO: replace this line with your code
