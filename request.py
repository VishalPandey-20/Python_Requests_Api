
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