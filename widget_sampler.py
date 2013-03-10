from PyQt4 import QtGui, QtCore
import preferences
from logger import log
Preferences = preferences.Preferences.Instance

## A node used to indicate the edges of the TV
class SamplerBoundsNode(QtGui.QGraphicsItem):
    Type = QtGui.QGraphicsItem.UserType + 1

    def __init__(self, pos=(0, 0)):
        super(SamplerBoundsNode, self).__init__()
        self.size = 12
        self.borderSize = 2

        # Clamp pos and set
        pos[0] = max(0, min(1, pos[0]))
        pos[1] = max(0, min(1, pos[1]))
        log.debug("...adding bounds node with position " + str(pos))
        self.setPos(pos[0], pos[1])

        # Item is movable with mouse
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(QtGui.QGraphicsItem.DeviceCoordinateCache)
        self.setZValue(2)

    def type(self):
        return SamplerBoundsNode.Type

    def paint(self, painter, option, widget):
        painter.setPen(QtCore.Qt.NoPen)

        if option.state & QtGui.QStyle.State_Sunken:
            painter.setBrush(QtCore.Qt.red)
            painter.drawEllipse(-self.size/2.0 - self.borderSize,
                                -self.size/2.0 - self.borderSize,
                                self.size + self.borderSize*2.0,
                                self.size + self.borderSize*2.0)

        painter.setBrush(QtCore.Qt.white)
        painter.drawEllipse(-self.size/2.0, -self.size/2.0, self.size, self.size)

    def boundingRect(self):
        return QtCore.QRectF(-self.size/2.0 - self.borderSize/2.0,
                             -self.size/2.0 - self.borderSize/2.0,
                             self.size + self.borderSize,
                             self.size + self.borderSize)

    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL("moved(bool)"), False)
        super(SamplerBoundsNode, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.emit(QtCore.SIGNAL("moved(bool)"), False)
        super(SamplerBoundsNode, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.emit(QtCore.SIGNAL("moved(bool)"), True)
        super(SamplerBoundsNode, self).mouseReleaseEvent(event)


## A line between two nodes
class SamplerBoundsNodeConnection(QtGui.QGraphicsItem):
    Type = QtGui.QGraphicsItem.UserType + 2

    def __init__(self, startNode, endNode):
        super(SamplerBoundsNodeConnection, self).__init__()
        self.setZValue(1)
        self.startNode = startNode
        self.endNode = endNode

    def type(self):
        return SamplerBoundsNodeConnection.Type

    def paint(self, painter, option, widget):
        if self.startNode is None or self.endNode is None:
            return

        # Create a line
        line = QtCore.QLineF(self.startNode.pos(), self.endNode.pos())
        if line.length() == 0.0:
            return

        # Draw the line
        painter.setPen(QtGui.QPen(QtCore.Qt.white, 3, QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawLine(line)

    def boundingRect(self):
        penWidth = 2.0
        extra = penWidth / 2.0
        return QtCore.QRectF(self.startNode.pos(),
                QtCore.QSizeF(self.endNode.x() - self.startNode.x(),
                        self.endNode.y() - self.startNode.y())).normalized().adjusted(-extra, -extra, extra, extra)

## Contains the nodes and lines
class SamplerNodesContainer(QtGui.QGraphicsView):
    def __init__(self, parent):
        super(SamplerNodesContainer, self).__init__(parent)
        self.setStyleSheet("SamplerNodesContainer { background: transparent; border: 0; }")

        self.scene = QtGui.QGraphicsScene(self)
        self.scene.setItemIndexMethod(QtGui.QGraphicsScene.NoIndex)
        self.scene.setSceneRect(0, 0, parent.width(), parent.height())
        self.setScene(self.scene)
        self.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QtGui.QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)

        # 4 Nodes
        self.nodes = []
        self.topLeft = self.addNode(Preferences.boundsTopLeft)
        self.topRight = self.addNode(Preferences.boundsTopRight)
        self.bottomRight = self.addNode(Preferences.boundsBottomRight)
        self.bottomLeft = self.addNode(Preferences.boundsBottomLeft)

        # Lines
        self.lines = []
        self.addConnectionLine(self.topLeft, self.topRight)
        self.addConnectionLine(self.topRight, self.bottomRight)
        self.addConnectionLine(self.bottomRight, self.bottomLeft)
        self.addConnectionLine(self.bottomLeft, self.topLeft)

    def addNode(self, position):
        node = SamplerBoundsNode(position)
        self.nodes.append(node)
        self.scene.addItem(node)
        #QtCore.QObject.connect(node, QtCore.SIGNAL('moved(bool)'), self.on_nodeMoved)
        return node

    def addConnectionLine(self, startNode, endNode):
        line = SamplerBoundsNodeConnection(startNode, endNode)
        self.lines.append(line)
        self.scene.addItem(line)
        return line

    def on_nodeMoved(self, finishedMoving):
        print("node moved!")

    def setBounds(self, topLeft, topRight, bottomRight, bottomLeft):
        self.topLeft.setPos(topLeft[0], topLeft[1])
        self.topRight.setPos(topRight[0], topRight[1])
        self.bottomRight.setPos(bottomRight[0], bottomRight[1])
        self.bottomLeft.setPos(bottomLeft[0], bottomLeft[1])



class Sampler(QtGui.QLabel):
    def __init__(self):
        super(Sampler, self).__init__()
        log.info("Initializing Sampler")

        self.setMinimumSize(640, 480)

        self.bgPixmap = QtGui.QPixmap(640, 480)
        self.bgPixmap.fill(QtCore.Qt.black)
        self.setScaledContents(True)
        self.nodesContainer = SamplerNodesContainer(self)
        self.setFrame(None, 0, 0)

    def setFrame(self, buffer, bufferWidth, bufferHeight):
        if buffer is None:
            self.setPixmap(self.bgPixmap)
            return

        image = QtGui.QImage(buffer, bufferWidth, bufferHeight, 0, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap(pixmap)