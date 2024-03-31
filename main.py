from fastapi import FastAPI
from faker import Faker
import random
import pandas as pd
from starlette.responses import FileResponse
import os

app = FastAPI(title='FastApi Pandas')
fake = Faker()

def generate_fake_data(num_entries):
    users = []
    for _ in range(num_entries):
        user = {
            'Full Name': fake.name(),
            'Email Address': fake.email(),
            'Age': random.randint(18, 80),
            'Gender': random.choice(['Male', 'Female', 'Other']),
            'Location': fake.city() + ', ' + fake.country(),
            'Pre-existing Conditions': fake.word() if random.random() < 0.3 else None,
            'Mental Health Disorders': fake.word() if random.random() < 0.2 else None,
            'Medications': fake.word() if random.random() < 0.4 else None,
            'Previous Treatments': fake.word() if random.random() < 0.3 else None,
            'Mood Rating': random.randint(1, 10),
            'Mood Notes': fake.sentence() if random.random() < 0.5 else None,
            'Mood Triggers': fake.sentence() if random.random() < 0.4 else None,
            'Steps Taken': random.randint(1000, 15000),
            'Distance Traveled (km)': round(random.uniform(1.0, 20.0), 2),
            'Active Minutes': random.randint(0, 180),
            'Sleep Duration (hours)': round(random.uniform(4.0, 12.0), 1),
            'Social Media Posts': fake.sentence() if random.random() < 0.3 else None,
            'App Usage': fake.sentence() if random.random() < 0.4 else None,
            'Lifestyle Habits': fake.sentence() if random.random() < 0.5 else None
        }
        users.append(user)
    return users

@app.get("/")
def generate_and_export_data():
    users = generate_fake_data(10000)
    df = pd.DataFrame(users)
    csv_filename = 'mindwell_data.csv'
    df.to_csv(csv_filename, index=False)
    return FileResponse(path=csv_filename, filename=os.path.basename(csv_filename), media_type='text/csv')


# from faker import Faker
# import random
# import pandas as pd

# fake = Faker()

# # Generate 500 user entries
# users = []
# for _ in range(100000):
#     user = {
#         'Full Name': fake.name(),
#         'Email Address': fake.email(),
#         'Age': random.randint(18, 80),
#         'Gender': random.choice(['Male', 'Female', 'Other']),
#         'Location': fake.city() + ', ' + fake.country(),
#         'Pre-existing Conditions': fake.word() if random.random() < 0.3 else None,
#         'Mental Health Disorders': fake.word() if random.random() < 0.2 else None,
#         'Medications': fake.word() if random.random() < 0.4 else None,
#         'Previous Treatments': fake.word() if random.random() < 0.3 else None,
#         'Mood Rating': random.randint(1, 10),
#         'Mood Notes': fake.sentence() if random.random() < 0.5 else None,
#         'Mood Triggers': fake.sentence() if random.random() < 0.4 else None,
#         'Steps Taken': random.randint(1000, 15000),
#         'Distance Traveled (km)': round(random.uniform(1.0, 20.0), 2),
#         'Active Minutes': random.randint(0, 180),
#         'Sleep Duration (hours)': round(random.uniform(4.0, 12.0), 1),
#         'Social Media Posts': fake.sentence() if random.random() < 0.3 else None,
#         'App Usage': fake.sentence() if random.random() < 0.4 else None,
#         'Lifestyle Habits': fake.sentence() if random.random() < 0.5 else None
#     }
#     users.append(user)


# df = pd.DataFrame(users)

# df.to_csv('mindwell_data.csv', index=False)

