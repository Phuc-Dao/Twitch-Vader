"""
Created on Oct 11, 2018
@author: Phuc Dao
"""
import time
from Socket import openSocket
from Start import joinRoom
#from Settings import RATE, CACHE
from Tools import getUser, getMessage, textAnalysis
from Socket import sendMessage

#PyQtGraph Setup
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys

#PyQtGraph Setup
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys

#graphics window pyqt instance to add plots too
win = pg.GraphicsWindow()
win.setWindowTitle('Twitch Disposition')
win.resize(800, 800)

#Adding 4 plots to graphics window with labels and formatting
p1 = win.addPlot(title="Net Sentiment")
p2 = win.addPlot(title="Neutrality")
win.nextRow()
p3 = win.addPlot(title="Negativity")
p4 = win.addPlot(title="Positivity")
p1.setYRange(-1.25, 1.25, padding=0)
p1.setLabel("bottom", "Chat")
p2.setYRange(-.25, 1.25, padding=0)
p2.setLabel("bottom", "Chat")
p3.setYRange(-1.25, .25, padding=0)
p3.setLabel("bottom", "Chat")
p4.setYRange(-.25, 1.25, padding=0)
p4.setLabel("bottom", "Chat")

#Initializing each of 4 graphs with numpy arrays of 20 0's
# data1 = np.random.normal(size=10)
data1 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
data2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
data3 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
data4 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

#Adding curve to plot instances
curve1 = p1.plot(data1)
curve2 = p2.plot(data2)
curve3 = p3.plot(data3)
curve4 = p4.plot(data4)

#chatCounter is the x axis that corresponds with chats analyzed
chatCounter = 0

#update function takes most recent sentiment analysis attributes and increments plot data
def update(net, neu, neg, pos, msgCacheLength):
    global data1, data2, data3, data4, curve1, curve2, curve3, curve4, chatCounter
    # data1[:-1] = data1[1:]  # shift data in the array one sample left
    data1 = np.roll(data1, -1) #shift data in the array one to the left
    data2 = np.roll(data2, -1) #shift data in the array one to the left
    data3 = np.roll(data3, -1) #shift data in the array one to the left
    data4 = np.roll(data4, -1) #shift data in the array one to the left
    data1[data1.shape[0] - 1] = net #replace oldest data point with new value, shape of an array is a tuple of integers giving the size of the array along each dimension. this is 1 dimension array
    data2[data2.shape[0] - 1] = neu
    data3[data3.shape[0] - 1] = neg*(-1.0)
    data4[data4.shape[0] - 1] = pos
    chatCounter += msgCacheLength #increment the plot by the volume of messages received
    # print(data1)
    # print(data2)
    # print(data3)
    # print(data4)
    curve1.setData(data1)
    curve1.setPos(chatCounter,0)
    curve2.setData(data2)
    curve2.setPos(chatCounter, 0)
    curve3.setData(data3)
    curve3.setPos(chatCounter, 0)
    curve4.setData(data4)
    curve4.setPos(chatCounter, 0)