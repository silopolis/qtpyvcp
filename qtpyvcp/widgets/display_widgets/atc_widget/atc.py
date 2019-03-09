import os

# Workarround for nvidia propietary drivers

import ctypes
import ctypes.util
from pprint import pprint

ctypes.CDLL(ctypes.util.find_library("GL"), mode=ctypes.RTLD_GLOBAL)

# end of Workarround

from qtpy.QtCore import Signal, Slot, QUrl
from qtpy.QtQuickWidgets import QQuickWidget

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger

LOG = logger.getLogger(__name__)
STATUS = getPlugin('status')
TOOLTABLE = getPlugin('tooltable')
IN_DESIGNER = os.getenv('DESIGNER', False)

WIDGET_PATH = os.path.dirname(os.path.abspath(__file__))


class DynATC(QQuickWidget):

    moveToPocketSig = Signal(int, int, arguments=['previous_pocket', 'pocket_num'])
    rotateFwdSig = Signal(int, arguments=['rotate_forward'])
    rotateRevSig = Signal(int, arguments=['rotate_reverse'])

    def __init__(self, parent=None):
        super(DynATC, self).__init__(parent)

        if IN_DESIGNER:
            return

        self.engine().rootContext().setContextProperty("atc_spiner", self)
        url = QUrl.fromLocalFile(os.path.join(WIDGET_PATH, "atc.qml"))
        self.setSource(url)

        self.atc_position = 1

        self.tools = list(STATUS.stat.tool_table)

        STATUS.tool_in_spindle.notify(self.on_tool_in_spindle)
        STATUS.pocket_prepped.notify(self.on_pocket_prepped)

    def on_pocket_prepped(self, pocket_num):
        if pocket_num > 0:
            print("Pocket Prepared: {}".format(pocket_num))
            print("Rotate from pocket {} to {}".format(self.atc_position, pocket_num))
            self.moveToPocketSig.emit(self.atc_position - 1, pocket_num - 1)
            self.atc_position = pocket_num
        else:
            print("Pocket Clear {}".format(pocket_num))

    def on_tool_in_spindle(self, tool_num):
        print("Tool in Spindle: {}".format(tool_num))

    @Slot()
    def rotate_forward(self):
        self.rotateFwdSig.emit(self.atc_position)
        self.atc_position += 1

    @Slot()
    def rotate_reverse(self):
        self.rotateRevSig.emit(self.atc_position)
        self.atc_position -= 1
