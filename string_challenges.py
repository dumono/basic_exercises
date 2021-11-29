# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vowels = set('аеиоуэюя')
print(sum(letter in vowels for letter in word.lower()))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split(' ')))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split(' '):
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
count = 0
len_word = 0
for word in sentence.split(' '):
    len_word += len(word)
    count += 1

print("средняя длина слова:", len_word / count)