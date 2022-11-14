from flask_seeder import Seeder, Faker, generator
from peinconn.peinconn.models import User
from peinconn.peinconn.extensions import db
import random, os, datetime
from werkzeug.security import generate_password_hash
import hashlib
from werkzeug.utils import secure_filename

class UserSeeder(Seeder):
    # def run(self):
    #     fakers = []
    #     for key, value in countries.items():
    #         faker = Faker(
    #             cls=Country,
    #             init={
    #                 "country_abbrev": key,
    #                 "country": value.lower()
    #             }
    #         )
    #         fakers.append(faker)

    #     for faker in fakers:
    #         for country in faker.create(1):  
    #             self.db.session.add(country) 

    def run(self):
    # Create a new Faker and tell it how to create User objects
        countries_id = [233,220,237,201,160,155]
        gender = ['male', 'female']
        password = generate_password_hash('good')

        path = 'C:/Users/idumeka oritogun/Documents/flask-projects/Peinconn_Project/backend/peinconn/peinconn/static/fake_profile_pic'
        new_path = 'C:/Users/idumeka oritogun/Documents/flask-projects/Peinconn_Project/backend/peinconn/peinconn/static'
        dir_path = os.listdir(path)

        new_dir_path = []

        for singleFile in dir_path:
            get_ext = singleFile.rsplit(".", 1)
            ext = get_ext[1]
            new_filename = secure_filename(singleFile)
            result = hashlib.md5(new_filename.encode())
            new_filename_without_ext = result.hexdigest()
            new_dir_path.append(f'{new_filename_without_ext}.{ext}')
            os.rename(f'{path}/{singleFile}', f'{new_path}/{new_filename_without_ext}.{ext}')
        print(new_dir_path)
        faker = Faker(
            cls=User,
            init={
                "name": generator.Name(),
                # "age": generator.Integer(start=20, end=100),
                "date_of_birth": datetime.date(random.randint(1959, 2005), random.randint(1, 12), random.randint(10, 28)),
                "country_id": random.choice(countries_id),
                "username": generator.Name(),
                "gender": random.choice(gender),
                "email": generator.Email(),
                "password": password,
                "userImage": random.choice(new_dir_path)
            }
        )

        for x in range(0, 5):
            for singleUser in faker.create(1):  
                self.db.session.add(singleUser)          