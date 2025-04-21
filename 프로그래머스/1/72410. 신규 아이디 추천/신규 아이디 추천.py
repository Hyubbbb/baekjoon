import re

def solution(new_id):
    print(f'step 0: {new_id}')
    # Step 1: 소문자 치환
    new_id = new_id.lower()
    
    print(f'step 1: {new_id}')
    # Step 2: [알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)]만 남기기
    
    tmp = ''
    for ch in new_id:
        if ch.isalnum() or ch in ['-', '_', '.']:
            tmp += ch
    print(f'step 2: {tmp}')
    
    # Step 3
    tmp = re.sub(r'\.+', '.', tmp)
    print(f'step 3: {tmp}')
    
    # Step 4: 마침표(.)가 처음이나 끝에 위치한다면 제거
    # 처음
    if tmp and tmp[0]=='.':
        tmp = tmp[1:]
    # 끝
    if tmp and tmp[-1]=='.':
        tmp = tmp[:-1]
        
    print(f'step 4: {tmp}')
    # Step 5: 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if not tmp:
        tmp = 'a'
    
    print(f'step 5: {tmp}')
    
    # Step 6: 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(tmp) >= 16:
        tmp = tmp[0:15]
        if tmp[-1] == '.':
            tmp = tmp[:-1]
    
    print(f'step 6: {tmp}')
    
    # Step 7: new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(tmp) <= 2:
        while True:
            tmp += tmp[-1]
            if len(tmp) == 3:
                break
    
    print(f'step 7: {tmp}')
    
    answer = tmp
    return answer