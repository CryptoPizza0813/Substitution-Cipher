import os, sys
import random

Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
in_file = 'BBC_news.txt'
out_file = 'Encrypted_news.txt'
dec_file = 'Decrypted_news.txt'


# 파일 불러오기
def readFile(in_file):
    if not os.path.exists(in_file):
        print('File %s does not exits.' % (in_file))
        sys.exit()
    # 입력 파일에서 텍스트 읽기
    InFileObj = open(in_file)
    my_content = InFileObj.read()
    InFileObj.close()
    return my_content

# 파일에 쓰기
def rewrite(out_file, my_content):  # out_file에 my_content를 쓴다
    if os.path.exists(out_file):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit' %(out_file))
        response = input('> ')  # 사용자 입력 기다리기
        if not response.lower().startswith('c'):
            sys.exit()
    OutFileObj = open(out_file, 'w')
    OutFileObj.write(my_content)
    OutFileObj.close()

def keyRandGen():
    key = ''
    for i in range(26):
        while (1):
            temp = chr(random.randint(65, 90))  # 아스키코드 A = 65, Z = 90
            if temp in key: # 랜덤 생성한 키 단어가 이미 존재한다면 다시 생성(continue)
                continue
            else:           # 랜덤 생성한 키 단어가 겹치지 않는다면 key string에 추가
                key += temp
                break
    return key

def keyValidation(key):
    if len(key) != 26:  # 키 길이가 26을 초과하는지
        print("key length must be 26!")
        sys.exit()
    for i in range(len(key)):   # 중복되는 키 단어가 존재하는지
        for j in range(len(key)):
            if i == j:
                continue
            else:
                if key[i] == key[j]:    # 동일한 단어가 키에 존재시
                    print("There is same key in key[%d](= %s) and key[%d](= %s)." %(i, key[i], j, key[j]), end = ' ')
                    print("Key must be all different!")
                    sys.exit()
    cnt = 0;
    for i in range(len(key)):   # 영단어 말고 다른것이 키에 존재하는지
        if key[i] not in Alphabet:
            print("key[%d](= %s) must be an alphabet! " %(i, key[i]))
            sys.exit()
    print("You can use this key!")

def encrypt(key, msg):
    result = ''
    InSet = Alphabet
    OutSet = key

    for ch in msg:
        if ch.upper() in InSet:  # 영문자면 대문자로 바꾸어줌, 그게 알파벳에 있는가?
            idx = InSet.find(ch.upper()) # 있으면 암호화 해야지. 그 알파벳의 위치를 저장
            if ch.isupper():    # 대문자인지 물어보는것
                result += OutSet[idx].upper()   # 혹시 모르니 대문자로 다 넣어줌
            else:
                result += OutSet[idx].lower()   # 소문자면 소문자로 바꿔서 넣어줘야함
        else:
            result += ch    # 영문자가 아니면 변환하지 않고 그대로 넣는다
    return result

def decrypt(key, msg):
    result = ''
    InSet = key
    OutSet = Alphabet

    for ch in msg:
        if ch.upper() in InSet:  # 영문자면 대문자로 바꾸어줌, 그게 알파벳에 있는가?
            idx = InSet.find(ch.upper()) # 있으면 암호화 해야지. 그 알파벳의 위치를 저장
            if ch.isupper():    # 대문자인지 물어보는것
                result += OutSet[idx].upper()   # 혹시 모르니 대문자로 다 넣어줌
            else:
                result += OutSet[idx].lower()   # 소문자면 소문자로 바꿔서 넣어줘야함
        else:
            result += ch    # 영문자가 아니면 변환하지 않고 그대로 넣는다
    return result


key = keyRandGen()
keyValidation(key)              # 키 랜덤 생성 후 유효성 확인
print("key = ", key)

message = readFile(in_file)     # message에 BBC_news.txt 내용을 복사함

cipher_msg = encrypt(key, message)
rewrite(out_file, cipher_msg)   # Encrypted_news.txt에 암호화 된 message 내용을 복사함





encrypted_msg = readFile(out_file)  # encrypted_msg에 Encrypted_news.txt 내용을 복사함

recovered_msg = decrypt(key, encrypted_msg)
rewrite(dec_file, recovered_msg)    # Decrypted_news.txt에 복호화된 message 내용을 복사함


# 사용된 키 =  DTPZRVYXEBKJMOCHWGQFISULAN

