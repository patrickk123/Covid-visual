import numpy as np
import matplotlib.pyplot as plt,mpld3
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animat
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import os
import matplotlib.dates
import matplotlib.dates as mdates
from datetime import datetime
import time

plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\Prateek Nautiyal\\Downloads\\ffmpeg-20200612-38737b3-win64-static\\ffmpeg-20200612-38737b3-win64-static\\bin\\ffmpeg.exe'
FFwriter = animat.FFMpegWriter(fps=4, extra_args=['-vcodec', 'libx264'])
stri='C:\\Users\\Prateek Nautiyal\\Downloads\\full_data (3).csv'
df=pd.read_csv(stri)
#ind =df.loc[(df['location']=="India")]
ind =df.loc[(df['location']=="India") & (df.date.between('2020-04-11', '2020-07-11'))]
print(df.head())
date= pd.to_datetime(ind['date'])
#date= pd.to_datetime(dtt)
print(len(date))
y_data=(ind['new_cases'])
y_ncase=(ind['total_deaths'])

d=[]
yd=[]
yn=[]

for i in date:
    d.append(i)
    
for i in y_data:
    yd.append(i)
for i in y_ncase:
    yn.append(i)
    
    
x=[]
y=[]
y_new=[]
#print(date)
fig, ax1 = plt.subplots()
#plt.xlabel('Date')
#plt.ylabel('Price')
ax1.legend(loc='upper right', frameon=True)
#ax1.text(loc='upper right', frameon=True)
print(plt.title('Live graph with matplotlib:India'))

def animate(i):
    try:
        if(i<=len(d)):
        
            if(i==0):
                pass
                
            if(i<len(d)):
                ax1.clear()
                #ax1.legend(loc='upper right', frameon=False)

            #count=count+1
            x.append(d[i])
            y.append(yd[i])
            y_new.append(yn[i])
           # td.append(y2t[i])
            #print(x[i])
            
            #td.append(y2t[i])
           
            ax1.plot(x, y,color='red',marker='.', markerfacecolor='red',label="new_cases per day",alpha=0.5,linestyle='dashdot')
            ax1.plot(x, y_new,color='blue',marker='.', markerfacecolor='blue',label="total_deaths--till now",alpha=0.5)
            ax1.legend(loc='upper left', frameon=False)
            #ax1.text(str(yd[i]), fontsize=15)
            #ax1.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)
            ax1.set_facecolor("wheat")
            
            plt.xlabel('Date')
            plt.ylabel('Cases')
            #print(xs[i])
            #print(ys[i])
            #print(y2s[i])
            plt.title('COVID-19 graph with matplotlib:India')
            plt.xticks(rotation=90)
            #ani = FuncAnimation(fig, animate, interval=1)
            
            #time.sleep(1/5)
            
            

    except:
        print("error occured:")
ani = FuncAnimation(fig, animate)
ani.save('C:\\Users\\Prateek Nautiyal\\AppData\\Local\\Programs\\Python\\Python37\\vedio\\mymoviedec.mp4', writer = FFwriter)

plt.show()
#ani.save('C:\\Users\\Prateek Nautiyal\\AppData\\Local\\Programs\\Python\\Python37\\vedio\\mymovief.mp4', writer = FFwriter)

