import os

def read_file(filename):
    chat = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            chat.append(line.strip())
    return chat

def convert(chat):
    new = []
    person = None #設定預設值為無
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果有預設值才跑下一行
            new.append(person + ': ' + line)
    return new

def write_file(filename, chat):
    with open(filename, 'w') as f:
        for line in chat:
            f.write(line + '\n')

def main():
    chat = read_file('input.txt')
    chat = convert(chat)
    write_file('output.txt', chat)

main()