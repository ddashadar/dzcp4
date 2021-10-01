name = input ('Имя - ')
surname = input ('Фамилия - ')
year = int (input ('Год рождения - '))
print (name, surname, year, sep = "_")
name, surname = surname, name
print (name, surname, year+60, sep = "_")
