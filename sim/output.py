# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xyz.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 750)
        Form.setToolTipDuration(-1)
        Form.setProperty("promptAtExit", False)
        Form.setProperty("promot_on_exit", True)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recentfilecombobox = RecentFileComboBox(self.verticalLayoutWidget)
        self.recentfilecombobox.setMinimumSize(QtCore.QSize(0, 0))
        self.recentfilecombobox.setObjectName("recentfilecombobox")
        self.verticalLayout_2.addWidget(self.recentfilecombobox)
        self.gcodeeditor = GcodeEditor(self.verticalLayoutWidget)
        self.gcodeeditor.setObjectName("gcodeeditor")
        self.verticalLayout_2.addWidget(self.gcodeeditor)
        self.entry = EntryWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.entry.setFont(font)
        self.entry.setObjectName("entry")
        self.verticalLayout_2.addWidget(self.entry)
        self.gcodebackplot = GcodeBackplot(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gcodebackplot.sizePolicy().hasHeightForWidth())
        self.gcodebackplot.setSizePolicy(sizePolicy)
        self.gcodebackplot.setProperty("renderProgramAlpha", True)
        self.gcodebackplot.setBackgroundColor(QtGui.QColor(46, 52, 54))
        self.gcodebackplot.setObjectName("gcodebackplot")
        self.horizontalLayout.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.buttonBox = QtWidgets.QWidget(self.groupBox_2)
        self.buttonBox.setGeometry(QtCore.QRect(160, 60, 141, 31))
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.buttonBox)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.buttonBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_7 = QtWidgets.QPushButton(self.buttonBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setAutoExclusive(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.buttonBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setAutoExclusive(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.power = QtWidgets.QPushButton(self.groupBox_2)
        self.power.setGeometry(QtCore.QRect(210, 30, 80, 23))
        self.power.setCheckable(True)
        self.power.setObjectName("power")
        self.axisactionbutton_4 = AxisActionButton(self.groupBox_2)
        self.axisactionbutton_4.setGeometry(QtCore.QRect(10, 80, 80, 23))
        self.axisactionbutton_4.setProperty("action_id", AxisActionButton.Home)
        self.axisactionbutton_4.setAxis(AxisActionButton.X)
        self.axisactionbutton_4.setObjectName("axisactionbutton_4")
        self.axisactionbutton_5 = AxisActionButton(self.groupBox_2)
        self.axisactionbutton_5.setGeometry(QtCore.QRect(10, 140, 80, 23))
        self.axisactionbutton_5.setProperty("action_id", AxisActionButton.Home)
        self.axisactionbutton_5.setAxis(AxisActionButton.Z)
        self.axisactionbutton_5.setObjectName("axisactionbutton_5")
        self.axisactionbutton_6 = AxisActionButton(self.groupBox_2)
        self.axisactionbutton_6.setGeometry(QtCore.QRect(10, 50, 80, 23))
        self.axisactionbutton_6.setProperty("action_id", AxisActionButton.Home)
        self.axisactionbutton_6.setAxis(AxisActionButton.ALL)
        self.axisactionbutton_6.setObjectName("axisactionbutton_6")
        self.axisactionbutton_7 = AxisActionButton(self.groupBox_2)
        self.axisactionbutton_7.setGeometry(QtCore.QRect(10, 110, 80, 23))
        self.axisactionbutton_7.setProperty("action_id", AxisActionButton.Home)
        self.axisactionbutton_7.setAxis(AxisActionButton.Y)
        self.axisactionbutton_7.setObjectName("axisactionbutton_7")
        self.horizontalLayout_9.addWidget(self.groupBox_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(30, 52, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_10.addWidget(self.pushButton_3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(110, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setInputMask("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_10.addWidget(self.lineEdit)
        self.dro = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro.setFont(font)
        self.dro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro.setProperty("reference_type", DROWidget.Relative)
        self.dro.setUnits(DROWidget.Program)
        self.dro.setObjectName("dro")
        self.horizontalLayout_10.addWidget(self.dro)
        self.dro_5 = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro_5.setFont(font)
        self.dro_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_5.setProperty("reference_type", DROWidget.DistanceToGo)
        self.dro_5.setUnits(DROWidget.Program)
        self.dro_5.setObjectName("dro_5")
        self.horizontalLayout_10.addWidget(self.dro_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_11.addWidget(self.pushButton_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(110, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_11.addWidget(self.lineEdit_2)
        self.dro_2 = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro_2.setFont(font)
        self.dro_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_2.setProperty("reference_type", DROWidget.Relative)
        self.dro_2.setAxis(DROWidget.Y)
        self.dro_2.setUnits(DROWidget.Program)
        self.dro_2.setObjectName("dro_2")
        self.horizontalLayout_11.addWidget(self.dro_2)
        self.dro_6 = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro_6.setFont(font)
        self.dro_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_6.setProperty("reference_type", DROWidget.DistanceToGo)
        self.dro_6.setAxis(DROWidget.Y)
        self.dro_6.setUnits(DROWidget.Program)
        self.dro_6.setObjectName("dro_6")
        self.horizontalLayout_11.addWidget(self.dro_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_12.addWidget(self.pushButton_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(110, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_12.addWidget(self.lineEdit_3)
        self.dro_3 = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro_3.setFont(font)
        self.dro_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_3.setProperty("reference_type", DROWidget.Relative)
        self.dro_3.setAxis(DROWidget.Z)
        self.dro_3.setUnits(DROWidget.Program)
        self.dro_3.setObjectName("dro_3")
        self.horizontalLayout_12.addWidget(self.dro_3)
        self.dro_7 = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro_7.setFont(font)
        self.dro_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_7.setProperty("reference_type", DROWidget.DistanceToGo)
        self.dro_7.setAxis(DROWidget.Z)
        self.dro_7.setUnits(DROWidget.Program)
        self.dro_7.setObjectName("dro_7")
        self.horizontalLayout_12.addWidget(self.dro_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_6.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_13.addWidget(self.pushButton_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(110, 0))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_13.addWidget(self.lineEdit_4)
        self.dro_4 = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro_4.setFont(font)
        self.dro_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_4.setProperty("reference_type", DROWidget.Relative)
        self.dro_4.setAxis(DROWidget.A)
        self.dro_4.setUnits(DROWidget.Program)
        self.dro_4.setObjectName("dro_4")
        self.horizontalLayout_13.addWidget(self.dro_4)
        self.dro_8 = DROWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.dro_8.setFont(font)
        self.dro_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.dro_8.setProperty("reference_type", DROWidget.DistanceToGo)
        self.dro_8.setAxis(DROWidget.A)
        self.dro_8.setUnits(DROWidget.Program)
        self.dro_8.setObjectName("dro_8")
        self.horizontalLayout_13.addWidget(self.dro_8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_9.addWidget(self.frame)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.groupBox_4.setObjectName("groupBox_4")
        self.actionbutton_2 = ActionButton(self.groupBox_4)
        self.actionbutton_2.setGeometry(QtCore.QRect(190, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.actionbutton_2.setFont(font)
        self.actionbutton_2.setCheckable(True)
        self.actionbutton_2.setProperty("action_id", ActionButton.MachinePower)
        self.actionbutton_2.setObjectName("actionbutton_2")
        self.actionbutton = ActionButton(self.groupBox_4)
        self.actionbutton.setGeometry(QtCore.QRect(190, 110, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.actionbutton.setFont(font)
        self.actionbutton.setCheckable(True)
        self.actionbutton.setProperty("action_id", ActionButton.EmergencyStop)
        self.actionbutton.setObjectName("actionbutton")
        self.actionbutton_4 = ActionButton(self.groupBox_4)
        self.actionbutton_4.setGeometry(QtCore.QRect(10, 60, 80, 23))
        self.actionbutton_4.setCheckable(True)
        self.actionbutton_4.setProperty("action_id", ActionButton.Flood)
        self.actionbutton_4.setObjectName("actionbutton_4")
        self.actionbutton_5 = ActionButton(self.groupBox_4)
        self.actionbutton_5.setGeometry(QtCore.QRect(100, 30, 80, 23))
        self.actionbutton_5.setCheckable(True)
        self.actionbutton_5.setProperty("action_id", ActionButton.BlockDelete)
        self.actionbutton_5.setProperty("action_type", ActionButton.Toggle)
        self.actionbutton_5.setProperty("option", True)
        self.actionbutton_5.setObjectName("actionbutton_5")
        self.actionbutton_6 = ActionButton(self.groupBox_4)
        self.actionbutton_6.setGeometry(QtCore.QRect(100, 60, 80, 23))
        self.actionbutton_6.setCheckable(True)
        self.actionbutton_6.setProperty("action_id", ActionButton.OptionalStop)
        self.actionbutton_6.setProperty("option", True)
        self.actionbutton_6.setObjectName("actionbutton_6")
        self.actionbutton_9 = ActionButton(self.groupBox_4)
        self.actionbutton_9.setGeometry(QtCore.QRect(10, 30, 80, 23))
        self.actionbutton_9.setCheckable(True)
        self.actionbutton_9.setProperty("action_id", ActionButton.Mist)
        self.actionbutton_9.setProperty("action_type", ActionButton.Toggle)
        self.actionbutton_9.setObjectName("actionbutton_9")
        self.jogbutton = JogButton(self.groupBox_4)
        self.jogbutton.setGeometry(QtCore.QRect(50, 120, 80, 23))
        self.jogbutton.setAxis(JogButton.X)
        self.jogbutton.setObjectName("jogbutton")
        self.horizontalLayout_9.addWidget(self.groupBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        Form.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(Form)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 20))
        self.menuBar.setObjectName("menuBar")
        self.menuExit = QtWidgets.QMenu(self.menuBar)
        self.menuExit.setObjectName("menuExit")
        self.menuRecentFiles = QtWidgets.QMenu(self.menuExit)
        self.menuRecentFiles.setObjectName("menuRecentFiles")
        self.menuMachine = QtWidgets.QMenu(self.menuBar)
        self.menuMachine.setObjectName("menuMachine")
        self.menuHoming = QtWidgets.QMenu(self.menuMachine)
        self.menuHoming.setObjectName("menuHoming")
        self.menuCooling = QtWidgets.QMenu(self.menuMachine)
        self.menuCooling.setObjectName("menuCooling")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        Form.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(Form)
        self.statusBar.setObjectName("statusBar")
        Form.setStatusBar(self.statusBar)
        self.actionExit = QtWidgets.QAction(Form)
        self.actionExit.setObjectName("actionExit")
        self.actionOpen = QtWidgets.QAction(Form)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(Form)
        self.actionClose.setObjectName("actionClose")
        self.actionReload = QtWidgets.QAction(Form)
        self.actionReload.setObjectName("actionReload")
        self.actionSave_As = QtWidgets.QAction(Form)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionHome_X = QtWidgets.QAction(Form)
        self.actionHome_X.setObjectName("actionHome_X")
        self.actionHome_Y = QtWidgets.QAction(Form)
        self.actionHome_Y.setObjectName("actionHome_Y")
        self.actionHome_Z = QtWidgets.QAction(Form)
        self.actionHome_Z.setObjectName("actionHome_Z")
        self.action_EmergencyStop_toggle = QtWidgets.QAction(Form)
        self.action_EmergencyStop_toggle.setObjectName("action_EmergencyStop_toggle")
        self.action_MachinePower_toggle = QtWidgets.QAction(Form)
        self.action_MachinePower_toggle.setProperty("_axis", 2)
        self.action_MachinePower_toggle.setObjectName("action_MachinePower_toggle")
        self.actionHome_All = QtWidgets.QAction(Form)
        self.actionHome_All.setObjectName("actionHome_All")
        self.actionRun_Program = QtWidgets.QAction(Form)
        self.actionRun_Program.setObjectName("actionRun_Program")
        self.actionFile1 = QtWidgets.QAction(Form)
        self.actionFile1.setObjectName("actionFile1")
        self.actionReport_Actual_Position = QtWidgets.QAction(Form)
        self.actionReport_Actual_Position.setCheckable(True)
        self.actionReport_Actual_Position.setObjectName("actionReport_Actual_Position")
        self.actionTest = QtWidgets.QAction(Form)
        self.actionTest.setObjectName("actionTest")
        self.action_Mist_toggle = QtWidgets.QAction(Form)
        self.action_Mist_toggle.setCheckable(True)
        self.action_Mist_toggle.setObjectName("action_Mist_toggle")
        self.action_Flood_toggle = QtWidgets.QAction(Form)
        self.action_Flood_toggle.setCheckable(True)
        self.action_Flood_toggle.setObjectName("action_Flood_toggle")
        self.menuRecentFiles.addAction(self.actionFile1)
        self.menuExit.addAction(self.actionOpen)
        self.menuExit.addAction(self.menuRecentFiles.menuAction())
        self.menuExit.addAction(self.actionReload)
        self.menuExit.addAction(self.actionClose)
        self.menuExit.addAction(self.actionSave_As)
        self.menuExit.addSeparator()
        self.menuExit.addAction(self.actionExit)
        self.menuHoming.addAction(self.actionHome_All)
        self.menuHoming.addAction(self.actionHome_X)
        self.menuHoming.addAction(self.actionHome_Y)
        self.menuHoming.addAction(self.actionHome_Z)
        self.menuCooling.addAction(self.action_Mist_toggle)
        self.menuCooling.addAction(self.action_Flood_toggle)
        self.menuMachine.addAction(self.action_EmergencyStop_toggle)
        self.menuMachine.addAction(self.action_MachinePower_toggle)
        self.menuMachine.addSeparator()
        self.menuMachine.addAction(self.actionRun_Program)
        self.menuMachine.addAction(self.menuHoming.menuAction())
        self.menuMachine.addAction(self.menuCooling.menuAction())
        self.menuView.addAction(self.actionReport_Actual_Position)
        self.menuView.addAction(self.actionTest)
        self.menuBar.addAction(self.menuExit.menuAction())
        self.menuBar.addAction(self.menuMachine.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QtPyVCP"))
        self.entry.setPlaceholderText(_translate("Form", "MDI"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Status"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tool Table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Probing"))
        self.groupBox_2.setTitle(_translate("Form", "PROGRAM"))
        self.pushButton_2.setText(_translate("Form", "ABS"))
        self.pushButton_2.setProperty("position", _translate("Form", "first"))
        self.pushButton_7.setText(_translate("Form", "REL"))
        self.pushButton_8.setText(_translate("Form", "DTG"))
        self.pushButton_8.setProperty("position", _translate("Form", "last"))
        self.power.setText(_translate("Form", "Power"))
        self.label.setText(_translate("Form", "ABS"))
        self.label_2.setText(_translate("Form", "REL"))
        self.label_3.setText(_translate("Form", "DTG"))
        self.pushButton_3.setText(_translate("Form", "X"))
        self.lineEdit.setText(_translate("Form", "0.1234"))
        self.pushButton_4.setText(_translate("Form", "Y"))
        self.lineEdit_2.setText(_translate("Form", "0.1234"))
        self.pushButton_5.setText(_translate("Form", "Z"))
        self.lineEdit_3.setText(_translate("Form", "0.1234"))
        self.pushButton_6.setText(_translate("Form", "A"))
        self.lineEdit_4.setText(_translate("Form", "0.1234"))
        self.groupBox_4.setTitle(_translate("Form", "GroupBox"))
        self.actionbutton_2.setText(_translate("Form", "Power "))
        self.actionbutton_6.setText(_translate("Form", "Opt Stop "))
        self.actionbutton_9.setText(_translate("Form", "Mist  Test"))
        self.menuExit.setTitle(_translate("Form", "File"))
        self.menuRecentFiles.setTitle(_translate("Form", "Recent &Files"))
        self.menuMachine.setTitle(_translate("Form", "Machine"))
        self.menuHoming.setTitle(_translate("Form", "Homing"))
        self.menuCooling.setTitle(_translate("Form", "Cooling"))
        self.menuView.setTitle(_translate("Form", "View"))
        self.actionExit.setText(_translate("Form", "Exit"))
        self.actionOpen.setText(_translate("Form", "&Open ..."))
        self.actionOpen.setShortcut(_translate("Form", "O"))
        self.actionClose.setText(_translate("Form", "Close"))
        self.actionReload.setText(_translate("Form", "&Reload"))
        self.actionReload.setShortcut(_translate("Form", "Ctrl+R"))
        self.actionSave_As.setText(_translate("Form", "Save As ..."))
        self.actionHome_X.setText(_translate("Form", "Home &X"))
        self.actionHome_Y.setText(_translate("Form", "Home &Y"))
        self.actionHome_Z.setText(_translate("Form", "Home &Z"))
        self.action_EmergencyStop_toggle.setText(_translate("Form", "Toggle E-stop"))
        self.action_EmergencyStop_toggle.setShortcut(_translate("Form", "F1"))
        self.action_MachinePower_toggle.setText(_translate("Form", "Machine Power"))
        self.action_MachinePower_toggle.setShortcut(_translate("Form", "F2"))
        self.actionHome_All.setText(_translate("Form", "Home All"))
        self.actionRun_Program.setText(_translate("Form", "Run Program"))
        self.actionRun_Program.setShortcut(_translate("Form", "R"))
        self.actionFile1.setText(_translate("Form", "File1"))
        self.actionReport_Actual_Position.setText(_translate("Form", "Report Actual Position"))
        self.actionTest.setText(_translate("Form", "Test"))
        self.action_Mist_toggle.setText(_translate("Form", "Mist On"))
        self.action_Mist_toggle.setShortcut(_translate("Form", "F7"))
        self.action_Flood_toggle.setText(_translate("Form", "Flood On"))
        self.action_Flood_toggle.setShortcut(_translate("Form", "F8"))

from QtPyVCP.widgets.control_widgets.action_button import ActionButton
from QtPyVCP.widgets.control_widgets.axis_button import AxisActionButton
from QtPyVCP.widgets.control_widgets.entry_widget import EntryWidget
from QtPyVCP.widgets.control_widgets.jog_button import JogButton
from QtPyVCP.widgets.display_widgets.dro_widget import DROWidget
from QtPyVCP.widgets.display_widgets.gcode_backplot import GcodeBackplot
from QtPyVCP.widgets.editor_widgets.gcode_editor import GcodeEditor
from QtPyVCP.widgets.editor_widgets.recent_file_combobox import RecentFileComboBox
from QtPyVCP.widgets.form_widgets.main_window import VCPMainWindow
import ui_rc
import xyz_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.VCPMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
