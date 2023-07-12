"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

con = sqlite3.connect('social_network.db')
cur = con.cursor()
def main():
    create_people_table()
    populate_people_table()

def create_people_table():
# Commit (save) pending transactions to the database.
# Transactions must be committed to be persistent.
 return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    add_person_query = """
    INSERT INTO people
    (
    name,
    email,
    address,
    city,
    province,
    bio,
    age,
    created_at,
    updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    new_person = ('Beast',
                  'beastyboy07@gmail.com',
                  '111 fake add st.',
                  'FakerSpot',
                  25,
                  datetime.now(),
                  datetime.now())
    cur.execute(add_person_query, new_person)
    con.commit()
    con.close()
    # Hint: See example code in lab instructions entitled "Working with Faker"
    fake = ("en_CA")
    for _ in range(10):
       province = fake.administrative_unit()
       population = fake.random_int(min=900000, max=100000000)
       print(f'The population of {province} is {population}.')
    return

if __name__ == '__main__':
   main()