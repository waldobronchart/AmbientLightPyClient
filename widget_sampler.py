from PyQt4 import QtGui, QtCore
import preferences
from logger import log
Preferences = preferences.Preferences.Instance

## A node used to indicate the edges of the TV
class SamplerBoundsNode(QtGui.QGraphicsItem):
    Type = QtGui.QGraphicsItem.UserType + 1

    def __init__(self, parent, pos, limitRect):
        super(SamplerBoundsNode, self).__init__()
        self.size = 12
        self.borderSize = 2
        self.container = parent

        # Clamp pos and set
        log.debug("...adding bounds node with position " + str(pos))
        self.setPos(pos[0], pos[1])
        self.limitRect = limitRect
        self.limitPosition()

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
        self.container.nodeMovedCallback(self, False)
        self.update()
        super(SamplerBoundsNode, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.container.nodeMovedCallback(self, False)
        self.update()
        super(SamplerBoundsNode, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.limitPosition()
        self.container.nodeMovedCallback(self, True)
        self.update()
        super(SamplerBoundsNode, self).mouseReleaseEvent(event)

    def limitPosition(self):
        pos = self.pos()
        if not self.limitRect.contains(pos):
            pos.setX(min(max(self.limitRect.x(), pos.x()), self.limitRect.right()))
            pos.setY(min(max(self.limitRect.y(), pos.y()), self.limitRect.bottom()))
            self.setPos(pos)


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
    nodesMoved = QtCore.pyqtSignal(bool)

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

        hWidth = parent.width()/2
        hHeight = parent.height()/2
        pad = 10

        # 4 Nodes
        self.nodes = []
        self.topLeft = self._addNode(Preferences.boundsTopLeft, QtCore.QRectF(pad, pad, hWidth-pad*2, hHeight-pad*2))
        self.topRight = self._addNode(Preferences.boundsTopRight, QtCore.QRectF(hWidth+pad, pad, hWidth-pad*2, hHeight-pad*2))
        self.bottomRight = self._addNode(Preferences.boundsBottomRight, QtCore.QRectF(hWidth+pad, hHeight+pad, hWidth-pad*2, hHeight-pad*2))
        self.bottomLeft = self._addNode(Preferences.boundsBottomLeft, QtCore.QRectF(pad, hHeight+pad, hWidth-pad*2, hHeight-pad*2))

        # Lines
        self.lines = []
        self._addConnectionLine(self.topLeft, self.topRight)
        self._addConnectionLine(self.topRight, self.bottomRight)
        self._addConnectionLine(self.bottomRight, self.bottomLeft)
        self._addConnectionLine(self.bottomLeft, self.topLeft)

    def nodeMovedCallback(self, node, finishedMoving):
        for line in self.lines:
            line.update()
        self.nodesMoved.emit(finishedMoving)
        
    def normalizedPosToPixel(self, pos):
        # Clamp between [0, 1]
        pos[0] = max(0, min(1, pos[0]))
        pos[1] = max(0, min(1, pos[1]))
        return [pos[0] * self.scene.width(), pos[1] * self.scene.height()]

    def _addNode(self, normalizedPos, limitRect):
        node = SamplerBoundsNode(self, self.normalizedPosToPixel(normalizedPos), limitRect)
        self.nodes.append(node)
        self.scene.addItem(node)
        return node

    def _addConnectionLine(self, startNode, endNode):
        line = SamplerBoundsNodeConnection(startNode, endNode)
        self.lines.append(line)
        self.scene.addItem(line)
        return line

    def setBounds(self, topLeft, topRight, bottomRight, bottomLeft):
        self.topLeft.setPos(topLeft[0], topLeft[1])
        self.topRight.setPos(topRight[0], topRight[1])
        self.bottomRight.setPos(bottomRight[0], bottomRight[1])
        self.bottomLeft.setPos(bottomLeft[0], bottomLeft[1])



class Sampler(QtGui.QLabel):
    nodesUpdated = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(Sampler, self).__init__(parent)
        log.info("Initializing Sampler")

        self.setMinimumSize(640, 480)

        self.bgPixmap = QtGui.QPixmap(640, 480)
        self.bgPixmap.fill(QtGui.QColor("#212426"))
        self.setScaledContents(True)

        self.nodesContainer = SamplerNodesContainer(self)
        self.nodesContainer.nodesMoved.connect(self.on_nodesContainer_nodesMoved)
        self.setFrame(None, 0, 0)

    def setFrame(self, buffer, bufferWidth, bufferHeight):
        if buffer is None:
            self.setPixmap(self.bgPixmap)
            return

        image = QtGui.QImage(buffer, bufferWidth, bufferHeight, 0, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.setPixmap(pixmap)

    def on_nodesContainer_nodesMoved(self, finishedMoving):
        self.update()
        if finishedMoving:
            log.debug("Sampler bounds nodes moved")
            self.nodesUpdated.emit()