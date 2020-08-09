import requests,json,os
data=requests.get('http://saral.navgurukul.org/api/courses').json()
# print("vishal",data)
# with open("vish.json","w") as vishal:
#     json.dump(data['availableCourses'],vishal)
#     print('successful')

def api():
    with open("vishal.json","r") as pandit:
        data=json.load(pandit)
        # print("data",data)
# api()
        list1=[]
        n=1
        print("total courses")
        for content in data:
            user={}
            # print("content",content)
                    
            print(n,content['name'])
            n+=1
            # print(content['id'])
            id=content["id"]   
            user["id"]=id 
            list1.append(user)
        # print(list1)
        user=int(input('enter'))
        # print(list1[user-1])
        # print(list1[user-1]["id"]) 
        print('http://saral.navgurukul.org/api/courses/'+list1[user-1]["id"]+'/exercises'+'-'+content['name'])

if os.path.isfile("vishal.json"):
    api()

else:
    data=requests.get('http://saral.navgurukul.org/api/courses').json()
    with open('vishal.json','w') as pandit: 
        json.dump(data['availableCourses'],pandit)

    api()