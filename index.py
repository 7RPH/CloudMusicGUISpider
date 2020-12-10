from pathlib import Path

from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from selenium import webdriver
from time import sleep
import openpyxl
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from selenium.webdriver.chrome.options import Options

from spiderfunc import *
import spiderfunc
import tes
from tes import *
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()