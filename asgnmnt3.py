courses = {'python': 1500, 'java': 1000, 'c': 800, 'c++': 1200}
sorted_lib = sorted((value,key) for (key,value) in courses.items())
course={}
for i in sorted_lib:
    course[i[1]]=i[0]
print("courses = ",course)
