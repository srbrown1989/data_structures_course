"""
Interview Question #4

Construct an algorithm to check whether two words (or phrases) are anagrams or not!

"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once"

For example: restful and fluster
"""

#My Solution
def is_anagram(s1, s2):
    s2 = list(s2)
    for c in s1:
        if c in s2:
            s2.pop(s2.index(c))
        else:
            return False
    return True

test = "resistance"
test2 = "ancestxies"
print(is_anagram(test,test2))

##Tutors solution
"""
def is_anagram(str1, str2):

    # if the length of the strings differ - they are not anagrams
    if len(str1) != len(str2):
        return False

    # we have to sort the letters of the strings and then we haev to compare
    # the letters with the same indexes
    # this is the bottlenect because it has O(NlogN)
    str1 = sorted(str1)
    str2 = sorted(str2)

    # after that we have to check the letters with the same indexes
    # O(N) running time
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    # overall running time is O(NlogN)+O(N)=O(NlogN)

    return True


if __name__ == '__main__':

    s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    s2 = ['r', 'e', 's', 't', 'f', 'e', 'l']

    print(is_anagram(s1, s2))

"""