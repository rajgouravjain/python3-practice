def anagram_solution(s1,s2) :
    c1 = [0] * 26
    c2 = [0] * 26

    for char in s1:
        pos1 = ord(char) - ord('a')
        c1[pos1] += 1
    for char in s2:
        pos2 = ord(char) -ord('a')
        c2[pos2] += 1

    j =0
    still_ok = True
    while j < 26 and still_ok==True:
        if c1[j] == c2[j] :
            pass
        else :
            still_ok = False
        j += 1
    return still_ok

if  __name__ == '__main__' :
    print(anagram_solution('asdfdsf','fsdfdsa'))
    print(anagram_solution('asdfdsf','ffdfdsa'))
