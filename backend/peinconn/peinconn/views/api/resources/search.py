from flask import request, jsonify, make_response
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import users_schema
from peinconn.peinconn.models import User
from peinconn.peinconn.helpers.pagination import get_pagination, get_pagination_info
from peinconn.peinconn.helpers.utils import approximate_DOB
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user

class Search(Resource):
    @token_required
    def get(self):
        try:
            authUser = get_current_user()

            pagination_info = get_pagination_info(request)

            allArgs = request.args.to_dict()

            username = request.args.get('username')
            search_username = "%{}%".format(username)
            country = request.args.get('country')
            age_range = request.args.get('age_range')
            gender = request.args.get('gender')

            if age_range is not None:
                age_list = age_range.split("-")

            if all(key in allArgs for key in ('age_range', 'country', 'gender')):
                user_model = User.query.filter(((User.username==username) | (User.name==username)) & (User.country_id==country) & (User.gender==gender) & (User.date_of_birth<=approximate_DOB(int(age_list[0]))) & (User.date_of_birth>=approximate_DOB(int(age_list[1])))).order_by(User.id.desc())
            elif len(allArgs) == 3 and all(key in allArgs for key in ('age_range', 'country')):  
                user_model = User.query.filter(((User.username==username) | (User.name==username)) & (User.country_id==country) & (User.date_of_birth<=approximate_DOB(int(age_list[0]))) & (User.date_of_birth>=approximate_DOB(int(age_list[1])))).order_by(User.id.desc())
            elif len(allArgs) == 3 and all(key in allArgs for key in ('age_range', 'gender')):  
                user_model = User.query.filter(((User.username==username) | (User.name==username)) & (User.gender==gender) & (User.date_of_birth<=approximate_DOB(int(age_list[0]))) & (User.date_of_birth>=approximate_DOB(int(age_list[1])))).order_by(User.id.desc())   
            elif len(allArgs) == 3 and all(key in allArgs for key in ('country', 'gender')):  
                user_model = User.query.filter(((User.username==username) | (User.name==username)) & (User.country_id==country) & (User.gender==gender)).order_by(User.id.desc())       
            elif len(allArgs) == 2 and all(key in allArgs for key in ('age_range')):  
                user_model = User.query.filter(((User.username==username) | (User.name==username)) & (User.date_of_birth<=approximate_DOB(int(age_list[0]))) & (User.date_of_birth>=approximate_DOB(int(age_list[1])))).order_by(User.id.desc())
            elif len(allArgs) == 2 and all(key in allArgs for key in ('gender')):  
                user_model = User.query.filter(((User.username==username) | (User.name==username)) & (User.gender==gender)).order_by(User.id.desc())  
            elif len(allArgs) == 2 and all(key in allArgs for key in ('country')):  
                user_model = User.query.filter(((User.username==username) | (User.name==username)) & (User.country_id==country)).order_by(User.id.desc())
            else:               
                user_model = User.query.filter(User.username.ilike(search_username)).order_by(User.id.desc())

            # if age_range is not None:
            #     age_list = age_range.split("-")
            #     user_model = User.query.filter((User.username==username) | (User.name==username) | (User.country_id==country) | (User.gender==gender) | (User.date_of_birth<=approximate_DOB(int(age_list[0]))) | (User.date_of_birth>=approximate_DOB(int(age_list[1])))).all()
            # else:
            #     user_model = User.query.filter((User.username==username) | (User.name==username) | (User.country_id==country) | (User.gender==gender)).all()

            users = user_model.paginate(page=pagination_info['page'], per_page=pagination_info['per_page'], max_per_page=pagination_info['max_per_page'])        

            userTransformer = users_schema.dump(user_model)

            links = get_pagination('api.search', users)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved User Successfully', 'data': userTransformer, 'links': links}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': f'Something went wrong, try again later {e}'}), 500)    

        # value = request.GET.get('q', None)
        # searcher = User.objects.get(username=request.user)
        # interests = Interests.objects.filter(user_hobby=searcher)
        # user_hobbies = []
        # for interest in interests:
        #     user_hobby = interest.id
        #     user_hobbies.append(user_hobby)
        # if value != None:
        #     captalizedValue = value.capitalize()
        #     result = User.objects.filter(username=captalizedValue).exists()
        #     users = User.objects.all()
        #     name_search = []
        #     if 'country' in request.GET:
        #         agerange = request.GET.get('age', "")
        #         gender = request.GET.get('gender', "")
        #         result = Countries.objects.filter(country__iexact=captalizedValue).exists()
        #         countries = Countries.objects.all()
        #         if result == True:
        #             country_id = Countries.objects.get(country__iexact=captalizedValue)
        #             if len(agerange) == 0 and len(gender) == 0:
        #                 if User.objects.filter(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies)).exists():
        #                     get_user = User.objects.get(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies)).distinct()
        #                     location = get_user
        #                     return JsonResponse(location.serialize())
        #                     print('female')
        #                     print(agerange)
        #             elif len(agerange) == 0 or agerange == None:
        #                 if User.objects.filter(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).exists():
        #                     get_user = User.objects.get(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).distinct()
        #                     location = get_user
        #                     return JsonResponse(location.serialize())
        #             elif len(gender) == 0 or gender == None:
        #                 age_list = agerange.split("-")
        #                 if User.objects.filter(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).exists():
        #                     get_user = User.objects.get(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).distinct() 
        #                     location = get_user
        #                     return JsonResponse(location.serialize())
        #             else:
        #                 age_list = agerange.split("-")
        #                 if User.objects.filter(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).exists():
        #                     get_user = User.objects.get(Q(citizen=country_id) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).distinct()
        #                     location = get_user
        #                     return JsonResponse(location.serialize())   
        #         else:
        #             for country in countries.iterator():
        #                 if value.lower() in country.country.lower(): 
                        
        #                     if len(agerange) == 0 and len(gender) == 0:
        #                         if User.objects.filter(Q(citizen=country) & Q(hobbysist__in=user_hobbies)).exists():
        #                             get_user = User.objects.get(Q(citizen=country) & Q(hobbysist__in=user_hobbies)).distinct()
        #                             location = get_user
        #                             name_search.append({"id": country.id, "person": location})
        #                             print('female')
        #                             print(agerange)
        #                     elif len(agerange) == 0 or agerange == None:
        #                         if User.objects.filter(Q(citizen=country) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).exists():
        #                             get_user = User.objects.get(Q(citizen=country) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).distinct()
        #                             location = get_user
        #                             name_search.append({"id": country.id, "person": location})
        #                     elif len(gender) == 0 or gender == None:
        #                         age_list = agerange.split("-")
        #                         if User.objects.filter(Q(citizen=country) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).exists():
        #                             get_user = User.objects.get(Q(citizen=country) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).distinct() 
        #                             location = get_user
        #                             name_search.append({"id": country.id, "person": location})
        #                     else:
        #                         age_list = agerange.split("-")
        #                         if User.objects.filter(Q(citizen=country) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).exists():
        #                             get_user = User.objects.get(Q(citizen=country) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).distinct()
        #                             location = get_user
        #                             name_search.append({"id": country.id, "person": location})
        #     else:
        #         agerange = request.GET.get('age', "")
        #         gender = request.GET.get('gender', "")
        #         result = User.objects.filter(username__iexact=captalizedValue).exists()
        #         users = User.objects.all()
        #         if result == True:
        #             if len(agerange) == 0 and len(gender) == 0:
        #                 if User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies)).exists():
        #                     user_id = User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies)).distinct()
                            
        #                     return JsonResponse([user_i.serialize() for user_i in user_id], safe=False)
        #             elif len(agerange) == 0 or agerange == None:
        #                 if User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).exists():
        #                     user_id = User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).distinct()
        #                     return JsonResponse([user_i.serialize() for user_i in user_id], safe=False)
        #             elif len(gender) == 0 or gender == None:
        #                 age_list = agerange.split("-")
        #                 if User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).exists():
        #                     user_id = User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).distinct() 
        #                     return JsonResponse([user_i.serialize() for user_i in user_id], safe=False)
        #             else:
        #                 age_list = agerange.split("-")
        #                 if User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).exists():
        #                     user_id = User.objects.filter(Q(username__iexact=captalizedValue) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).distinct()
        #                     return JsonResponse([user_i.serialize() for user_i in user_id], safe=False)   
        #         else:
        #             for user in users.iterator():
        #                 if value.lower() in user.username.lower(): 
        #                     if len(agerange) == 0 and len(gender) == 0:
        #                         if User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies)).exists():
        #                             user_result = User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies)).distinct()[0]
        #                             name_search.append({"id": user_result.id, "username": user_result.username, "userImage": user_result.userImage.url})
        #                             print('female')
        #                             print(agerange)
        #                     elif len(agerange) == 0 or agerange == None:
        #                         if User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).exists():
        #                             user_result = User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies) & Q(gender=gender)).distinct()[0]
        #                             name_search.append({"id": user_result.id, "username": user_result.username, "userImage": user_result.userImage.url})
        #                     elif len(gender) == 0 or gender == None:
        #                         age_list = agerange.split("-")
        #                         if User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).exists():
        #                             user_result = User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1])))).distinct()[0]
        #                             name_search.append({"id": user_result.id, "username": user_result.username, "userImage": user_result.userImage.url})
        #                     else:
        #                         age_list = agerange.split("-")
        #                         if User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).exists():
        #                             user_result = User.objects.filter(Q(username__iexact=user.username) & Q(hobbysist__in=user_hobbies) & Q(age__range=(int(age_list[0]), int(age_list[1]))) & Q(gender=gender)).distinct()[0]
        #                             name_search.append({"id": user_result.id, "username": user_result.username, "userImage": user_result.userImage.url})
        #     if len(name_search) == 0:
        #         return JsonResponse({"person":"false"})
        #     else:
        #         print(name_search)
        #         return JsonResponse(name_search, safe=False) 


    # value = request.GET['q']
    # entry_items = util.list_entries()
    # results = []
    # entries = []
    # for entry_item in entry_items:
    #     case_insestive = entry_item.lower()
    #     entries.append(case_insestive)

    # if value.lower() in entries:
    #     return HttpResponseRedirect(reverse("display", kwargs={'title': value }))

    # else:
    #     for entry in entries:
    #         if value.lower() in entry:
    #             results.append(entry)
    #     if len(results) == 0:
    #         message = "Sorry! Page doesn't exist"
    #         code = 400
    #         return util.errorMessage(request, code, message)
    #     else:
    #         return render(request, "encyclopedia/searchResult.html", {
    #         "results": results,
    #         "navlink1": "activate"
    #     })