def solution(s):
    words = s.split(" ")

    for idx, word in enumerate(words):
        if word=='':
            word = word
        elif len(word)==1: # 공백이 아니고, 한 글자 단어인 경우
            word = word[0].upper()
        else: # 일반적인 경우
            word = word[0].upper() + word[1:].lower()
        words[idx] = word

    answer = ' '.join(words)
    return answer