# Задача №16
numberArray = int(input('Введите количество чисел в массиве: '))
userArray = []
while numberArray > 0:
    userArray.append(int(input('Введите число: ')))
    numberArray -= 1
numberX = int(input('Введите число, которое будем искать: '))
print(f'Число в массиве встречается {userArray.count(numberX)} раз')

# Задача №18
numberArray = int(input('Введите количество чисел в массиве: '))
userArray = []
while numberArray > 0:
    userArray.append(int(input('Введите число: ')))
    numberArray -= 1
numberX = int(input('Введите число, для поиска близкого числа: '))
temp = numberX - abs(userArray[0])
result = userArray[0]
for i in userArray:
    if abs(numberX-i) < temp:
        temp = numberX - i
        result = i
print(f'Самое близкое число из массива: {result}')

# Задача №20
userWord = input('Введите слово для игры Scrabble: ')
alphabetRus = 'АВЕИНОРСТДКЛМПУБГЁЬЯЙЫЖЗХЦЧШЭЮФЩЪ'
alphabetEng = 'AEIOULNSTRDGBCMPFHVWYKJXQZ'
result = 0
if userWord[0].upper() in alphabetRus:
    alphabetDictRus = {1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
                   2:['Д', 'К', 'Л', 'М', 'П', 'У'],
                   3:['Б', 'Г', 'Ё', 'Ь', 'Я'],
                   4:['Й', 'Ы'],
                   5: ['Ж', 'З', 'Х', 'Ц', 'Ч'],
                   8: ['Ш', 'Э', 'Ю'],
                   10: ['Ф', 'Щ', 'Ъ']}
    for i in userWord:
        for l, k in alphabetDictRus.items():
            if i.upper() in k:
                result += l
else:
    alphabetDictRus = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
                       2: ['D', 'G'],
                       3: ['B', 'C', 'M', 'P'],
                       4: ['F', 'H', 'V', 'W', 'Y'],
                       5: ['K'],
                       8: ['J', 'X'],
                       10: ['Q', 'Z']}
    for i in userWord:
        for l, k in alphabetDictRus.items():
            if i.upper() in k:
                result += l
print(result)
