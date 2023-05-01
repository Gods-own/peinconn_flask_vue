from flask_seeder import Seeder, Faker, generator
from flask import current_app
from peinconn.peinconn.models import Activity, User, Interest
from peinconn.peinconn.extensions import db
import random, os, datetime
from werkzeug.security import generate_password_hash
import hashlib
import shutil
from werkzeug.utils import secure_filename
from essential_generators import DocumentGenerator

class ReadingSeeder(Seeder):

    def run(self):
    # Create a new Faker and tell it how to create User objects
    #activity, interest_id, picture, user_id
        gen = DocumentGenerator()
        users = User.query.filter(User.interests.any(Interest.id==1)).all()

        path = rf"{current_app.config['BASE_DIR']}\peinconn\static\reading"
        new_path = rf"{current_app.config['BASE_DIR']}\peinconn\static\images\uploads"
        dir_path = os.listdir(path)

        new_dir_path = []

        for singleFile in dir_path:
            get_ext = singleFile.rsplit(".", 1)
            ext = get_ext[1]
            new_filename = secure_filename(singleFile)
            result = hashlib.md5(new_filename.encode())
            new_filename_without_ext = result.hexdigest()
            new_dir_path.append(f'{new_filename_without_ext}.{ext}')
            shutil.copy2(f'{path}/{singleFile}', f'{new_path}/{new_filename_without_ext}.{ext}')
        faker = Faker(
            cls=Activity,
            init={}
        )

        for x in new_dir_path:
            for singleActivity in faker.create(1):  
                if len(users) != 0:
                    singleUser = random.choice(users).id
                    singleActivity.interest_id = 1
                    singleActivity.user_id = singleUser
                    singleActivity.picture = x
                    singleActivity.activity = gen.sentence()
                    self.db.session.add(singleActivity)     