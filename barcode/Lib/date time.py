import datetime

attendace =["wole","oye"]
attendToday=[]
attend=[]

i="wole"

if i in attendace :
    if i not in attend:
        t={}
        t["name"]="wole"
        t["time"]= datetime.datetime.now().strftime("%X")
        t["day"]= datetime.datetime.now().strftime("%A")
        t["date"]=datetime.datetime.now().strftime("%d")+" "+datetime.datetime.now().strftime("%B")
        attendToday.append(t)
        attend.append(i)
        try:        
            f = open(f"attend{t['date']}.txt", "x")
            f.write("name,time,day,\n")
        except:        
            f = open(f"attend{t['date']}.txt", "a")        
        finally:
            f.write(f'{t["name"]},{t["time"]},{t["day"]}')
            f.write("\n")
            f.close()
        
        
    
print(attendToday,attend)      
