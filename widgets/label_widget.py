from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class LabelWidget(QtGui.QWidget):
    def __init__(self, item, father):
        super(LabelWidget, self).__init__()
        self.layout = QtGui.QHBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.layout)
        self.style = 'QLabel { background-color : #AAAAAA; color: black; }'
        self.father = father
        self.item = item
        self.item.setTextColor(QtGui.QColor(255,255,255))
        
    def labelsToString(self):
         if self.layout.count() > 0:
            labels = self.layout.itemAt(0).widget().text()
            for i in range(1,self.layout.count()):
                labels = labels + ', ' + self.layout.itemAt(i).widget().text()
         else: 
            labels = ''
            
         return labels
         
    def toString(self):
        return self.labelsToString()
         
    def stringToLabels(self, text):
        # Removing the elements in the layout
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)                            
        
        # Adding the labels
        labels = text.split(',')
        #if not (len(labels) == 1 and labels[0] == ''):
        # removing duplicates and sorting
        labels = list(set(labels))
        
        # Adding label widgets
        for i in range(0,len(labels)):
            label = QtGui.QLabel(str(labels[i]).strip())
            label.setStyleSheet(self.style)
            self.layout.addWidget(label)
                
        self.item.setText(text)
                
    def getLabels(self):
        labels = []
        if self.layout.count() > 0:
            for i in range(0,self.layout.count()):
                labels.append(self.layout.itemAt(i).widget().text())
            
        return labels
        
    def mousePressEvent(self, event):
        labels = self.labelsToString()     
        text, ok = QtGui.QInputDialog.getText(self, 'Labels', 'Enter labels (comma-separated)', QtGui.QLineEdit.Normal, labels)        
        if ok:
            self.stringToLabels(text)

        
        QtGui.qApp.processEvents() # this line makes the labels to be
                                   # painted before resizing the table's
                                   # columns
        
        
        
                