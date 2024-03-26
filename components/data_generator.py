import csv

from faker import Faker
from random import randint
from openpyxl import Workbook

fake = Faker()

def generate_data(number_of_students):
  fake = Faker()
  data = []
  for _ in range(number_of_students):
    data.append({
      'id': randint(1, 100),
      'name': fake.name(),
      'address': fake.address(),
      'email': fake.email(),
      'phone': fake.phone_number()
    })
  return data

def save_data_to_excel(data):
  wb = Workbook()
  ws = wb.active
  ws.append(['ID', 'Name', 'Address', 'Email', 'Phone'])
  for student in data:
    ws.append(list(student.values()))
  return wb

