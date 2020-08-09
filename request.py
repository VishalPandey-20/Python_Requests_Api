# requde
# import requests,json
# res = requests.get('https://saral.navgurukul.org/api/courses').json()
# # data = res['availableCourses']
# print(res)

# json code
# with open("courses.json","w") as file:
#     json.dump(data,file)

# with open('courses.json',"r") as open:
#     new_data = json.load(open)
#     print(new_data)



# =======================

# import requests,json,pprint,os
# id_of_slug=[]
# list_slug=[]
# courses_Id=0
# exercise_slug=" "
# def open_file():
#     global open
#     n=1
#     with open("courses.json","r") as open:
#         new_data = json.load(open)
#         for i in new_data: 
#             id_of_slug.append(i['id']) 
#             print(n,i['name'])
#             n+=1

#         user_input("exercises")
# def exercise(ex_id):
#     print(ex_id)
# #     user_input("slug")

# # def slug(ex_slug):
# #     exercise_slug=ex_slug
# #     second_req=requests.get("http://saral.navgurukul.org/api/courses/"+str(courses_Id)+"/exercise/getBySlug?slug="+ex_slug).json()
# #     print(second_req["content"])
                          
# def user_input(quri):
#     user=int(input('enter any number of '+quri+' id'))

#     if quri == "exercises":
#         exercise(id_of_slug[user-1])
#     # elif quri == "slug":
#     #     slug(list_slug[user-1])


# if(os.path.isfile('courses.json')): 
#     open_file()
# else:
#     res = requests.get('https://saral.navgurukul.org/api/courses').json()
#     data = res['availableCourses']
#     with open("courses.json","w") as file:
#         json.dump(data,file)
#     open_file()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# import requests,json,pprint,os
# list1 = []
# # def exercise():

# def open_file():
#     global open
#     n=1
#     with open("courses.json","r") as open:
#         new_data = json.load(open)
#         for i in new_data:
#             user={}
#             print(n,i['name'])
#             user["no"]=n
#             a = i["name"]
#             user["name"]=a
#             b = i['id']
#             user['id']= b
            
        
#             # print(user)
#             list1.append(user)
#         # #     print(n,a)           
#             n+=1  
#         # print(list1)
#         user=int(input('enter any number of "id"..'))
#         obj_of_id=list1[user-1]["id"]
#         print("id of object",obj_of_id)
#         print(" http://saral.navgurukul.org/api/courses/"+obj_of_id+"/exercises",)
#         req=requests.get("http://saral.navgurukul.org/api/courses/"+obj_of_id+"/exercises").json()
#         # print(req)
        
#         data=req['data']
#         # # print(data)
#         emp_list=[]
#         n1=1
#         for a in data:
#             # print(a)
#             print(n1,a['name'])
#             n1+=1
#             user={}
#             slug=a['slug']
#             user["slug"]=slug
#             emp_list.append(user)
#         u=int(input("enter the number of slug.."))

#         print("slug",emp_list[u-1]["slug"])
#         print("http://saral.navgurukul.org/api/courses/"+obj_of_id+"/exercise/getBySlug?slug="+emp_list[u-1]["slug"])

#         second_req=requests.get("http://saral.navgurukul.org/api/courses/"+obj_of_id+"/exercise/getBySlug?slug="+emp_list[u-1]["slug"]).json()
#         print(second_req)
#         print(second_req["id"])
#         print("second_req",second_req["content"])


# if(os.path.isfile('courses.json')): 
#     open_file()
# else:
#     res = requests.get('https://saral.navgurukul.org/api/courses').json()
#     data = res['availableCourses']
#     with open("courses.json","w") as file:
#         json.dump(data,file)
#     open_file()




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...whats next...>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# import requests,json,pprint,os
# list1 = []
# def open_file():
#     data=r




# if(os.path.isfile('courses.json')): 
#     open_file()
# else:
#     res = requests.get('https://saral.navgurukul.org/api/courses').json()
#     data = res['availableCourses']
#     with open("courses.json","w") as file:
#         json.dump(data,file)
#     open_file()
  
# import json

# data = {}
# data['people'] = []
# data['people'].append({
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

#     print(data,end='')

# import json

# with open('data.txt') as json_file:
#     data = json.load(json_file)
# #     for p in data['people']:
# #         print(p)
# #         # print('Name: ' + p['name'])
# #         # print('Website: ' + p['website'])
# #         # print('From: ' + p['from'])
# #         # print('')


# #  from io import StringIO
# # >>> io = StringIO()
# # >>> json.dump(['streaming API'], io)
# # >>> io.getvalue()
# # '["streaming API"]


# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#@@...made by parkash bhai...@@#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


import requests,json,pprint,os
id_of_slug=[]
list_slug=[]
courses_Id=0
exercise_slug=" "
def open_file():
    global open
    n=1
    with open("courses.json","r") as open:
        new_data = json.load(open)
        for i in new_data: 
            id_of_slug.append(i['id']) 
            print(n,i['name'])
            n+=1

        user_input("exercises")
def exercise(ex_id):
    courses_Id = ex_id
    req=requests.get("http://saral.navgurukul.org/api/courses/"+ex_id+"/exercises").json()
    data=req['data']
    n1=1
    for a in data:
        list_slug.append(a['slug'])
        print(n1,a['name'])
        n1+=1
    user_input("slug")
def slug(ex_slug):
    exercise_slug=ex_slug
    second_req=requests.get("http://saral.navgurukul.org/api/courses/"+str(courses_Id)+"/exercise/getBySlug?slug="+ex_slug).json()
    print(second_req["content"])
                          
def user_input(quri):
    user=int(input('enter any number of '+quri+' id'))
    
    if quri == "exercises":
        exercise(id_of_slug[user-1])
    elif quri == "slug":
        slug(list_slug[user-1])


if(os.path.isfile('courses.json')): 7667414170
    open_file()
else:
    res = requests.get('https://saral.navgurukul.org/api/courses').json()
    data = res['availableCourses']
    with open("courses.json","w") as file:
        json.dump(data,file)
    open_file()