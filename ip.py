
from random import *
import subprocess,os,threading,time
from queue import Queue
lock=threading.Lock()
_start=time.time()
list=[]

#dict de ip

global locuri,alin
locuri=[]
alin={}
with open("ramn_demo.txt","r") as f:
   for line in f:
       (nr_crt,ramn,loc) = line.split(':')
       locuri.append(loc[0:len(loc)-1])
       alin[loc[0:len(loc) - 1]] = ramn



global d,dict_ip_loc
d = {}
dict_ip_loc={}

with open("ip_demo.txt") as f:
    for line in f:
        (ip, nume,loc) = line.split(":")
        d[int(ip)] = nume
        dict_ip_loc[int(ip)] = loc[0:len(loc)-1]





def afis(alin,nume,sir_ip,sir_ip_negasite):
   #if len(sir_ip) > 0:
   if sir_ip != "...(0)...":
       
       
       print ("<div  style='text-align: justify;margin-bottom: 3px;border:1px solid black;margin-left: "+str(alin*30)+"px'>")
       print("<font color='black'>"+nume+ ""+sir_ip +   "</font>")
       

       if sir_ip_negasite != "...(0)...":
            # print ("<style='margin-left: 30px'>")
            print("<font color='grey '>" + "" + sir_ip_negasite + "</font>")
       print ("</div>")

   else:
       
       print ("<div alingn='justify' style='text-align: justify;margin-bottom: 3px;border:1px solid red;margin-left: "+str(alin*30)+"px'>")
       print("<font color='red'>" + nume + ""+ sir_ip + "</font>")
       
       if sir_ip_negasite != "...(0)...":
            # print ("<style='margin-left: 30px'>")
            print("<font color='grey '>" + "" + sir_ip_negasite + "</font>")
       print ("</div>")

def caut(olista,list):
  nr=0
  nr_negasite=0
  vv = ""
  sir_ip_negasite = ""
  nr_gasite=0
  for x in olista:

      if ("192.168.0." + str(x)) in list:
          # print("192.168.0." + str(x))
          #vv = vv + str(x) + ">"+(d[int(x)]).lower()+ ","
          nr = nr + 1
          if int(x) in d:
            vv = vv + str(x) + ">"+(d[int(x)]).lower()+ ", "  #apare si info
            #vv = vv + str(x) + ","

          else:
              vv = vv + str(x) + ",====NU APARE niciodata====="
          #nr_gasite=nr_gasite+1
          #else:
           # pass
      else:
          nr_negasite=nr_negasite+1
          sir_ip_negasite+=str(x) + ">"+(d[int(x)]).lower()+ ", "
          # pass

  vv="...("+str(nr)+")..."+vv
  sir_ip_negasite = "...(" + str(nr_negasite) + ")..." + sir_ip_negasite

  #vv="("+str(nr_gasite)+"/"+str(len(olista))+") "+vv
  return vv,sir_ip_negasite

def check(n):
 with open(os.devnull, "wb") as limbo:
             ip="192.168.0.{0}".format(n)
             result=subprocess.Popen(["ping", "-n", "1", "-w", "300", ip],shell=True,stdout=limbo, stderr=limbo).wait()
             with lock:
                 if not result:
                     # print (ip, "active")
                     list.append(ip)

                 else:
                     pass

def threader():
 while True:
     worker=q.get()
     check(worker)
     q.task_done()
q=Queue()


#for tim in range(10):
for x in range(255):
 t=threading.Thread(target=threader)
 t.daemon=True
 t.start()
for worker in range(1,255):
 q.put(worker)
q.join()

list.sort()
for x in range(0,255):
  if ("192.168.0." + str(x)) in list:
      # print("192.168.0." + str(x))
      pass



#print("<html>")
#print ("<body>")
#print ("<h1  ><font color='BLUE'>Hello World</font></h1")
#print ("</body>")
#print ("</html>")


# print("<br>")
# cpu=["53","76","135","143","237"]
# sir_ip=caut(cpu,list)
# nume="Cpu"
# afis(nume,sir_ip)


#print("<br>")

lista_loc=[]
#=============

# print ("<div alingn='justify' style='margin-bottom: 3px;border:1px solid black;margin-left: "+str(alin*30)+"px'>")
# print("salut")
# print("<br>")
print ("<div alingn='justify' style='background-color:lightblue;margin-bottom: 3px'>")
print("<b>Arborescenta Ip-uri. Scanare realizata in: ",str(time.time()-_start)[0:4]," secunde","la ora",time.strftime("%H:%M:%S"),". Numar generat aleator: ",randint(1, 255) , "</b><br>")
print ("</div>")
# print (time.strftime("%H:%M:%S"))

# v1=randint(1, 255)
# print('<br>',randint(1, 255))
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
# Wait for 5 seconds
#time.sleep(6)
# print("/<table>")


for x in locuri:
    # print("<br>")
    #print(len(alin.get(x)))
    #for a in range(len(alin.get(x))-1):
    # print("<tr>")
    # print("<td >")

    # print("............"*(len(alin.get(x))-1))  ///asta era inainte
    # print("<td></td>" * (len(alin.get(x)) - 1))

    lista_loc.clear()
    for ip,loc in dict_ip_loc.items():
        if loc == x:
            lista_loc.append(ip)
    #print (lista_loc)

    sir_ip,sir_ip_negasite=caut(lista_loc,list)
    nume=(x.upper())
    lung_alineat=len(alin.get(x))-1

    afis(lung_alineat,nume,sir_ip,sir_ip_negasite)
    # print("</tr>")
    # print("</td>")


