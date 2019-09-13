'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    for i in range(0, len(word)-1):
        if word[i] == "t" and word[i+1] == "h":
            count += 1    
    
    return count