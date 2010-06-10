# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/phil/SVN/Python/SpikePy/sim/gui/gui_main.ui'
#
# Created: Mon May 31 18:09:19 2010
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SimGui(object):
    def setupUi(self, SimGui):
        SimGui.setObjectName("SimGui")
        SimGui.resize(874, 594)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SimGui.sizePolicy().hasHeightForWidth())
        SimGui.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/neural_sim_server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SimGui.setWindowIcon(icon)
        SimGui.setDockNestingEnabled(True)
        SimGui.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AnimatedDocks)
        SimGui.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(SimGui)
        self.centralwidget.setObjectName("centralwidget")
        self.lo_central = QtGui.QHBoxLayout(self.centralwidget)
        self.lo_central.setObjectName("lo_central")
        self.lo_log = QtGui.QVBoxLayout()
        self.lo_log.setObjectName("lo_log")
        self.lo_over_log = QtGui.QHBoxLayout()
        self.lo_over_log.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.lo_over_log.setObjectName("lo_over_log")
        self.lbl_frame = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lbl_frame.setFont(font)
        self.lbl_frame.setObjectName("lbl_frame")
        self.lo_over_log.addWidget(self.lbl_frame)
        self.edt_frame = QtGui.QLineEdit(self.centralwidget)
        self.edt_frame.setMinimumSize(QtCore.QSize(100, 0))
        self.edt_frame.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.edt_frame.setFont(font)
        self.edt_frame.setReadOnly(True)
        self.edt_frame.setObjectName("edt_frame")
        self.lo_over_log.addWidget(self.edt_frame)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lo_over_log.addItem(spacerItem)
        self.lbl_frame_size = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lbl_frame_size.setFont(font)
        self.lbl_frame_size.setObjectName("lbl_frame_size")
        self.lo_over_log.addWidget(self.lbl_frame_size)
        self.cb_frame_size = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_frame_size.sizePolicy().hasHeightForWidth())
        self.cb_frame_size.setSizePolicy(sizePolicy)
        self.cb_frame_size.setEditable(False)
        self.cb_frame_size.setObjectName("cb_frame_size")
        self.cb_frame_size.addItem("")
        self.cb_frame_size.addItem("")
        self.cb_frame_size.addItem("")
        self.cb_frame_size.addItem("")
        self.cb_frame_size.addItem("")
        self.lo_over_log.addWidget(self.cb_frame_size)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lo_over_log.addItem(spacerItem1)
        self.lbl_sample_rate = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.lbl_sample_rate.setFont(font)
        self.lbl_sample_rate.setObjectName("lbl_sample_rate")
        self.lo_over_log.addWidget(self.lbl_sample_rate)
        self.cb_sample_rate = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_sample_rate.sizePolicy().hasHeightForWidth())
        self.cb_sample_rate.setSizePolicy(sizePolicy)
        self.cb_sample_rate.setEditable(False)
        self.cb_sample_rate.setObjectName("cb_sample_rate")
        self.cb_sample_rate.addItem("")
        self.cb_sample_rate.addItem("")
        self.cb_sample_rate.addItem("")
        self.cb_sample_rate.addItem("")
        self.cb_sample_rate.addItem("")
        self.cb_sample_rate.addItem("")
        self.cb_sample_rate.addItem("")
        self.lo_over_log.addWidget(self.cb_sample_rate)
        self.lo_log.addLayout(self.lo_over_log)
        self.lst_log = QtGui.QListView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_log.sizePolicy().hasHeightForWidth())
        self.lst_log.setSizePolicy(sizePolicy)
        self.lst_log.setMinimumSize(QtCore.QSize(300, 200))
        self.lst_log.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.lst_log.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lst_log.setProperty("showDropIndicator", False)
        self.lst_log.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.lst_log.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.lst_log.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.lst_log.setResizeMode(QtGui.QListView.Adjust)
        self.lst_log.setObjectName("lst_log")
        self.lo_log.addWidget(self.lst_log)
        self.progress = QtGui.QProgressBar(self.centralwidget)
        self.progress.setEnabled(True)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setObjectName("progress")
        self.lo_log.addWidget(self.progress)
        self.lo_central.addLayout(self.lo_log)
        self.lo_right = QtGui.QVBoxLayout()
        self.lo_right.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.lo_right.setObjectName("lo_right")
        self.gb_timer = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_timer.sizePolicy().hasHeightForWidth())
        self.gb_timer.setSizePolicy(sizePolicy)
        self.gb_timer.setObjectName("gb_timer")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gb_timer)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_timer = QtGui.QPushButton(self.gb_timer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_timer.sizePolicy().hasHeightForWidth())
        self.btn_timer.setSizePolicy(sizePolicy)
        self.btn_timer.setMaximumSize(QtCore.QSize(90, 16777215))
        self.btn_timer.setAutoDefault(True)
        self.btn_timer.setObjectName("btn_timer")
        self.verticalLayout_3.addWidget(self.btn_timer)
        self.edt_timer = QtGui.QLineEdit(self.gb_timer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_timer.sizePolicy().hasHeightForWidth())
        self.edt_timer.setSizePolicy(sizePolicy)
        self.edt_timer.setMaximumSize(QtCore.QSize(90, 16777215))
        self.edt_timer.setMaxLength(6)
        self.edt_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_timer.setObjectName("edt_timer")
        self.verticalLayout_3.addWidget(self.edt_timer)
        self.lo_right.addWidget(self.gb_timer)
        spacerItem2 = QtGui.QSpacerItem(0, 25, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.lo_right.addItem(spacerItem2)
        self.gb_steps = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_steps.sizePolicy().hasHeightForWidth())
        self.gb_steps.setSizePolicy(sizePolicy)
        self.gb_steps.setObjectName("gb_steps")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gb_steps)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_steps = QtGui.QPushButton(self.gb_steps)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_steps.sizePolicy().hasHeightForWidth())
        self.btn_steps.setSizePolicy(sizePolicy)
        self.btn_steps.setMaximumSize(QtCore.QSize(90, 16777215))
        self.btn_steps.setObjectName("btn_steps")
        self.verticalLayout_4.addWidget(self.btn_steps)
        self.edt_steps = QtGui.QLineEdit(self.gb_steps)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edt_steps.sizePolicy().hasHeightForWidth())
        self.edt_steps.setSizePolicy(sizePolicy)
        self.edt_steps.setMaximumSize(QtCore.QSize(90, 16777215))
        self.edt_steps.setMaxLength(6)
        self.edt_steps.setAlignment(QtCore.Qt.AlignCenter)
        self.edt_steps.setObjectName("edt_steps")
        self.verticalLayout_4.addWidget(self.edt_steps)
        self.lo_right.addWidget(self.gb_steps)
        spacerItem3 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.lo_right.addItem(spacerItem3)
        self.btn_reset = QtGui.QPushButton(self.centralwidget)
        self.btn_reset.setObjectName("btn_reset")
        self.lo_right.addWidget(self.btn_reset)
        self.btn_quit = QtGui.QPushButton(self.centralwidget)
        self.btn_quit.setObjectName("btn_quit")
        self.lo_right.addWidget(self.btn_quit)
        self.lo_central.addLayout(self.lo_right)
        SimGui.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SimGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 20))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        SimGui.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SimGui)
        self.statusbar.setObjectName("statusbar")
        SimGui.setStatusBar(self.statusbar)
        self.dock_scene = QtGui.QDockWidget(SimGui)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dock_scene.sizePolicy().hasHeightForWidth())
        self.dock_scene.setSizePolicy(sizePolicy)
        self.dock_scene.setObjectName("dock_scene")
        self.dock_scene_contents = QtGui.QWidget()
        self.dock_scene_contents.setObjectName("dock_scene_contents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dock_scene_contents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tre_scene = QtGui.QTreeView(self.dock_scene_contents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_scene.sizePolicy().hasHeightForWidth())
        self.tre_scene.setSizePolicy(sizePolicy)
        self.tre_scene.setMinimumSize(QtCore.QSize(250, 150))
        self.tre_scene.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tre_scene.setProperty("showDropIndicator", False)
        self.tre_scene.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tre_scene.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tre_scene.setIndentation(15)
        self.tre_scene.setRootIsDecorated(True)
        self.tre_scene.setUniformRowHeights(True)
        self.tre_scene.setAnimated(True)
        self.tre_scene.setObjectName("tre_scene")
        self.tre_scene.header().setCascadingSectionResizes(True)
        self.tre_scene.header().setDefaultSectionSize(140)
        self.verticalLayout.addWidget(self.tre_scene)
        self.lo_dscene_upper_btns = QtGui.QHBoxLayout()
        self.lo_dscene_upper_btns.setObjectName("lo_dscene_upper_btns")
        self.btn_dscene_neuron = QtGui.QToolButton(self.dock_scene_contents)
        self.btn_dscene_neuron.setObjectName("btn_dscene_neuron")
        self.lo_dscene_upper_btns.addWidget(self.btn_dscene_neuron)
        self.btn_dscene_recorder = QtGui.QToolButton(self.dock_scene_contents)
        self.btn_dscene_recorder.setObjectName("btn_dscene_recorder")
        self.lo_dscene_upper_btns.addWidget(self.btn_dscene_recorder)
        spacerItem4 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lo_dscene_upper_btns.addItem(spacerItem4)
        self.btn_dscene_neuron_data = QtGui.QToolButton(self.dock_scene_contents)
        self.btn_dscene_neuron_data.setObjectName("btn_dscene_neuron_data")
        self.lo_dscene_upper_btns.addWidget(self.btn_dscene_neuron_data)
        self.verticalLayout.addLayout(self.lo_dscene_upper_btns)
        self.lo_dscene_lower_btns = QtGui.QHBoxLayout()
        self.lo_dscene_lower_btns.setObjectName("lo_dscene_lower_btns")
        self.btn_dscene_sc_load = QtGui.QToolButton(self.dock_scene_contents)
        self.btn_dscene_sc_load.setObjectName("btn_dscene_sc_load")
        self.lo_dscene_lower_btns.addWidget(self.btn_dscene_sc_load)
        self.btn_dscene_sc_save = QtGui.QToolButton(self.dock_scene_contents)
        self.btn_dscene_sc_save.setObjectName("btn_dscene_sc_save")
        self.lo_dscene_lower_btns.addWidget(self.btn_dscene_sc_save)
        spacerItem5 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lo_dscene_lower_btns.addItem(spacerItem5)
        self.btn_dscene_remove = QtGui.QToolButton(self.dock_scene_contents)
        self.btn_dscene_remove.setObjectName("btn_dscene_remove")
        self.lo_dscene_lower_btns.addWidget(self.btn_dscene_remove)
        self.btn_dscene_refresh = QtGui.QToolButton(self.dock_scene_contents)
        self.btn_dscene_refresh.setObjectName("btn_dscene_refresh")
        self.lo_dscene_lower_btns.addWidget(self.btn_dscene_refresh)
        self.verticalLayout.addLayout(self.lo_dscene_lower_btns)
        self.dock_scene.setWidget(self.dock_scene_contents)
        SimGui.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_scene)
        self.dockWidget = QtGui.QDockWidget(SimGui)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tre_output = QtGui.QTreeView(self.dockWidgetContents_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tre_output.sizePolicy().hasHeightForWidth())
        self.tre_output.setSizePolicy(sizePolicy)
        self.tre_output.setMinimumSize(QtCore.QSize(250, 150))
        self.tre_output.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tre_output.setTabKeyNavigation(False)
        self.tre_output.setProperty("showDropIndicator", False)
        self.tre_output.setDragDropOverwriteMode(False)
        self.tre_output.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tre_output.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tre_output.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tre_output.setObjectName("tre_output")
        self.verticalLayout_2.addWidget(self.tre_output)
        self.lo_out_lower_btns = QtGui.QHBoxLayout()
        self.lo_out_lower_btns.setObjectName("lo_out_lower_btns")
        self.btn_dio_restart = QtGui.QToolButton(self.dockWidgetContents_3)
        self.btn_dio_restart.setObjectName("btn_dio_restart")
        self.lo_out_lower_btns.addWidget(self.btn_dio_restart)
        spacerItem6 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lo_out_lower_btns.addItem(spacerItem6)
        self.btn_dio_refresh = QtGui.QToolButton(self.dockWidgetContents_3)
        self.btn_dio_refresh.setObjectName("btn_dio_refresh")
        self.lo_out_lower_btns.addWidget(self.btn_dio_refresh)
        self.verticalLayout_2.addLayout(self.lo_out_lower_btns)
        self.dockWidget.setWidget(self.dockWidgetContents_3)
        SimGui.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionAbout = QtGui.QAction(SimGui)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreferences = QtGui.QAction(SimGui)
        self.actionPreferences.setMenuRole(QtGui.QAction.PreferencesRole)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionQuit = QtGui.QAction(SimGui)
        self.actionQuit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_Qt = QtGui.QAction(SimGui)
        self.actionAbout_Qt.setMenuRole(QtGui.QAction.AboutQtRole)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionScene_Manager = QtGui.QAction(SimGui)
        self.actionScene_Manager.setCheckable(True)
        self.actionScene_Manager.setChecked(True)
        self.actionScene_Manager.setMenuRole(QtGui.QAction.ApplicationSpecificRole)
        self.actionScene_Manager.setObjectName("actionScene_Manager")
        self.actionOutput_Manager = QtGui.QAction(SimGui)
        self.actionOutput_Manager.setCheckable(True)
        self.actionOutput_Manager.setChecked(True)
        self.actionOutput_Manager.setMenuRole(QtGui.QAction.ApplicationSpecificRole)
        self.actionOutput_Manager.setObjectName("actionOutput_Manager")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionOutput_Manager)
        self.menuSettings.addAction(self.actionScene_Manager)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionQuit)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.lbl_frame.setBuddy(self.edt_frame)
        self.lbl_frame_size.setBuddy(self.cb_frame_size)
        self.lbl_sample_rate.setBuddy(self.cb_sample_rate)

        self.retranslateUi(SimGui)
        self.cb_frame_size.setCurrentIndex(3)
        self.cb_sample_rate.setCurrentIndex(0)
        QtCore.QObject.connect(self.edt_timer, QtCore.SIGNAL("returnPressed()"), self.btn_timer.click)
        QtCore.QObject.connect(self.edt_steps, QtCore.SIGNAL("returnPressed()"), self.btn_steps.click)
        QtCore.QObject.connect(self.dockWidget, QtCore.SIGNAL("visibilityChanged(bool)"), self.actionOutput_Manager.setChecked)
        QtCore.QObject.connect(self.dock_scene, QtCore.SIGNAL("visibilityChanged(bool)"), self.actionScene_Manager.setChecked)
        QtCore.QObject.connect(self.actionOutput_Manager, QtCore.SIGNAL("toggled(bool)"), self.dockWidget.setVisible)
        QtCore.QObject.connect(self.actionScene_Manager, QtCore.SIGNAL("toggled(bool)"), self.dock_scene.setVisible)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL("triggered()"), SimGui.close)
        QtCore.QObject.connect(self.btn_quit, QtCore.SIGNAL("clicked()"), SimGui.close)
        QtCore.QMetaObject.connectSlotsByName(SimGui)
        SimGui.setTabOrder(self.edt_frame, self.cb_sample_rate)
        SimGui.setTabOrder(self.cb_sample_rate, self.lst_log)
        SimGui.setTabOrder(self.lst_log, self.btn_timer)
        SimGui.setTabOrder(self.btn_timer, self.edt_timer)
        SimGui.setTabOrder(self.edt_timer, self.btn_steps)
        SimGui.setTabOrder(self.btn_steps, self.edt_steps)
        SimGui.setTabOrder(self.edt_steps, self.btn_reset)
        SimGui.setTabOrder(self.btn_reset, self.btn_quit)
        SimGui.setTabOrder(self.btn_quit, self.tre_scene)
        SimGui.setTabOrder(self.tre_scene, self.btn_dscene_neuron)
        SimGui.setTabOrder(self.btn_dscene_neuron, self.btn_dscene_recorder)
        SimGui.setTabOrder(self.btn_dscene_recorder, self.btn_dscene_neuron_data)
        SimGui.setTabOrder(self.btn_dscene_neuron_data, self.btn_dscene_sc_load)
        SimGui.setTabOrder(self.btn_dscene_sc_load, self.btn_dscene_sc_save)
        SimGui.setTabOrder(self.btn_dscene_sc_save, self.btn_dscene_remove)
        SimGui.setTabOrder(self.btn_dscene_remove, self.btn_dscene_refresh)
        SimGui.setTabOrder(self.btn_dscene_refresh, self.tre_output)
        SimGui.setTabOrder(self.tre_output, self.btn_dio_restart)
        SimGui.setTabOrder(self.btn_dio_restart, self.btn_dio_refresh)

    def retranslateUi(self, SimGui):
        SimGui.setWindowTitle(QtGui.QApplication.translate("SimGui", "Neural Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_frame.setText(QtGui.QApplication.translate("SimGui", "Frame:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_frame_size.setText(QtGui.QApplication.translate("SimGui", "Frame Size:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_frame_size.setItemText(0, QtGui.QApplication.translate("SimGui", "128", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_frame_size.setItemText(1, QtGui.QApplication.translate("SimGui", "256", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_frame_size.setItemText(2, QtGui.QApplication.translate("SimGui", "512", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_frame_size.setItemText(3, QtGui.QApplication.translate("SimGui", "1024", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_frame_size.setItemText(4, QtGui.QApplication.translate("SimGui", "2048", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_sample_rate.setText(QtGui.QApplication.translate("SimGui", "Sample Rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_sample_rate.setItemText(0, QtGui.QApplication.translate("SimGui", "1000.0", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_sample_rate.setItemText(1, QtGui.QApplication.translate("SimGui", "2000.0", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_sample_rate.setItemText(2, QtGui.QApplication.translate("SimGui", "4000.0", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_sample_rate.setItemText(3, QtGui.QApplication.translate("SimGui", "8000.0", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_sample_rate.setItemText(4, QtGui.QApplication.translate("SimGui", "16000.0", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_sample_rate.setItemText(5, QtGui.QApplication.translate("SimGui", "24000.0", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_sample_rate.setItemText(6, QtGui.QApplication.translate("SimGui", "32000.0", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_timer.setTitle(QtGui.QApplication.translate("SimGui", "Timer Control", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_timer.setText(QtGui.QApplication.translate("SimGui", "Start Timer", None, QtGui.QApplication.UnicodeUTF8))
        self.edt_timer.setToolTip(QtGui.QApplication.translate("SimGui", "tooltip", None, QtGui.QApplication.UnicodeUTF8))
        self.edt_timer.setStatusTip(QtGui.QApplication.translate("SimGui", "status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.edt_timer.setWhatsThis(QtGui.QApplication.translate("SimGui", "what is this", None, QtGui.QApplication.UnicodeUTF8))
        self.edt_timer.setText(QtGui.QApplication.translate("SimGui", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.gb_steps.setTitle(QtGui.QApplication.translate("SimGui", "Step Control", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_steps.setText(QtGui.QApplication.translate("SimGui", "Step(s)", None, QtGui.QApplication.UnicodeUTF8))
        self.edt_steps.setText(QtGui.QApplication.translate("SimGui", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reset.setText(QtGui.QApplication.translate("SimGui", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setText(QtGui.QApplication.translate("SimGui", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("SimGui", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("SimGui", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.dock_scene.setWindowTitle(QtGui.QApplication.translate("SimGui", "Scene Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dscene_neuron.setText(QtGui.QApplication.translate("SimGui", "NEURON", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dscene_recorder.setText(QtGui.QApplication.translate("SimGui", "RECORDER", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dscene_neuron_data.setText(QtGui.QApplication.translate("SimGui", "Neuron Data", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dscene_sc_load.setText(QtGui.QApplication.translate("SimGui", "load", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dscene_sc_save.setText(QtGui.QApplication.translate("SimGui", "save", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dscene_remove.setText(QtGui.QApplication.translate("SimGui", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dscene_refresh.setText(QtGui.QApplication.translate("SimGui", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("SimGui", "Output Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dio_restart.setText(QtGui.QApplication.translate("SimGui", "RESTART", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_dio_refresh.setText(QtGui.QApplication.translate("SimGui", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("SimGui", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("SimGui", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("SimGui", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Qt.setText(QtGui.QApplication.translate("SimGui", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionScene_Manager.setText(QtGui.QApplication.translate("SimGui", "Scene Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOutput_Manager.setText(QtGui.QApplication.translate("SimGui", "Output Manager", None, QtGui.QApplication.UnicodeUTF8))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SimGui = QtGui.QMainWindow()
    ui = Ui_SimGui()
    ui.setupUi(SimGui)
    SimGui.show()
    sys.exit(app.exec_())

