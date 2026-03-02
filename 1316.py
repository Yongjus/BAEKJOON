import sys
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    set_letter = set(word)
    for letter in set_letter:
        split_word= word[word.find(letter):word.rfind(letter)+1]
        if split_word.replace(letter, ""):
            N -= 1
            break
print(N)
