
import json



with open('db.json', 'r') as file:
    data = json.load(file)

def is_task_completed(email, project_name, subject_name, task_name, data) :
    for dict_ in data["PomodorosApp"]["Users"]:
       if dict_["Email"]==email:
           for dict_2 in dict_["Projects"]:
               if dict_2["ProjectName"]==project_name:
                   for dict_3 in dict_2["Subjects"]:
                       if dict_3["SubjectName"]==subject_name:
                           for dict_4 in dict_3["PomodoroSessions"]:
                              for dict_5 in dict_4["Tasks"]:
                                  if dict_5["TaskName"]==task_name:
                                      return dict_5["Completed"]
                           raise Exception("Task not found")
                   




print(is_task_completed("ramy@ramy.nl","Project01"  , "Subject01", "Task02", data))

