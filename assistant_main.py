from collections import UserDict
import re

class Field:                     # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):               # Клас для зберігання імені контакту. Обов'язкове поле.
    def __init__(self, name:str):
         if not name:            # Обов'язкове поле. Перевірка
              raise ValueError("Поле імʼя не може бути порожнім")
         super().__init__(name)

class Phone(Field):              # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, phone_number: str):
         ph = str(phone_number).strip()               # приводимо до єдиного формату
         if len(ph) != 10 or not ph.isdigit():        # check fot 10 and for digits
              raise ValueError("Номер має бути у форматі 10 цифр")
         else:
             super().__init__(ph)
         
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value     # To be able to compare two phone obj in Record dd change remove phone

class Record:                    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            print(f"Такий номер вже є")
         
    def remove_phone(self, phone: Phone):
        self.phones = [p for p in self.phones if p != phone]  # New list withou phone to delete
        print(f"Видалено номер {phone}")

    def edit_phone(self, old_phone:Phone, new_phone:Phone):
        for p in range(len(self.phones)):
            if self.phones[p] == old_phone:
                self.phones[p] = new_phone
                print(f"{old_phone} замінено на {new_phone}")
                break        # заміна першого знайденого
            else:
                print(f"{old_phone} не знайдено")

    def find_phone(self, phone: str):
        phone_obj = Phone(phone)
        for p in self.phones:
            if p == phone_obj:
                return p.value
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):     # Клас для зберігання та управління записами.

    def add_record(self, record: Record):
          self.data[record.name.value] = record

    def find(self, name_to_find: str):
        return self.data.get(name_to_find)    # To get the record by name
               
    def delete(self, name: str):
        record = self.data.pop(name, None)    # Deleting or returning a message of not found
        if record:
            print(f"Запис {name} видалено")
        else:
            print(f"Запис {name} не знайдено")  





# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")                   
john_record.add_phone(Phone("1234567890"))             # додаємо номер через створення обєкту Phone
john_record.add_phone(Phone("5555555555"))

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone(Phone("9876543210"))
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone(Phone("1234567890"), Phone("1112223333"))

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

for name, record in book.data.items():
    print(record)