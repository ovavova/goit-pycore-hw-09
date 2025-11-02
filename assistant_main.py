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
         super().__init(name)

class Phone(Field):              # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, phone_number: str):
         ph = str(phone_number).strip() # приводимо до єдиного формату
         if len(ph) != 10 or not ph.isdigit():
              raise ValueError("Номер має бути у форматі 10 цифр")


class Record:                    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: Phone):
         
    def remove_phone(self, phone: Phone):

    def edit_phone(self, old_phone:Phone, new_phone: Phone):

    def find_phone(self, Phone):
             

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):     # Клас для зберігання та управління записами.
    
    def add_rercord(self, record):
          self.data[record.name] = record.phones

    def find(self, name):
           result = (filter(lambda))
               
    def delete(self, name):
           
           