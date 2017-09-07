# -*- coding: utf-8 -*-
"""
Created on Fri Sep 01 15:24:04 2017

@author: Aditi
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

files = {'./sustainmentaveragessimpsonsdrought.csv',
         './sustainmentaveragessimpsonsFree_Play_Session.csv',
         './sustainmentaveragessimpsonsEasy_Session.csv',
         './sustainmentaverageslv4drought.csv',
         './sustainmentaverageslv4Free_Play_Session.csv',
         './sustainmentaverageslv4Easy_Session.csv'}
for single_file in files:         
    mode=[]
    with open(single_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        values = list(readCSV)
        i=0
        mode.append(np.arange(12))
        for modes in values:
            popped = modes.pop(0)
            if(i>0):
                temp = [float(x) for x in modes]
                mode.append(temp)        
            i=i+1
    print single_file,",",mode[6]        
    fig, ax = plt.subplots()
    plt.plot([],[],color='dodgerblue', label='0', linewidth=5)
    plt.plot([],[],color='darkorchid', label='1', linewidth=5)
    plt.plot([],[],color='crimson', label='2', linewidth=5)
    plt.plot([],[],color='orange', label='3', linewidth=5)
    plt.plot([],[],color='darkgreen', label='4', linewidth=5)
    plt.plot([],[],color='lime', label='WF', linewidth=5)
    plt.plot([],[],color='navy', label='TC', linewidth=5)
    plt.plot([],[],color='deeppink', label='TU', linewidth=5)

    fig.subplots_adjust(right=0.70)
    axes = [ax, ax.twinx(), ax.twinx(),ax.twinx()]

    # Move the last y-axis spine over to the right by 20% of the width of the axes
    axes[-1].spines['right'].set_position(('axes', 1))
    axes[-2].spines['right'].set_position(('axes', 1.15))
    axes[-3].spines['right'].set_position(('axes',1.30))

    # To make the border of the right-most axis visible, we need to turn the frame
    # on. This hides the other plots, however, so we need to turn its fill off.
    axes[-1].set_frame_on(True)
    axes[-1].patch.set_visible(False)
    ax.stackplot(mode[0],mode[1],mode[2],mode[3],mode[4]
                ,mode[5]
                ,colors=('dodgerblue','darkorchid','crimson','orange','darkgreen'), edgecolor ='face')
    handles, labels = ax.get_legend_handles_labels()
    axes[0].set_ylabel('Average span durations(minutes)')
    axes[1].plot(mode[0],mode[6],color='lime', linewidth =2)
    axes[1].set_ylabel('Average waterfall water')
    axes[2].plot(mode[0],mode[7],color='navy', linewidth = 2)
    axes[2].set_ylabel('Average Total Clouds')
    axes[3].plot(mode[0],mode[8],color='deeppink', linewidth =2)
    axes[3].set_ylabel('Average Total Users')
#    axes[0].set_xlabel('Minutes')
    plt.title('Span durations and Modes')
    lgd = ax.legend(bbox_to_anchor=(0.5, -0.05), loc='upper center',
            ncol=2,mode="expand", borderaxespad=0.)
    plt.show()
    figurename= single_file.split(".csv")
    figurename = str(figurename[0])+".png"
    fig.savefig(figurename, bbox_extra_artists=(lgd,), bbox_inches='tight')

