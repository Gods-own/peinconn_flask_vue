from flask_seeder import Seeder, Faker, generator
from peinconn.peinconn.models import Activity, User
from peinconn.peinconn.extensions import db
import random, os, datetime
from werkzeug.security import generate_password_hash
import hashlib
from werkzeug.utils import secure_filename
from essential_generators import DocumentGenerator

class ActivitySeeder(Seeder):

    def run(self):
    # Create a new Faker and tell it how to create User objects
    #activity, interest_id, picture, user_id
        gen = DocumentGenerator()
        users = User.query.all();

        path = 'C:/Users/idumeka oritogun/Documents/flask-projects/Peinconn_Project/backend/peinconn/peinconn/static/fake_activity_images'
        new_path = 'C:/Users/idumeka oritogun/Documents/flask-projects/Peinconn_Project/backend/peinconn/peinconn/static/images/uploads'
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
        faker = Faker(
            cls=Activity,
            init={}
        )

        for x in dir_path:
            for singleActivity in faker.create(1):  
                singleUser = random.choice(users).id
                user_model = User.query.filter(User.interests.any(User.id==singleUser)).all()
                if len(user_model) != 0:     
                    user_model_interests = user_model[0].interests
                    selected_interest = random.choice(user_model_interests)
                    singleActivity.interest_id = selected_interest.id
                    singleActivity.user_id = singleUser
                    singleActivity.picture = random.choice(new_dir_path)
                    singleActivity.activity = gen.sentence()
                    self.db.session.add(singleActivity)      