from datetime import datetime
from time import sleep
import sys,subprocess,os,pyautogui


d = {

"Monday":
    {
        1:"psp",2:"psp",3:"beee",4:"eng",5:"phy"
    },
"Tuesday":
    {
        1:"phy",2:"eng",3:"che",4:"beee",5:"mde"
    },
"Wednesday":
    {
        1:"phy",2:"beee",3:"che",4:"mde",5:"eng"
    },
"Thursday":
    {
        1:"che",2:"beee",3:"phy",4:"psp",5:"eng"
    },
"Friday":
    {
        1:"beee",2:"che",3:"mde",4:"psp",5:"psp"
    },
"Saturday":

    {
        1:"mde",2:"phy",3:"che",4:"eng",5:"mde"
    }
}

period_time=((9,35),(10,45),(11,40),(13,30),(14,25))
#period_time=((9,00),(10,00),(11,15),(12,15),(14,14))



link = {
    "eng":"https://meet.google.com/pbg-jzgy-ekm",
    "mde":"https://meet.google.com/phb-thzc-qid",
    "phy":"http://meet.google.com/gpm-domf-cyz",
    "che":"https://meet.google.com/noy-igcp-gda",
    "beee":"http://meet.google.com/xkx-sdir-biq",
    "psp":"https://meet.google.com/qro-nusg-cdi",
    None:None
}


#day
day=datetime.today().strftime('%A')

#Periods
period_curr=None
period_prev=None
period_next=None
period_num=1

#autojoin
autojoin=False

def join_class(name):
    
    if name == None:
        print("Class null")
        return
    os.system("firefox --P school "+link[name])
    sleep(1)
    pyautogui.hotkey("winright","2")
    sleep(3)
    pyautogui.hotkey("ctrl","d")
    pyautogui.hotkey("ctrl","e")
    sleep(2)
    pyautogui.moveTo(1270,635)
    pyautogui.click()


def update_class():

    #get the time
    now = datetime.now()
    ctime = (now.strftime("%H"), now.strftime("%M"))
    ch,cm = (int(now.strftime("%H")), int(now.strftime("%M")))
    global period_curr,period_prev,period_next,period_num

    for t in period_time:
        if ch <= t[0]:
            if cm <= t[1]:
                period_num = period_time.index(t)+1
                if period_num < 6:
                    period_next = d[day][period_num]
                else:
                    period_next = None
            else:
                period_num = period_time.index(t)+2 
                if period_num < 6:
                    period_next = d[day][period_num]
                else:
                    period_next = None

            if period_num-1 >= 1:
                period_curr = d[day][period_num-1]
            else:
                period_curr = None
            if period_num-2 >= 1:
                period_prev = d[day][period_num-2]
            else: 
                period_prev = None
            break
        else:
            pass    
            
def get_class():
    update_class()
    return period_prev,period_curr,period_next

def get_link(klass):
    return link[klass]

def loop():

    global period_num

    update_class()

    #get the time
    now = datetime.now()
    ctime = (now.strftime("%H"), now.strftime("%M"))
    ch,cm = (int(now.strftime("%H")), int(now.strftime("%M")))
    time_left=0
    
    #temp
    period_num=1
    ch,cm = 10,35

    if period_num < 6:
        ph,pm = period_time[period_num-1]
        if ph > ch:
            if pm > cm:
                time_left = cm - pm + (ph - ch) * 60
            else:
                time_left = (ph - ch) * 60 - (cm - pm)
        else:
            if pm < cm:
                time_left = cm - pm 
            elif pm > cm:
                time_left = pm - cm 
            else:
                print("working")
                if autojoin:
                    join_class(d[day][period_num])
                    period_num += 1
        print(time_left)
        sleep(time_left*60)
        loop()



#main
if __name__ == "__main__":
    args = sys.argv[1:]
    i=0
    while(i<len(args)):
        if args[i] in ("-h","--help"):
            print("Usage:\n\t--get_class\n\t--get_link <class>\n\t--get_curr_link\n\t--get_curr_class\n\t--get_next_class\n\t--get_prev_class\n\t--join_next_class")
        elif args[i] == "--get_link":
            print(get_link(args[i+1]))
            i+=1
        elif args[i] == "--get_class":
            print(get_class())
        elif args[i] == "--get_curr_class":
            print(get_class()[1])
        elif args[i] == "--get_next_class":
            print(get_class()[0])
        elif args[i] == "--get_prev_class":
            print(get_class()[2])
        elif args[i] == "--join_class":
            join_class(args[i+1])
            i+=1
        elif args[i] == "--join_next_class":
            join_class(get_class()[2])
        elif args[i] == "--loop":
            loop()
        else:
            print("invalid arg",args[i])

        i+=1



