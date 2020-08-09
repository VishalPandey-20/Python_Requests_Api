import requests,json,os,pprint
list_id=[]
courses_Id = 0
exercise_slug = " "
list_slug=[]
def new_fun():
    with open("pandit.json","r") as file:
        data=json.load(file)
        # print(data)
        n=1
        for value in data:
            list_id.append(value['id'])
            print(n,value['name'])
            n+=1
        user_input("exercises")
def exercises(exe_id):
    # global courses_Id
    courses_Id = exe_id
    print("id of course.",exe_id)
    req=requests.get("http://saral.navgurukul.org/api/courses/"+exe_id+"/exercises").json()
    # print(req['data'])
    n1=1
    for i in req['data']:
        
        list_slug.append(i['slug'])

        print(n1,i['name'])
        n1+=1
    print(i['slug'])
    user_input("slug")


def slug_id(ex_slug):
    exercise_slug = ex_slug
    print("slug",ex_slug)
    sec_req=requests.get("http://saral.navgurukul.org/api/courses/"+str(courses_Id)+"/exercise/getBySlug?slug="+ex_slug).json()
    print(sec_req)
    print(sec_req['content'])



def user_input(quri):
    user=int(input("enter the number of "+quri+" id..."))

    if quri=="exercises":
        exercises(list_id[user-1])
    elif quri=="slug":
        slug_id(list_slug[user-1])



if os.path.isfile("pandit.json"):
    new_fun()
else:
    data=requests.get("http://saral.navgurukul.org/api/courses").json()
    with open("pandit.json","w") as file:
        json.dump(data['availableCourses'],file)
    new_fun()
    # print(data['availableCourses'])

