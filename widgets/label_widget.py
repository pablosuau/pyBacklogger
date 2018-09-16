'''
User-defined widget with functionality to deal with labels in
an interactive way
'''

from PyQt5 import QtGui, QtWidgets, QtCore

class LabelWidget(QtWidgets.QWidget):
    '''
    Widget to visualise and assign labels
    '''

    def __init__(self, item, father):
        '''
        Initialises the widget.

        parameters
            - item: the table item around which we wrap the functionality
            - father: the parent widget
        '''
        super(LabelWidget, self).__init__()
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(self.layout)
        self.style = 'QLabel { background-color : #AAAAAA; color: black; }'
        self.father = father
        self.item = item
        self.item.setForeground(QtGui.QColor(255, 255, 255))
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def labels_to_string(self):
        '''
        Transforms a set of labels into a single string.

        returns:
            - A string representation of the widget's labels
        '''
        if self.layout.count() > 0:
            labels = self.layout.itemAt(0).widget().text()
            for i in range(1, self.layout.count()):
                labels = labels + ', ' + self.layout.itemAt(i).widget().text()
        else:
            labels = ''

        return labels

    def string_to_labels(self, text):
        '''
        Transform a string representation into a set of labels. Labels are
        supposed to be comma-separated.

        parameters:
            - text: the string to parse for labels
        '''
        # Removing the elements in the layout
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Adding the labels
        labels = text.split(',')
        #if not (len(labels) == 1 and labels[0] == ''):
        # removing duplicates and sorting
        labels = list(set(labels))

        # Adding label widgets
        for label in labels:
            label_text = str(label).strip()
            if label_text != '':
                label_widget = QtWidgets.QLabel(label_text)
                label_widget.setStyleSheet(self.style)
                self.layout.addWidget(label_widget)

        self.item.setText(self.labels_to_string())

    def get_labels(self):
        '''
        Getter for the labels contained by the widget

        returns:
            - a list which contains the labels in the widget
        '''
        labels = []
        if self.layout.count() > 0:
            for i in range(0, self.layout.count()):
                labels.append(self.layout.itemAt(i).widget().text())

        return labels

    def mousePressEvent(self, event):
        '''
        Signal slot for the event of clicking on the widget. The event parameter is unused.
        '''
        # pylint: disable=invalid-name
        # pylint: disable=unused-argument
        labels = self.labels_to_string()
        for label in self.get_labels():
            self.father.models['label_list_model'].remove(label)
        text, ok = QtWidgets.QInputDialog.getText(
            self,
            'Labels',
            'Enter labels (comma-separated)',
            QtWidgets.QLineEdit.Normal,
            labels)
        if ok:
            self.string_to_labels(text)
            self.father.changed = text != labels
            for label in self.get_labels():
                self.father.models['label_list_model'].add(label)

        QtWidgets.qApp.processEvents() # this line makes the labels to be
                                   # painted before resizing the table's
                                   # columns
