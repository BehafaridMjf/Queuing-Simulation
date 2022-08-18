EL = [["Time","Customer", "Departure", "Customer", "Arrival"]]
import numpy as np
import matplotlib.pyplot as plt
servicetime1_list = []
servicetime2_list = []
servicetime3_list = []
servicetime4_list = []
servicetime5_list = []
def Remove(nextdepartures):
    final_list = []
    for num in nextdepartures:
        if num not in final_list:
            final_list.append(num)
    return final_list
print("choose your policy")
print("1.RR")
print("2.LIR")
print("3.SIR")
print("4.LTIR")
nb = input('Choose policy: ')
runtime = input('Enter Runtime: ')
coldtimezero=input('coldtime: ')
coldtime = int(coldtimezero)
policy=int(nb)
r=int(runtime)
print("do you need chart?")
chart = input("write yes if you need a chart and write no if you don't")
if chart == "yes":
    r=1
percentage_list =[]
servicetime_list=[]
percentageaftercoldtime_list=[]
for r in range (0,r):
  FEL = [["Time",  "Future Departures", "Customer", "Arrival"]]
  NewFEL = [["Time", "Customer", "Departure", "Customer", "Arrival"]]
  Departure = []
  arrivaltimes = []
  moshtariha=0
  server = []
  mean_service = []
  serveraftercoldtime=[]
  server1aftercoldtime=[]
  server2aftercoldtime=[]
  server3aftercoldtime=[]
  server4aftercoldtime=[]
  server5aftercoldtime=[]
  std_service = []
  servicetime = 1
  serverchosen = 10
  servicetime1 = 0
  servicetime2 = 0
  servicetime3 = 0
  servicetime4 = 0
  servicetime5 = 0
  arrival = 0
  f = []
  Departureserver=[]
  addedFEL = []
  arrivaltimes.append(arrival)
  i = 0
  Time = 0
  X = np.array([0, 0, 0, 0, 0])
  servers = np.array([0, 0, 0, 0, 0])
  b = 0
  print("******************",r,"******")
  server1=[]
  Departureserver1=[1,0]
  Departureserver2=[2,0]
  Departureserver3=[3,0]
  Departureserver4=[4,0]
  Departureserver5=[5,0]
  server2=[]
  server3=[]
  server4=[]
  server5=[]
  nextdepartures=[]
  percentserver1_list=[]
  percentserver2_list = []
  percentserver3_list = []
  percentserver4_list = []
  percentserver5_list = []
  servicetime1_list = []
  servicetime2_list = []
  servicetime3_list = []
  servicetime4_list = []
  servicetime5_list = []
  x=[]
  while Time <20:
      servicetime = 1
      print(servicetime)
      if chart == "yes":
          v=server
          x.append(Time)
          if Time == 0:
              percentserver1_list.append([0])
              percentserver2_list.append([0])
              percentserver3_list.append([0])
              percentserver4_list.append([0])
              percentserver5_list.append([0])
          if Time != 0:
              get_indexes = lambda v, vs: [i for (g, i) in zip(vs, range(len(vs))) if v == g]
              server1 = (get_indexes(1, v))
              server1customers = len(server1)
              server2 = (get_indexes(2, v))
              server2customers = len(server2)
              server3 = (get_indexes(3, v))
              server3customers = len(server3)
              server4 = (get_indexes(4, v))
              server4customers = len(server4)
              server5 = (get_indexes(5, v))
              server5customers = len(server5)
              moshtariha = (get_indexes(0, v))
              percentserver1 = server1customers / (len(server) - len(moshtariha)) * 100
              percentserver2 = server2customers / (len(server) - len(moshtariha)) * 100
              percentserver3 = server3customers / (len(server) - len(moshtariha)) * 100
              percentserver4 = server4customers / (len(server) - len(moshtariha)) * 100
              percentserver5 = server5customers / (len(server) - len(moshtariha)) * 100
              percentserver1_list.append([percentserver1])
              percentserver2_list.append([percentserver2])
              percentserver3_list.append([percentserver3])
              percentserver4_list.append([percentserver4])
              percentserver5_list.append([percentserver5])
      policy2 = []
      Departureserver = [Departureserver1, Departureserver2, Departureserver3, Departureserver4, Departureserver5]
      i += 1
      if Time > Departureserver1[1]:
              p = Departureserver1[0]-1
              servers[p] = 0
      if Time > Departureserver2[1]:
              p = Departureserver2[0]-1
              servers[p] = 0
      if Time > Departureserver3[1]:
              p = Departureserver3[0]-1
              servers[p] = 0
      if Time > Departureserver4[1]:
              p = Departureserver4[0]-1
              servers[p] = 0
      if Time > Departureserver5[1]:
              p = Departureserver5[0]-1
              servers[p] = 0
      print("**Customre number**",i,"arrives")
      print("time is",Time)
      interarrivaltime = np.random.exponential(3.3)
      arrival = arrival + interarrivaltime
      arrivaltimes.append(arrival)
      print("next arrival is",arrival)
      print(nextdepartures)
      if i > 1:
          addedFEL = [Time, nextdepartures, i+1, arrival]
          print(addedFEL)
          FEL = np.vstack([FEL, addedFEL])
      X = servers
      get_indexes = lambda X, Xs: [i for (y, i) in zip(Xs, range(len(Xs))) if X == y]
      idleservers = (get_indexes(0 , X))
      new_idleservers = [X + 1 for X in idleservers]
      print("idle servers are ",new_idleservers)
      if not new_idleservers:
         print("all servers are busy")
         servicetime = 0
         Departure.append(10000)
         server.append(0)
      print("Service time is",servicetime)
      if servicetime != 0:
       if policy == 2:
        for m in range (0,len(new_idleservers)):
            policy2.append(Departureserver[new_idleservers[m] - 1])
            serverchosen=min(policy2, key=lambda L: L[1])[0]
            m += 1
       if policy == 4 :
            serverchosen= min([[servicetime1,1],[servicetime2,2],[servicetime3,3],[servicetime4,4],[servicetime5,5]], key=lambda L:L[0])[1]
       if policy == 3:
        for m in range (0,len(new_idleservers)):
            policy2.append(Departureserver[new_idleservers[m] - 1])
            serverchosen=max(policy2, key=lambda L: L[1])[0]
            m += 1
       if policy == 1:
        serverchosen = np.random.choice(new_idleservers, 1 , replace=False)
       print("serverchosen is", serverchosen)
       server.append(serverchosen)
       if Time > coldtime :
         serveraftercoldtime.append(serverchosen)
       if serverchosen == 1:
         servicetime = np.random.exponential(6)
         if Time > coldtime:
            servicetime1=servicetime1+servicetime
         Departureserver1 = [1, arrivaltimes[i - 1] + servicetime]
       if serverchosen == 2:
         servicetime = np.random.exponential(8)
         if Time > coldtime :
            servicetime2=servicetime2+servicetime
         Departureserver2 =[ 2,arrivaltimes[i - 1] + servicetime]
       if serverchosen == 3:
         servicetime = np.random.exponential(10)
         if Time > coldtime :
            servicetime3=servicetime3+servicetime
         Departureserver3 = [3,arrivaltimes[i - 1] + servicetime]
       if serverchosen == 4:
         servicetime = np.random.exponential(12)
         if Time > coldtime :
            servicetime4=servicetime4+servicetime
         Departureserver4 = [4,arrivaltimes[i - 1] + servicetime]
       if serverchosen == 5:
         servicetime = np.random.exponential(14)
         if Time > coldtime :
           servicetime5=servicetime5+servicetime
         Departureserver5 = [5,arrivaltimes[i - 1] + servicetime]
       print("servicetime is", servicetime)
       Departuretime = arrivaltimes[i - 1] + servicetime
       print("Departure time is", Departuretime)
       Departure.append(Departuretime)
       w= serverchosen - 1
       servers[w] = 1
       print(servers)
       print(x)
       print("***************************************")
       if i == 1:
           addedFEL=[0,[Departure[0],1],2,arrival]
           FEL = np.vstack([FEL, addedFEL])
           nextdepartures.append([Departure[0],1])
           NewFEL.append([0, 0, 0, 0])
           NewFEL[1][0] = Time
           NewFEL[1][1] = [Departure[0],1]
           NewFEL[1][2] = 2
           NewFEL[1][3] = arrival
           addedFEL = NewFEL[1]
           FEL = np.vstack([FEL, addedFEL])
           if Departure[0] < NewFEL[1][3]:
            Time = NewFEL[1][1]
            d = server[0]
            servers[d - 1] = 0
            print("Customer", 1, "departured in time", Time)
            addedFEL = [Time, nextdepartures, 2, arrival]
            FEL = np.vstack([FEL, addedFEL])
            Time = arrivaltimes[1]
           if Departure[0] > NewFEL[1][3]:
            Time = arrivaltimes[1]
       if i>1 :
           for j in range(0, i):
               if Departure[j] > Time:
                   f = [Departure[j], j + 1]
                   nextdepartures.append(f)
                   nextdepartures = sorted(nextdepartures, key=lambda L: L[0])
               j += 1
           print(len(nextdepartures))
           if len(nextdepartures)!= 0:
             while (len(nextdepartures) != 0 ) and nextdepartures[0][0]< arrival:
                Time = nextdepartures[0][0]
                nextdepartures.pop(0)
                nextdepartures=Remove(nextdepartures)
                addedFEL = [Time, nextdepartures, i + 1, arrival]
                FEL = np.vstack([FEL, addedFEL])
           Time = arrival
           if Time < 20:
               print("Time is ", Time)
               print("Customer", i + 1, "arrives")
           if Time > 20:
               print("END")
      if servicetime == 0:
           print("Customer", i, "leaves!")
           Time = arrival
           if Time <20:
              print("Time is ", Time)
              print("Customer", i + 1, "arrives")
           if Time > 20:
              print("END")
  print(FEL)
  h=serveraftercoldtime
  get_indexes = lambda h, hs: [i for (y, i) in zip(hs, range(len(hs))) if h == y]
  server1aftercoldtime = (get_indexes(1, h))
  server1customersaftercoldtime=len(server1aftercoldtime)
  server2aftercoldtime = (get_indexes(2, h))
  server2customersaftercoldtime = len(server2aftercoldtime)
  server3aftercoldtime = (get_indexes(3, h))
  server3customersaftercoldtime = len(server3aftercoldtime)
  server4aftercoldtime = (get_indexes(4, h))
  server4customersaftercoldtime = len(server4aftercoldtime)
  server5aftercoldtime = (get_indexes(5, h))
  server5customersaftercoldtime = len(server5aftercoldtime)
  moshtarihaaftercoldtime = (get_indexes(0, h))
  if len(serveraftercoldtime) == 0 :
      percentserver1aftercoldtime_list.append([0])
      percentserver2aftercoldtime_list.append([0])
      percentserver3aftercoldtime_list.append([0])
      percentserver4aftercoldtime_list.append([0])
      percentserver5aftercoldtime_list.append([0])
  if len(serveraftercoldtime) != 0:
      percentserver1aftercoldtime = server1customersaftercoldtime / (len(serveraftercoldtime)- len(moshtarihaaftercoldtime))*100
      percentserver2aftercoldtime = server2customersaftercoldtime / (len(serveraftercoldtime)- len(moshtarihaaftercoldtime)) * 100
      percentserver3aftercoldtime = server3customersaftercoldtime / (len(serveraftercoldtime)- len(moshtarihaaftercoldtime)) * 100
      percentserver4aftercoldtime = server4customersaftercoldtime / (len(serveraftercoldtime)- len(moshtarihaaftercoldtime)) * 100
      percentserver5aftercoldtime = server5customersaftercoldtime /(len(serveraftercoldtime)- len(moshtarihaaftercoldtime)) * 100
      percentageaftercoldtime_list.append([percentserver1aftercoldtime,percentserver2aftercoldtime,percentserver3aftercoldtime,percentserver4aftercoldtime,percentserver5aftercoldtime])
  print("DARSADE KHEDMATDEHI",percentserver1aftercoldtime,percentserver2aftercoldtime,percentserver3aftercoldtime,percentserver4aftercoldtime,percentserver5aftercoldtime)
  servicetime_list.append([1000 - coldtime - servicetime1,1000 - coldtime - servicetime2,1000 - coldtime-servicetime3,1000 - coldtime - servicetime4,1000 - coldtime - servicetime5])
  r += 1
  if chart == "yes":
      print(percentserver1_list)
      print (x)
      plt.plot(x, percentserver1_list, label="Server1")
      plt.plot(x, percentserver2_list, label="Server2")
      plt.plot(x, percentserver3_list, label="Server3")
      plt.plot(x, percentserver4_list, label="Server4")
      plt.plot(x, percentserver5_list, label="Server5")
      plt.grid(True)
      plt.xticks(np.arange(0,1000,100))
      plt.xlabel("Time")
      plt.ylabel("Darsade khedmat dehi")
      plt.title("darsade khedmat dehie har server dar zaman")
      plt.legend()
      plt.show()


mean_service = np.mean(percentageaftercoldtime_list, axis=0)
mean_bikari = np.mean(servicetime_list, axis=0)
print("MEAN FOR SERVERS after coldtime", mean_service)
print ( "Mean for bikarie har server bade coldtime",mean_bikari)
std_service = np.std(percentageaftercoldtime_list, axis=0)
print("Standard deviasion for service",std_service)
std_bikari = np.std(servicetime_list, axis=0)
print("Standard deviasion for mean",std_bikari)
