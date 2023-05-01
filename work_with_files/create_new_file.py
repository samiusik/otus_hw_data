import csv
import json
from files import JSON_FILE_PATH
from files import CSV_FILE_PATH


new_books_data = []
with open(CSV_FILE_PATH) as f:
    old_book_data = csv.DictReader(f)
    for row in old_book_data:
        new_book_dict = {
            "title": row['Title'],
            "author": row['Author'],
            "pages": int(row['Pages']),
            "genre": row['Genre']
        }
        new_books_data.append(new_book_dict)
print(new_books_data)


new_users_data = []
with open(JSON_FILE_PATH, 'r') as json_file:
    old_user_data = json.load(json_file)
for user in old_user_data:
    new_user_dict = {
        "name": user['name'],
        "gender": user['gender'],
        "address": user['address'],
        "age": user['age'],
        "books": []
    }
    new_users_data.append(new_user_dict)
print(new_users_data)


user_counter = 0
while len(new_books_data) != 0:
    if user_counter == len(new_users_data):
        user_counter = 0
    else:
        book_in_this_iteration = new_books_data.pop(0)
        new_users_data[user_counter]['books'].append(book_in_this_iteration)
        user_counter += 1


with open('../files/reference.json', 'w') as f:
    json.dump(new_users_data, f, indent=4)
    f.writelines([])
