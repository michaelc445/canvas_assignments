import requests,json
from datetime import datetime

courses =  {"Information storage and management 1":36855,
            "Logic Design":36889,
            "Operating systems 1":36893,
            "Computer Architecture":36910,
            "Intermediate Programming":36930,
            "Algorithms and data structures":36938
            }

def get_assignment_for_course(course_id):
    url = "https://ucc.instructure.com/api/v1/courses/"+str(course_id)+"/assignments"
    token = "token can be created on your canvas profile -> settings -> new access token"
    headers = {'Authorization': 'Bearer '+ token}
    response = requests.get(url,headers=headers).json()
    assignments = ""
    now = datetime.now()
    for item in response:
        due_at = None
        lock_at = None
        if item["name"] is not None:
            if item["due_at"] is not None:
                due_at = str2time(item["due_at"])
            if item["lock_at"] is not None:
                lock_at = str2time(item["lock_at"])
            if due_at is not None and due_at > now:
                assignments += "%s\nPoints Possible: %s\nDue at: %s\nLock at: %s\nTime left: %s\n"%(item["name"],item["points_possible"],str(due_at),str(lock_at),time_left(due_at))
            elif lock_at is not None and lock_at > now:
                assignments += "%s\nPoints Possible: %s\nDue at: %s\nLock at: %s\nTime left: %s\n"%(item["name"],item["points_possible"],str(due_at),str(lock_at),time_left(lock_at))                
    
    if assignments == "":
        return None
    return assignments

def str2time(string):
    time = string.replace("Z","")
    date_time = time.split("T")
    assignment_date = date_time[0].split("-")
    assignment_time =date_time[1].split(":")
    return datetime(int(assignment_date[0]),int(assignment_date[1]),int(assignment_date[2]),int(assignment_time[0]),int(assignment_time[1]),int(assignment_time[2]))

def time_left(date_time_due):
    now = datetime.now()
    difference = date_time_due-now
    left_str = str(difference)
    time_list = left_str.split(" ")
    if "days," in time_list or "day," in time_list:
        days = time_list[0]
        time = time_list[2].split(":")
        hours = time[0]
        mins = time[1]
        return "Days: %s, Hours: %s, Minutes: %s"%(days,hours,mins)
    else:
        days = 0
        time = time_list[0].split(":")
        hours = time[0]
        mins = time[1]
        return "Days: %d, Hours: %s, Minutes: %s"%(days,hours,mins)

def get_all_assignments(course_dict):
    result_str = ""
    for course in course_dict:
        result = get_assignment_for_course(course_dict[course])
        if result is not None:
            result_str += course+"\n"+result+"\n"
            print(course)
            print(result) 
    outfile = open("assignment.txt",'w')
    outfile.write(result_str)
    outfile.close()
    return result_str

if __name__ == "__main__":
    get_all_assignments(courses)
    #get_assignment_for_course(36910)
