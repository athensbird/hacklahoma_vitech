
import json
import csv
from urllib.request import urlopen
t={}
count =1
x=300001
y=400000
data=open('C:/Users/VGK/Desktop/great/partic_new_300000.csv', 'a',encoding="utf-8")
while(y<600003):
   var=('https://v3v10.vitechinc.com/solr/v_us_participant/select?indent=on&q=id:[%d%%20TO%%20%d]&rows=100000&wt=json'% (x ,y))

   connection = urlopen(var)



   response =json.load(connection)
   print(x)





   t=response['response']['docs']

   writ=csv.writer(data)



   for a in t:
      if (count==0):
        writ.writerow(a.keys())
        count=1

      writ.writerow(a.values())

   x=y+1
   y=y+100000
print("done")









