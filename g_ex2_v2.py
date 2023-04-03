from operator import itemgetter
import datetime
import csv

RUN = True
FILE = 's_list.txt'
HELP = '''
Available commands:
/show <date>    - show all tasks for date (first 10 if date is empty)
/add            - add new task
/del            - del task by ID
/clear <date>   - dell all tasks for 1 day (del all tasks if date is empty)
/HELP           - show all available commands
/exit           - stop programm\n
'''
#[(1,'2023-03-30','15:30','Test task n1','N','','ToDo/Done')]

#1,2023-03-30,15:30,Test task n1,N,,ToDo
#2,2023-03-31,08:30,Test task n2,N,,ToDo

list_tasks = []
f_list_tasks = open(FILE, 'r')
for str in f_list_tasks :
    list_tasks.append(tuple(str.replace('\n','').split(',')))
f_list_tasks.close()
list_tasks.sort(key=itemgetter(0))
max_task_in_file = int(list_tasks[-1][0])
changed = False


def check_date(msg) :
    date_format = '%Y-%m-%d'
    date_loop = True
    while date_loop :
        t_date_in = input(msg)
        try:
            dateObject = datetime.datetime.strptime(t_date_in, date_format)
            date_loop = False
        except ValueError:
            print('It\'s not correct date!')
    return t_date_in


def check_time(msg) :
    time_loop = True
    while time_loop :
        t_time_in = input(msg)
        try :
            hh = int(t_time_in[0:2])
            mm = int(t_time_in[3:5])
            if hh < 25 and mm < 60  and t_time_in[2] ==':':
                time_loop = False
            else :
                print('It\'s not correct time!')
        except ValueError:
            print('It\'s not correct time!')
    return t_time_in


def add_task() :
    global max_task_in_file, list_tasks, changed
    max_task_in_file +=1
    t_id = max_task_in_file
    t_date = check_date('Input date (YYYY-MM-DD): ')
    t_time = check_time('Input task time (HH:MM): ')
    t_text = input('Input Task: ')
    t_not = input('Need notification? (input Y or N): ')
    if t_not == 'Y' :
        t_time_not = check_time('Input notification time (HH:MM): ')
    else :
        t_time_not = ''
    t_status = 'ToDo'
    list_tasks.append(tuple((t_id,t_date,t_time,t_text,t_not,t_time_not,t_status)))
    changed = True
    
        
def show(cur_command_in) :
    global list_tasks
    if cur_command == '/show' :
        print(list_tasks)
    else :
        p_date_in = cur_command[cur_command.find(' ')+1:len(cur_command)]
        list_tasks_filtred = filter(lambda t: (t[1] == p_date_in) , list_tasks)
        print(list(list_tasks_filtred))


def save_list_tasks() :
    global list_tasks, changed
    if changed :
        with open(FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(list_tasks)


while RUN :
    cur_command = input('Input command pls:\n')
    if cur_command == '/exit' :
        save_list_tasks()
        RUN = False
    elif cur_command.find('/show') > -1 : #cur_command == '/show' :
        show(cur_command)
    elif cur_command == '/HELP' :
        print(HELP)
    elif cur_command == '/add' :
        add_task()
    else :
        print('\nWrong command!!!\nUse /HELP for show list_tasks of available comands.\n')


print('\nBye!!!')