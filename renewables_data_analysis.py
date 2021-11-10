import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import sqlite3
import pyqtgraph as pg
import numpy as np
import time
from utils import TimeAxisItem, timestamp
from pyqtgraph.Qt import QtCore, QtGui

graph_title = "GeeksforGeeks PyQtGraph"

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI/renewables_data_analysis.ui", self)

        self.wind_energy.clicked.connect(self.load_wind_energy_data)
        self.solar_energy.clicked.connect(self.load_solar_energy_data)
        self.hydro_energy.clicked.connect(self.load_hydro_energy_data)
        self.biomass_energy.clicked.connect(self.load_biomass_energy_data)
        self.geothermal_energy.clicked.connect(self.load_geothermal_energy_data)
        self.top_10_graph.clicked.connect(self.create_graph)
        self.least_10_graph.clicked.connect(self.load_least_10_graph)
        self.load_wind_energy_data()

    def load(self):
        self.top_10_area.clear()

    def load_wind_energy_data(self):
        connection = sqlite3.connect("Data/Renewable_Energy_Sources.db")
        cur = connection.cursor()

        # comboBox
        """comboBoxQuery1 = "SELECT country FROM 'annual-percentage-change-wind'";
        for item in list(set(cur.execute(comboBoxQuery1))):
            self.comboBox1.addItem(item[0])"""
        # RE1 table 1
        top_10_query = "SELECT country, year, growth FROM 'annual-percentage-change-wind' ORDER BY growth DESC LIMIT 10"
        self.top_10_area.setRowCount(10)
        top_10_row_counter = 0
        for top_10 in cur.execute(top_10_query):
            # print(row)
            self.top_10_area.setItem(top_10_row_counter, 0, QtWidgets.QTableWidgetItem(str(top_10[0])))
            self.top_10_area.setItem(top_10_row_counter, 1, QtWidgets.QTableWidgetItem(str(top_10[1])))
            self.top_10_area.setItem(top_10_row_counter, 2, QtWidgets.QTableWidgetItem(str(top_10[2])))
            top_10_row_counter += 1

        # RE1 table 2
        least_10_query = "SELECT country, year, growth FROM 'annual-percentage-change-wind' ORDER BY growth ASC LIMIT 10"
        self.least_10_area.setRowCount(10)
        least_10_row_counter = 0
        for least_10 in cur.execute(least_10_query):
            # print(row)
            self.least_10_area.setItem(least_10_row_counter, 0, QtWidgets.QTableWidgetItem(str(least_10[0])))
            self.least_10_area.setItem(least_10_row_counter, 1, QtWidgets.QTableWidgetItem(str(least_10[1])))
            self.least_10_area.setItem(least_10_row_counter, 2, QtWidgets.QTableWidgetItem(str(least_10[2])))
            least_10_row_counter += 1

    def load_solar_energy_data(self):
        connection = sqlite3.connect("Data/Renewable_Energy_Sources.db")
        cur = connection.cursor()

        top_10_query = "SELECT Entity, Year, Solar FROM 'annual-percentage-change-solar' ORDER BY Solar DESC LIMIT 10"
        self.top_10_area.setRowCount(10)
        top_10_row_counter = 0
        for row in cur.execute(top_10_query):
            # print(row)
            self.top_10_area.setItem(top_10_row_counter, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.top_10_area.setItem(top_10_row_counter, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.top_10_area.setItem(top_10_row_counter, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            top_10_row_counter += 1

        # RE1 table 2
        least_10_query = "SELECT Entity, Year, Solar FROM 'annual-percentage-change-solar' ORDER BY Solar ASC LIMIT 10"
        self.least_10_area.setRowCount(10)
        least_10_row_counter = 0
        for row in cur.execute(least_10_query):
            # print(row)
            self.least_10_area.setItem(least_10_row_counter, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.least_10_area.setItem(least_10_row_counter, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.least_10_area.setItem(least_10_row_counter, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            least_10_row_counter += 1

    def load_hydro_energy_data(self):
        connection = sqlite3.connect("Data/Renewable_Energy_Sources.db")
        cur = connection.cursor()
        top_10_query = "SELECT Country, Year, Hydro FROM 'annual-percentage-change-hydro' ORDER BY Hydro DESC LIMIT 10"
        self.top_10_area.setRowCount(10)
        top_10_row_counter = 0
        for row in cur.execute(top_10_query):
            # print(row)
            self.top_10_area.setItem(top_10_row_counter, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.top_10_area.setItem(top_10_row_counter, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.top_10_area.setItem(top_10_row_counter, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            top_10_row_counter += 1

        # RE1 table 2
        least_10_query = "SELECT Country, Year, Hydro FROM 'annual-percentage-change-hydro' ORDER BY Hydro ASC LIMIT 10"
        self.least_10_area.setRowCount(10)
        least_10_row_counter = 0
        for row in cur.execute(least_10_query):
            # print(row)
            self.least_10_area.setItem(least_10_row_counter, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.least_10_area.setItem(least_10_row_counter, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.least_10_area.setItem(least_10_row_counter, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            least_10_row_counter += 1

    def load_biomass_energy_data(self):
        connection = sqlite3.connect("Data/Renewable_Energy_Sources.db")
        cur = connection.cursor()
        self.top_10_area.setRowCount(10)
        top_10_row_counter = 0
        for row in range(10):
            # print(row)
            self.top_10_area.setItem(top_10_row_counter, 0, QtWidgets.QTableWidgetItem(str("")))
            self.top_10_area.setItem(top_10_row_counter, 1, QtWidgets.QTableWidgetItem(str("")))
            self.top_10_area.setItem(top_10_row_counter, 2, QtWidgets.QTableWidgetItem(str("")))
            top_10_row_counter += 1

        # RE1 table 2
        least_10_query = "SELECT Country, Year, Hydro FROM 'annual-percentage-change-hydro' ORDER BY Hydro ASC LIMIT 10"
        self.least_10_area.setRowCount(10)
        least_10_row_counter = 0
        for row in range(10):
            # print(row)
            self.least_10_area.setItem(least_10_row_counter, 0, QtWidgets.QTableWidgetItem(str("")))
            self.least_10_area.setItem(least_10_row_counter, 1, QtWidgets.QTableWidgetItem(str("")))
            self.least_10_area.setItem(least_10_row_counter, 2, QtWidgets.QTableWidgetItem(str("")))
            least_10_row_counter += 1

    def load_geothermal_energy_data(self):
        connection = sqlite3.connect("Data/Renewable_Energy_Sources.db")
        cur = connection.cursor()
        self.top_10_area.setRowCount(10)
        top_10_row_counter = 0
        for row in range(10):
            # print(row)
            self.top_10_area.setItem(top_10_row_counter, 0, QtWidgets.QTableWidgetItem(str("")))
            self.top_10_area.setItem(top_10_row_counter, 1, QtWidgets.QTableWidgetItem(str("")))
            self.top_10_area.setItem(top_10_row_counter, 2, QtWidgets.QTableWidgetItem(str("")))
            top_10_row_counter += 1

        # RE1 table 2
        self.least_10_area.setRowCount(10)
        least_10_row_counter = 0
        for row in range(10):
            # print(row)
            self.least_10_area.setItem(least_10_row_counter, 0, QtWidgets.QTableWidgetItem(str("")))
            self.least_10_area.setItem(least_10_row_counter, 1, QtWidgets.QTableWidgetItem(str("")))
            self.least_10_area.setItem(least_10_row_counter, 2, QtWidgets.QTableWidgetItem(str("")))
            least_10_row_counter += 1

    def load_top_10_graph(self):
        self.top_10_area.clearContents()

    def load_least_10_graph(self):
        self.least_10_area.clearContents()

    def create_graph(self):
        title = "GeeksforGeeks PyQtGraph"

        connection = sqlite3.connect("Data/Renewable_Energy_Sources.db")
        cur = connection.cursor()

        # comboBox
        """comboBoxQuery1 = "SELECT country FROM 'annual-percentage-change-wind'";
        for item in list(set(cur.execute(comboBoxQuery1))):
            self.comboBox1.addItem(item[0])"""
        # RE1 table 1
        all_wind_energy_query = "SELECT country, year, growth FROM " \
                                "'annual-percentage-change-wind' " \
                                "where country in ('Australia','Canada','India','United States','Germany','United Kingdom','World') " \

        all_data = []

        for data in cur.execute(all_wind_energy_query):
            all_data.append(data)

        # filter all greater than 400%
        all_data = list(filter(lambda value: value[2] < 400, all_data))

        import itertools
        import operator
        import random

        widget = pg.PlotWidget()
        widget.showGrid(x=True, y=True)

        for key,group in itertools.groupby(all_data,operator.itemgetter(0)):
            group_list = list(group)
            growth = list(map(lambda x:x[2], group_list))
            years = list(map(lambda x:x[1], group_list))
            name = group_list[0][0]
            widget.plot(years,
                        growth,
                        pen=(random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                        name=name)


        widget.setWindowTitle('Renewables Energy Data Analysis')
        widget.show()

        pg.plot(widget)


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(900)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Existing")
