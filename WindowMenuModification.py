# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuModification.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowMenuModification(object):
    def __init__(self):
        self.CurrentWindow = None
        self.WindowChef = None
    
    def setupUi(self, CurrentWindow, WindowChef):
        self.WindowChef = WindowChef
        self.CurrentWindow = CurrentWindow
        CurrentWindow.setObjectName("WindowMenuModification")
        CurrentWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(CurrentWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.foodmenuLabel = QtWidgets.QLabel(self.centralwidget)
        self.foodmenuLabel.setGeometry(QtCore.QRect(0, 0, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.foodmenuLabel.setFont(font)
        self.foodmenuLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.foodmenuLabel.setObjectName("foodmenuLabel")
        self.addgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.addgroupBox.setGeometry(QtCore.QRect(30, 60, 331, 221))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addgroupBox.setFont(font)
        self.addgroupBox.setObjectName("addgroupBox")
        self.addButton = QtWidgets.QPushButton(self.addgroupBox)
        self.addButton.setGeometry(QtCore.QRect(40, 160, 75, 23))
        self.addButton.setObjectName("addButton")
        self.addresetButton = QtWidgets.QPushButton(self.addgroupBox)
        self.addresetButton.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.addresetButton.setObjectName("addresetButton")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.addgroupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 311, 101))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.line_33 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.gridLayout_3.addWidget(self.line_33, 4, 1, 1, 1)
        self.line_34 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_34.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setObjectName("line_34")
        self.gridLayout_3.addWidget(self.line_34, 4, 7, 1, 1)
        self.line_35 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_35.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.gridLayout_3.addWidget(self.line_35, 4, 5, 1, 1)
        self.line_36 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_36.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setObjectName("line_36")
        self.gridLayout_3.addWidget(self.line_36, 4, 3, 1, 1)
        self.line_37 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_37.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.gridLayout_3.addWidget(self.line_37, 0, 3, 1, 1)
        self.line_38 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.gridLayout_3.addWidget(self.line_38, 0, 1, 1, 1)
        self.line_39 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.gridLayout_3.addWidget(self.line_39, 0, 7, 1, 1)
        self.line_40 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_40.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.gridLayout_3.addWidget(self.line_40, 3, 0, 1, 1)
        self.line_41 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.gridLayout_3.addWidget(self.line_41, 0, 5, 1, 1)
        self.line_42 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_42.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.gridLayout_3.addWidget(self.line_42, 1, 0, 1, 1)
        self.line_43 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_43.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_43.setObjectName("line_43")
        self.gridLayout_3.addWidget(self.line_43, 2, 1, 1, 1)
        self.line_44 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_44.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setObjectName("line_44")
        self.gridLayout_3.addWidget(self.line_44, 2, 3, 1, 1)
        self.line_45 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_45.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_45.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_45.setObjectName("line_45")
        self.gridLayout_3.addWidget(self.line_45, 2, 5, 1, 1)
        self.line_46 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_46.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_46.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_46.setObjectName("line_46")
        self.gridLayout_3.addWidget(self.line_46, 3, 2, 1, 1)
        self.line_47 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_47.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_47.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_47.setObjectName("line_47")
        self.gridLayout_3.addWidget(self.line_47, 3, 4, 1, 1)
        self.line_48 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_48.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_48.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_48.setObjectName("line_48")
        self.gridLayout_3.addWidget(self.line_48, 1, 6, 1, 1)
        self.line_49 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_49.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_49.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_49.setObjectName("line_49")
        self.gridLayout_3.addWidget(self.line_49, 1, 4, 1, 1)
        self.line_50 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_50.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_50.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_50.setObjectName("line_50")
        self.gridLayout_3.addWidget(self.line_50, 1, 2, 1, 1)
        self.line_51 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_51.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_51.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_51.setObjectName("line_51")
        self.gridLayout_3.addWidget(self.line_51, 3, 6, 1, 1)
        self.line_52 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_52.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_52.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_52.setObjectName("line_52")
        self.gridLayout_3.addWidget(self.line_52, 2, 7, 1, 1)
        self.priceLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.priceLabel.setFont(font)
        self.priceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.priceLabel.setObjectName("priceLabel")
        self.gridLayout_3.addWidget(self.priceLabel, 1, 5, 1, 1)
        self.classificationLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.classificationLabel.setFont(font)
        self.classificationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.classificationLabel.setObjectName("classificationLabel")
        self.gridLayout_3.addWidget(self.classificationLabel, 1, 3, 1, 1)
        self.nameLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout_3.addWidget(self.nameLabel, 1, 1, 1, 1)
        self.addspicyCheckbox = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.addspicyCheckbox.setFont(font)
        self.addspicyCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addspicyCheckbox.setText("")
        self.addspicyCheckbox.setObjectName("addspicyCheckbox")
        self.gridLayout_3.addWidget(self.addspicyCheckbox, 3, 7, 1, 1)
        self.additemLine = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.additemLine.setFont(font)
        self.additemLine.setObjectName("additemLine")
        self.gridLayout_3.addWidget(self.additemLine, 3, 1, 1, 1)
        self.addclassificationCombo = QtWidgets.QComboBox(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.addclassificationCombo.setFont(font)
        self.addclassificationCombo.setObjectName("addclassificationCombo")
        self.addclassificationCombo.addItem("")
        self.addclassificationCombo.setItemText(0, "")
        self.addclassificationCombo.addItem("")
        self.addclassificationCombo.addItem("")
        self.addclassificationCombo.addItem("")
        self.addclassificationCombo.addItem("")
        self.addclassificationCombo.addItem("")
        self.gridLayout_3.addWidget(self.addclassificationCombo, 3, 3, 1, 1)
        self.addpriceLine = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.addpriceLine.setFont(font)
        self.addpriceLine.setObjectName("addpriceLine")
        self.gridLayout_3.addWidget(self.addpriceLine, 3, 5, 1, 1)
        self.spicyLabel = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spicyLabel.setFont(font)
        self.spicyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.spicyLabel.setObjectName("spicyLabel")
        self.gridLayout_3.addWidget(self.spicyLabel, 1, 7, 1, 1)
        self.line_53 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_53.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_53.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_53.setObjectName("line_53")
        self.gridLayout_3.addWidget(self.line_53, 1, 8, 1, 1)
        self.line_54 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.line_54.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_54.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_54.setObjectName("line_54")
        self.gridLayout_3.addWidget(self.line_54, 3, 8, 1, 1)
        self.previewButton = QtWidgets.QPushButton(self.centralwidget)
        self.previewButton.setGeometry(QtCore.QRect(280, 400, 231, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.previewButton.setFont(font)
        self.previewButton.setObjectName("previewButton")
        self.removegroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.removegroupBox.setGeometry(QtCore.QRect(430, 60, 331, 221))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.removegroupBox.setFont(font)
        self.removegroupBox.setObjectName("removegroupBox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.removegroupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 311, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_27 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.gridLayout_2.addWidget(self.line_27, 4, 1, 1, 1)
        self.line_30 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.gridLayout_2.addWidget(self.line_30, 4, 7, 1, 1)
        self.line_29 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.gridLayout_2.addWidget(self.line_29, 4, 5, 1, 1)
        self.line_28 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.gridLayout_2.addWidget(self.line_28, 4, 3, 1, 1)
        self.line_22 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.gridLayout_2.addWidget(self.line_22, 0, 3, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_2.addWidget(self.line_21, 0, 1, 1, 1)
        self.line_24 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.gridLayout_2.addWidget(self.line_24, 0, 7, 1, 1)
        self.line_26 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.gridLayout_2.addWidget(self.line_26, 3, 0, 1, 1)
        self.line_23 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.gridLayout_2.addWidget(self.line_23, 0, 5, 1, 1)
        self.line_25 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.gridLayout_2.addWidget(self.line_25, 1, 0, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_2.addWidget(self.line_11, 2, 1, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_2.addWidget(self.line_12, 2, 3, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_2.addWidget(self.line_13, 2, 5, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_2.addWidget(self.line_16, 3, 2, 1, 1)
        self.line_18 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_18.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_2.addWidget(self.line_18, 3, 4, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_19.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.gridLayout_2.addWidget(self.line_19, 1, 6, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_17.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_2.addWidget(self.line_17, 1, 4, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_2.addWidget(self.line_15, 1, 2, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.gridLayout_2.addWidget(self.line_20, 3, 6, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_2.addWidget(self.line_14, 2, 7, 1, 1)
        self.priceLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.priceLabel_2.setFont(font)
        self.priceLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.priceLabel_2.setObjectName("priceLabel_2")
        self.gridLayout_2.addWidget(self.priceLabel_2, 1, 5, 1, 1)
        self.classificationLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.classificationLabel_2.setFont(font)
        self.classificationLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.classificationLabel_2.setObjectName("classificationLabel_2")
        self.gridLayout_2.addWidget(self.classificationLabel_2, 1, 3, 1, 1)
        self.nameLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel_2.setFont(font)
        self.nameLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.gridLayout_2.addWidget(self.nameLabel_2, 1, 1, 1, 1)
        self.removespicyCheckbox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.removespicyCheckbox.setFont(font)
        self.removespicyCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.removespicyCheckbox.setText("")
        self.removespicyCheckbox.setObjectName("removespicyCheckbox")
        self.gridLayout_2.addWidget(self.removespicyCheckbox, 3, 7, 1, 1)
        self.removeitemLine = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.removeitemLine.setFont(font)
        self.removeitemLine.setObjectName("removeitemLine")
        self.gridLayout_2.addWidget(self.removeitemLine, 3, 1, 1, 1)
        self.removeclassificationCombo = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.removeclassificationCombo.setFont(font)
        self.removeclassificationCombo.setObjectName("removeclassificationCombo")
        self.removeclassificationCombo.addItem("")
        self.removeclassificationCombo.setItemText(0, "")
        self.removeclassificationCombo.addItem("")
        self.removeclassificationCombo.addItem("")
        self.removeclassificationCombo.addItem("")
        self.removeclassificationCombo.addItem("")
        self.removeclassificationCombo.addItem("")
        self.gridLayout_2.addWidget(self.removeclassificationCombo, 3, 3, 1, 1)
        self.removepriceLine = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.removepriceLine.setFont(font)
        self.removepriceLine.setObjectName("removepriceLine")
        self.gridLayout_2.addWidget(self.removepriceLine, 3, 5, 1, 1)
        self.spicyLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.spicyLabel_2.setFont(font)
        self.spicyLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spicyLabel_2.setObjectName("spicyLabel_2")
        self.gridLayout_2.addWidget(self.spicyLabel_2, 1, 7, 1, 1)
        self.line_31 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.gridLayout_2.addWidget(self.line_31, 1, 8, 1, 1)
        self.line_32 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.gridLayout_2.addWidget(self.line_32, 3, 8, 1, 1)
        self.removeButton = QtWidgets.QPushButton(self.removegroupBox)
        self.removeButton.setGeometry(QtCore.QRect(40, 160, 75, 23))
        self.removeButton.setObjectName("removeButton")
        self.removeresetButton = QtWidgets.QPushButton(self.removegroupBox)
        self.removeresetButton.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.removeresetButton.setObjectName("removeresetButton")
        self.gobackButton = QtWidgets.QPushButton(self.centralwidget)
        self.gobackButton.setGeometry(QtCore.QRect(0, 0, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.gobackButton.setFont(font)
        self.gobackButton.setObjectName("gobackButton")
        CurrentWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CurrentWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CurrentWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CurrentWindow)
        self.statusbar.setObjectName("statusbar")
        CurrentWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CurrentWindow)
        QtCore.QMetaObject.connectSlotsByName(CurrentWindow)

        # Button functionality to go back to chef page
        self.gobackButton.clicked.connect(self.open_chef)
        # Button to add item to menu
        self.addButton.clicked.connect(self.addtoMenu)
        # Button to remove item from menu
        self.removeButton.clicked.connect(self.removefromMenu)
        # Button to reset fields on add item side
        self.addresetButton.clicked.connect(self.resetAdd)
        # Button to reset fields on remove item side
        self.removeresetButton.clicked.connect(self.resetRemove)
        # Button to preview menu
        self.previewButton.clicked.connect(self.previewMenu)

    def retranslateUi(self, CurrentWindow):
        _translate = QtCore.QCoreApplication.translate
        CurrentWindow.setWindowTitle(_translate("WindowMenuModification", "MainWindow"))
        self.foodmenuLabel.setText(_translate("WindowMenuModification", "Food Menu Modification"))
        self.addgroupBox.setTitle(_translate("WindowMenuModification", "Add an item"))
        self.addButton.setText(_translate("WindowMenuModification", "Add it"))
        self.addresetButton.setText(_translate("WindowMenuModification", "Reset Fields"))
        self.priceLabel.setText(_translate("WindowMenuModification", "Price ($)"))
        self.classificationLabel.setText(_translate("WindowMenuModification", "Classification"))
        self.nameLabel.setText(_translate("WindowMenuModification", "Item Name"))
        self.addclassificationCombo.setItemText(1, _translate("WindowMenuModification", "Appetizers"))
        self.addclassificationCombo.setItemText(2, _translate("WindowMenuModification", "Sides"))
        self.addclassificationCombo.setItemText(3, _translate("WindowMenuModification", "Entrees"))
        self.addclassificationCombo.setItemText(4, _translate("WindowMenuModification", "Desserts"))
        self.addclassificationCombo.setItemText(5, _translate("WindowMenuModification", "Beverages"))
        self.spicyLabel.setText(_translate("WindowMenuModification", "Spicy?"))
        self.previewButton.setText(_translate("WindowMenuModification", "Preview Food Menu"))
        self.removegroupBox.setTitle(_translate("WindowMenuModification", "Remove an item"))
        self.priceLabel_2.setText(_translate("WindowMenuModification", "Price ($)"))
        self.classificationLabel_2.setText(_translate("WindowMenuModification", "Classification"))
        self.nameLabel_2.setText(_translate("WindowMenuModification", "Item Name"))
        self.removeclassificationCombo.setItemText(1, _translate("WindowMenuModification", "Appetizers"))
        self.removeclassificationCombo.setItemText(2, _translate("WindowMenuModification", "Sides"))
        self.removeclassificationCombo.setItemText(3, _translate("WindowMenuModification", "Entrees"))
        self.removeclassificationCombo.setItemText(4, _translate("WindowMenuModification", "Desserts"))
        self.removeclassificationCombo.setItemText(5, _translate("WindowMenuModification", "Beverages"))
        self.spicyLabel_2.setText(_translate("WindowMenuModification", "Spicy?"))
        self.removeButton.setText(_translate("WindowMenuModification", "Remove it"))
        self.removeresetButton.setText(_translate("WindowMenuModification", "Reset Fields"))
        self.gobackButton.setText(_translate("WindowMenuModification", "Go back"))

    def open_chef(self):
        self.CurrentWindow.hide()
        self.LoginWindow.show()    

    def addtoMenu(self):
        print(self.additemLine.text())
        print(self.addclassificationCombo.currentText())
        print(self.addpriceLine.text())
        print(self.addspicyCheckbox.isChecked())

    def removefromMenu(self):
        print(self.removeitemLine.text())
        print(self.removeclassificationCombo.currentText())
        print(self.removepriceLine.text())
        print(self.removespicyCheckbox.isChecked())
    
    def resetAdd(self):
        self.additemLine.clear()
        self.addclassificationCombo.setCurrentIndex(0)
        self.addpriceLine.clear()
        self.addspicyCheckbox.setChecked(0)

    def resetRemove(self):
        self.removeitemLine.clear()
        self.removeclassificationCombo.setCurrentIndex(0)
        self.removepriceLine.clear()
        self.removespicyCheckbox.setChecked(0)

    def previewMenu(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrentWindow = QtWidgets.QMainWindow()
    ui = Ui_WindowMenuModification()
    ui.setupUi(CurrentWindow, None)
    CurrentWindow.show()
    sys.exit(app.exec_())
