import datetime
import uuid
class Task():
    #ceating a list of tasks to hold all tasks
    TaskList =[]
    def __init__(self) -> None:
        self.task=''
        self.created_time = None 
        self.updated_time = None
        self.completed_time = None
        self.task_done = False
        self.Id = None
    #create task function will create each individual task
    def create_task(self, task):
        self.tasks=dict() # this dictionary hold all the info of a task together then send to tasklist
        self.Id = uuid.uuid4()
        self.task_done=False
        self.task=task
        self.created_time=datetime.datetime.now()
        self.updated_time=None
        self.completed_time=None
        self.tasks["Id"]=self.Id
        self.tasks["task_done"]=self.task_done  
        self.tasks["task"]=self.task
        self.tasks["created_time"] = self.created_time
        self.tasks["updated_time"] = self.updated_time
        self.tasks["completed_time"] = self.completed_time
        self.TaskList.append(self.tasks)

    
    def update_task(self,tNO):
        for t in range(0,len(self.TaskList)):
            if(t==tNO-1):
                if(self.TaskList[t]["task_done"]==False):
                    self.TaskList[t]["task"] = input("Enter New Task : ")
                    self.TaskList[t]["updated_time"] = datetime.datetime.now()
                    print("\n Task Updated Successfully\n")
                else:
                    print("Sorry!, This task is already Completed\n")
                

    def complete_task(self, tN):
        for t in range(0,len(self.TaskList)):
            if(t==tN-1):
                if(self.TaskList[t]["task_done"]==False):
                    self.TaskList[t]["task_done"] = True
                    self.TaskList[t]["completed_time"] = datetime.datetime.now()
                    print("\n Task Completed Successfully\n")
                else:
                    print("Sorry! ,This task is already Completed\n")

    #this method is to showing all the task. I have to show all task multiple time that's why I'm creating this method
    def Show_task(self):
        for i in self.TaskList:
            print(f"\nID- {i['Id']} \nTask - {i['task']} \nCreated time - {i['created_time']} \nUpdated time - {i['updated_time']} \nCompleted - {i['task_done']} \nCompleted Time- {i['completed_time']}\n")

# calling Task class
t = Task()


print("1. Add new Task \n")
print("2. Show All Tasks \n")
print("3. Show Incomplete Tasks\n")
print("4. Show Complete Tasks \n")
print("5. Update Task \n")
print("6. Mark A Task Completed\n")
print("7. press 7 to exist\n")
option = int(input("Enter Option: "))
while(option != 7):
    if(option==1):
        op = input("Enter New Task: ")
        t.create_task(op) #creating new task
        print("\nTask Created Successfully\n")

    elif(option==2):
        print("\nAll tasks are: ")
        t.Show_task()
        
    elif(option==3):
        if(len(t.TaskList)==0):
            print("There is no task \n") # if tasklist is empty then it will show this message
        else:
            c=0
            print("\nIncomplete tasks are: ")
            for task in t.TaskList:
                if(task['task_done']==False):
                    c +=1
                    print(f"\nID- {task['Id']} \nTask - {task['task']} \nCreated time - {task['created_time']} \nUpdated time - {task['updated_time']} \nCompleted - {task['task_done']} \nCompleted Time- {task['completed_time']}\n")
            if(c==0):
                print("There is no incomplete task") # if all task is complete then this message will be shown

    elif(option==4):
        cc=0
        for task in t.TaskList:
            if(task['task_done']==True):
                cc +=1
                print(f"\nID- {task['Id']} \nTask - {task['task']} \nCreated time - {task['created_time']} \nUpdated time - {task['updated_time']} \nCompleted - {task['task_done']} \nCompleted Time- {task['completed_time']}\n")
        if(cc==0):
            print("No completed task\n")

    elif(option==5):
        print("\nSelect Which Task to Update\n")
        con=0;
        for task in t.TaskList:
            con +=1
            print("Task NO - ",con)
            print(f"ID- {task['Id']} \nTask - {task['task']} \nCreated time - {task['created_time']} \nUpdated time - {task['updated_time']} \nCompleted - {task['task_done']} \nCompleted Time- {task['completed_time']}\n")
        
        taskNo = int(input("Enter Task Number : "))
        t.update_task(taskNo)

    elif (option == 6):
        print("\nSelect Which Task to Complete\n")
        con=0;
        for task in t.TaskList:
            con +=1
            print("Task NO - ",con)
            print(f"ID- {task['Id']} \nTask - {task['task']} \nCreated time - {task['created_time']} \nUpdated time - {task['updated_time']} \nCompleted - {task['task_done']} \nCompleted Time- {task['completed_time']}\n")
        
        taskNo = int(input("Enter Task Number : "))
        t.complete_task(taskNo)

    print("1. Add new Task \n")
    print("2. Show All Tasks \n")
    print("3. Show Incomplete Tasks\n")
    print("4. Show Complete Tasks \n")
    print("5. Update Task \n")
    print("6. Mark A Task Completed\n")
    print("7. press 7 to exist\n")
    option = int(input("Enter Option: "))
    



