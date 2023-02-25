from flask_seeder import Seeder, Faker, generator
from peinconn.peinconn.models import User, Interest
from peinconn.peinconn.extensions import db
import random

class RegisterInterestSeeder(Seeder):

    def run(self):
    # Create a new Faker and tell it how to create User objects
        interests_id = [1,2,3,4,5,6,7,8,9,]
        users = User.query.all();
        faker = Faker(
            cls=User,
           init={}
        )
        for user in users:
            iteration_no = 2
            user_interests = []
            user_model = User.query.filter(User.interests.any(User.id==user.id)).all()
            if len(user_model) != 0:     
                user_model_interests = user_model[0].interests
                if len(user_model_interests) >= 2:
                    continue
                if len(user_model_interests) == 1:
                    iteration_no = 1
                    user_interests.append(user_model_interests[0].id)
            for x in range(0, iteration_no):
                interest_id = random.choice(interests_id)
                if interest_id in user_interests:
                    interest_id = random.choice(interests_id)
                user_interests.append(interest_id)
                interest_data = db.session.query(Interest).filter_by(id = interest_id).one();
                user.interests.append(interest_data)
            user_interests = []    
            for singleUser in faker.create(1):  
                self.db.session.add(user)  