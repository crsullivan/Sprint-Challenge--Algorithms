'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    
    # count = 0
    check = 'th'
    if word[0:2] == check:
        # check first 2 els for th, if found +1 and return everything after to re-check
        print(word[0:2])
        print('found')
        print(word[1:])
        # count + 1
        # print(count)
        # print(count + 1)
        return count_th(word[2:]) + 1
        # return count
    elif len(word) < len(check): # if nothing found check if even valid
        return 0
    else:
        # return everythintg after 1st el to check for th again
        print('not found')
        print(word[1:])
        return count_th(word[1:])

print(count_th('wbjkithnjklbvthhj'))

