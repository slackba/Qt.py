# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QAbstractButton(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None

  class PaintDeviceMetric(object):

    PdmDepth = None
    PdmDpiX = None
    PdmDpiY = None
    PdmHeight = None
    PdmHeightMM = None
    PdmNumColors = None
    PdmPhysicalDpiX = None
    PdmPhysicalDpiY = None
    PdmWidth = None
    PdmWidthMM = None
    name = property(None, None, None,
                    )

    values = {}

  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None

  class RenderFlag(object):

    DrawChildren = None
    DrawWindowBackground = None
    IgnoreMask = None
    name = property(None, None, None,
                    )

    values = {}

  class RenderFlags(object):

    pass

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def animateClick():
    pass

  def autoExclusive():
    pass

  def autoRepeat():
    pass

  def autoRepeatDelay():
    pass

  def autoRepeatInterval():
    pass

  def changeEvent():
    pass

  def checkStateSet():
    pass

  def click():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def group():
    pass

  def hitButton():
    pass

  def icon():
    pass

  def iconSize():
    pass

  def isCheckable():
    pass

  def isChecked():
    pass

  def isDown():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def nextCheckState():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def released():
    """ Signal """
    pass

  def setAutoExclusive():
    pass

  def setAutoRepeat():
    pass

  def setAutoRepeatDelay():
    pass

  def setAutoRepeatInterval():
    pass

  def setCheckable():
    pass

  def setChecked():
    pass

  def setDown():
    pass

  def setIcon():
    pass

  def setIconSize():
    pass

  def setShortcut():
    pass

  def setTabOrder():
    pass

  def setText():
    pass

  def shortcut():
    pass

  staticMetaObject = None

  def text():
    pass

  def timerEvent():
    pass

  def toggle():
    pass

  def toggled():
    """ Signal """
    pass

class QAbstractGraphicsShapeItem(QGraphicsItem):

  class CacheMode(object):

    DeviceCoordinateCache = None
    ItemCoordinateCache = None
    NoCache = None
    name = property(None, None, None,
                    )

    values = {}

  DeviceCoordinateCache = None

  class Extension(object):

    UserExtension = None
    name = property(None, None, None,
                    )

    values = {}

  class GraphicsItemChange(object):

    ItemChildAddedChange = None
    ItemChildRemovedChange = None
    ItemCursorChange = None
    ItemCursorHasChanged = None
    ItemEnabledChange = None
    ItemEnabledHasChanged = None
    ItemFlagsChange = None
    ItemFlagsHaveChanged = None
    ItemMatrixChange = None
    ItemOpacityChange = None
    ItemOpacityHasChanged = None
    ItemParentChange = None
    ItemParentHasChanged = None
    ItemPositionChange = None
    ItemPositionHasChanged = None
    ItemRotationChange = None
    ItemRotationHasChanged = None
    ItemScaleChange = None
    ItemScaleHasChanged = None
    ItemSceneChange = None
    ItemSceneHasChanged = None
    ItemScenePositionHasChanged = None
    ItemSelectedChange = None
    ItemSelectedHasChanged = None
    ItemToolTipChange = None
    ItemToolTipHasChanged = None
    ItemTransformChange = None
    ItemTransformHasChanged = None
    ItemTransformOriginPointChange = None
    ItemTransformOriginPointHasChanged = None
    ItemVisibleChange = None
    ItemVisibleHasChanged = None
    ItemZValueChange = None
    ItemZValueHasChanged = None
    name = property(None, None, None,
                    )

    values = {}

  class GraphicsItemFlag(object):

    ItemAcceptsInputMethod = None
    ItemClipsChildrenToShape = None
    ItemClipsToShape = None
    ItemDoesntPropagateOpacityToChildren = None
    ItemHasNoContents = None
    ItemIgnoresParentOpacity = None
    ItemIgnoresTransformations = None
    ItemIsFocusScope = None
    ItemIsFocusable = None
    ItemIsMovable = None
    ItemIsPanel = None
    ItemIsSelectable = None
    ItemNegativeZStacksBehindParent = None
    ItemSendsGeometryChanges = None
    ItemSendsScenePositionChanges = None
    ItemStacksBehindParent = None
    ItemStopsClickFocusPropagation = None
    ItemStopsFocusHandling = None
    ItemUsesExtendedStyleOption = None
    name = property(None, None, None,
                    )

    values = {}

  class GraphicsItemFlags(object):

    pass

  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None

  class PanelModality(object):

    NonModal = None
    PanelModal = None
    SceneModal = None
    name = property(None, None, None,
                    )

    values = {}

  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def brush():
    pass

  def isObscuredBy():
    pass

  def opaqueArea():
    pass

  def pen():
    pass

  def setBrush():
    pass

  def setPen():
    pass

class QAbstractItemDelegate(QObject):

  EditNextItem = None
  EditPreviousItem = None

  class EndEditHint(object):

    EditNextItem = None
    EditPreviousItem = None
    NoHint = None
    RevertModelCache = None
    SubmitModelCache = None
    name = property(None, None, None,
                    )

    values = {}

  NoHint = None
  RevertModelCache = None
  SubmitModelCache = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def closeEditor():
    """ Signal """
    pass

  def commitData():
    """ Signal """
    pass

  def connect():
    pass

  def createEditor():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editorEvent():
    pass

  def helpEvent():
    pass

  def paint():
    pass

  def registerUserData():
    pass

  def setEditorData():
    pass

  def setModelData():
    pass

  def sizeHint():
    pass

  def sizeHintChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def updateEditorGeometry():
    pass

class QAbstractItemView(QAbstractScrollArea):

  AboveItem = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None

  class CursorAction(object):

    MoveDown = None
    MoveEnd = None
    MoveHome = None
    MoveLeft = None
    MoveNext = None
    MovePageDown = None
    MovePageUp = None
    MovePrevious = None
    MoveRight = None
    MoveUp = None
    name = property(None, None, None,
                    )

    values = {}

  DoubleClicked = None
  DragDrop = None

  class DragDropMode(object):

    DragDrop = None
    DragOnly = None
    DropOnly = None
    InternalMove = None
    NoDragDrop = None
    name = property(None, None, None,
                    )

    values = {}

  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None

  class DropIndicatorPosition(object):

    AboveItem = None
    BelowItem = None
    OnItem = None
    OnViewport = None
    name = property(None, None, None,
                    )

    values = {}

  DropOnly = None
  EditKeyPressed = None

  class EditTrigger(object):

    AllEditTriggers = None
    AnyKeyPressed = None
    CurrentChanged = None
    DoubleClicked = None
    EditKeyPressed = None
    NoEditTriggers = None
    SelectedClicked = None
    name = property(None, None, None,
                    )

    values = {}

  class EditTriggers(object):

    pass

  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  HLine = None
  IgnoreMask = None
  InternalMove = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  class ScrollHint(object):

    EnsureVisible = None
    PositionAtBottom = None
    PositionAtCenter = None
    PositionAtTop = None
    name = property(None, None, None,
                    )

    values = {}

  class ScrollMode(object):

    ScrollPerItem = None
    ScrollPerPixel = None
    name = property(None, None, None,
                    )

    values = {}

  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None

  class SelectionBehavior(object):

    SelectColumns = None
    SelectItems = None
    SelectRows = None
    name = property(None, None, None,
                    )

    values = {}

  class SelectionMode(object):

    ContiguousSelection = None
    ExtendedSelection = None
    MultiSelection = None
    NoSelection = None
    SingleSelection = None
    name = property(None, None, None,
                    )

    values = {}

  class Shadow(object):

    Plain = None
    Raised = None
    Sunken = None
    name = property(None, None, None,
                    )

    values = {}

  Shadow_Mask = None

  class Shape(object):

    Box = None
    HLine = None
    NoFrame = None
    Panel = None
    StyledPanel = None
    VLine = None
    WinPanel = None
    name = property(None, None, None,
                    )

    values = {}

  Shape_Mask = None
  SingleSelection = None

  class State(object):

    AnimatingState = None
    CollapsingState = None
    DragSelectingState = None
    DraggingState = None
    EditingState = None
    ExpandingState = None
    NoState = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleMask(object):

    Shadow_Mask = None
    Shape_Mask = None
    name = property(None, None, None,
                    )

    values = {}

  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def alternatingRowColors():
    pass

  def autoScrollMargin():
    pass

  def clearSelection():
    pass

  def clicked():
    """ Signal """
    pass

  def closeEditor():
    pass

  def closePersistentEditor():
    pass

  def commitData():
    pass

  def connect():
    pass

  def currentChanged():
    pass

  def currentIndex():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def dataChanged():
    pass

  def defaultDropAction():
    pass

  def destroyed():
    """ Signal """
    pass

  def dirtyRegionOffset():
    pass

  def disconnect():
    pass

  def doAutoScroll():
    pass

  def doItemsLayout():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def dragDropMode():
    pass

  def dragDropOverwriteMode():
    pass

  def dragEnabled():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def dropIndicatorPosition():
    pass

  def edit():
    pass

  def editTriggers():
    pass

  def editorDestroyed():
    pass

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def executeDelayedItemsLayout():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def hasAutoScroll():
    pass

  def horizontalOffset():
    pass

  def horizontalScrollMode():
    pass

  def horizontalScrollbarAction():
    pass

  def horizontalScrollbarValueChanged():
    pass

  def iconSize():
    pass

  def indexAt():
    pass

  def indexWidget():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def isIndexHidden():
    pass

  def itemDelegate():
    pass

  def itemDelegateForColumn():
    pass

  def itemDelegateForRow():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def keyboardSearch():
    pass

  def model():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveCursor():
    pass

  def openPersistentEditor():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def resizeEvent():
    pass

  def rootIndex():
    pass

  def rowsAboutToBeRemoved():
    pass

  def rowsInserted():
    pass

  def scheduleDelayedItemsLayout():
    pass

  def scrollDirtyRegion():
    pass

  def scrollTo():
    pass

  def scrollToBottom():
    pass

  def scrollToTop():
    pass

  def selectAll():
    pass

  def selectedIndexes():
    pass

  def selectionBehavior():
    pass

  def selectionChanged():
    pass

  def selectionCommand():
    pass

  def selectionMode():
    pass

  def selectionModel():
    pass

  def setAlternatingRowColors():
    pass

  def setAutoScroll():
    pass

  def setAutoScrollMargin():
    pass

  def setCurrentIndex():
    pass

  def setDefaultDropAction():
    pass

  def setDirtyRegion():
    pass

  def setDragDropMode():
    pass

  def setDragDropOverwriteMode():
    pass

  def setDragEnabled():
    pass

  def setDropIndicatorShown():
    pass

  def setEditTriggers():
    pass

  def setHorizontalScrollMode():
    pass

  def setIconSize():
    pass

  def setIndexWidget():
    pass

  def setItemDelegate():
    pass

  def setItemDelegateForColumn():
    pass

  def setItemDelegateForRow():
    pass

  def setModel():
    pass

  def setRootIndex():
    pass

  def setSelection():
    pass

  def setSelectionBehavior():
    pass

  def setSelectionMode():
    pass

  def setSelectionModel():
    pass

  def setState():
    pass

  def setTabKeyNavigation():
    pass

  def setTabOrder():
    pass

  def setTextElideMode():
    pass

  def setVerticalScrollMode():
    pass

  def showDropIndicator():
    pass

  def sizeHintForColumn():
    pass

  def sizeHintForIndex():
    pass

  def sizeHintForRow():
    pass

  def startAutoScroll():
    pass

  def startDrag():
    pass

  def state():
    pass

  staticMetaObject = None

  def stopAutoScroll():
    pass

  def tabKeyNavigation():
    pass

  def textElideMode():
    pass

  def timerEvent():
    pass

  def update():
    pass

  def updateEditorData():
    pass

  def updateEditorGeometries():
    pass

  def updateGeometries():
    pass

  def verticalOffset():
    pass

  def verticalScrollMode():
    pass

  def verticalScrollbarAction():
    pass

  def verticalScrollbarValueChanged():
    pass

  def viewOptions():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def viewportEvent():
    pass

  def visualRect():
    pass

  def visualRegionForSelection():
    pass

class QAbstractScrollArea(QFrame):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addScrollBarWidget():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def cornerWidget():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def event():
    pass

  def horizontalScrollBar():
    pass

  def horizontalScrollBarPolicy():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def maximumViewportSize():
    pass

  def minimumSizeHint():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def scrollBarWidgets():
    pass

  def scrollContentsBy():
    pass

  def setCornerWidget():
    pass

  def setHorizontalScrollBar():
    pass

  def setHorizontalScrollBarPolicy():
    pass

  def setTabOrder():
    pass

  def setVerticalScrollBar():
    pass

  def setVerticalScrollBarPolicy():
    pass

  def setViewport():
    pass

  def setViewportMargins():
    pass

  def setupViewport():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def verticalScrollBar():
    pass

  def verticalScrollBarPolicy():
    pass

  def viewport():
    pass

  def viewportEvent():
    pass

  def wheelEvent():
    pass

class QAbstractSlider(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  class SliderAction(object):

    SliderMove = None
    SliderNoAction = None
    SliderPageStepAdd = None
    SliderPageStepSub = None
    SliderSingleStepAdd = None
    SliderSingleStepSub = None
    SliderToMaximum = None
    SliderToMinimum = None
    name = property(None, None, None,
                    )

    values = {}

  class SliderChange(object):

    SliderOrientationChange = None
    SliderRangeChange = None
    SliderStepsChange = None
    SliderValueChange = None
    name = property(None, None, None,
                    )

    values = {}

  SliderMove = None
  SliderNoAction = None
  SliderOrientationChange = None
  SliderPageStepAdd = None
  SliderPageStepSub = None
  SliderRangeChange = None
  SliderSingleStepAdd = None
  SliderSingleStepSub = None
  SliderStepsChange = None
  SliderToMaximum = None
  SliderToMinimum = None
  SliderValueChange = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionTriggered():
    """ Signal """
    pass

  def changeEvent():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def hasTracking():
    pass

  def invertedAppearance():
    pass

  def invertedControls():
    pass

  def isSliderDown():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def maximum():
    pass

  def minimum():
    pass

  def mouseGrabber():
    pass

  def orientation():
    pass

  def pageStep():
    pass

  def rangeChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def repeatAction():
    pass

  def setInvertedAppearance():
    pass

  def setInvertedControls():
    pass

  def setMaximum():
    pass

  def setMinimum():
    pass

  def setOrientation():
    pass

  def setPageStep():
    pass

  def setRange():
    pass

  def setRepeatAction():
    pass

  def setSingleStep():
    pass

  def setSliderDown():
    pass

  def setSliderPosition():
    pass

  def setTabOrder():
    pass

  def setTracking():
    pass

  def setValue():
    pass

  def singleStep():
    pass

  def sliderChange():
    pass

  def sliderMoved():
    """ Signal """
    pass

  def sliderPosition():
    pass

  def sliderPressed():
    """ Signal """
    pass

  def sliderReleased():
    """ Signal """
    pass

  staticMetaObject = None

  def timerEvent():
    pass

  def triggerAction():
    pass

  def value():
    pass

  def valueChanged():
    """ Signal """
    pass

  def wheelEvent():
    pass

class QAbstractSpinBox(QWidget):

  class ButtonSymbols(object):

    NoButtons = None
    PlusMinus = None
    UpDownArrows = None
    name = property(None, None, None,
                    )

    values = {}

  CorrectToNearestValue = None
  CorrectToPreviousValue = None

  class CorrectionMode(object):

    CorrectToNearestValue = None
    CorrectToPreviousValue = None
    name = property(None, None, None,
                    )

    values = {}

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  NoButtons = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  PlusMinus = None
  StepDownEnabled = None

  class StepEnabled(object):

    pass

  class StepEnabledFlag(object):

    StepDownEnabled = None
    StepNone = None
    StepUpEnabled = None
    name = property(None, None, None,
                    )

    values = {}

  StepNone = None
  StepUpEnabled = None
  UpDownArrows = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def buttonSymbols():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def correctionMode():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editingFinished():
    """ Signal """
    pass

  def event():
    pass

  def fixup():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def hasAcceptableInput():
    pass

  def hasFrame():
    pass

  def hideEvent():
    pass

  def initStyleOption():
    pass

  def inputMethodQuery():
    pass

  def interpretText():
    pass

  def isAccelerated():
    pass

  def isReadOnly():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def keyboardGrabber():
    pass

  def keyboardTracking():
    pass

  def lineEdit():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def selectAll():
    pass

  def setAccelerated():
    pass

  def setAlignment():
    pass

  def setButtonSymbols():
    pass

  def setCorrectionMode():
    pass

  def setFrame():
    pass

  def setKeyboardTracking():
    pass

  def setLineEdit():
    pass

  def setReadOnly():
    pass

  def setSpecialValueText():
    pass

  def setTabOrder():
    pass

  def setWrapping():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  def specialValueText():
    pass

  staticMetaObject = None

  def stepBy():
    pass

  def stepDown():
    pass

  def stepEnabled():
    pass

  def stepUp():
    pass

  def text():
    pass

  def timerEvent():
    pass

  def validate():
    pass

  def wheelEvent():
    pass

  def wrapping():
    pass

class QAction(QObject):

  AboutQtRole = None
  AboutRole = None

  class ActionEvent(object):

    Hover = None
    Trigger = None
    name = property(None, None, None,
                    )

    values = {}

  ApplicationSpecificRole = None
  HighPriority = None
  Hover = None
  LowPriority = None

  class MenuRole(object):

    AboutQtRole = None
    AboutRole = None
    ApplicationSpecificRole = None
    NoRole = None
    PreferencesRole = None
    QuitRole = None
    TextHeuristicRole = None
    name = property(None, None, None,
                    )

    values = {}

  NegativeSoftKey = None
  NoRole = None
  NoSoftKey = None
  NormalPriority = None
  PositiveSoftKey = None
  PreferencesRole = None

  class Priority(object):

    HighPriority = None
    LowPriority = None
    NormalPriority = None
    name = property(None, None, None,
                    )

    values = {}

  QuitRole = None
  SelectSoftKey = None

  class SoftKeyRole(object):

    NegativeSoftKey = None
    NoSoftKey = None
    PositiveSoftKey = None
    SelectSoftKey = None
    name = property(None, None, None,
                    )

    values = {}

  TextHeuristicRole = None
  Trigger = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionGroup():
    pass

  def activate():
    pass

  def activated():
    """ Signal """
    pass

  def associatedGraphicsWidgets():
    pass

  def associatedWidgets():
    pass

  def autoRepeat():
    pass

  def changed():
    """ Signal """
    pass

  def connect():
    pass

  def data():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def font():
    pass

  def hover():
    pass

  def hovered():
    """ Signal """
    pass

  def icon():
    pass

  def iconText():
    pass

  def isCheckable():
    pass

  def isChecked():
    pass

  def isEnabled():
    pass

  def isIconVisibleInMenu():
    pass

  def isSeparator():
    pass

  def isVisible():
    pass

  def menu():
    pass

  def menuRole():
    pass

  def parentWidget():
    pass

  def priority():
    pass

  def registerUserData():
    pass

  def setActionGroup():
    pass

  def setAutoRepeat():
    pass

  def setCheckable():
    pass

  def setChecked():
    pass

  def setData():
    pass

  def setDisabled():
    pass

  def setEnabled():
    pass

  def setFont():
    pass

  def setIcon():
    pass

  def setIconText():
    pass

  def setIconVisibleInMenu():
    pass

  def setMenu():
    pass

  def setMenuRole():
    pass

  def setPriority():
    pass

  def setSeparator():
    pass

  def setShortcut():
    pass

  def setShortcutContext():
    pass

  def setShortcuts():
    pass

  def setSoftKeyRole():
    pass

  def setStatusTip():
    pass

  def setText():
    pass

  def setToolTip():
    pass

  def setVisible():
    pass

  def setWhatsThis():
    pass

  def shortcut():
    pass

  def shortcutContext():
    pass

  def shortcuts():
    pass

  def showStatusText():
    pass

  def softKeyRole():
    pass

  staticMetaObject = None

  def statusTip():
    pass

  def text():
    pass

  def toggle():
    pass

  def toggled():
    """ Signal """
    pass

  def toolTip():
    pass

  def trigger():
    pass

  def triggered():
    """ Signal """
    pass

  def whatsThis():
    pass

class QActionGroup(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actions():
    pass

  def addAction():
    pass

  def checkedAction():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def hovered():
    """ Signal """
    pass

  def isEnabled():
    pass

  def isExclusive():
    pass

  def isVisible():
    pass

  def registerUserData():
    pass

  def removeAction():
    pass

  def selected():
    """ Signal """
    pass

  def setDisabled():
    pass

  def setEnabled():
    pass

  def setExclusive():
    pass

  def setVisible():
    pass

  staticMetaObject = None

  def triggered():
    """ Signal """
    pass

class QApplication(QCoreApplication):

  ApplicationFlags = 17041413
  CodecForTr = None

  class ColorSpec(object):

    CustomColor = None
    ManyColor = None
    NormalColor = None
    name = property(None, None, None,
                    )

    values = {}

  CustomColor = None
  DefaultCodec = None

  class Encoding(object):

    CodecForTr = None
    DefaultCodec = None
    UnicodeUTF8 = None
    name = property(None, None, None,
                    )

    values = {}

  GuiClient = None
  GuiServer = None
  ManyColor = None
  NormalColor = None
  Tty = None

  class Type(object):

    GuiClient = None
    GuiServer = None
    Tty = None
    name = property(None, None, None,
                    )

    values = {}

  UnicodeUTF8 = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutQt():
    pass

  def aboutToQuit():
    """ Signal """
    pass

  def activeModalWidget():
    pass

  def activePopupWidget():
    pass

  def activeWindow():
    pass

  def addLibraryPath():
    pass

  def alert():
    pass

  def allWidgets():
    pass

  def applicationDirPath():
    pass

  def applicationFilePath():
    pass

  def applicationName():
    pass

  def applicationPid():
    pass

  def applicationVersion():
    pass

  def arguments():
    pass

  def autoSipEnabled():
    pass

  def beep():
    pass

  def changeOverrideCursor():
    pass

  def clipboard():
    pass

  def closeAllWindows():
    pass

  def closingDown():
    pass

  def colorSpec():
    pass

  def commitData():
    pass

  def commitDataRequest():
    """ Signal """
    pass

  def connect():
    pass

  def cursorFlashTime():
    pass

  def desktop():
    pass

  def desktopSettingsAware():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doubleClickInterval():
    pass

  def event():
    pass

  def exec_():
    pass

  def exit():
    pass

  def flush():
    pass

  def focusChanged():
    """ Signal """
    pass

  def focusWidget():
    pass

  def font():
    pass

  def fontDatabaseChanged():
    """ Signal """
    pass

  def fontMetrics():
    pass

  def globalStrut():
    pass

  def hasPendingEvents():
    pass

  def inputContext():
    pass

  def installTranslator():
    pass

  def instance():
    pass

  def isEffectEnabled():
    pass

  def isLeftToRight():
    pass

  def isRightToLeft():
    pass

  def isSessionRestored():
    pass

  def keyboardInputDirection():
    pass

  def keyboardInputInterval():
    pass

  def keyboardInputLocale():
    pass

  def keyboardModifiers():
    pass

  def lastWindowClosed():
    """ Signal """
    pass

  def layoutDirection():
    pass

  def libraryPaths():
    pass

  def mouseButtons():
    pass

  def notify():
    pass

  def organizationDomain():
    pass

  def organizationName():
    pass

  def overrideCursor():
    pass

  def palette():
    pass

  def postEvent():
    pass

  def processEvents():
    pass

  def queryKeyboardModifiers():
    pass

  def quit():
    pass

  def quitOnLastWindowClosed():
    pass

  def registerUserData():
    pass

  def removeLibraryPath():
    pass

  def removePostedEvents():
    pass

  def removeTranslator():
    pass

  def restoreOverrideCursor():
    pass

  def saveState():
    pass

  def saveStateRequest():
    """ Signal """
    pass

  def sendEvent():
    pass

  def sendPostedEvents():
    pass

  def sessionId():
    pass

  def sessionKey():
    pass

  def setActiveWindow():
    pass

  def setApplicationName():
    pass

  def setApplicationVersion():
    pass

  def setAttribute():
    pass

  def setAutoSipEnabled():
    pass

  def setColorSpec():
    pass

  def setCursorFlashTime():
    pass

  def setDesktopSettingsAware():
    pass

  def setDoubleClickInterval():
    pass

  def setEffectEnabled():
    pass

  def setFont():
    pass

  def setGlobalStrut():
    pass

  def setGraphicsSystem():
    pass

  def setInputContext():
    pass

  def setKeyboardInputInterval():
    pass

  def setLayoutDirection():
    pass

  def setLibraryPaths():
    pass

  def setOrganizationDomain():
    pass

  def setOrganizationName():
    pass

  def setOverrideCursor():
    pass

  def setPalette():
    pass

  def setQuitOnLastWindowClosed():
    pass

  def setStartDragDistance():
    pass

  def setStartDragTime():
    pass

  def setStyle():
    pass

  def setStyleSheet():
    pass

  def setWheelScrollLines():
    pass

  def setWindowIcon():
    pass

  def startDragDistance():
    pass

  def startDragTime():
    pass

  def startingUp():
    pass

  staticMetaObject = None

  def style():
    pass

  def styleSheet():
    pass

  def syncX():
    pass

  def testAttribute():
    pass

  def topLevelAt():
    pass

  def topLevelWidgets():
    pass

  def translate():
    pass

  def type():
    pass

  def unixSignal():
    """ Signal """
    pass

  def wheelScrollLines():
    pass

  def widgetAt():
    pass

  def winFocus():
    pass

  def winMouseButtonUp():
    pass

  def windowIcon():
    pass

class QBoxLayout(QLayout):

  BottomToTop = None

  class Direction(object):

    BottomToTop = None
    Down = None
    LeftToRight = None
    RightToLeft = None
    TopToBottom = None
    Up = None
    name = property(None, None, None,
                    )

    values = {}

  Down = None
  LeftToRight = None
  RightToLeft = None
  SetDefaultConstraint = None
  SetFixedSize = None
  SetMaximumSize = None
  SetMinAndMaxSize = None
  SetMinimumSize = None
  SetNoConstraint = None

  class SizeConstraint(object):

    SetDefaultConstraint = None
    SetFixedSize = None
    SetMaximumSize = None
    SetMinAndMaxSize = None
    SetMinimumSize = None
    SetNoConstraint = None
    name = property(None, None, None,
                    )

    values = {}

  TopToBottom = None
  Up = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addItem():
    pass

  def addLayout():
    pass

  def addSpacerItem():
    pass

  def addSpacing():
    pass

  def addStretch():
    pass

  def addStrut():
    pass

  def addWidget():
    pass

  def closestAcceptableSize():
    pass

  def connect():
    pass

  def count():
    pass

  def destroyed():
    """ Signal """
    pass

  def direction():
    pass

  def disconnect():
    pass

  def expandingDirections():
    pass

  def hasHeightForWidth():
    pass

  def heightForWidth():
    pass

  def insertItem():
    pass

  def insertLayout():
    pass

  def insertSpacerItem():
    pass

  def insertSpacing():
    pass

  def insertStretch():
    pass

  def insertWidget():
    pass

  def invalidate():
    pass

  def itemAt():
    pass

  def maximumSize():
    pass

  def minimumHeightForWidth():
    pass

  def minimumSize():
    pass

  def registerUserData():
    pass

  def setDirection():
    pass

  def setGeometry():
    pass

  def setSpacing():
    pass

  def setStretch():
    pass

  def setStretchFactor():
    pass

  def sizeHint():
    pass

  def spacing():
    pass

  staticMetaObject = None

  def stretch():
    pass

  def takeAt():
    pass

class QButtonGroup(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addButton():
    pass

  def button():
    pass

  def buttonClicked():
    """ Signal """
    pass

  def buttonPressed():
    """ Signal """
    pass

  def buttonReleased():
    """ Signal """
    pass

  def buttons():
    pass

  def checkedButton():
    pass

  def checkedId():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def exclusive():
    pass

  def id():
    pass

  def registerUserData():
    pass

  def removeButton():
    pass

  def setExclusive():
    pass

  def setId():
    pass

  staticMetaObject = None

class QCalendarWidget(QWidget):

  DrawChildren = None
  DrawWindowBackground = None

  class HorizontalHeaderFormat(object):

    LongDayNames = None
    NoHorizontalHeader = None
    ShortDayNames = None
    SingleLetterDayNames = None
    name = property(None, None, None,
                    )

    values = {}

  ISOWeekNumbers = None
  IgnoreMask = None
  LongDayNames = None
  NoHorizontalHeader = None
  NoSelection = None
  NoVerticalHeader = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  class SelectionMode(object):

    NoSelection = None
    SingleSelection = None
    name = property(None, None, None,
                    )

    values = {}

  ShortDayNames = None
  SingleLetterDayNames = None
  SingleSelection = None

  class VerticalHeaderFormat(object):

    ISOWeekNumbers = None
    NoVerticalHeader = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def currentPageChanged():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def dateEditAcceptDelay():
    pass

  def dateTextFormat():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def firstDayOfWeek():
    pass

  def headerTextFormat():
    pass

  def horizontalHeaderFormat():
    pass

  def isDateEditEnabled():
    pass

  def isGridVisible():
    pass

  def isNavigationBarVisible():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def maximumDate():
    pass

  def minimumDate():
    pass

  def minimumSizeHint():
    pass

  def monthShown():
    pass

  def mouseGrabber():
    pass

  def mousePressEvent():
    pass

  def paintCell():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def selectedDate():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def selectionMode():
    pass

  def setCurrentPage():
    pass

  def setDateEditAcceptDelay():
    pass

  def setDateEditEnabled():
    pass

  def setDateRange():
    pass

  def setDateTextFormat():
    pass

  def setFirstDayOfWeek():
    pass

  def setGridVisible():
    pass

  def setHeaderTextFormat():
    pass

  def setHorizontalHeaderFormat():
    pass

  def setMaximumDate():
    pass

  def setMinimumDate():
    pass

  def setNavigationBarVisible():
    pass

  def setSelectedDate():
    pass

  def setSelectionMode():
    pass

  def setTabOrder():
    pass

  def setVerticalHeaderFormat():
    pass

  def setWeekdayTextFormat():
    pass

  def showNextMonth():
    pass

  def showNextYear():
    pass

  def showPreviousMonth():
    pass

  def showPreviousYear():
    pass

  def showSelectedDate():
    pass

  def showToday():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def updateCell():
    pass

  def updateCells():
    pass

  def verticalHeaderFormat():
    pass

  def weekdayTextFormat():
    pass

  def yearShown():
    pass

class QCheckBox(QAbstractButton):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def checkState():
    pass

  def checkStateSet():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def hitButton():
    pass

  def initStyleOption():
    pass

  def isTristate():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def nextCheckState():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def released():
    """ Signal """
    pass

  def setCheckState():
    pass

  def setTabOrder():
    pass

  def setTristate():
    pass

  def sizeHint():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def toggled():
    """ Signal """
    pass

class QColorDialog(QDialog):

  Accepted = None

  class ColorDialogOption(object):

    DontUseNativeDialog = None
    NoButtons = None
    ShowAlphaChannel = None
    name = property(None, None, None,
                    )

    values = {}

  class ColorDialogOptions(object):

    pass

  class DialogCode(object):

    Accepted = None
    Rejected = None
    name = property(None, None, None,
                    )

    values = {}

  DontUseNativeDialog = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  NoButtons = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rejected = None
  ShowAlphaChannel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def changeEvent():
    pass

  def colorSelected():
    """ Signal """
    pass

  def connect():
    pass

  def currentColor():
    pass

  def currentColorChanged():
    """ Signal """
    pass

  def customColor():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def customCount():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def done():
    pass

  def finished():
    """ Signal """
    pass

  def getColor():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def open():
    pass

  def options():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def selectedColor():
    pass

  def setCurrentColor():
    pass

  def setCustomColor():
    pass

  def setOption():
    pass

  def setOptions():
    pass

  def setStandardColor():
    pass

  def setTabOrder():
    pass

  def setVisible():
    pass

  staticMetaObject = None

  def testOption():
    pass

class QColumnView(QAbstractItemView):

  AboveItem = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  HLine = None
  IgnoreMask = None
  InternalMove = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SingleSelection = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def clicked():
    """ Signal """
    pass

  def columnWidths():
    pass

  def connect():
    pass

  def createColumn():
    pass

  def currentChanged():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def entered():
    """ Signal """
    pass

  def horizontalOffset():
    pass

  def indexAt():
    pass

  def initializeColumn():
    pass

  def isIndexHidden():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def moveCursor():
    pass

  def pressed():
    """ Signal """
    pass

  def previewWidget():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def resizeGripsVisible():
    pass

  def rowsInserted():
    pass

  def scrollContentsBy():
    pass

  def scrollTo():
    pass

  def selectAll():
    pass

  def setColumnWidths():
    pass

  def setModel():
    pass

  def setPreviewWidget():
    pass

  def setResizeGripsVisible():
    pass

  def setRootIndex():
    pass

  def setSelection():
    pass

  def setSelectionModel():
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def updatePreviewWidget():
    """ Signal """
    pass

  def verticalOffset():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def visualRect():
    pass

  def visualRegionForSelection():
    pass

class QComboBox(QWidget):

  AdjustToContents = None
  AdjustToContentsOnFirstShow = None
  AdjustToMinimumContentsLength = None
  AdjustToMinimumContentsLengthWithIcon = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  InsertAfterCurrent = None
  InsertAlphabetically = None
  InsertAtBottom = None
  InsertAtCurrent = None
  InsertAtTop = None
  InsertBeforeCurrent = None

  class InsertPolicy(object):

    InsertAfterCurrent = None
    InsertAlphabetically = None
    InsertAtBottom = None
    InsertAtCurrent = None
    InsertAtTop = None
    InsertBeforeCurrent = None
    NoInsert = None
    name = property(None, None, None,
                    )

    values = {}

  NoInsert = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  class SizeAdjustPolicy(object):

    AdjustToContents = None
    AdjustToContentsOnFirstShow = None
    AdjustToMinimumContentsLength = None
    AdjustToMinimumContentsLengthWithIcon = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def addItem():
    pass

  def addItems():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def clearEditText():
    pass

  def completer():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def count():
    pass

  def currentIndex():
    pass

  def currentIndexChanged():
    """ Signal """
    pass

  def currentText():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def duplicatesEnabled():
    pass

  def editTextChanged():
    """ Signal """
    pass

  def event():
    pass

  def findData():
    pass

  def findText():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def hasFrame():
    pass

  def hideEvent():
    pass

  def hidePopup():
    pass

  def highlighted():
    """ Signal """
    pass

  def iconSize():
    pass

  def initStyleOption():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def insertItem():
    pass

  def insertItems():
    pass

  def insertPolicy():
    pass

  def insertSeparator():
    pass

  def isEditable():
    pass

  def itemData():
    pass

  def itemDelegate():
    pass

  def itemIcon():
    pass

  def itemText():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def keyboardGrabber():
    pass

  def lineEdit():
    pass

  def maxCount():
    pass

  def maxVisibleItems():
    pass

  def minimumContentsLength():
    pass

  def minimumSizeHint():
    pass

  def model():
    pass

  def modelColumn():
    pass

  def mouseGrabber():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def removeItem():
    pass

  def resizeEvent():
    pass

  def rootModelIndex():
    pass

  def setCompleter():
    pass

  def setCurrentIndex():
    pass

  def setDuplicatesEnabled():
    pass

  def setEditText():
    pass

  def setEditable():
    pass

  def setFrame():
    pass

  def setIconSize():
    pass

  def setInsertPolicy():
    pass

  def setItemData():
    pass

  def setItemDelegate():
    pass

  def setItemIcon():
    pass

  def setItemText():
    pass

  def setLineEdit():
    pass

  def setMaxCount():
    pass

  def setMaxVisibleItems():
    pass

  def setMinimumContentsLength():
    pass

  def setModel():
    pass

  def setModelColumn():
    pass

  def setRootModelIndex():
    pass

  def setSizeAdjustPolicy():
    pass

  def setTabOrder():
    pass

  def setValidator():
    pass

  def setView():
    pass

  def showEvent():
    pass

  def showPopup():
    pass

  def sizeAdjustPolicy():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def textChanged():
    """ Signal """
    pass

  def validator():
    pass

  def view():
    pass

  def wheelEvent():
    pass

class QCommandLinkButton(QPushButton):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def description():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def heightForWidth():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def released():
    """ Signal """
    pass

  def setDescription():
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def toggled():
    """ Signal """
    pass

class QCommonStyle(QStyle):

  CC_ComboBox = None
  CC_CustomBase = None
  CC_Dial = None
  CC_GroupBox = None
  CC_MdiControls = None
  CC_Q3ListView = None
  CC_ScrollBar = None
  CC_Slider = None
  CC_SpinBox = None
  CC_TitleBar = None
  CC_ToolButton = None
  CE_CheckBox = None
  CE_CheckBoxLabel = None
  CE_ColumnViewGrip = None
  CE_ComboBoxLabel = None
  CE_CustomBase = None
  CE_DockWidgetTitle = None
  CE_FocusFrame = None
  CE_Header = None
  CE_HeaderEmptyArea = None
  CE_HeaderLabel = None
  CE_HeaderSection = None
  CE_ItemViewItem = None
  CE_MenuBarEmptyArea = None
  CE_MenuBarItem = None
  CE_MenuEmptyArea = None
  CE_MenuHMargin = None
  CE_MenuItem = None
  CE_MenuScroller = None
  CE_MenuTearoff = None
  CE_MenuVMargin = None
  CE_ProgressBar = None
  CE_ProgressBarContents = None
  CE_ProgressBarGroove = None
  CE_ProgressBarLabel = None
  CE_PushButton = None
  CE_PushButtonBevel = None
  CE_PushButtonLabel = None
  CE_Q3DockWindowEmptyArea = None
  CE_RadioButton = None
  CE_RadioButtonLabel = None
  CE_RubberBand = None
  CE_ScrollBarAddLine = None
  CE_ScrollBarAddPage = None
  CE_ScrollBarFirst = None
  CE_ScrollBarLast = None
  CE_ScrollBarSlider = None
  CE_ScrollBarSubLine = None
  CE_ScrollBarSubPage = None
  CE_ShapedFrame = None
  CE_SizeGrip = None
  CE_Splitter = None
  CE_TabBarTab = None
  CE_TabBarTabLabel = None
  CE_TabBarTabShape = None
  CE_ToolBar = None
  CE_ToolBoxTab = None
  CE_ToolBoxTabLabel = None
  CE_ToolBoxTabShape = None
  CE_ToolButtonLabel = None
  CT_CheckBox = None
  CT_ComboBox = None
  CT_CustomBase = None
  CT_DialogButtons = None
  CT_GroupBox = None
  CT_HeaderSection = None
  CT_ItemViewItem = None
  CT_LineEdit = None
  CT_MdiControls = None
  CT_Menu = None
  CT_MenuBar = None
  CT_MenuBarItem = None
  CT_MenuItem = None
  CT_ProgressBar = None
  CT_PushButton = None
  CT_Q3DockWindow = None
  CT_Q3Header = None
  CT_RadioButton = None
  CT_ScrollBar = None
  CT_SizeGrip = None
  CT_Slider = None
  CT_SpinBox = None
  CT_Splitter = None
  CT_TabBarTab = None
  CT_TabWidget = None
  CT_ToolButton = None

  class ComplexControl(object):

    CC_ComboBox = None
    CC_CustomBase = None
    CC_Dial = None
    CC_GroupBox = None
    CC_MdiControls = None
    CC_Q3ListView = None
    CC_ScrollBar = None
    CC_Slider = None
    CC_SpinBox = None
    CC_TitleBar = None
    CC_ToolButton = None
    name = property(None, None, None,
                    )

    values = {}

  class ContentsType(object):

    CT_CheckBox = None
    CT_ComboBox = None
    CT_CustomBase = None
    CT_DialogButtons = None
    CT_GroupBox = None
    CT_HeaderSection = None
    CT_ItemViewItem = None
    CT_LineEdit = None
    CT_MdiControls = None
    CT_Menu = None
    CT_MenuBar = None
    CT_MenuBarItem = None
    CT_MenuItem = None
    CT_ProgressBar = None
    CT_PushButton = None
    CT_Q3DockWindow = None
    CT_Q3Header = None
    CT_RadioButton = None
    CT_ScrollBar = None
    CT_SizeGrip = None
    CT_Slider = None
    CT_SpinBox = None
    CT_Splitter = None
    CT_TabBarTab = None
    CT_TabWidget = None
    CT_ToolButton = None
    name = property(None, None, None,
                    )

    values = {}

  class ControlElement(object):

    CE_CheckBox = None
    CE_CheckBoxLabel = None
    CE_ColumnViewGrip = None
    CE_ComboBoxLabel = None
    CE_CustomBase = None
    CE_DockWidgetTitle = None
    CE_FocusFrame = None
    CE_Header = None
    CE_HeaderEmptyArea = None
    CE_HeaderLabel = None
    CE_HeaderSection = None
    CE_ItemViewItem = None
    CE_MenuBarEmptyArea = None
    CE_MenuBarItem = None
    CE_MenuEmptyArea = None
    CE_MenuHMargin = None
    CE_MenuItem = None
    CE_MenuScroller = None
    CE_MenuTearoff = None
    CE_MenuVMargin = None
    CE_ProgressBar = None
    CE_ProgressBarContents = None
    CE_ProgressBarGroove = None
    CE_ProgressBarLabel = None
    CE_PushButton = None
    CE_PushButtonBevel = None
    CE_PushButtonLabel = None
    CE_Q3DockWindowEmptyArea = None
    CE_RadioButton = None
    CE_RadioButtonLabel = None
    CE_RubberBand = None
    CE_ScrollBarAddLine = None
    CE_ScrollBarAddPage = None
    CE_ScrollBarFirst = None
    CE_ScrollBarLast = None
    CE_ScrollBarSlider = None
    CE_ScrollBarSubLine = None
    CE_ScrollBarSubPage = None
    CE_ShapedFrame = None
    CE_SizeGrip = None
    CE_Splitter = None
    CE_TabBarTab = None
    CE_TabBarTabLabel = None
    CE_TabBarTabShape = None
    CE_ToolBar = None
    CE_ToolBoxTab = None
    CE_ToolBoxTabLabel = None
    CE_ToolBoxTabShape = None
    CE_ToolButtonLabel = None
    name = property(None, None, None,
                    )

    values = {}

  PE_CustomBase = None
  PE_Frame = None
  PE_FrameButtonBevel = None
  PE_FrameButtonTool = None
  PE_FrameDefaultButton = None
  PE_FrameDockWidget = None
  PE_FrameFocusRect = None
  PE_FrameGroupBox = None
  PE_FrameLineEdit = None
  PE_FrameMenu = None
  PE_FrameStatusBar = None
  PE_FrameStatusBarItem = None
  PE_FrameTabBarBase = None
  PE_FrameTabWidget = None
  PE_FrameWindow = None
  PE_IndicatorArrowDown = None
  PE_IndicatorArrowLeft = None
  PE_IndicatorArrowRight = None
  PE_IndicatorArrowUp = None
  PE_IndicatorBranch = None
  PE_IndicatorButtonDropDown = None
  PE_IndicatorCheckBox = None
  PE_IndicatorColumnViewArrow = None
  PE_IndicatorDockWidgetResizeHandle = None
  PE_IndicatorHeaderArrow = None
  PE_IndicatorItemViewItemCheck = None
  PE_IndicatorItemViewItemDrop = None
  PE_IndicatorMenuCheckMark = None
  PE_IndicatorProgressChunk = None
  PE_IndicatorRadioButton = None
  PE_IndicatorSpinDown = None
  PE_IndicatorSpinMinus = None
  PE_IndicatorSpinPlus = None
  PE_IndicatorSpinUp = None
  PE_IndicatorTabClose = None
  PE_IndicatorTabTear = None
  PE_IndicatorToolBarHandle = None
  PE_IndicatorToolBarSeparator = None
  PE_IndicatorViewItemCheck = None
  PE_PanelButtonBevel = None
  PE_PanelButtonCommand = None
  PE_PanelButtonTool = None
  PE_PanelItemViewItem = None
  PE_PanelItemViewRow = None
  PE_PanelLineEdit = None
  PE_PanelMenu = None
  PE_PanelMenuBar = None
  PE_PanelScrollAreaCorner = None
  PE_PanelStatusBar = None
  PE_PanelTipLabel = None
  PE_PanelToolBar = None
  PE_Q3CheckListController = None
  PE_Q3CheckListExclusiveIndicator = None
  PE_Q3CheckListIndicator = None
  PE_Q3DockWindowSeparator = None
  PE_Q3Separator = None
  PE_Widget = None
  PM_ButtonDefaultIndicator = None
  PM_ButtonIconSize = None
  PM_ButtonMargin = None
  PM_ButtonShiftHorizontal = None
  PM_ButtonShiftVertical = None
  PM_CheckBoxLabelSpacing = None
  PM_CheckListButtonSize = None
  PM_CheckListControllerSize = None
  PM_ComboBoxFrameWidth = None
  PM_CustomBase = None
  PM_DefaultChildMargin = None
  PM_DefaultFrameWidth = None
  PM_DefaultLayoutSpacing = None
  PM_DefaultTopLevelMargin = None
  PM_DialogButtonsButtonHeight = None
  PM_DialogButtonsButtonWidth = None
  PM_DialogButtonsSeparator = None
  PM_DockWidgetFrameWidth = None
  PM_DockWidgetHandleExtent = None
  PM_DockWidgetSeparatorExtent = None
  PM_DockWidgetTitleBarButtonMargin = None
  PM_DockWidgetTitleMargin = None
  PM_ExclusiveIndicatorHeight = None
  PM_ExclusiveIndicatorWidth = None
  PM_FocusFrameHMargin = None
  PM_FocusFrameVMargin = None
  PM_HeaderGripMargin = None
  PM_HeaderMargin = None
  PM_HeaderMarkSize = None
  PM_IconViewIconSize = None
  PM_IndicatorHeight = None
  PM_IndicatorWidth = None
  PM_LargeIconSize = None
  PM_LayoutBottomMargin = None
  PM_LayoutHorizontalSpacing = None
  PM_LayoutLeftMargin = None
  PM_LayoutRightMargin = None
  PM_LayoutTopMargin = None
  PM_LayoutVerticalSpacing = None
  PM_ListViewIconSize = None
  PM_MDIFrameWidth = None
  PM_MDIMinimizedWidth = None
  PM_MaximumDragDistance = None
  PM_MdiSubWindowFrameWidth = None
  PM_MdiSubWindowMinimizedWidth = None
  PM_MenuBarHMargin = None
  PM_MenuBarItemSpacing = None
  PM_MenuBarPanelWidth = None
  PM_MenuBarVMargin = None
  PM_MenuButtonIndicator = None
  PM_MenuDesktopFrameWidth = None
  PM_MenuHMargin = None
  PM_MenuPanelWidth = None
  PM_MenuScrollerHeight = None
  PM_MenuTearoffHeight = None
  PM_MenuVMargin = None
  PM_MessageBoxIconSize = None
  PM_ProgressBarChunkWidth = None
  PM_RadioButtonLabelSpacing = None
  PM_ScrollBarExtent = None
  PM_ScrollBarSliderMin = None
  PM_ScrollView_ScrollBarSpacing = None
  PM_SizeGripSize = None
  PM_SliderControlThickness = None
  PM_SliderLength = None
  PM_SliderSpaceAvailable = None
  PM_SliderThickness = None
  PM_SliderTickmarkOffset = None
  PM_SmallIconSize = None
  PM_SpinBoxFrameWidth = None
  PM_SpinBoxSliderHeight = None
  PM_SplitterWidth = None
  PM_SubMenuOverlap = None
  PM_TabBarBaseHeight = None
  PM_TabBarBaseOverlap = None
  PM_TabBarIconSize = None
  PM_TabBarScrollButtonWidth = None
  PM_TabBarTabHSpace = None
  PM_TabBarTabOverlap = None
  PM_TabBarTabShiftHorizontal = None
  PM_TabBarTabShiftVertical = None
  PM_TabBarTabVSpace = None
  PM_TabBar_ScrollButtonOverlap = None
  PM_TabCloseIndicatorHeight = None
  PM_TabCloseIndicatorWidth = None
  PM_TextCursorWidth = None
  PM_TitleBarHeight = None
  PM_ToolBarExtensionExtent = None
  PM_ToolBarFrameWidth = None
  PM_ToolBarHandleExtent = None
  PM_ToolBarIconSize = None
  PM_ToolBarItemMargin = None
  PM_ToolBarItemSpacing = None
  PM_ToolBarSeparatorExtent = None
  PM_ToolTipLabelFrameWidth = None

  class PixelMetric(object):

    PM_ButtonDefaultIndicator = None
    PM_ButtonIconSize = None
    PM_ButtonMargin = None
    PM_ButtonShiftHorizontal = None
    PM_ButtonShiftVertical = None
    PM_CheckBoxLabelSpacing = None
    PM_CheckListButtonSize = None
    PM_CheckListControllerSize = None
    PM_ComboBoxFrameWidth = None
    PM_CustomBase = None
    PM_DefaultChildMargin = None
    PM_DefaultFrameWidth = None
    PM_DefaultLayoutSpacing = None
    PM_DefaultTopLevelMargin = None
    PM_DialogButtonsButtonHeight = None
    PM_DialogButtonsButtonWidth = None
    PM_DialogButtonsSeparator = None
    PM_DockWidgetFrameWidth = None
    PM_DockWidgetHandleExtent = None
    PM_DockWidgetSeparatorExtent = None
    PM_DockWidgetTitleBarButtonMargin = None
    PM_DockWidgetTitleMargin = None
    PM_ExclusiveIndicatorHeight = None
    PM_ExclusiveIndicatorWidth = None
    PM_FocusFrameHMargin = None
    PM_FocusFrameVMargin = None
    PM_HeaderGripMargin = None
    PM_HeaderMargin = None
    PM_HeaderMarkSize = None
    PM_IconViewIconSize = None
    PM_IndicatorHeight = None
    PM_IndicatorWidth = None
    PM_LargeIconSize = None
    PM_LayoutBottomMargin = None
    PM_LayoutHorizontalSpacing = None
    PM_LayoutLeftMargin = None
    PM_LayoutRightMargin = None
    PM_LayoutTopMargin = None
    PM_LayoutVerticalSpacing = None
    PM_ListViewIconSize = None
    PM_MDIFrameWidth = None
    PM_MDIMinimizedWidth = None
    PM_MaximumDragDistance = None
    PM_MdiSubWindowFrameWidth = None
    PM_MdiSubWindowMinimizedWidth = None
    PM_MenuBarHMargin = None
    PM_MenuBarItemSpacing = None
    PM_MenuBarPanelWidth = None
    PM_MenuBarVMargin = None
    PM_MenuButtonIndicator = None
    PM_MenuDesktopFrameWidth = None
    PM_MenuHMargin = None
    PM_MenuPanelWidth = None
    PM_MenuScrollerHeight = None
    PM_MenuTearoffHeight = None
    PM_MenuVMargin = None
    PM_MessageBoxIconSize = None
    PM_ProgressBarChunkWidth = None
    PM_RadioButtonLabelSpacing = None
    PM_ScrollBarExtent = None
    PM_ScrollBarSliderMin = None
    PM_ScrollView_ScrollBarSpacing = None
    PM_SizeGripSize = None
    PM_SliderControlThickness = None
    PM_SliderLength = None
    PM_SliderSpaceAvailable = None
    PM_SliderThickness = None
    PM_SliderTickmarkOffset = None
    PM_SmallIconSize = None
    PM_SpinBoxFrameWidth = None
    PM_SpinBoxSliderHeight = None
    PM_SplitterWidth = None
    PM_SubMenuOverlap = None
    PM_TabBarBaseHeight = None
    PM_TabBarBaseOverlap = None
    PM_TabBarIconSize = None
    PM_TabBarScrollButtonWidth = None
    PM_TabBarTabHSpace = None
    PM_TabBarTabOverlap = None
    PM_TabBarTabShiftHorizontal = None
    PM_TabBarTabShiftVertical = None
    PM_TabBarTabVSpace = None
    PM_TabBar_ScrollButtonOverlap = None
    PM_TabCloseIndicatorHeight = None
    PM_TabCloseIndicatorWidth = None
    PM_TextCursorWidth = None
    PM_TitleBarHeight = None
    PM_ToolBarExtensionExtent = None
    PM_ToolBarFrameWidth = None
    PM_ToolBarHandleExtent = None
    PM_ToolBarIconSize = None
    PM_ToolBarItemMargin = None
    PM_ToolBarItemSpacing = None
    PM_ToolBarSeparatorExtent = None
    PM_ToolTipLabelFrameWidth = None
    name = property(None, None, None,
                    )

    values = {}

  class PrimitiveElement(object):

    PE_CustomBase = None
    PE_Frame = None
    PE_FrameButtonBevel = None
    PE_FrameButtonTool = None
    PE_FrameDefaultButton = None
    PE_FrameDockWidget = None
    PE_FrameFocusRect = None
    PE_FrameGroupBox = None
    PE_FrameLineEdit = None
    PE_FrameMenu = None
    PE_FrameStatusBar = None
    PE_FrameStatusBarItem = None
    PE_FrameTabBarBase = None
    PE_FrameTabWidget = None
    PE_FrameWindow = None
    PE_IndicatorArrowDown = None
    PE_IndicatorArrowLeft = None
    PE_IndicatorArrowRight = None
    PE_IndicatorArrowUp = None
    PE_IndicatorBranch = None
    PE_IndicatorButtonDropDown = None
    PE_IndicatorCheckBox = None
    PE_IndicatorColumnViewArrow = None
    PE_IndicatorDockWidgetResizeHandle = None
    PE_IndicatorHeaderArrow = None
    PE_IndicatorItemViewItemCheck = None
    PE_IndicatorItemViewItemDrop = None
    PE_IndicatorMenuCheckMark = None
    PE_IndicatorProgressChunk = None
    PE_IndicatorRadioButton = None
    PE_IndicatorSpinDown = None
    PE_IndicatorSpinMinus = None
    PE_IndicatorSpinPlus = None
    PE_IndicatorSpinUp = None
    PE_IndicatorTabClose = None
    PE_IndicatorTabTear = None
    PE_IndicatorToolBarHandle = None
    PE_IndicatorToolBarSeparator = None
    PE_IndicatorViewItemCheck = None
    PE_PanelButtonBevel = None
    PE_PanelButtonCommand = None
    PE_PanelButtonTool = None
    PE_PanelItemViewItem = None
    PE_PanelItemViewRow = None
    PE_PanelLineEdit = None
    PE_PanelMenu = None
    PE_PanelMenuBar = None
    PE_PanelScrollAreaCorner = None
    PE_PanelStatusBar = None
    PE_PanelTipLabel = None
    PE_PanelToolBar = None
    PE_Q3CheckListController = None
    PE_Q3CheckListExclusiveIndicator = None
    PE_Q3CheckListIndicator = None
    PE_Q3DockWindowSeparator = None
    PE_Q3Separator = None
    PE_Widget = None
    name = property(None, None, None,
                    )

    values = {}

  RSIP_OnMouseClick = None
  RSIP_OnMouseClickAndAlreadyFocused = None

  class RequestSoftwareInputPanel(object):

    RSIP_OnMouseClick = None
    RSIP_OnMouseClickAndAlreadyFocused = None
    name = property(None, None, None,
                    )

    values = {}

  SC_All = None
  SC_ComboBoxArrow = None
  SC_ComboBoxEditField = None
  SC_ComboBoxFrame = None
  SC_ComboBoxListBoxPopup = None
  SC_CustomBase = None
  SC_DialGroove = None
  SC_DialHandle = None
  SC_DialTickmarks = None
  SC_GroupBoxCheckBox = None
  SC_GroupBoxContents = None
  SC_GroupBoxFrame = None
  SC_GroupBoxLabel = None
  SC_MdiCloseButton = None
  SC_MdiMinButton = None
  SC_MdiNormalButton = None
  SC_None = None
  SC_Q3ListView = None
  SC_Q3ListViewBranch = None
  SC_Q3ListViewExpand = None
  SC_ScrollBarAddLine = None
  SC_ScrollBarAddPage = None
  SC_ScrollBarFirst = None
  SC_ScrollBarGroove = None
  SC_ScrollBarLast = None
  SC_ScrollBarSlider = None
  SC_ScrollBarSubLine = None
  SC_ScrollBarSubPage = None
  SC_SliderGroove = None
  SC_SliderHandle = None
  SC_SliderTickmarks = None
  SC_SpinBoxDown = None
  SC_SpinBoxEditField = None
  SC_SpinBoxFrame = None
  SC_SpinBoxUp = None
  SC_TitleBarCloseButton = None
  SC_TitleBarContextHelpButton = None
  SC_TitleBarLabel = None
  SC_TitleBarMaxButton = None
  SC_TitleBarMinButton = None
  SC_TitleBarNormalButton = None
  SC_TitleBarShadeButton = None
  SC_TitleBarSysMenu = None
  SC_TitleBarUnshadeButton = None
  SC_ToolButton = None
  SC_ToolButtonMenu = None
  SE_CheckBoxClickRect = None
  SE_CheckBoxContents = None
  SE_CheckBoxFocusRect = None
  SE_CheckBoxIndicator = None
  SE_CheckBoxLayoutItem = None
  SE_ComboBoxFocusRect = None
  SE_ComboBoxLayoutItem = None
  SE_CustomBase = None
  SE_DateTimeEditLayoutItem = None
  SE_DialogButtonAbort = None
  SE_DialogButtonAccept = None
  SE_DialogButtonAll = None
  SE_DialogButtonApply = None
  SE_DialogButtonBoxLayoutItem = None
  SE_DialogButtonCustom = None
  SE_DialogButtonHelp = None
  SE_DialogButtonIgnore = None
  SE_DialogButtonReject = None
  SE_DialogButtonRetry = None
  SE_DockWidgetCloseButton = None
  SE_DockWidgetFloatButton = None
  SE_DockWidgetIcon = None
  SE_DockWidgetTitleBarText = None
  SE_FrameContents = None
  SE_FrameLayoutItem = None
  SE_GroupBoxLayoutItem = None
  SE_HeaderArrow = None
  SE_HeaderLabel = None
  SE_ItemViewItemCheckIndicator = None
  SE_ItemViewItemDecoration = None
  SE_ItemViewItemFocusRect = None
  SE_ItemViewItemText = None
  SE_LabelLayoutItem = None
  SE_LineEditContents = None
  SE_ProgressBarContents = None
  SE_ProgressBarGroove = None
  SE_ProgressBarLabel = None
  SE_ProgressBarLayoutItem = None
  SE_PushButtonContents = None
  SE_PushButtonFocusRect = None
  SE_PushButtonLayoutItem = None
  SE_Q3DockWindowHandleRect = None
  SE_RadioButtonClickRect = None
  SE_RadioButtonContents = None
  SE_RadioButtonFocusRect = None
  SE_RadioButtonIndicator = None
  SE_RadioButtonLayoutItem = None
  SE_ShapedFrameContents = None
  SE_SliderFocusRect = None
  SE_SliderLayoutItem = None
  SE_SpinBoxLayoutItem = None
  SE_TabBarTabLeftButton = None
  SE_TabBarTabRightButton = None
  SE_TabBarTabText = None
  SE_TabBarTearIndicator = None
  SE_TabWidgetLayoutItem = None
  SE_TabWidgetLeftCorner = None
  SE_TabWidgetRightCorner = None
  SE_TabWidgetTabBar = None
  SE_TabWidgetTabContents = None
  SE_TabWidgetTabPane = None
  SE_ToolBarHandle = None
  SE_ToolBoxTabContents = None
  SE_ToolButtonLayoutItem = None
  SE_TreeViewDisclosureItem = None
  SE_ViewItemCheckIndicator = None
  SH_BlinkCursorWhenTextSelected = None
  SH_Button_FocusPolicy = None
  SH_ComboBox_LayoutDirection = None
  SH_ComboBox_ListMouseTracking = None
  SH_ComboBox_Popup = None
  SH_ComboBox_PopupFrameStyle = None
  SH_CustomBase = None
  SH_Dial_BackgroundRole = None
  SH_DialogButtonBox_ButtonsHaveIcons = None
  SH_DialogButtonLayout = None
  SH_DialogButtons_DefaultButton = None
  SH_DitherDisabledText = None
  SH_DockWidget_ButtonsHaveFrame = None
  SH_DrawMenuBarSeparator = None
  SH_EtchDisabledText = None
  SH_FocusFrame_AboveWidget = None
  SH_FocusFrame_Mask = None
  SH_FontDialog_SelectAssociatedText = None
  SH_FormLayoutFieldGrowthPolicy = None
  SH_FormLayoutFormAlignment = None
  SH_FormLayoutLabelAlignment = None
  SH_FormLayoutWrapPolicy = None
  SH_GroupBox_TextLabelColor = None
  SH_GroupBox_TextLabelVerticalAlignment = None
  SH_Header_ArrowAlignment = None
  SH_ItemView_ActivateItemOnSingleClick = None
  SH_ItemView_ArrowKeysNavigateIntoChildren = None
  SH_ItemView_ChangeHighlightOnFocus = None
  SH_ItemView_DrawDelegateFrame = None
  SH_ItemView_EllipsisLocation = None
  SH_ItemView_MovementWithoutUpdatingSelection = None
  SH_ItemView_PaintAlternatingRowColorsForEmptyArea = None
  SH_ItemView_ShowDecorationSelected = None
  SH_LineEdit_PasswordCharacter = None
  SH_MainWindow_SpaceBelowMenuBar = None
  SH_MenuBar_AltKeyNavigation = None
  SH_MenuBar_DismissOnSecondClick = None
  SH_MenuBar_MouseTracking = None
  SH_Menu_AllowActiveAndDisabled = None
  SH_Menu_FadeOutOnHide = None
  SH_Menu_FillScreenWithScroll = None
  SH_Menu_FlashTriggeredItem = None
  SH_Menu_KeyboardSearch = None
  SH_Menu_Mask = None
  SH_Menu_MouseTracking = None
  SH_Menu_Scrollable = None
  SH_Menu_SelectionWrap = None
  SH_Menu_SloppySubMenus = None
  SH_Menu_SpaceActivatesItem = None
  SH_Menu_SubMenuPopupDelay = None
  SH_MessageBox_CenterButtons = None
  SH_MessageBox_TextInteractionFlags = None
  SH_MessageBox_UseBorderForButtonSpacing = None
  SH_PrintDialog_RightAlignButtons = None
  SH_ProgressDialog_CenterCancelButton = None
  SH_ProgressDialog_TextLabelAlignment = None
  SH_Q3ListViewExpand_SelectMouseType = None
  SH_RequestSoftwareInputPanel = None
  SH_RichText_FullWidthSelection = None
  SH_RubberBand_Mask = None
  SH_ScrollBar_ContextMenu = None
  SH_ScrollBar_LeftClickAbsolutePosition = None
  SH_ScrollBar_MiddleClickAbsolutePosition = None
  SH_ScrollBar_RollBetweenButtons = None
  SH_ScrollBar_ScrollWhenPointerLeavesControl = None
  SH_ScrollBar_StopMouseOverSlider = None
  SH_ScrollView_FrameOnlyAroundContents = None
  SH_Slider_AbsoluteSetButtons = None
  SH_Slider_PageSetButtons = None
  SH_Slider_SloppyKeyEvents = None
  SH_Slider_SnapToValue = None
  SH_Slider_StopMouseOverSlider = None
  SH_SpellCheckUnderlineStyle = None
  SH_SpinBox_AnimateButton = None
  SH_SpinBox_ClickAutoRepeatRate = None
  SH_SpinBox_ClickAutoRepeatThreshold = None
  SH_SpinBox_KeyPressAutoRepeatRate = None
  SH_SpinControls_DisableOnBounds = None
  SH_TabBar_Alignment = None
  SH_TabBar_CloseButtonPosition = None
  SH_TabBar_ElideMode = None
  SH_TabBar_PreferNoArrows = None
  SH_TabBar_SelectMouseType = None
  SH_TabWidget_DefaultTabPosition = None
  SH_Table_GridLineColor = None
  SH_TextControl_FocusIndicatorTextCharFormat = None
  SH_TitleBar_AutoRaise = None
  SH_TitleBar_ModifyNotification = None
  SH_TitleBar_NoBorder = None
  SH_ToolBar_Movable = None
  SH_ToolBox_SelectedPageTitleBold = None
  SH_ToolButtonStyle = None
  SH_ToolButton_PopupDelay = None
  SH_ToolTipLabel_Opacity = None
  SH_ToolTip_Mask = None
  SH_UnderlineShortcut = None
  SH_Widget_ShareActivation = None
  SH_WindowFrame_Mask = None
  SH_WizardStyle = None
  SH_Workspace_FillSpaceOnMaximize = None
  SP_ArrowBack = None
  SP_ArrowDown = None
  SP_ArrowForward = None
  SP_ArrowLeft = None
  SP_ArrowRight = None
  SP_ArrowUp = None
  SP_BrowserReload = None
  SP_BrowserStop = None
  SP_CommandLink = None
  SP_ComputerIcon = None
  SP_CustomBase = None
  SP_DesktopIcon = None
  SP_DialogApplyButton = None
  SP_DialogCancelButton = None
  SP_DialogCloseButton = None
  SP_DialogDiscardButton = None
  SP_DialogHelpButton = None
  SP_DialogNoButton = None
  SP_DialogOkButton = None
  SP_DialogOpenButton = None
  SP_DialogResetButton = None
  SP_DialogSaveButton = None
  SP_DialogYesButton = None
  SP_DirClosedIcon = None
  SP_DirHomeIcon = None
  SP_DirIcon = None
  SP_DirLinkIcon = None
  SP_DirOpenIcon = None
  SP_DockWidgetCloseButton = None
  SP_DriveCDIcon = None
  SP_DriveDVDIcon = None
  SP_DriveFDIcon = None
  SP_DriveHDIcon = None
  SP_DriveNetIcon = None
  SP_FileDialogBack = None
  SP_FileDialogContentsView = None
  SP_FileDialogDetailedView = None
  SP_FileDialogEnd = None
  SP_FileDialogInfoView = None
  SP_FileDialogListView = None
  SP_FileDialogNewFolder = None
  SP_FileDialogStart = None
  SP_FileDialogToParent = None
  SP_FileIcon = None
  SP_FileLinkIcon = None
  SP_MediaPause = None
  SP_MediaPlay = None
  SP_MediaSeekBackward = None
  SP_MediaSeekForward = None
  SP_MediaSkipBackward = None
  SP_MediaSkipForward = None
  SP_MediaStop = None
  SP_MediaVolume = None
  SP_MediaVolumeMuted = None
  SP_MessageBoxCritical = None
  SP_MessageBoxInformation = None
  SP_MessageBoxQuestion = None
  SP_MessageBoxWarning = None
  SP_TitleBarCloseButton = None
  SP_TitleBarContextHelpButton = None
  SP_TitleBarMaxButton = None
  SP_TitleBarMenuButton = None
  SP_TitleBarMinButton = None
  SP_TitleBarNormalButton = None
  SP_TitleBarShadeButton = None
  SP_TitleBarUnshadeButton = None
  SP_ToolBarHorizontalExtensionButton = None
  SP_ToolBarVerticalExtensionButton = None
  SP_TrashIcon = None
  SP_VistaShield = None

  class StandardPixmap(object):

    SP_ArrowBack = None
    SP_ArrowDown = None
    SP_ArrowForward = None
    SP_ArrowLeft = None
    SP_ArrowRight = None
    SP_ArrowUp = None
    SP_BrowserReload = None
    SP_BrowserStop = None
    SP_CommandLink = None
    SP_ComputerIcon = None
    SP_CustomBase = None
    SP_DesktopIcon = None
    SP_DialogApplyButton = None
    SP_DialogCancelButton = None
    SP_DialogCloseButton = None
    SP_DialogDiscardButton = None
    SP_DialogHelpButton = None
    SP_DialogNoButton = None
    SP_DialogOkButton = None
    SP_DialogOpenButton = None
    SP_DialogResetButton = None
    SP_DialogSaveButton = None
    SP_DialogYesButton = None
    SP_DirClosedIcon = None
    SP_DirHomeIcon = None
    SP_DirIcon = None
    SP_DirLinkIcon = None
    SP_DirOpenIcon = None
    SP_DockWidgetCloseButton = None
    SP_DriveCDIcon = None
    SP_DriveDVDIcon = None
    SP_DriveFDIcon = None
    SP_DriveHDIcon = None
    SP_DriveNetIcon = None
    SP_FileDialogBack = None
    SP_FileDialogContentsView = None
    SP_FileDialogDetailedView = None
    SP_FileDialogEnd = None
    SP_FileDialogInfoView = None
    SP_FileDialogListView = None
    SP_FileDialogNewFolder = None
    SP_FileDialogStart = None
    SP_FileDialogToParent = None
    SP_FileIcon = None
    SP_FileLinkIcon = None
    SP_MediaPause = None
    SP_MediaPlay = None
    SP_MediaSeekBackward = None
    SP_MediaSeekForward = None
    SP_MediaSkipBackward = None
    SP_MediaSkipForward = None
    SP_MediaStop = None
    SP_MediaVolume = None
    SP_MediaVolumeMuted = None
    SP_MessageBoxCritical = None
    SP_MessageBoxInformation = None
    SP_MessageBoxQuestion = None
    SP_MessageBoxWarning = None
    SP_TitleBarCloseButton = None
    SP_TitleBarContextHelpButton = None
    SP_TitleBarMaxButton = None
    SP_TitleBarMenuButton = None
    SP_TitleBarMinButton = None
    SP_TitleBarNormalButton = None
    SP_TitleBarShadeButton = None
    SP_TitleBarUnshadeButton = None
    SP_ToolBarHorizontalExtensionButton = None
    SP_ToolBarVerticalExtensionButton = None
    SP_TrashIcon = None
    SP_VistaShield = None
    name = property(None, None, None,
                    )

    values = {}

  class State(object):

    pass

  class StateFlag(object):

    State_Active = None
    State_AutoRaise = None
    State_Bottom = None
    State_Children = None
    State_DownArrow = None
    State_Editing = None
    State_Enabled = None
    State_FocusAtBorder = None
    State_HasFocus = None
    State_Horizontal = None
    State_Item = None
    State_KeyboardFocusChange = None
    State_Mini = None
    State_MouseOver = None
    State_NoChange = None
    State_None = None
    State_Off = None
    State_On = None
    State_Open = None
    State_Raised = None
    State_ReadOnly = None
    State_Selected = None
    State_Sibling = None
    State_Small = None
    State_Sunken = None
    State_Top = None
    State_UpArrow = None
    State_Window = None
    name = property(None, None, None,
                    )

    values = {}

  State_Active = None
  State_AutoRaise = None
  State_Bottom = None
  State_Children = None
  State_DownArrow = None
  State_Editing = None
  State_Enabled = None
  State_FocusAtBorder = None
  State_HasFocus = None
  State_Horizontal = None
  State_Item = None
  State_KeyboardFocusChange = None
  State_Mini = None
  State_MouseOver = None
  State_NoChange = None
  State_None = None
  State_Off = None
  State_On = None
  State_Open = None
  State_Raised = None
  State_ReadOnly = None
  State_Selected = None
  State_Sibling = None
  State_Small = None
  State_Sunken = None
  State_Top = None
  State_UpArrow = None
  State_Window = None

  class StyleHint(object):

    SH_BlinkCursorWhenTextSelected = None
    SH_Button_FocusPolicy = None
    SH_ComboBox_LayoutDirection = None
    SH_ComboBox_ListMouseTracking = None
    SH_ComboBox_Popup = None
    SH_ComboBox_PopupFrameStyle = None
    SH_CustomBase = None
    SH_Dial_BackgroundRole = None
    SH_DialogButtonBox_ButtonsHaveIcons = None
    SH_DialogButtonLayout = None
    SH_DialogButtons_DefaultButton = None
    SH_DitherDisabledText = None
    SH_DockWidget_ButtonsHaveFrame = None
    SH_DrawMenuBarSeparator = None
    SH_EtchDisabledText = None
    SH_FocusFrame_AboveWidget = None
    SH_FocusFrame_Mask = None
    SH_FontDialog_SelectAssociatedText = None
    SH_FormLayoutFieldGrowthPolicy = None
    SH_FormLayoutFormAlignment = None
    SH_FormLayoutLabelAlignment = None
    SH_FormLayoutWrapPolicy = None
    SH_GroupBox_TextLabelColor = None
    SH_GroupBox_TextLabelVerticalAlignment = None
    SH_Header_ArrowAlignment = None
    SH_ItemView_ActivateItemOnSingleClick = None
    SH_ItemView_ArrowKeysNavigateIntoChildren = None
    SH_ItemView_ChangeHighlightOnFocus = None
    SH_ItemView_DrawDelegateFrame = None
    SH_ItemView_EllipsisLocation = None
    SH_ItemView_MovementWithoutUpdatingSelection = None
    SH_ItemView_PaintAlternatingRowColorsForEmptyArea = None
    SH_ItemView_ShowDecorationSelected = None
    SH_LineEdit_PasswordCharacter = None
    SH_MainWindow_SpaceBelowMenuBar = None
    SH_MenuBar_AltKeyNavigation = None
    SH_MenuBar_DismissOnSecondClick = None
    SH_MenuBar_MouseTracking = None
    SH_Menu_AllowActiveAndDisabled = None
    SH_Menu_FadeOutOnHide = None
    SH_Menu_FillScreenWithScroll = None
    SH_Menu_FlashTriggeredItem = None
    SH_Menu_KeyboardSearch = None
    SH_Menu_Mask = None
    SH_Menu_MouseTracking = None
    SH_Menu_Scrollable = None
    SH_Menu_SelectionWrap = None
    SH_Menu_SloppySubMenus = None
    SH_Menu_SpaceActivatesItem = None
    SH_Menu_SubMenuPopupDelay = None
    SH_MessageBox_CenterButtons = None
    SH_MessageBox_TextInteractionFlags = None
    SH_MessageBox_UseBorderForButtonSpacing = None
    SH_PrintDialog_RightAlignButtons = None
    SH_ProgressDialog_CenterCancelButton = None
    SH_ProgressDialog_TextLabelAlignment = None
    SH_Q3ListViewExpand_SelectMouseType = None
    SH_RequestSoftwareInputPanel = None
    SH_RichText_FullWidthSelection = None
    SH_RubberBand_Mask = None
    SH_ScrollBar_ContextMenu = None
    SH_ScrollBar_LeftClickAbsolutePosition = None
    SH_ScrollBar_MiddleClickAbsolutePosition = None
    SH_ScrollBar_RollBetweenButtons = None
    SH_ScrollBar_ScrollWhenPointerLeavesControl = None
    SH_ScrollBar_StopMouseOverSlider = None
    SH_ScrollView_FrameOnlyAroundContents = None
    SH_Slider_AbsoluteSetButtons = None
    SH_Slider_PageSetButtons = None
    SH_Slider_SloppyKeyEvents = None
    SH_Slider_SnapToValue = None
    SH_Slider_StopMouseOverSlider = None
    SH_SpellCheckUnderlineStyle = None
    SH_SpinBox_AnimateButton = None
    SH_SpinBox_ClickAutoRepeatRate = None
    SH_SpinBox_ClickAutoRepeatThreshold = None
    SH_SpinBox_KeyPressAutoRepeatRate = None
    SH_SpinControls_DisableOnBounds = None
    SH_TabBar_Alignment = None
    SH_TabBar_CloseButtonPosition = None
    SH_TabBar_ElideMode = None
    SH_TabBar_PreferNoArrows = None
    SH_TabBar_SelectMouseType = None
    SH_TabWidget_DefaultTabPosition = None
    SH_Table_GridLineColor = None
    SH_TextControl_FocusIndicatorTextCharFormat = None
    SH_TitleBar_AutoRaise = None
    SH_TitleBar_ModifyNotification = None
    SH_TitleBar_NoBorder = None
    SH_ToolBar_Movable = None
    SH_ToolBox_SelectedPageTitleBold = None
    SH_ToolButtonStyle = None
    SH_ToolButton_PopupDelay = None
    SH_ToolTipLabel_Opacity = None
    SH_ToolTip_Mask = None
    SH_UnderlineShortcut = None
    SH_Widget_ShareActivation = None
    SH_WindowFrame_Mask = None
    SH_WizardStyle = None
    SH_Workspace_FillSpaceOnMaximize = None
    name = property(None, None, None,
                    )

    values = {}

  class SubControl(object):

    SC_All = None
    SC_ComboBoxArrow = None
    SC_ComboBoxEditField = None
    SC_ComboBoxFrame = None
    SC_ComboBoxListBoxPopup = None
    SC_CustomBase = None
    SC_DialGroove = None
    SC_DialHandle = None
    SC_DialTickmarks = None
    SC_GroupBoxCheckBox = None
    SC_GroupBoxContents = None
    SC_GroupBoxFrame = None
    SC_GroupBoxLabel = None
    SC_MdiCloseButton = None
    SC_MdiMinButton = None
    SC_MdiNormalButton = None
    SC_None = None
    SC_Q3ListView = None
    SC_Q3ListViewBranch = None
    SC_Q3ListViewExpand = None
    SC_ScrollBarAddLine = None
    SC_ScrollBarAddPage = None
    SC_ScrollBarFirst = None
    SC_ScrollBarGroove = None
    SC_ScrollBarLast = None
    SC_ScrollBarSlider = None
    SC_ScrollBarSubLine = None
    SC_ScrollBarSubPage = None
    SC_SliderGroove = None
    SC_SliderHandle = None
    SC_SliderTickmarks = None
    SC_SpinBoxDown = None
    SC_SpinBoxEditField = None
    SC_SpinBoxFrame = None
    SC_SpinBoxUp = None
    SC_TitleBarCloseButton = None
    SC_TitleBarContextHelpButton = None
    SC_TitleBarLabel = None
    SC_TitleBarMaxButton = None
    SC_TitleBarMinButton = None
    SC_TitleBarNormalButton = None
    SC_TitleBarShadeButton = None
    SC_TitleBarSysMenu = None
    SC_TitleBarUnshadeButton = None
    SC_ToolButton = None
    SC_ToolButtonMenu = None
    name = property(None, None, None,
                    )

    values = {}

  class SubControls(object):

    pass

  class SubElement(object):

    SE_CheckBoxClickRect = None
    SE_CheckBoxContents = None
    SE_CheckBoxFocusRect = None
    SE_CheckBoxIndicator = None
    SE_CheckBoxLayoutItem = None
    SE_ComboBoxFocusRect = None
    SE_ComboBoxLayoutItem = None
    SE_CustomBase = None
    SE_DateTimeEditLayoutItem = None
    SE_DialogButtonAbort = None
    SE_DialogButtonAccept = None
    SE_DialogButtonAll = None
    SE_DialogButtonApply = None
    SE_DialogButtonBoxLayoutItem = None
    SE_DialogButtonCustom = None
    SE_DialogButtonHelp = None
    SE_DialogButtonIgnore = None
    SE_DialogButtonReject = None
    SE_DialogButtonRetry = None
    SE_DockWidgetCloseButton = None
    SE_DockWidgetFloatButton = None
    SE_DockWidgetIcon = None
    SE_DockWidgetTitleBarText = None
    SE_FrameContents = None
    SE_FrameLayoutItem = None
    SE_GroupBoxLayoutItem = None
    SE_HeaderArrow = None
    SE_HeaderLabel = None
    SE_ItemViewItemCheckIndicator = None
    SE_ItemViewItemDecoration = None
    SE_ItemViewItemFocusRect = None
    SE_ItemViewItemText = None
    SE_LabelLayoutItem = None
    SE_LineEditContents = None
    SE_ProgressBarContents = None
    SE_ProgressBarGroove = None
    SE_ProgressBarLabel = None
    SE_ProgressBarLayoutItem = None
    SE_PushButtonContents = None
    SE_PushButtonFocusRect = None
    SE_PushButtonLayoutItem = None
    SE_Q3DockWindowHandleRect = None
    SE_RadioButtonClickRect = None
    SE_RadioButtonContents = None
    SE_RadioButtonFocusRect = None
    SE_RadioButtonIndicator = None
    SE_RadioButtonLayoutItem = None
    SE_ShapedFrameContents = None
    SE_SliderFocusRect = None
    SE_SliderLayoutItem = None
    SE_SpinBoxLayoutItem = None
    SE_TabBarTabLeftButton = None
    SE_TabBarTabRightButton = None
    SE_TabBarTabText = None
    SE_TabBarTearIndicator = None
    SE_TabWidgetLayoutItem = None
    SE_TabWidgetLeftCorner = None
    SE_TabWidgetRightCorner = None
    SE_TabWidgetTabBar = None
    SE_TabWidgetTabContents = None
    SE_TabWidgetTabPane = None
    SE_ToolBarHandle = None
    SE_ToolBoxTabContents = None
    SE_ToolButtonLayoutItem = None
    SE_TreeViewDisclosureItem = None
    SE_ViewItemCheckIndicator = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignedRect():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def drawComplexControl():
    pass

  def drawControl():
    pass

  def drawPrimitive():
    pass

  def generatedIconPixmap():
    pass

  def hitTestComplexControl():
    pass

  def pixelMetric():
    pass

  def polish():
    pass

  def registerUserData():
    pass

  def sizeFromContents():
    pass

  def sliderPositionFromValue():
    pass

  def sliderValueFromPosition():
    pass

  def standardIconImplementation():
    pass

  staticMetaObject = None

  def styleHint():
    pass

  def subControlRect():
    pass

  def subElementRect():
    pass

  def unpolish():
    pass

  def visualAlignment():
    pass

  def visualPos():
    pass

  def visualRect():
    pass

class QCompleter(QObject):

  CaseInsensitivelySortedModel = None
  CaseSensitivelySortedModel = None

  class CompletionMode(object):

    InlineCompletion = None
    PopupCompletion = None
    UnfilteredPopupCompletion = None
    name = property(None, None, None,
                    )

    values = {}

  InlineCompletion = None

  class ModelSorting(object):

    CaseInsensitivelySortedModel = None
    CaseSensitivelySortedModel = None
    UnsortedModel = None
    name = property(None, None, None,
                    )

    values = {}

  PopupCompletion = None
  UnfilteredPopupCompletion = None
  UnsortedModel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def caseSensitivity():
    pass

  def complete():
    pass

  def completionColumn():
    pass

  def completionCount():
    pass

  def completionMode():
    pass

  def completionModel():
    pass

  def completionPrefix():
    pass

  def completionRole():
    pass

  def connect():
    pass

  def currentCompletion():
    pass

  def currentIndex():
    pass

  def currentRow():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def highlighted():
    """ Signal """
    pass

  def maxVisibleItems():
    pass

  def model():
    pass

  def modelSorting():
    pass

  def pathFromIndex():
    pass

  def popup():
    pass

  def registerUserData():
    pass

  def setCaseSensitivity():
    pass

  def setCompletionColumn():
    pass

  def setCompletionMode():
    pass

  def setCompletionPrefix():
    pass

  def setCompletionRole():
    pass

  def setCurrentRow():
    pass

  def setMaxVisibleItems():
    pass

  def setModel():
    pass

  def setModelSorting():
    pass

  def setPopup():
    pass

  def setWidget():
    pass

  def setWrapAround():
    pass

  def splitPath():
    pass

  staticMetaObject = None

  def widget():
    pass

  def wrapAround():
    pass

class QDataWidgetMapper(QObject):

  AutoSubmit = None
  ManualSubmit = None

  class SubmitPolicy(object):

    AutoSubmit = None
    ManualSubmit = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addMapping():
    pass

  def clearMapping():
    pass

  def connect():
    pass

  def currentIndex():
    pass

  def currentIndexChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def itemDelegate():
    pass

  def mappedPropertyName():
    pass

  def mappedSection():
    pass

  def mappedWidgetAt():
    pass

  def model():
    pass

  def orientation():
    pass

  def registerUserData():
    pass

  def removeMapping():
    pass

  def revert():
    pass

  def rootIndex():
    pass

  def setCurrentIndex():
    pass

  def setCurrentModelIndex():
    pass

  def setItemDelegate():
    pass

  def setModel():
    pass

  def setOrientation():
    pass

  def setRootIndex():
    pass

  def setSubmitPolicy():
    pass

  staticMetaObject = None

  def submit():
    pass

  def submitPolicy():
    pass

  def toFirst():
    pass

  def toLast():
    pass

  def toNext():
    pass

  def toPrevious():
    pass

class QDateEdit(QDateTimeEdit):

  AmPmSection = None
  CorrectToNearestValue = None
  CorrectToPreviousValue = None
  DateSections_Mask = None
  DaySection = None
  DrawChildren = None
  DrawWindowBackground = None
  HourSection = None
  IgnoreMask = None
  MSecSection = None
  MinuteSection = None
  MonthSection = None
  NoButtons = None
  NoSection = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  PlusMinus = None
  SecondSection = None

  class Section(object):

    AmPmSection = None
    DateSections_Mask = None
    DaySection = None
    HourSection = None
    MSecSection = None
    MinuteSection = None
    MonthSection = None
    NoSection = None
    SecondSection = None
    TimeSections_Mask = None
    YearSection = None
    name = property(None, None, None,
                    )

    values = {}

  class Sections(object):

    pass

  StepDownEnabled = None
  StepNone = None
  StepUpEnabled = None
  TimeSections_Mask = None
  UpDownArrows = None
  YearSection = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def dateChanged():
    """ Signal """
    pass

  def dateTimeChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editingFinished():
    """ Signal """
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def timeChanged():
    """ Signal """
    pass

class QDateTimeEdit(QAbstractSpinBox):

  AmPmSection = None
  CorrectToNearestValue = None
  CorrectToPreviousValue = None
  DateSections_Mask = None
  DaySection = None
  DrawChildren = None
  DrawWindowBackground = None
  HourSection = None
  IgnoreMask = None
  MSecSection = None
  MinuteSection = None
  MonthSection = None
  NoButtons = None
  NoSection = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  PlusMinus = None
  SecondSection = None
  StepDownEnabled = None
  StepNone = None
  StepUpEnabled = None
  TimeSections_Mask = None
  UpDownArrows = None
  YearSection = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def calendarPopup():
    pass

  def calendarWidget():
    pass

  def clear():
    pass

  def clearMaximumDate():
    pass

  def clearMaximumDateTime():
    pass

  def clearMaximumTime():
    pass

  def clearMinimumDate():
    pass

  def clearMinimumDateTime():
    pass

  def clearMinimumTime():
    pass

  def connect():
    pass

  def currentSection():
    pass

  def currentSectionIndex():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def date():
    pass

  def dateChanged():
    """ Signal """
    pass

  def dateTime():
    pass

  def dateTimeChanged():
    """ Signal """
    pass

  def dateTimeFromText():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def displayFormat():
    pass

  def displayedSections():
    pass

  def editingFinished():
    """ Signal """
    pass

  def event():
    pass

  def fixup():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def initStyleOption():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def maximumDate():
    pass

  def maximumDateTime():
    pass

  def maximumTime():
    pass

  def minimumDate():
    pass

  def minimumDateTime():
    pass

  def minimumTime():
    pass

  def mouseGrabber():
    pass

  def mousePressEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def sectionAt():
    pass

  def sectionCount():
    pass

  def sectionText():
    pass

  def setCalendarPopup():
    pass

  def setCalendarWidget():
    pass

  def setCurrentSection():
    pass

  def setCurrentSectionIndex():
    pass

  def setDate():
    pass

  def setDateRange():
    pass

  def setDateTime():
    pass

  def setDateTimeRange():
    pass

  def setDisplayFormat():
    pass

  def setMaximumDate():
    pass

  def setMaximumDateTime():
    pass

  def setMaximumTime():
    pass

  def setMinimumDate():
    pass

  def setMinimumDateTime():
    pass

  def setMinimumTime():
    pass

  def setSelectedSection():
    pass

  def setTabOrder():
    pass

  def setTime():
    pass

  def setTimeRange():
    pass

  def setTimeSpec():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def stepBy():
    pass

  def stepEnabled():
    pass

  def textFromDateTime():
    pass

  def time():
    pass

  def timeChanged():
    """ Signal """
    pass

  def timeSpec():
    pass

  def validate():
    pass

  def wheelEvent():
    pass

class QDesktopWidget(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def availableGeometry():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def isVirtualDesktop():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def numScreens():
    pass

  def primaryScreen():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def resized():
    """ Signal """
    pass

  def screen():
    pass

  def screenCount():
    pass

  def screenCountChanged():
    """ Signal """
    pass

  def screenGeometry():
    pass

  def screenNumber():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def workAreaResized():
    """ Signal """
    pass

class QDial(QAbstractSlider):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  SliderMove = None
  SliderNoAction = None
  SliderOrientationChange = None
  SliderPageStepAdd = None
  SliderPageStepSub = None
  SliderRangeChange = None
  SliderSingleStepAdd = None
  SliderSingleStepSub = None
  SliderStepsChange = None
  SliderToMaximum = None
  SliderToMinimum = None
  SliderValueChange = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionTriggered():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def dialMoved():
    """ Signal """
    pass

  def dialPressed():
    """ Signal """
    pass

  def dialReleased():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def initStyleOption():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def notchSize():
    pass

  def notchTarget():
    pass

  def notchesVisible():
    pass

  def paintEvent():
    pass

  def rangeChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def setNotchTarget():
    pass

  def setNotchesVisible():
    pass

  def setTabOrder():
    pass

  def setWrapping():
    pass

  def sizeHint():
    pass

  def sliderChange():
    pass

  def sliderMoved():
    """ Signal """
    pass

  def sliderPressed():
    """ Signal """
    pass

  def sliderReleased():
    """ Signal """
    pass

  staticMetaObject = None

  def valueChanged():
    """ Signal """
    pass

  def wrapping():
    pass

class QDialog(QWidget):

  Accepted = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rejected = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accept():
    pass

  def accepted():
    """ Signal """
    pass

  def adjustPosition():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def done():
    pass

  def eventFilter():
    pass

  def exec_():
    pass

  def finished():
    """ Signal """
    pass

  def isSizeGripEnabled():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def open():
    pass

  def registerUserData():
    pass

  def reject():
    pass

  def rejected():
    """ Signal """
    pass

  def resizeEvent():
    pass

  def result():
    pass

  def setModal():
    pass

  def setResult():
    pass

  def setSizeGripEnabled():
    pass

  def setTabOrder():
    pass

  def setVisible():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

class QDialogButtonBox(QWidget):

  Abort = None
  AcceptRole = None
  ActionRole = None
  Apply = None
  ApplyRole = None

  class ButtonLayout(object):

    GnomeLayout = None
    KdeLayout = None
    MacLayout = None
    WinLayout = None
    name = property(None, None, None,
                    )

    values = {}

  class ButtonRole(object):

    AcceptRole = None
    ActionRole = None
    ApplyRole = None
    DestructiveRole = None
    HelpRole = None
    InvalidRole = None
    NRoles = None
    NoRole = None
    RejectRole = None
    ResetRole = None
    YesRole = None
    name = property(None, None, None,
                    )

    values = {}

  Cancel = None
  Close = None
  DestructiveRole = None
  Discard = None
  DrawChildren = None
  DrawWindowBackground = None
  FirstButton = None
  GnomeLayout = None
  Help = None
  HelpRole = None
  Ignore = None
  IgnoreMask = None
  InvalidRole = None
  KdeLayout = None
  LastButton = None
  MacLayout = None
  NRoles = None
  No = None
  NoButton = None
  NoRole = None
  NoToAll = None
  Ok = None
  Open = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  RejectRole = None
  Reset = None
  ResetRole = None
  RestoreDefaults = None
  Retry = None
  Save = None
  SaveAll = None

  class StandardButton(object):

    Abort = None
    Apply = None
    Cancel = None
    Close = None
    Discard = None
    FirstButton = None
    Help = None
    Ignore = None
    LastButton = None
    No = None
    NoButton = None
    NoToAll = None
    Ok = None
    Open = None
    Reset = None
    RestoreDefaults = None
    Retry = None
    Save = None
    SaveAll = None
    Yes = None
    YesToAll = None
    name = property(None, None, None,
                    )

    values = {}

  class StandardButtons(object):

    pass

  WinLayout = None
  Yes = None
  YesRole = None
  YesToAll = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def addButton():
    pass

  def button():
    pass

  def buttonRole():
    pass

  def buttons():
    pass

  def centerButtons():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def helpRequested():
    """ Signal """
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def orientation():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def removeButton():
    pass

  def setCenterButtons():
    pass

  def setOrientation():
    pass

  def setStandardButtons():
    pass

  def setTabOrder():
    pass

  def standardButton():
    pass

  def standardButtons():
    pass

  staticMetaObject = None

class QDirModel(QAbstractItemModel):

  FileIconRole = None
  FileNameRole = None
  FilePathRole = None

  class Roles(object):

    FileIconRole = None
    FileNameRole = None
    FilePathRole = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def columnCount():
    pass

  def columnsAboutToBeInserted():
    """ Signal """
    pass

  def columnsAboutToBeMoved():
    """ Signal """
    pass

  def columnsAboutToBeRemoved():
    """ Signal """
    pass

  def columnsInserted():
    """ Signal """
    pass

  def columnsMoved():
    """ Signal """
    pass

  def columnsRemoved():
    """ Signal """
    pass

  def connect():
    pass

  def data():
    pass

  def dataChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dropMimeData():
    pass

  def fileIcon():
    pass

  def fileInfo():
    pass

  def fileName():
    pass

  def filePath():
    pass

  def filter():
    pass

  def flags():
    pass

  def hasChildren():
    pass

  def headerData():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def iconProvider():
    pass

  def index():
    pass

  def isDir():
    pass

  def isReadOnly():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def lazyChildCount():
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def mkdir():
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def nameFilters():
    pass

  def parent():
    pass

  def refresh():
    pass

  def registerUserData():
    pass

  def remove():
    pass

  def resolveSymlinks():
    pass

  def rmdir():
    pass

  def rowCount():
    pass

  def rowsAboutToBeInserted():
    """ Signal """
    pass

  def rowsAboutToBeMoved():
    """ Signal """
    pass

  def rowsAboutToBeRemoved():
    """ Signal """
    pass

  def rowsInserted():
    """ Signal """
    pass

  def rowsMoved():
    """ Signal """
    pass

  def rowsRemoved():
    """ Signal """
    pass

  def setData():
    pass

  def setFilter():
    pass

  def setIconProvider():
    pass

  def setLazyChildCount():
    pass

  def setNameFilters():
    pass

  def setReadOnly():
    pass

  def setResolveSymlinks():
    pass

  def setSorting():
    pass

  def sort():
    pass

  def sorting():
    pass

  staticMetaObject = None

  def supportedDropActions():
    pass

class QDockWidget(QWidget):

  AllDockWidgetFeatures = None
  DockWidgetClosable = None

  class DockWidgetFeature(object):

    AllDockWidgetFeatures = None
    DockWidgetClosable = None
    DockWidgetFeatureMask = None
    DockWidgetFloatable = None
    DockWidgetMovable = None
    DockWidgetVerticalTitleBar = None
    NoDockWidgetFeatures = None
    Reserved = None
    name = property(None, None, None,
                    )

    values = {}

  DockWidgetFeatureMask = None

  class DockWidgetFeatures(object):

    pass

  DockWidgetFloatable = None
  DockWidgetMovable = None
  DockWidgetVerticalTitleBar = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  NoDockWidgetFeatures = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Reserved = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def allowedAreas():
    pass

  def allowedAreasChanged():
    """ Signal """
    pass

  def changeEvent():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dockLocationChanged():
    """ Signal """
    pass

  def event():
    pass

  def features():
    pass

  def featuresChanged():
    """ Signal """
    pass

  def initStyleOption():
    pass

  def isAreaAllowed():
    pass

  def isFloating():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def setAllowedAreas():
    pass

  def setFeatures():
    pass

  def setFloating():
    pass

  def setTabOrder():
    pass

  def setTitleBarWidget():
    pass

  def setWidget():
    pass

  staticMetaObject = None

  def titleBarWidget():
    pass

  def toggleViewAction():
    pass

  def topLevelChanged():
    """ Signal """
    pass

  def visibilityChanged():
    """ Signal """
    pass

  def widget():
    pass

class QDoubleSpinBox(QAbstractSpinBox):

  CorrectToNearestValue = None
  CorrectToPreviousValue = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  NoButtons = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  PlusMinus = None
  StepDownEnabled = None
  StepNone = None
  StepUpEnabled = None
  UpDownArrows = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cleanText():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def decimals():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editingFinished():
    """ Signal """
    pass

  def fixup():
    pass

  def keyboardGrabber():
    pass

  def maximum():
    pass

  def minimum():
    pass

  def mouseGrabber():
    pass

  def prefix():
    pass

  def registerUserData():
    pass

  def setDecimals():
    pass

  def setMaximum():
    pass

  def setMinimum():
    pass

  def setPrefix():
    pass

  def setRange():
    pass

  def setSingleStep():
    pass

  def setSuffix():
    pass

  def setTabOrder():
    pass

  def setValue():
    pass

  def singleStep():
    pass

  staticMetaObject = None

  def suffix():
    pass

  def textFromValue():
    pass

  def validate():
    pass

  def value():
    pass

  def valueChanged():
    """ Signal """
    pass

  def valueFromText():
    pass

class QErrorMessage(QDialog):

  Accepted = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rejected = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def changeEvent():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def done():
    pass

  def finished():
    """ Signal """
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def qtHandler():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def setTabOrder():
    pass

  def showMessage():
    pass

  staticMetaObject = None

class QFileDialog(QDialog):

  Accept = None

  class AcceptMode(object):

    AcceptOpen = None
    AcceptSave = None
    name = property(None, None, None,
                    )

    values = {}

  AcceptOpen = None
  AcceptSave = None
  Accepted = None
  AnyFile = None
  Detail = None
  class DialogLabel(object):

    Accept = None
    FileName = None
    FileType = None
    LookIn = None
    Reject = None
    name = property(None, None, None,
                    )

    values = {}

  Directory = None
  DirectoryOnly = None
  DontConfirmOverwrite = None
  DontResolveSymlinks = None
  DontUseNativeDialog = None
  DontUseSheet = None
  DrawChildren = None
  DrawWindowBackground = None
  ExistingFile = None
  ExistingFiles = None

  class FileMode(object):

    AnyFile = None
    Directory = None
    DirectoryOnly = None
    ExistingFile = None
    ExistingFiles = None
    name = property(None, None, None,
                    )

    values = {}

  FileName = None
  FileType = None
  HideNameFilterDetails = None
  IgnoreMask = None
  List = None
  LookIn = None

  class Option(object):

    DontConfirmOverwrite = None
    DontResolveSymlinks = None
    DontUseNativeDialog = None
    DontUseSheet = None
    HideNameFilterDetails = None
    ReadOnly = None
    ShowDirsOnly = None
    name = property(None, None, None,
                    )

    values = {}

  class Options(object):

    pass

  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  ReadOnly = None
  Reject = None
  Rejected = None
  ShowDirsOnly = None

  class ViewMode(object):

    Detail = None
    List = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accept():
    pass

  def acceptMode():
    pass

  def accepted():
    """ Signal """
    pass

  def changeEvent():
    pass

  def confirmOverwrite():
    pass

  def connect():
    pass

  def currentChanged():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def defaultSuffix():
    pass

  def destroyed():
    """ Signal """
    pass

  def directory():
    pass

  def directoryEntered():
    """ Signal """
    pass

  def disconnect():
    pass

  def done():
    pass

  def fileMode():
    pass

  def fileSelected():
    """ Signal """
    pass

  def filesSelected():
    """ Signal """
    pass

  def filter():
    pass

  def filterSelected():
    """ Signal """
    pass

  def filters():
    pass

  def finished():
    """ Signal """
    pass

  def getExistingDirectory():
    pass

  def getOpenFileName():
    pass

  def getOpenFileNames():
    pass

  def getSaveFileName():
    pass

  def history():
    pass

  def iconProvider():
    pass

  def isNameFilterDetailsVisible():
    pass

  def isReadOnly():
    pass

  def itemDelegate():
    pass

  def keyboardGrabber():
    pass

  def labelText():
    pass

  def mouseGrabber():
    pass

  def nameFilters():
    pass

  def open():
    pass

  def options():
    pass

  def proxyModel():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def resolveSymlinks():
    pass

  def restoreState():
    pass

  def saveState():
    pass

  def selectFile():
    pass

  def selectFilter():
    pass

  def selectNameFilter():
    pass

  def selectedFiles():
    pass

  def selectedFilter():
    pass

  def selectedNameFilter():
    pass

  def setAcceptMode():
    pass

  def setConfirmOverwrite():
    pass

  def setDefaultSuffix():
    pass

  def setDirectory():
    pass

  def setFileMode():
    pass

  def setFilter():
    pass

  def setFilters():
    pass

  def setHistory():
    pass

  def setIconProvider():
    pass

  def setItemDelegate():
    pass

  def setLabelText():
    pass

  def setNameFilter():
    pass

  def setNameFilterDetailsVisible():
    pass

  def setNameFilters():
    pass

  def setOption():
    pass

  def setOptions():
    pass

  def setProxyModel():
    pass

  def setReadOnly():
    pass

  def setResolveSymlinks():
    pass

  def setSidebarUrls():
    pass

  def setTabOrder():
    pass

  def setViewMode():
    pass

  def setVisible():
    pass

  def sidebarUrls():
    pass

  staticMetaObject = None

  def testOption():
    pass

  def viewMode():
    pass

class QFileIconProvider(Object):

  Computer = None
  Desktop = None
  Drive = None
  File = None
  Folder = None

  class IconType(object):

    Computer = None
    Desktop = None
    Drive = None
    File = None
    Folder = None
    Network = None
    Trashcan = None
    name = property(None, None, None,
                    )

    values = {}

  Network = None
  Trashcan = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def icon():
    pass

  def type():
    pass

class QFileSystemModel(QAbstractItemModel):

  FileIconRole = None
  FileNameRole = None
  FilePathRole = None
  FilePermissions = None

  class Roles(object):

    FileIconRole = None
    FileNameRole = None
    FilePathRole = None
    FilePermissions = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def canFetchMore():
    pass

  def columnCount():
    pass

  def columnsAboutToBeInserted():
    """ Signal """
    pass

  def columnsAboutToBeMoved():
    """ Signal """
    pass

  def columnsAboutToBeRemoved():
    """ Signal """
    pass

  def columnsInserted():
    """ Signal """
    pass

  def columnsMoved():
    """ Signal """
    pass

  def columnsRemoved():
    """ Signal """
    pass

  def connect():
    pass

  def data():
    pass

  def dataChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def directoryLoaded():
    """ Signal """
    pass

  def disconnect():
    pass

  def dropMimeData():
    pass

  def event():
    pass

  def fetchMore():
    pass

  def fileIcon():
    pass

  def fileInfo():
    pass

  def fileName():
    pass

  def filePath():
    pass

  def fileRenamed():
    """ Signal """
    pass

  def filter():
    pass

  def flags():
    pass

  def hasChildren():
    pass

  def headerData():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def iconProvider():
    pass

  def index():
    pass

  def isDir():
    pass

  def isReadOnly():
    pass

  def lastModified():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def mkdir():
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def myComputer():
    pass

  def nameFilterDisables():
    pass

  def nameFilters():
    pass

  def parent():
    pass

  def permissions():
    pass

  def registerUserData():
    pass

  def remove():
    pass

  def resolveSymlinks():
    pass

  def rmdir():
    pass

  def rootDirectory():
    pass

  def rootPath():
    pass

  def rootPathChanged():
    """ Signal """
    pass

  def rowCount():
    pass

  def rowsAboutToBeInserted():
    """ Signal """
    pass

  def rowsAboutToBeMoved():
    """ Signal """
    pass

  def rowsAboutToBeRemoved():
    """ Signal """
    pass

  def rowsInserted():
    """ Signal """
    pass

  def rowsMoved():
    """ Signal """
    pass

  def rowsRemoved():
    """ Signal """
    pass

  def setData():
    pass

  def setFilter():
    pass

  def setIconProvider():
    pass

  def setNameFilterDisables():
    pass

  def setNameFilters():
    pass

  def setReadOnly():
    pass

  def setResolveSymlinks():
    pass

  def setRootPath():
    pass

  def size():
    pass

  def sort():
    pass

  staticMetaObject = None

  def supportedDropActions():
    pass

  def timerEvent():
    pass

  def type():
    pass

class QFocusFrame(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def initStyleOption():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  def setWidget():
    pass

  staticMetaObject = None

  def widget():
    pass

class QFontComboBox(QComboBox):

  AdjustToContents = None
  AdjustToContentsOnFirstShow = None
  AdjustToMinimumContentsLength = None
  AdjustToMinimumContentsLengthWithIcon = None
  AllFonts = None
  DrawChildren = None
  DrawWindowBackground = None

  class FontFilter(object):

    AllFonts = None
    MonospacedFonts = None
    NonScalableFonts = None
    ProportionalFonts = None
    ScalableFonts = None
    name = property(None, None, None,
                    )

    values = {}

  class FontFilters(object):

    pass

  IgnoreMask = None
  InsertAfterCurrent = None
  InsertAlphabetically = None
  InsertAtBottom = None
  InsertAtCurrent = None
  InsertAtTop = None
  InsertBeforeCurrent = None
  MonospacedFonts = None
  NoInsert = None
  NonScalableFonts = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  ProportionalFonts = None
  ScalableFonts = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def connect():
    pass

  def currentFont():
    pass

  def currentFontChanged():
    """ Signal """
    pass

  def currentIndexChanged():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editTextChanged():
    """ Signal """
    pass

  def event():
    pass

  def fontFilters():
    pass

  def highlighted():
    """ Signal """
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def setCurrentFont():
    pass

  def setFontFilters():
    pass

  def setTabOrder():
    pass

  def setWritingSystem():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def textChanged():
    """ Signal """
    pass

  def writingSystem():
    pass

class QFontDialog(QDialog):

  Accepted = None
  DontUseNativeDialog = None
  DrawChildren = None
  DrawWindowBackground = None

  class FontDialogOption(object):

    DontUseNativeDialog = None
    NoButtons = None
    name = property(None, None, None,
                    )

    values = {}

  class FontDialogOptions(object):

    pass

  IgnoreMask = None
  NoButtons = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rejected = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def changeEvent():
    pass

  def connect():
    pass

  def currentFont():
    pass

  def currentFontChanged():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def done():
    pass

  def eventFilter():
    pass

  def finished():
    """ Signal """
    pass

  def fontSelected():
    """ Signal """
    pass

  def getFont():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def open():
    pass

  def options():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def selectedFont():
    pass

  def setCurrentFont():
    pass

  def setOption():
    pass

  def setOptions():
    pass

  def setTabOrder():
    pass

  def setVisible():
    pass

  staticMetaObject = None

  def testOption():
    pass

class QFormLayout(QLayout):

  AllNonFixedFieldsGrow = None
  DontWrapRows = None
  ExpandingFieldsGrow = None

  class FieldGrowthPolicy(object):

    AllNonFixedFieldsGrow = None
    ExpandingFieldsGrow = None
    FieldsStayAtSizeHint = None
    name = property(None, None, None,
                    )

    values = {}

  FieldRole = None
  FieldsStayAtSizeHint = None

  class ItemRole(object):

    FieldRole = None
    LabelRole = None
    SpanningRole = None
    name = property(None, None, None,
                    )

    values = {}

  LabelRole = None

  class RowWrapPolicy(object):

    DontWrapRows = None
    WrapAllRows = None
    WrapLongRows = None
    name = property(None, None, None,
                    )

    values = {}

  SetDefaultConstraint = None
  SetFixedSize = None
  SetMaximumSize = None
  SetMinAndMaxSize = None
  SetMinimumSize = None
  SetNoConstraint = None
  SpanningRole = None
  WrapAllRows = None
  WrapLongRows = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addItem():
    pass

  def addRow():
    pass

  def closestAcceptableSize():
    pass

  def connect():
    pass

  def count():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def expandingDirections():
    pass

  def fieldGrowthPolicy():
    pass

  def formAlignment():
    pass

  def getItemPosition():
    pass

  def getLayoutPosition():
    pass

  def getWidgetPosition():
    pass

  def hasHeightForWidth():
    pass

  def heightForWidth():
    pass

  def horizontalSpacing():
    pass

  def insertRow():
    pass

  def invalidate():
    pass

  def itemAt():
    pass

  def labelAlignment():
    pass

  def labelForField():
    pass

  def minimumSize():
    pass

  def registerUserData():
    pass

  def rowCount():
    pass

  def rowWrapPolicy():
    pass

  def setFieldGrowthPolicy():
    pass

  def setFormAlignment():
    pass

  def setGeometry():
    pass

  def setHorizontalSpacing():
    pass

  def setItem():
    pass

  def setLabelAlignment():
    pass

  def setLayout():
    pass

  def setRowWrapPolicy():
    pass

  def setSpacing():
    pass

  def setVerticalSpacing():
    pass

  def setWidget():
    pass

  def sizeHint():
    pass

  def spacing():
    pass

  staticMetaObject = None

  def takeAt():
    pass

  def verticalSpacing():
    pass

class QFrame(QWidget):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def changeEvent():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def drawFrame():
    pass

  def event():
    pass

  def frameRect():
    pass

  def frameShadow():
    pass

  def frameShape():
    pass

  def frameStyle():
    pass

  def frameWidth():
    pass

  def keyboardGrabber():
    pass

  def lineWidth():
    pass

  def midLineWidth():
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def setFrameRect():
    pass

  def setFrameShadow():
    pass

  def setFrameShape():
    pass

  def setFrameStyle():
    pass

  def setLineWidth():
    pass

  def setMidLineWidth():
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

class QGesture(QObject):

  CancelAllInContext = None
  CancelNone = None

  class GestureCancelPolicy(object):

    CancelAllInContext = None
    CancelNone = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def gestureCancelPolicy():
    pass

  def gestureType():
    pass

  def hasHotSpot():
    pass

  def hotSpot():
    pass

  def registerUserData():
    pass

  def setGestureCancelPolicy():
    pass

  def setHotSpot():
    pass

  def state():
    pass

  staticMetaObject = None

  def unsetHotSpot():
    pass

class QGestureEvent(QEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None

  class Type(object):

    AcceptDropsChange = None
    AccessibilityDescription = None
    AccessibilityHelp = None
    AccessibilityPrepare = None
    ActionAdded = None
    ActionChanged = None
    ActionRemoved = None
    ActivateControl = None
    ActivationChange = None
    ApplicationActivate = None
    ApplicationActivated = None
    ApplicationDeactivate = None
    ApplicationDeactivated = None
    ApplicationFontChange = None
    ApplicationLayoutDirectionChange = None
    ApplicationPaletteChange = None
    ApplicationWindowIconChange = None
    ChildAdded = None
    ChildPolished = None
    ChildRemoved = None
    Clipboard = None
    Close = None
    CloseSoftwareInputPanel = None
    ContentsRectChange = None
    ContextMenu = None
    Create = None
    CursorChange = None
    DeactivateControl = None
    DeferredDelete = None
    Destroy = None
    DragEnter = None
    DragLeave = None
    DragMove = None
    DragResponse = None
    Drop = None
    DynamicPropertyChange = None
    EmbeddingControl = None
    EnabledChange = None
    Enter = None
    EnterWhatsThisMode = None
    FileOpen = None
    FocusIn = None
    FocusOut = None
    FontChange = None
    FutureCallOut = None
    Gesture = None
    GestureOverride = None
    GrabKeyboard = None
    GrabMouse = None
    GraphicsSceneContextMenu = None
    GraphicsSceneDragEnter = None
    GraphicsSceneDragLeave = None
    GraphicsSceneDragMove = None
    GraphicsSceneDrop = None
    GraphicsSceneHelp = None
    GraphicsSceneHoverEnter = None
    GraphicsSceneHoverLeave = None
    GraphicsSceneHoverMove = None
    GraphicsSceneMouseDoubleClick = None
    GraphicsSceneMouseMove = None
    GraphicsSceneMousePress = None
    GraphicsSceneMouseRelease = None
    GraphicsSceneMove = None
    GraphicsSceneResize = None
    GraphicsSceneWheel = None
    HelpRequest = None
    Hide = None
    HideToParent = None
    HoverEnter = None
    HoverLeave = None
    HoverMove = None
    IconDrag = None
    IconTextChange = None
    InputMethod = None
    KeyPress = None
    KeyRelease = None
    KeyboardLayoutChange = None
    LanguageChange = None
    LayoutDirectionChange = None
    LayoutRequest = None
    Leave = None
    LeaveWhatsThisMode = None
    LocaleChange = None
    MacGLClearDrawable = None
    MacGLWindowChange = None
    MacSizeChange = None
    MaxUser = None
    MenubarUpdated = None
    MetaCall = None
    ModifiedChange = None
    MouseButtonDblClick = None
    MouseButtonPress = None
    MouseButtonRelease = None
    MouseMove = None
    MouseTrackingChange = None
    Move = None
    NativeGesture = None
    NetworkReplyUpdated = None
    NonClientAreaMouseButtonDblClick = None
    NonClientAreaMouseButtonPress = None
    NonClientAreaMouseButtonRelease = None
    NonClientAreaMouseMove = None
    None = None
    OkRequest = None
    Paint = None
    PaletteChange = None
    ParentAboutToChange = None
    ParentChange = None
    PlatformPanel = None
    Polish = None
    PolishRequest = None
    QueryWhatsThis = None
    Quit = None
    RequestSoftwareInputPanel = None
    Resize = None
    Shortcut = None
    ShortcutOverride = None
    Show = None
    ShowToParent = None
    ShowWindowRequest = None
    SockAct = None
    Speech = None
    StateMachineSignal = None
    StateMachineWrapped = None
    StatusTip = None
    Style = None
    StyleChange = None
    TabletEnterProximity = None
    TabletLeaveProximity = None
    TabletMove = None
    TabletPress = None
    TabletRelease = None
    ThreadChange = None
    Timer = None
    ToolBarChange = None
    ToolTip = None
    ToolTipChange = None
    TouchBegin = None
    TouchEnd = None
    TouchUpdate = None
    UngrabKeyboard = None
    UngrabMouse = None
    UpdateLater = None
    UpdateRequest = None
    UpdateSoftKeys = None
    User = None
    WhatsThis = None
    WhatsThisClicked = None
    Wheel = None
    WinEventAct = None
    WinIdChange = None
    WindowActivate = None
    WindowBlocked = None
    WindowDeactivate = None
    WindowIconChange = None
    WindowStateChange = None
    WindowTitleChange = None
    WindowUnblocked = None
    ZOrderChange = None
    ZeroTimerEvent = None
    name = property(None, None, None,
                    )

    values = {}

  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accept():
    pass

  def activeGestures():
    pass

  def canceledGestures():
    pass

  def gesture():
    pass

  def gestures():
    pass

  def ignore():
    pass

  def isAccepted():
    pass

  def mapToGraphicsScene():
    pass

  def registerEventType():
    pass

  def setAccepted():
    pass

  def setWidget():
    pass

  def widget():
    pass

class QGestureRecognizer(Object):

  CancelGesture = None
  ConsumeEventHint = None
  FinishGesture = None
  Ignore = None
  MayBeGesture = None

  class Result(object):

    pass

  class ResultFlag(object):

    CancelGesture = None
    ConsumeEventHint = None
    FinishGesture = None
    Ignore = None
    MayBeGesture = None
    ResultHint_Mask = None
    ResultState_Mask = None
    TriggerGesture = None
    name = property(None, None, None,
                    )

    values = {}

  ResultHint_Mask = None
  ResultState_Mask = None
  TriggerGesture = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def create():
    pass

  def recognize():
    pass

  def registerRecognizer():
    pass

  def reset():
    pass

  def unregisterRecognizer():
    pass

class QGraphicsAnchor(QObject):

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def registerUserData():
    pass

  def setSizePolicy():
    pass

  def setSpacing():
    pass

  def sizePolicy():
    pass

  def spacing():
    pass

  staticMetaObject = None

  def unsetSpacing():
    pass

class QGraphicsAnchorLayout(QGraphicsLayout):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addAnchor():
    pass

  def addAnchors():
    pass

  def addCornerAnchors():
    pass

  def anchor():
    pass

  def count():
    pass

  def horizontalSpacing():
    pass

  def instantInvalidatePropagation():
    pass

  def invalidate():
    pass

  def itemAt():
    pass

  def removeAt():
    pass

  def setGeometry():
    pass

  def setHorizontalSpacing():
    pass

  def setInstantInvalidatePropagation():
    pass

  def setSpacing():
    pass

  def setVerticalSpacing():
    pass

  def sizeHint():
    pass

  def verticalSpacing():
    pass

class QGraphicsBlurEffect(QGraphicsEffect):

  AnimationHint = None

  class BlurHint(object):

    AnimationHint = None
    PerformanceHint = None
    QualityHint = None
    name = property(None, None, None,
                    )

    values = {}

  class BlurHints(object):

    pass

  class ChangeFlag(object):

    SourceAttached = None
    SourceBoundingRectChanged = None
    SourceDetached = None
    SourceInvalidated = None
    name = property(None, None, None,
                    )

    values = {}

  class ChangeFlags(object):

    pass

  NoPad = None
  PadToEffectiveBoundingRect = None
  PadToTransparentBorder = None
  PerformanceHint = None

  class PixmapPadMode(object):

    NoPad = None
    PadToEffectiveBoundingRect = None
    PadToTransparentBorder = None
    name = property(None, None, None,
                    )

    values = {}

  QualityHint = None
  SourceAttached = None
  SourceBoundingRectChanged = None
  SourceDetached = None
  SourceInvalidated = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def blurHints():
    pass

  def blurHintsChanged():
    """ Signal """
    pass

  def blurRadius():
    pass

  def blurRadiusChanged():
    """ Signal """
    pass

  def boundingRectFor():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def draw():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setBlurHints():
    pass

  def setBlurRadius():
    pass

  staticMetaObject = None

class QGraphicsColorizeEffect(QGraphicsEffect):

  NoPad = None
  PadToEffectiveBoundingRect = None
  PadToTransparentBorder = None
  SourceAttached = None
  SourceBoundingRectChanged = None
  SourceDetached = None
  SourceInvalidated = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def color():
    pass

  def colorChanged():
    """ Signal """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def draw():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setColor():
    pass

  def setStrength():
    pass

  staticMetaObject = None

  def strength():
    pass

  def strengthChanged():
    """ Signal """
    pass

class QGraphicsDropShadowEffect(QGraphicsEffect):

  NoPad = None
  PadToEffectiveBoundingRect = None
  PadToTransparentBorder = None
  SourceAttached = None
  SourceBoundingRectChanged = None
  SourceDetached = None
  SourceInvalidated = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def blurRadius():
    pass

  def blurRadiusChanged():
    """ Signal """
    pass

  def boundingRectFor():
    pass

  def color():
    pass

  def colorChanged():
    """ Signal """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def draw():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def offset():
    pass

  def offsetChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setBlurRadius():
    pass

  def setColor():
    pass

  def setOffset():
    pass

  def setXOffset():
    pass

  def setYOffset():
    pass

  staticMetaObject = None

  def xOffset():
    pass

  def yOffset():
    pass

class QGraphicsEffect(QObject):

  NoPad = None
  PadToEffectiveBoundingRect = None
  PadToTransparentBorder = None
  SourceAttached = None
  SourceBoundingRectChanged = None
  SourceDetached = None
  SourceInvalidated = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def boundingRectFor():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def draw():
    pass

  def drawSource():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def isEnabled():
    pass

  def registerUserData():
    pass

  def setEnabled():
    pass

  def sourceBoundingRect():
    pass

  def sourceChanged():
    pass

  def sourceIsPixmap():
    pass

  def sourcePixmap():
    pass

  staticMetaObject = None

  def update():
    pass

  def updateBoundingRect():
    pass

class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def extension():
    pass

  def isObscuredBy():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def rect():
    pass

  def setRect():
    pass

  def setSpanAngle():
    pass

  def setStartAngle():
    pass

  def shape():
    pass

  def spanAngle():
    pass

  def startAngle():
    pass

  def type():
    pass

class QGraphicsGridLayout(QGraphicsLayout):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addItem():
    pass

  def alignment():
    pass

  def columnAlignment():
    pass

  def columnCount():
    pass

  def columnMaximumWidth():
    pass

  def columnMinimumWidth():
    pass

  def columnPreferredWidth():
    pass

  def columnSpacing():
    pass

  def columnStretchFactor():
    pass

  def count():
    pass

  def horizontalSpacing():
    pass

  def instantInvalidatePropagation():
    pass

  def invalidate():
    pass

  def itemAt():
    pass

  def removeAt():
    pass

  def removeItem():
    pass

  def rowAlignment():
    pass

  def rowCount():
    pass

  def rowMaximumHeight():
    pass

  def rowMinimumHeight():
    pass

  def rowPreferredHeight():
    pass

  def rowSpacing():
    pass

  def rowStretchFactor():
    pass

  def setAlignment():
    pass

  def setColumnAlignment():
    pass

  def setColumnFixedWidth():
    pass

  def setColumnMaximumWidth():
    pass

  def setColumnMinimumWidth():
    pass

  def setColumnPreferredWidth():
    pass

  def setColumnSpacing():
    pass

  def setColumnStretchFactor():
    pass

  def setGeometry():
    pass

  def setHorizontalSpacing():
    pass

  def setInstantInvalidatePropagation():
    pass

  def setRowAlignment():
    pass

  def setRowFixedHeight():
    pass

  def setRowMaximumHeight():
    pass

  def setRowMinimumHeight():
    pass

  def setRowPreferredHeight():
    pass

  def setRowSpacing():
    pass

  def setRowStretchFactor():
    pass

  def setSpacing():
    pass

  def setVerticalSpacing():
    pass

  def sizeHint():
    pass

  def verticalSpacing():
    pass

class QGraphicsItem(Object):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def acceptDrops():
    pass

  def acceptHoverEvents():
    pass

  def acceptTouchEvents():
    pass

  def acceptedMouseButtons():
    pass

  def acceptsHoverEvents():
    pass

  def addToIndex():
    pass

  def advance():
    pass

  def boundingRect():
    pass

  def boundingRegion():
    pass

  def boundingRegionGranularity():
    pass

  def cacheMode():
    pass

  def childItems():
    pass

  def childrenBoundingRect():
    pass

  def clearFocus():
    pass

  def clipPath():
    pass

  def collidesWithItem():
    pass

  def collidesWithPath():
    pass

  def collidingItems():
    pass

  def commonAncestorItem():
    pass

  def contains():
    pass

  def contextMenuEvent():
    pass

  def cursor():
    pass

  def data():
    pass

  def deviceTransform():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def effectiveOpacity():
    pass

  def ensureVisible():
    pass

  def extension():
    pass

  def filtersChildEvents():
    pass

  def flags():
    pass

  def focusInEvent():
    pass

  def focusItem():
    pass

  def focusOutEvent():
    pass

  def focusProxy():
    pass

  def focusScopeItem():
    pass

  def grabKeyboard():
    pass

  def grabMouse():
    pass

  def graphicsEffect():
    pass

  def group():
    pass

  def handlesChildEvents():
    pass

  def hasCursor():
    pass

  def hasFocus():
    pass

  def hide():
    pass

  def hoverEnterEvent():
    pass

  def hoverLeaveEvent():
    pass

  def hoverMoveEvent():
    pass

  def inputMethodEvent():
    pass

  def inputMethodHints():
    pass

  def inputMethodQuery():
    pass

  def installSceneEventFilter():
    pass

  def isActive():
    pass

  def isAncestorOf():
    pass

  def isBlockedByModalPanel():
    pass

  def isClipped():
    pass

  def isEnabled():
    pass

  def isObscured():
    pass

  def isObscuredBy():
    pass

  def isPanel():
    pass

  def isSelected():
    pass

  def isUnderMouse():
    pass

  def isVisible():
    pass

  def isVisibleTo():
    pass

  def isWidget():
    pass

  def isWindow():
    pass

  def itemChange():
    pass

  def itemTransform():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def mapFromItem():
    pass

  def mapFromParent():
    pass

  def mapFromScene():
    pass

  def mapRectFromItem():
    pass

  def mapRectFromParent():
    pass

  def mapRectFromScene():
    pass

  def mapRectToItem():
    pass

  def mapRectToParent():
    pass

  def mapRectToScene():
    pass

  def mapToItem():
    pass

  def mapToParent():
    pass

  def mapToScene():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveBy():
    pass

  def opacity():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def panel():
    pass

  def panelModality():
    pass

  def parentItem():
    pass

  def parentObject():
    pass

  def parentWidget():
    pass

  def pos():
    pass

  def prepareGeometryChange():
    pass

  def removeFromIndex():
    pass

  def removeSceneEventFilter():
    pass

  def resetTransform():
    pass

  def rotate():
    pass

  def rotation():
    pass

  def scale():
    pass

  def scene():
    pass

  def sceneBoundingRect():
    pass

  def sceneEvent():
    pass

  def sceneEventFilter():
    pass

  def scenePos():
    pass

  def sceneTransform():
    pass

  def scroll():
    pass

  def setAcceptDrops():
    pass

  def setAcceptHoverEvents():
    pass

  def setAcceptTouchEvents():
    pass

  def setAcceptedMouseButtons():
    pass

  def setAcceptsHoverEvents():
    pass

  def setActive():
    pass

  def setBoundingRegionGranularity():
    pass

  def setCacheMode():
    pass

  def setCursor():
    pass

  def setData():
    pass

  def setEnabled():
    pass

  def setFiltersChildEvents():
    pass

  def setFlag():
    pass

  def setFlags():
    pass

  def setFocus():
    pass

  def setFocusProxy():
    pass

  def setGraphicsEffect():
    pass

  def setGroup():
    pass

  def setHandlesChildEvents():
    pass

  def setInputMethodHints():
    pass

  def setOpacity():
    pass

  def setPanelModality():
    pass

  def setParentItem():
    pass

  def setPos():
    pass

  def setRotation():
    pass

  def setScale():
    pass

  def setSelected():
    pass

  def setToolTip():
    pass

  def setTransform():
    pass

  def setTransformOriginPoint():
    pass

  def setTransformations():
    pass

  def setVisible():
    pass

  def setX():
    pass

  def setY():
    pass

  def setZValue():
    pass

  def shape():
    pass

  def shear():
    pass

  def show():
    pass

  def stackBefore():
    pass

  def toGraphicsObject():
    pass

  def toolTip():
    pass

  def topLevelItem():
    pass

  def topLevelWidget():
    pass

  def transform():
    pass

  def transformOriginPoint():
    pass

  def transformations():
    pass

  def translate():
    pass

  def type():
    pass

  def ungrabKeyboard():
    pass

  def ungrabMouse():
    pass

  def unsetCursor():
    pass

  def update():
    pass

  def updateMicroFocus():
    pass

  def wheelEvent():
    pass

  def window():
    pass

  def x():
    pass

  def y():
    pass

  def zValue():
    pass

class QGraphicsItemGroup(QGraphicsItem):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addToGroup():
    pass

  def boundingRect():
    pass

  def isObscuredBy():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def removeFromGroup():
    pass

  def type():
    pass

class QGraphicsLayout(QGraphicsLayoutItem):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activate():
    pass

  def addChildLayoutItem():
    pass

  def count():
    pass

  def getContentsMargins():
    pass

  def instantInvalidatePropagation():
    pass

  def invalidate():
    pass

  def isActivated():
    pass

  def itemAt():
    pass

  def removeAt():
    pass

  def setContentsMargins():
    pass

  def setInstantInvalidatePropagation():
    pass

  def updateGeometry():
    pass

  def widgetEvent():
    pass

class QGraphicsLayoutItem(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def contentsRect():
    pass

  def effectiveSizeHint():
    pass

  def geometry():
    pass

  def getContentsMargins():
    pass

  def graphicsItem():
    pass

  def isLayout():
    pass

  def maximumHeight():
    pass

  def maximumSize():
    pass

  def maximumWidth():
    pass

  def minimumHeight():
    pass

  def minimumSize():
    pass

  def minimumWidth():
    pass

  def ownedByLayout():
    pass

  def parentLayoutItem():
    pass

  def preferredHeight():
    pass

  def preferredSize():
    pass

  def preferredWidth():
    pass

  def setGeometry():
    pass

  def setGraphicsItem():
    pass

  def setMaximumHeight():
    pass

  def setMaximumSize():
    pass

  def setMaximumWidth():
    pass

  def setMinimumHeight():
    pass

  def setMinimumSize():
    pass

  def setMinimumWidth():
    pass

  def setOwnedByLayout():
    pass

  def setParentLayoutItem():
    pass

  def setPreferredHeight():
    pass

  def setPreferredSize():
    pass

  def setPreferredWidth():
    pass

  def setSizePolicy():
    pass

  def sizeHint():
    pass

  def sizePolicy():
    pass

  def updateGeometry():
    pass

class QGraphicsLineItem(QGraphicsItem):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def extension():
    pass

  def isObscuredBy():
    pass

  def line():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def pen():
    pass

  def setLine():
    pass

  def setPen():
    pass

  def shape():
    pass

  def type():
    pass

class QGraphicsLinearLayout(QGraphicsLayout):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addItem():
    pass

  def addStretch():
    pass

  def alignment():
    pass

  def count():
    pass

  def dump():
    pass

  def insertItem():
    pass

  def insertStretch():
    pass

  def instantInvalidatePropagation():
    pass

  def invalidate():
    pass

  def itemAt():
    pass

  def itemSpacing():
    pass

  def orientation():
    pass

  def removeAt():
    pass

  def removeItem():
    pass

  def setAlignment():
    pass

  def setGeometry():
    pass

  def setInstantInvalidatePropagation():
    pass

  def setItemSpacing():
    pass

  def setOrientation():
    pass

  def setSpacing():
    pass

  def setStretchFactor():
    pass

  def sizeHint():
    pass

  def spacing():
    pass

  def stretchFactor():
    pass

class QGraphicsObject(QObject):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def childrenChanged():
    """ Signal """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def grabGesture():
    pass

  def heightChanged():
    """ Signal """
    pass

  def opacityChanged():
    """ Signal """
    pass

  def parentChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def rotationChanged():
    """ Signal """
    pass

  def scaleChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def ungrabGesture():
    pass

  def updateMicroFocus():
    pass

  def visibleChanged():
    """ Signal """
    pass

  def widthChanged():
    """ Signal """
    pass

  def xChanged():
    """ Signal """
    pass

  def yChanged():
    """ Signal """
    pass

  def zChanged():
    """ Signal """
    pass

class QGraphicsOpacityEffect(QGraphicsEffect):

  NoPad = None
  PadToEffectiveBoundingRect = None
  PadToTransparentBorder = None
  SourceAttached = None
  SourceBoundingRectChanged = None
  SourceDetached = None
  SourceInvalidated = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def draw():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def opacity():
    pass

  def opacityChanged():
    """ Signal """
    pass

  def opacityMask():
    pass

  def opacityMaskChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setOpacity():
    pass

  def setOpacityMask():
    pass

  staticMetaObject = None

class QGraphicsPathItem(QAbstractGraphicsShapeItem):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def extension():
    pass

  def isObscuredBy():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def path():
    pass

  def setPath():
    pass

  def shape():
    pass

  def type():
    pass

class QGraphicsPixmapItem(QGraphicsItem):

  BoundingRectShape = None
  DeviceCoordinateCache = None
  HeuristicMaskShape = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  MaskShape = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None

  class ShapeMode(object):

    BoundingRectShape = None
    HeuristicMaskShape = None
    MaskShape = None
    name = property(None, None, None,
                    )

    values = {}

  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def extension():
    pass

  def isObscuredBy():
    pass

  def offset():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def pixmap():
    pass

  def setOffset():
    pass

  def setPixmap():
    pass

  def setShapeMode():
    pass

  def setTransformationMode():
    pass

  def shape():
    pass

  def shapeMode():
    pass

  def transformationMode():
    pass

  def type():
    pass

class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def extension():
    pass

  def fillRule():
    pass

  def isObscuredBy():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def polygon():
    pass

  def setFillRule():
    pass

  def setPolygon():
    pass

  def shape():
    pass

  def type():
    pass

class QGraphicsProxyWidget(QGraphicsWidget):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def childrenChanged():
    """ Signal """
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def createProxyForChildWidget():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def event():
    pass

  def eventFilter():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def geometryChanged():
    """ Signal """
    pass

  def grabMouseEvent():
    pass

  def heightChanged():
    """ Signal """
    pass

  def hideEvent():
    pass

  def hoverEnterEvent():
    pass

  def hoverLeaveEvent():
    pass

  def hoverMoveEvent():
    pass

  def itemChange():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def layoutChanged():
    """ Signal """
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def newProxyWidget():
    pass

  def opacityChanged():
    """ Signal """
    pass

  def paint():
    pass

  def parentChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def rotationChanged():
    """ Signal """
    pass

  def scaleChanged():
    """ Signal """
    pass

  def setGeometry():
    pass

  def setTabOrder():
    pass

  def setWidget():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def subWidgetRect():
    pass

  def type():
    pass

  def ungrabMouseEvent():
    pass

  def visibleChanged():
    """ Signal """
    pass

  def wheelEvent():
    pass

  def widget():
    pass

  def widthChanged():
    """ Signal """
    pass

  def xChanged():
    """ Signal """
    pass

  def yChanged():
    """ Signal """
    pass

  def zChanged():
    """ Signal """
    pass

class QGraphicsRectItem(QAbstractGraphicsShapeItem):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def extension():
    pass

  def isObscuredBy():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def rect():
    pass

  def setRect():
    pass

  def shape():
    pass

  def type():
    pass

class QGraphicsRotation(QGraphicsTransform):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def angle():
    pass

  def angleChanged():
    """ Signal """
    pass

  def applyTo():
    pass

  def axis():
    pass

  def axisChanged():
    """ Signal """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def origin():
    pass

  def originChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setAngle():
    pass

  def setAxis():
    pass

  def setOrigin():
    pass

  staticMetaObject = None

class QGraphicsScale(QGraphicsTransform):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def applyTo():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def origin():
    pass

  def originChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def scaleChanged():
    """ Signal """
    pass

  def setOrigin():
    pass

  def setXScale():
    pass

  def setYScale():
    pass

  def setZScale():
    pass

  staticMetaObject = None

  def xScale():
    pass

  def xScaleChanged():
    """ Signal """
    pass

  def yScale():
    pass

  def yScaleChanged():
    """ Signal """
    pass

  def zScale():
    pass

  def zScaleChanged():
    """ Signal """
    pass

class QGraphicsScene(QObject):

  AllLayers = None
  BackgroundLayer = None
  BspTreeIndex = None
  ForegroundLayer = None

  class ItemIndexMethod(object):

    BspTreeIndex = None
    NoIndex = None
    name = property(None, None, None,
                    )

    values = {}

  ItemLayer = None
  NoIndex = None

  class SceneLayer(object):

    AllLayers = None
    BackgroundLayer = None
    ForegroundLayer = None
    ItemLayer = None
    name = property(None, None, None,
                    )

    values = {}

  class SceneLayers(object):

    pass

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activePanel():
    pass

  def activeWindow():
    pass

  def addEllipse():
    pass

  def addItem():
    pass

  def addLine():
    pass

  def addPath():
    pass

  def addPixmap():
    pass

  def addPolygon():
    pass

  def addRect():
    pass

  def addSimpleText():
    pass

  def addText():
    pass

  def addWidget():
    pass

  def advance():
    pass

  def backgroundBrush():
    pass

  def bspTreeDepth():
    pass

  def changed():
    """ Signal """
    pass

  def clear():
    pass

  def clearFocus():
    pass

  def clearSelection():
    pass

  def collidingItems():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def createItemGroup():
    pass

  def destroyItemGroup():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def drawBackground():
    pass

  def drawForeground():
    pass

  def dropEvent():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def focusInEvent():
    pass

  def focusItem():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def font():
    pass

  def foregroundBrush():
    pass

  def hasFocus():
    pass

  def height():
    pass

  def helpEvent():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def invalidate():
    pass

  def isActive():
    pass

  def isSortCacheEnabled():
    pass

  def itemAt():
    pass

  def itemIndexMethod():
    pass

  def items():
    pass

  def itemsBoundingRect():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabberItem():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def palette():
    pass

  def registerUserData():
    pass

  def removeItem():
    pass

  def render():
    pass

  def sceneRect():
    pass

  def sceneRectChanged():
    """ Signal """
    pass

  def selectedItems():
    pass

  def selectionArea():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def sendEvent():
    pass

  def setActivePanel():
    pass

  def setActiveWindow():
    pass

  def setBackgroundBrush():
    pass

  def setBspTreeDepth():
    pass

  def setFocus():
    pass

  def setFocusItem():
    pass

  def setFont():
    pass

  def setForegroundBrush():
    pass

  def setItemIndexMethod():
    pass

  def setPalette():
    pass

  def setSceneRect():
    pass

  def setSelectionArea():
    pass

  def setSortCacheEnabled():
    pass

  def setStickyFocus():
    pass

  def setStyle():
    pass

  staticMetaObject = None

  def stickyFocus():
    pass

  def style():
    pass

  def update():
    pass

  def views():
    pass

  def wheelEvent():
    pass

  def width():
    pass

class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  Keyboard = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  Mouse = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Other = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None

  class Reason(object):

    Keyboard = None
    Mouse = None
    Other = None
    name = property(None, None, None,
                    )

    values = {}

  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def modifiers():
    pass

  def pos():
    pass

  def reason():
    pass

  def registerEventType():
    pass

  def scenePos():
    pass

  def screenPos():
    pass

  def setModifiers():
    pass

  def setPos():
    pass

  def setReason():
    pass

  def setScenePos():
    pass

  def setScreenPos():
    pass

class QGraphicsSceneDragDropEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def acceptProposedAction():
    pass

  def buttons():
    pass

  def dropAction():
    pass

  def mimeData():
    pass

  def modifiers():
    pass

  def pos():
    pass

  def possibleActions():
    pass

  def proposedAction():
    pass

  def registerEventType():
    pass

  def scenePos():
    pass

  def screenPos():
    pass

  def setButtons():
    pass

  def setDropAction():
    pass

  def setModifiers():
    pass

  def setPos():
    pass

  def setPossibleActions():
    pass

  def setProposedAction():
    pass

  def setScenePos():
    pass

  def setScreenPos():
    pass

  def source():
    pass

class QGraphicsSceneEvent(QEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def registerEventType():
    pass

  def widget():
    pass

class QGraphicsSceneHelpEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def registerEventType():
    pass

  def scenePos():
    pass

  def screenPos():
    pass

  def setScenePos():
    pass

  def setScreenPos():
    pass

class QGraphicsSceneHoverEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def lastPos():
    pass

  def lastScenePos():
    pass

  def lastScreenPos():
    pass

  def modifiers():
    pass

  def pos():
    pass

  def registerEventType():
    pass

  def scenePos():
    pass

  def screenPos():
    pass

  def setLastPos():
    pass

  def setLastScenePos():
    pass

  def setLastScreenPos():
    pass

  def setModifiers():
    pass

  def setPos():
    pass

  def setScenePos():
    pass

  def setScreenPos():
    pass

class QGraphicsSceneMouseEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def button():
    pass

  def buttonDownPos():
    pass

  def buttonDownScenePos():
    pass

  def buttonDownScreenPos():
    pass

  def buttons():
    pass

  def lastPos():
    pass

  def lastScenePos():
    pass

  def lastScreenPos():
    pass

  def modifiers():
    pass

  def pos():
    pass

  def registerEventType():
    pass

  def scenePos():
    pass

  def screenPos():
    pass

  def setButton():
    pass

  def setButtonDownPos():
    pass

  def setButtonDownScenePos():
    pass

  def setButtonDownScreenPos():
    pass

  def setButtons():
    pass

  def setLastPos():
    pass

  def setLastScenePos():
    pass

  def setLastScreenPos():
    pass

  def setModifiers():
    pass

  def setPos():
    pass

  def setScenePos():
    pass

  def setScreenPos():
    pass

class QGraphicsSceneMoveEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def newPos():
    pass

  def oldPos():
    pass

  def registerEventType():
    pass

  def setNewPos():
    pass

  def setOldPos():
    pass

class QGraphicsSceneResizeEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def newSize():
    pass

  def oldSize():
    pass

  def registerEventType():
    pass

  def setNewSize():
    pass

  def setOldSize():
    pass

class QGraphicsSceneWheelEvent(QGraphicsSceneEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  ApplicationActivate = None
  ApplicationActivated = None
  ApplicationDeactivate = None
  ApplicationDeactivated = None
  ApplicationFontChange = None
  ApplicationLayoutDirectionChange = None
  ApplicationPaletteChange = None
  ApplicationWindowIconChange = None
  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  CursorChange = None
  DeactivateControl = None
  DeferredDelete = None
  Destroy = None
  DragEnter = None
  DragLeave = None
  DragMove = None
  DragResponse = None
  Drop = None
  DynamicPropertyChange = None
  EmbeddingControl = None
  EnabledChange = None
  Enter = None
  EnterWhatsThisMode = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FutureCallOut = None
  Gesture = None
  GestureOverride = None
  GrabKeyboard = None
  GrabMouse = None
  GraphicsSceneContextMenu = None
  GraphicsSceneDragEnter = None
  GraphicsSceneDragLeave = None
  GraphicsSceneDragMove = None
  GraphicsSceneDrop = None
  GraphicsSceneHelp = None
  GraphicsSceneHoverEnter = None
  GraphicsSceneHoverLeave = None
  GraphicsSceneHoverMove = None
  GraphicsSceneMouseDoubleClick = None
  GraphicsSceneMouseMove = None
  GraphicsSceneMousePress = None
  GraphicsSceneMouseRelease = None
  GraphicsSceneMove = None
  GraphicsSceneResize = None
  GraphicsSceneWheel = None
  HelpRequest = None
  Hide = None
  HideToParent = None
  HoverEnter = None
  HoverLeave = None
  HoverMove = None
  IconDrag = None
  IconTextChange = None
  InputMethod = None
  KeyPress = None
  KeyRelease = None
  KeyboardLayoutChange = None
  LanguageChange = None
  LayoutDirectionChange = None
  LayoutRequest = None
  Leave = None
  LeaveWhatsThisMode = None
  LocaleChange = None
  MacGLClearDrawable = None
  MacGLWindowChange = None
  MacSizeChange = None
  MaxUser = None
  MenubarUpdated = None
  MetaCall = None
  ModifiedChange = None
  MouseButtonDblClick = None
  MouseButtonPress = None
  MouseButtonRelease = None
  MouseMove = None
  MouseTrackingChange = None
  Move = None
  NativeGesture = None
  NetworkReplyUpdated = None
  NonClientAreaMouseButtonDblClick = None
  NonClientAreaMouseButtonPress = None
  NonClientAreaMouseButtonRelease = None
  NonClientAreaMouseMove = None
  None = None
  OkRequest = None
  Paint = None
  PaletteChange = None
  ParentAboutToChange = None
  ParentChange = None
  PlatformPanel = None
  Polish = None
  PolishRequest = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  Shortcut = None
  ShortcutOverride = None
  Show = None
  ShowToParent = None
  ShowWindowRequest = None
  SockAct = None
  Speech = None
  StateMachineSignal = None
  StateMachineWrapped = None
  StatusTip = None
  Style = None
  StyleChange = None
  TabletEnterProximity = None
  TabletLeaveProximity = None
  TabletMove = None
  TabletPress = None
  TabletRelease = None
  ThreadChange = None
  Timer = None
  ToolBarChange = None
  ToolTip = None
  ToolTipChange = None
  TouchBegin = None
  TouchEnd = None
  TouchUpdate = None
  UngrabKeyboard = None
  UngrabMouse = None
  UpdateLater = None
  UpdateRequest = None
  UpdateSoftKeys = None
  User = None
  WhatsThis = None
  WhatsThisClicked = None
  Wheel = None
  WinEventAct = None
  WinIdChange = None
  WindowActivate = None
  WindowBlocked = None
  WindowDeactivate = None
  WindowIconChange = None
  WindowStateChange = None
  WindowTitleChange = None
  WindowUnblocked = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def buttons():
    pass

  def delta():
    pass

  def modifiers():
    pass

  def orientation():
    pass

  def pos():
    pass

  def registerEventType():
    pass

  def scenePos():
    pass

  def screenPos():
    pass

  def setButtons():
    pass

  def setDelta():
    pass

  def setModifiers():
    pass

  def setOrientation():
    pass

  def setPos():
    pass

  def setScenePos():
    pass

  def setScreenPos():
    pass

class QGraphicsSimpleTextItem(QAbstractGraphicsShapeItem):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def extension():
    pass

  def font():
    pass

  def isObscuredBy():
    pass

  def opaqueArea():
    pass

  def paint():
    pass

  def setFont():
    pass

  def setText():
    pass

  def shape():
    pass

  def text():
    pass

  def type():
    pass

class QGraphicsTextItem(QGraphicsObject):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def adjustSize():
    pass

  def boundingRect():
    pass

  def childrenChanged():
    """ Signal """
    pass

  def connect():
    pass

  def contains():
    pass

  def contextMenuEvent():
    pass

  def defaultTextColor():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def document():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def extension():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def font():
    pass

  def heightChanged():
    """ Signal """
    pass

  def hoverEnterEvent():
    pass

  def hoverLeaveEvent():
    pass

  def hoverMoveEvent():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def isObscuredBy():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def linkActivated():
    """ Signal """
    pass

  def linkHovered():
    """ Signal """
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def opacityChanged():
    """ Signal """
    pass

  def opaqueArea():
    pass

  def openExternalLinks():
    pass

  def paint():
    pass

  def parentChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def rotationChanged():
    """ Signal """
    pass

  def scaleChanged():
    """ Signal """
    pass

  def sceneEvent():
    pass

  def setDefaultTextColor():
    pass

  def setDocument():
    pass

  def setFont():
    pass

  def setHtml():
    pass

  def setOpenExternalLinks():
    pass

  def setPlainText():
    pass

  def setTabChangesFocus():
    pass

  def setTextCursor():
    pass

  def setTextInteractionFlags():
    pass

  def setTextWidth():
    pass

  def shape():
    pass

  staticMetaObject = None

  def tabChangesFocus():
    pass

  def textCursor():
    pass

  def textInteractionFlags():
    pass

  def textWidth():
    pass

  def toHtml():
    pass

  def toPlainText():
    pass

  def type():
    pass

  def visibleChanged():
    """ Signal """
    pass

  def widthChanged():
    """ Signal """
    pass

  def xChanged():
    """ Signal """
    pass

  def yChanged():
    """ Signal """
    pass

  def zChanged():
    """ Signal """
    pass

class QGraphicsTransform(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def applyTo():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

  def update():
    pass

class QGraphicsView(QAbstractScrollArea):

  AnchorUnderMouse = None
  AnchorViewCenter = None
  BoundingRectViewportUpdate = None
  Box = None
  CacheBackground = None

  class CacheMode(object):

    pass

  class CacheModeFlag(object):

    CacheBackground = None
    CacheNone = None
    name = property(None, None, None,
                    )

    values = {}

  CacheNone = None
  DontAdjustForAntialiasing = None
  DontClipPainter = None
  DontSavePainterState = None

  class DragMode(object):

    NoDrag = None
    RubberBandDrag = None
    ScrollHandDrag = None
    name = property(None, None, None,
                    )

    values = {}

  DrawChildren = None
  DrawWindowBackground = None
  FullViewportUpdate = None
  HLine = None
  IgnoreMask = None
  IndirectPainting = None
  MinimalViewportUpdate = None
  NoAnchor = None
  NoDrag = None
  NoFrame = None
  NoViewportUpdate = None

  class OptimizationFlag(object):

    DontAdjustForAntialiasing = None
    DontClipPainter = None
    DontSavePainterState = None
    IndirectPainting = None
    name = property(None, None, None,
                    )

    values = {}

  class OptimizationFlags(object):

    pass

  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  RubberBandDrag = None
  ScrollHandDrag = None
  Shadow_Mask = None
  Shape_Mask = None
  SmartViewportUpdate = None
  StyledPanel = None
  Sunken = None
  VLine = None

  class ViewportAnchor(object):

    AnchorUnderMouse = None
    AnchorViewCenter = None
    NoAnchor = None
    name = property(None, None, None,
                    )

    values = {}

  class ViewportUpdateMode(object):

    BoundingRectViewportUpdate = None
    FullViewportUpdate = None
    MinimalViewportUpdate = None
    NoViewportUpdate = None
    SmartViewportUpdate = None
    name = property(None, None, None,
                    )

    values = {}

  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def backgroundBrush():
    pass

  def cacheMode():
    pass

  def centerOn():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMode():
    pass

  def dragMoveEvent():
    pass

  def drawBackground():
    pass

  def drawForeground():
    pass

  def drawItems():
    pass

  def dropEvent():
    pass

  def ensureVisible():
    pass

  def event():
    pass

  def fitInView():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def foregroundBrush():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def invalidateScene():
    pass

  def isInteractive():
    pass

  def isTransformed():
    pass

  def itemAt():
    pass

  def items():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def keyboardGrabber():
    pass

  def mapFromScene():
    pass

  def mapToScene():
    pass

  def matrix():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def optimizationFlags():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def render():
    pass

  def renderHints():
    pass

  def resetCachedContent():
    pass

  def resetMatrix():
    pass

  def resetTransform():
    pass

  def resizeAnchor():
    pass

  def resizeEvent():
    pass

  def rotate():
    pass

  def rubberBandSelectionMode():
    pass

  def scale():
    pass

  def scene():
    pass

  def sceneRect():
    pass

  def scrollContentsBy():
    pass

  def setAlignment():
    pass

  def setBackgroundBrush():
    pass

  def setCacheMode():
    pass

  def setDragMode():
    pass

  def setForegroundBrush():
    pass

  def setInteractive():
    pass

  def setMatrix():
    pass

  def setOptimizationFlag():
    pass

  def setOptimizationFlags():
    pass

  def setRenderHint():
    pass

  def setRenderHints():
    pass

  def setResizeAnchor():
    pass

  def setRubberBandSelectionMode():
    pass

  def setScene():
    pass

  def setSceneRect():
    pass

  def setTabOrder():
    pass

  def setTransform():
    pass

  def setTransformationAnchor():
    pass

  def setViewportUpdateMode():
    pass

  def setupViewport():
    pass

  def shear():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def transform():
    pass

  def transformationAnchor():
    pass

  def translate():
    pass

  def updateScene():
    pass

  def updateSceneRect():
    pass

  def viewportEvent():
    pass

  def viewportTransform():
    pass

  def viewportUpdateMode():
    pass

  def wheelEvent():
    pass

class QGraphicsWidget(QGraphicsObject):

  DeviceCoordinateCache = None
  ItemAcceptsInputMethod = None
  ItemChildAddedChange = None
  ItemChildRemovedChange = None
  ItemClipsChildrenToShape = None
  ItemClipsToShape = None
  ItemCoordinateCache = None
  ItemCursorChange = None
  ItemCursorHasChanged = None
  ItemDoesntPropagateOpacityToChildren = None
  ItemEnabledChange = None
  ItemEnabledHasChanged = None
  ItemFlagsChange = None
  ItemFlagsHaveChanged = None
  ItemHasNoContents = None
  ItemIgnoresParentOpacity = None
  ItemIgnoresTransformations = None
  ItemIsFocusScope = None
  ItemIsFocusable = None
  ItemIsMovable = None
  ItemIsPanel = None
  ItemIsSelectable = None
  ItemMatrixChange = None
  ItemNegativeZStacksBehindParent = None
  ItemOpacityChange = None
  ItemOpacityHasChanged = None
  ItemParentChange = None
  ItemParentHasChanged = None
  ItemPositionChange = None
  ItemPositionHasChanged = None
  ItemRotationChange = None
  ItemRotationHasChanged = None
  ItemScaleChange = None
  ItemScaleHasChanged = None
  ItemSceneChange = None
  ItemSceneHasChanged = None
  ItemScenePositionHasChanged = None
  ItemSelectedChange = None
  ItemSelectedHasChanged = None
  ItemSendsGeometryChanges = None
  ItemSendsScenePositionChanges = None
  ItemStacksBehindParent = None
  ItemStopsClickFocusPropagation = None
  ItemStopsFocusHandling = None
  ItemToolTipChange = None
  ItemToolTipHasChanged = None
  ItemTransformChange = None
  ItemTransformHasChanged = None
  ItemTransformOriginPointChange = None
  ItemTransformOriginPointHasChanged = None
  ItemUsesExtendedStyleOption = None
  ItemVisibleChange = None
  ItemVisibleHasChanged = None
  ItemZValueChange = None
  ItemZValueHasChanged = None
  NoCache = None
  NonModal = None
  PanelModal = None
  SceneModal = None
  UserExtension = None
  UserType = 65536

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actions():
    pass

  def addAction():
    pass

  def addActions():
    pass

  def adjustSize():
    pass

  def autoFillBackground():
    pass

  def boundingRect():
    pass

  def changeEvent():
    pass

  def childrenChanged():
    """ Signal """
    pass

  def close():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def enabledChanged():
    """ Signal """
    pass

  def event():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def focusPolicy():
    pass

  def focusWidget():
    pass

  def font():
    pass

  def geometryChanged():
    """ Signal """
    pass

  def getContentsMargins():
    pass

  def getWindowFrameMargins():
    pass

  def grabKeyboardEvent():
    pass

  def grabMouseEvent():
    pass

  def grabShortcut():
    pass

  def heightChanged():
    """ Signal """
    pass

  def hideEvent():
    pass

  def hoverLeaveEvent():
    pass

  def hoverMoveEvent():
    pass

  def initStyleOption():
    pass

  def insertAction():
    pass

  def insertActions():
    pass

  def isActiveWindow():
    pass

  def itemChange():
    pass

  def layout():
    pass

  def layoutChanged():
    """ Signal """
    pass

  def layoutDirection():
    pass

  def moveEvent():
    pass

  def opacityChanged():
    """ Signal """
    pass

  def paint():
    pass

  def paintWindowFrame():
    pass

  def palette():
    pass

  def parentChanged():
    """ Signal """
    pass

  def polishEvent():
    pass

  def propertyChange():
    pass

  def rect():
    pass

  def registerUserData():
    pass

  def releaseShortcut():
    pass

  def removeAction():
    pass

  def resize():
    pass

  def resizeEvent():
    pass

  def rotationChanged():
    """ Signal """
    pass

  def scaleChanged():
    """ Signal """
    pass

  def sceneEvent():
    pass

  def setAttribute():
    pass

  def setAutoFillBackground():
    pass

  def setContentsMargins():
    pass

  def setFocusPolicy():
    pass

  def setFont():
    pass

  def setGeometry():
    pass

  def setLayout():
    pass

  def setLayoutDirection():
    pass

  def setPalette():
    pass

  def setShortcutAutoRepeat():
    pass

  def setShortcutEnabled():
    pass

  def setStyle():
    pass

  def setTabOrder():
    pass

  def setWindowFlags():
    pass

  def setWindowFrameMargins():
    pass

  def setWindowTitle():
    pass

  def shape():
    pass

  def showEvent():
    pass

  def size():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def style():
    pass

  def testAttribute():
    pass

  def type():
    pass

  def ungrabKeyboardEvent():
    pass

  def ungrabMouseEvent():
    pass

  def unsetLayoutDirection():
    pass

  def unsetWindowFrameMargins():
    pass

  def updateGeometry():
    pass

  def visibleChanged():
    """ Signal """
    pass

  def widthChanged():
    """ Signal """
    pass

  def windowFlags():
    pass

  def windowFrameEvent():
    pass

  def windowFrameGeometry():
    pass

  def windowFrameRect():
    pass

  def windowFrameSectionAt():
    pass

  def windowTitle():
    pass

  def windowType():
    pass

  def xChanged():
    """ Signal """
    pass

  def yChanged():
    """ Signal """
    pass

  def zChanged():
    """ Signal """
    pass

class QGridLayout(QLayout):

  SetDefaultConstraint = None
  SetFixedSize = None
  SetMaximumSize = None
  SetMinAndMaxSize = None
  SetMinimumSize = None
  SetNoConstraint = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addItem():
    pass

  def addLayout():
    pass

  def addWidget():
    pass

  def cellRect():
    pass

  def closestAcceptableSize():
    pass

  def columnCount():
    pass

  def columnMinimumWidth():
    pass

  def columnStretch():
    pass

  def connect():
    pass

  def count():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def expandingDirections():
    pass

  def getItemPosition():
    pass

  def hasHeightForWidth():
    pass

  def heightForWidth():
    pass

  def horizontalSpacing():
    pass

  def invalidate():
    pass

  def itemAt():
    pass

  def itemAtPosition():
    pass

  def maximumSize():
    pass

  def minimumHeightForWidth():
    pass

  def minimumSize():
    pass

  def originCorner():
    pass

  def registerUserData():
    pass

  def rowCount():
    pass

  def rowMinimumHeight():
    pass

  def rowStretch():
    pass

  def setColumnMinimumWidth():
    pass

  def setColumnStretch():
    pass

  def setDefaultPositioning():
    pass

  def setGeometry():
    pass

  def setHorizontalSpacing():
    pass

  def setOriginCorner():
    pass

  def setRowMinimumHeight():
    pass

  def setRowStretch():
    pass

  def setSpacing():
    pass

  def setVerticalSpacing():
    pass

  def sizeHint():
    pass

  def spacing():
    pass

  staticMetaObject = None

  def takeAt():
    pass

  def verticalSpacing():
    pass

class QGroupBox(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def changeEvent():
    pass

  def childEvent():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def focusInEvent():
    pass

  def initStyleOption():
    pass

  def isCheckable():
    pass

  def isChecked():
    pass

  def isFlat():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def setAlignment():
    pass

  def setCheckable():
    pass

  def setChecked():
    pass

  def setFlat():
    pass

  def setTabOrder():
    pass

  def setTitle():
    pass

  staticMetaObject = None

  def title():
    pass

  def toggled():
    """ Signal """
    pass

class QHBoxLayout(QBoxLayout):

  BottomToTop = None
  Down = None
  LeftToRight = None
  RightToLeft = None
  SetDefaultConstraint = None
  SetFixedSize = None
  SetMaximumSize = None
  SetMinAndMaxSize = None
  SetMinimumSize = None
  SetNoConstraint = None
  TopToBottom = None
  Up = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def closestAcceptableSize():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

class QHeaderView(QAbstractItemView):

  AboveItem = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  Custom = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  Fixed = None
  HLine = None
  IgnoreMask = None
  Interactive = None
  InternalMove = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  class ResizeMode(object):

    Custom = None
    Fixed = None
    Interactive = None
    ResizeToContents = None
    Stretch = None
    name = property(None, None, None,
                    )

    values = {}

  ResizeToContents = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SingleSelection = None
  Stretch = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def cascadingSectionResizes():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def count():
    pass

  def currentChanged():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def dataChanged():
    pass

  def defaultAlignment():
    pass

  def defaultSectionSize():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doItemsLayout():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def geometriesChanged():
    """ Signal """
    pass

  def headerDataChanged():
    pass

  def hiddenSectionCount():
    pass

  def hideSection():
    pass

  def highlightSections():
    pass

  def horizontalOffset():
    pass

  def indexAt():
    pass

  def initStyleOption():
    pass

  def initialize():
    pass

  def initializeSections():
    pass

  def isClickable():
    pass

  def isIndexHidden():
    pass

  def isMovable():
    pass

  def isSectionHidden():
    pass

  def isSortIndicatorShown():
    pass

  def keyboardGrabber():
    pass

  def length():
    pass

  def logicalIndex():
    pass

  def logicalIndexAt():
    pass

  def minimumSectionSize():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveCursor():
    pass

  def moveSection():
    pass

  def offset():
    pass

  def orientation():
    pass

  def paintEvent():
    pass

  def paintSection():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def resizeMode():
    pass

  def resizeSection():
    pass

  def resizeSections():
    pass

  def restoreState():
    pass

  def rowsInserted():
    pass

  def saveState():
    pass

  def scrollContentsBy():
    pass

  def scrollTo():
    pass

  def sectionAutoResize():
    """ Signal """
    pass

  def sectionClicked():
    """ Signal """
    pass

  def sectionCountChanged():
    """ Signal """
    pass

  def sectionDoubleClicked():
    """ Signal """
    pass

  def sectionEntered():
    """ Signal """
    pass

  def sectionHandleDoubleClicked():
    """ Signal """
    pass

  def sectionMoved():
    """ Signal """
    pass

  def sectionPosition():
    pass

  def sectionPressed():
    """ Signal """
    pass

  def sectionResized():
    """ Signal """
    pass

  def sectionSize():
    pass

  def sectionSizeFromContents():
    pass

  def sectionSizeHint():
    pass

  def sectionViewportPosition():
    pass

  def sectionsAboutToBeRemoved():
    pass

  def sectionsHidden():
    pass

  def sectionsInserted():
    pass

  def sectionsMoved():
    pass

  def setCascadingSectionResizes():
    pass

  def setClickable():
    pass

  def setDefaultAlignment():
    pass

  def setDefaultSectionSize():
    pass

  def setHighlightSections():
    pass

  def setMinimumSectionSize():
    pass

  def setModel():
    pass

  def setMovable():
    pass

  def setOffset():
    pass

  def setOffsetToLastSection():
    pass

  def setOffsetToSectionPosition():
    pass

  def setResizeMode():
    pass

  def setSectionHidden():
    pass

  def setSelection():
    pass

  def setSortIndicator():
    pass

  def setSortIndicatorShown():
    pass

  def setStretchLastSection():
    pass

  def setTabOrder():
    pass

  def showSection():
    pass

  def sizeHint():
    pass

  def sortIndicatorChanged():
    """ Signal """
    pass

  def sortIndicatorOrder():
    pass

  def sortIndicatorSection():
    pass

  staticMetaObject = None

  def stretchLastSection():
    pass

  def stretchSectionCount():
    pass

  def swapSections():
    pass

  def updateGeometries():
    pass

  def updateSection():
    pass

  def verticalOffset():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def viewportEvent():
    pass

  def visualIndex():
    pass

  def visualIndexAt():
    pass

  def visualRect():
    pass

  def visualRegionForSelection():
    pass

class QInputDialog(QDialog):

  Accepted = None
  DoubleInput = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None

  class InputDialogOption(object):

    NoButtons = None
    UseListViewForComboBoxItems = None
    name = property(None, None, None,
                    )

    values = {}

  class InputMode(object):

    DoubleInput = None
    IntInput = None
    TextInput = None
    name = property(None, None, None,
                    )

    values = {}

  IntInput = None
  NoButtons = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rejected = None
  TextInput = None
  UseListViewForComboBoxItems = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def cancelButtonText():
    pass

  def comboBoxItems():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def done():
    pass

  def doubleDecimals():
    pass

  def doubleMaximum():
    pass

  def doubleMinimum():
    pass

  def doubleValue():
    pass

  def doubleValueChanged():
    """ Signal """
    pass

  def doubleValueSelected():
    """ Signal """
    pass

  def finished():
    """ Signal """
    pass

  def getDouble():
    pass

  def getInt():
    pass

  def getInteger():
    pass

  def getItem():
    pass

  def getText():
    pass

  def inputMode():
    pass

  def intMaximum():
    pass

  def intMinimum():
    pass

  def intStep():
    pass

  def intValue():
    pass

  def intValueChanged():
    """ Signal """
    pass

  def intValueSelected():
    """ Signal """
    pass

  def isComboBoxEditable():
    pass

  def keyboardGrabber():
    pass

  def labelText():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def okButtonText():
    pass

  def open():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def setCancelButtonText():
    pass

  def setComboBoxEditable():
    pass

  def setComboBoxItems():
    pass

  def setDoubleDecimals():
    pass

  def setDoubleMaximum():
    pass

  def setDoubleMinimum():
    pass

  def setDoubleRange():
    pass

  def setDoubleValue():
    pass

  def setInputMode():
    pass

  def setIntMaximum():
    pass

  def setIntMinimum():
    pass

  def setIntRange():
    pass

  def setIntStep():
    pass

  def setIntValue():
    pass

  def setLabelText():
    pass

  def setOkButtonText():
    pass

  def setOption():
    pass

  def setTabOrder():
    pass

  def setTextEchoMode():
    pass

  def setTextValue():
    pass

  def setVisible():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def testOption():
    pass

  def textEchoMode():
    pass

  def textValue():
    pass

  def textValueChanged():
    """ Signal """
    pass

  def textValueSelected():
    """ Signal """
    pass

class QItemDelegate(QAbstractItemDelegate):

  EditNextItem = None
  EditPreviousItem = None
  NoHint = None
  RevertModelCache = None
  SubmitModelCache = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def check():
    pass

  def closeEditor():
    """ Signal """
    pass

  def commitData():
    """ Signal """
    pass

  def connect():
    pass

  def createEditor():
    pass

  def decoration():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def drawBackground():
    pass

  def drawCheck():
    pass

  def drawDecoration():
    pass

  def drawDisplay():
    pass

  def drawFocus():
    pass

  def editorEvent():
    pass

  def eventFilter():
    pass

  def hasClipping():
    pass

  def itemEditorFactory():
    pass

  def paint():
    pass

  def rect():
    pass

  def registerUserData():
    pass

  def setClipping():
    pass

  def setEditorData():
    pass

  def setItemEditorFactory():
    pass

  def setModelData():
    pass

  def setOptions():
    pass

  def sizeHint():
    pass

  def sizeHintChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def textRectangle():
    pass

  def updateEditorGeometry():
    pass

class QItemEditorCreatorBase(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def createWidget():
    pass

  def valuePropertyName():
    pass

class QItemEditorFactory(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def createEditor():
    pass

  def defaultFactory():
    pass

  def registerEditor():
    pass

  def setDefaultFactory():
    pass

  def valuePropertyName():
    pass

class QKeyEventTransition(QEventTransition):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def eventTest():
    pass

  def key():
    pass

  def modifierMask():
    pass

  def onTransition():
    pass

  def registerUserData():
    pass

  def setKey():
    pass

  def setModifierMask():
    pass

  staticMetaObject = None

  def triggered():
    """ Signal """
    pass

class QLCDNumber(QFrame):

  Bin = None
  Box = None
  Dec = None
  DrawChildren = None
  DrawWindowBackground = None
  Filled = None
  Flat = None
  HLine = None
  Hex = None
  IgnoreMask = None

  class Mode(object):

    Bin = None
    Dec = None
    Hex = None
    Oct = None
    name = property(None, None, None,
                    )

    values = {}

  NoFrame = None
  Oct = None
  Outline = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  class SegmentStyle(object):

    Filled = None
    Flat = None
    Outline = None
    name = property(None, None, None,
                    )

    values = {}

  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def checkOverflow():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def digitCount():
    pass

  def disconnect():
    pass

  def display():
    pass

  def event():
    pass

  def intValue():
    pass

  def keyboardGrabber():
    pass

  def mode():
    pass

  def mouseGrabber():
    pass

  def numDigits():
    pass

  def overflow():
    """ Signal """
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def segmentStyle():
    pass

  def setBinMode():
    pass

  def setDecMode():
    pass

  def setDigitCount():
    pass

  def setHexMode():
    pass

  def setMode():
    pass

  def setNumDigits():
    pass

  def setOctMode():
    pass

  def setSegmentStyle():
    pass

  def setSmallDecimalPoint():
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  def smallDecimalPoint():
    pass

  staticMetaObject = None

  def value():
    pass

class QLabel(QFrame):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def buddy():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def hasScaledContents():
    pass

  def hasSelectedText():
    pass

  def heightForWidth():
    pass

  def indent():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def linkActivated():
    """ Signal """
    pass

  def linkHovered():
    """ Signal """
    pass

  def margin():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def movie():
    pass

  def openExternalLinks():
    pass

  def paintEvent():
    pass

  def picture():
    pass

  def pixmap():
    pass

  def registerUserData():
    pass

  def selectedText():
    pass

  def selectionStart():
    pass

  def setAlignment():
    pass

  def setBuddy():
    pass

  def setIndent():
    pass

  def setMargin():
    pass

  def setMovie():
    pass

  def setNum():
    pass

  def setOpenExternalLinks():
    pass

  def setPicture():
    pass

  def setPixmap():
    pass

  def setScaledContents():
    pass

  def setSelection():
    pass

  def setTabOrder():
    pass

  def setText():
    pass

  def setTextFormat():
    pass

  def setTextInteractionFlags():
    pass

  def setWordWrap():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def text():
    pass

  def textFormat():
    pass

  def textInteractionFlags():
    pass

  def wordWrap():
    pass

class QLayout(QObject):

  SetDefaultConstraint = None
  SetFixedSize = None
  SetMaximumSize = None
  SetMinAndMaxSize = None
  SetMinimumSize = None
  SetNoConstraint = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activate():
    pass

  def addChildLayout():
    pass

  def addChildWidget():
    pass

  def addItem():
    pass

  def addWidget():
    pass

  def adoptLayout():
    pass

  def alignmentRect():
    pass

  def childEvent():
    pass

  def closestAcceptableSize():
    pass

  def connect():
    pass

  def contentsMargins():
    pass

  def contentsRect():
    pass

  def count():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def expandingDirections():
    pass

  def geometry():
    pass

  def getContentsMargins():
    pass

  def indexOf():
    pass

  def invalidate():
    pass

  def isEmpty():
    pass

  def isEnabled():
    pass

  def itemAt():
    pass

  def layout():
    pass

  def maximumSize():
    pass

  def menuBar():
    pass

  def minimumSize():
    pass

  def parentWidget():
    pass

  def registerUserData():
    pass

  def removeItem():
    pass

  def removeWidget():
    pass

  def setAlignment():
    pass

  def setContentsMargins():
    pass

  def setEnabled():
    pass

  def setGeometry():
    pass

  def setMenuBar():
    pass

  def setSizeConstraint():
    pass

  def setSpacing():
    pass

  def sizeConstraint():
    pass

  def spacing():
    pass

  staticMetaObject = None

  def takeAt():
    pass

  def totalHeightForWidth():
    pass

  def totalMaximumSize():
    pass

  def totalMinimumSize():
    pass

  def totalSizeHint():
    pass

  def update():
    pass

  def widgetEvent():
    pass

class QLayoutItem(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  align = property(None, None, None,
                   )


  def alignment():
    pass

  def controlTypes():
    pass

  def expandingDirections():
    pass

  def geometry():
    pass

  def hasHeightForWidth():
    pass

  def heightForWidth():
    pass

  def invalidate():
    pass

  def isEmpty():
    pass

  def layout():
    pass

  def maximumSize():
    pass

  def minimumHeightForWidth():
    pass

  def minimumSize():
    pass

  def setAlignment():
    pass

  def setGeometry():
    pass

  def sizeHint():
    pass

  def spacerItem():
    pass

  def widget():
    pass

class QLineEdit(QWidget):

  DrawChildren = None
  DrawWindowBackground = None

  class EchoMode(object):

    NoEcho = None
    Normal = None
    Password = None
    PasswordEchoOnEdit = None
    name = property(None, None, None,
                    )

    values = {}

  IgnoreMask = None
  NoEcho = None
  Normal = None
  Password = None
  PasswordEchoOnEdit = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def backspace():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def completer():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def copy():
    pass

  def createStandardContextMenu():
    pass

  def cursorBackward():
    pass

  def cursorForward():
    pass

  def cursorMoveStyle():
    pass

  def cursorPosition():
    pass

  def cursorPositionAt():
    pass

  def cursorPositionChanged():
    """ Signal """
    pass

  def cursorRect():
    pass

  def cursorWordBackward():
    pass

  def cursorWordForward():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def cut():
    pass

  def del_():
    pass

  def deselect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def displayText():
    pass

  def dragEnabled():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def echoMode():
    pass

  def editingFinished():
    """ Signal """
    pass

  def end():
    pass

  def event():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def getTextMargins():
    pass

  def hasAcceptableInput():
    pass

  def hasFrame():
    pass

  def hasSelectedText():
    pass

  def home():
    pass

  def initStyleOption():
    pass

  def inputMask():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def insert():
    pass

  def isModified():
    pass

  def isReadOnly():
    pass

  def isRedoAvailable():
    pass

  def isUndoAvailable():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def lostFocus():
    """ Signal """
    pass

  def maxLength():
    pass

  def minimumSizeHint():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def paste():
    pass

  def placeholderText():
    pass

  def redo():
    pass

  def registerUserData():
    pass

  def returnPressed():
    """ Signal """
    pass

  def selectAll():
    pass

  def selectedText():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def selectionStart():
    pass

  def setAlignment():
    pass

  def setCompleter():
    pass

  def setCursorMoveStyle():
    pass

  def setCursorPosition():
    pass

  def setDragEnabled():
    pass

  def setEchoMode():
    pass

  def setFrame():
    pass

  def setInputMask():
    pass

  def setMaxLength():
    pass

  def setModified():
    pass

  def setPlaceholderText():
    pass

  def setReadOnly():
    pass

  def setSelection():
    pass

  def setTabOrder():
    pass

  def setText():
    pass

  def setTextMargins():
    pass

  def setValidator():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def text():
    pass

  def textChanged():
    """ Signal """
    pass

  def textEdited():
    """ Signal """
    pass

  def textMargins():
    pass

  def undo():
    pass

  def validator():
    pass

class QListView(QAbstractItemView):

  AboveItem = None
  Adjust = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  Batched = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  Fixed = None

  class Flow(object):

    LeftToRight = None
    TopToBottom = None
    name = property(None, None, None,
                    )

    values = {}

  Free = None
  HLine = None
  IconMode = None
  IgnoreMask = None
  InternalMove = None

  class LayoutMode(object):

    Batched = None
    SinglePass = None
    name = property(None, None, None,
                    )

    values = {}

  LeftToRight = None
  ListMode = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None

  class Movement(object):

    Free = None
    Snap = None
    Static = None
    name = property(None, None, None,
                    )

    values = {}

  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  class ResizeMode(object):

    Adjust = None
    Fixed = None
    name = property(None, None, None,
                    )

    values = {}

  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SinglePass = None
  SingleSelection = None
  Snap = None
  Static = None
  StyledPanel = None
  Sunken = None
  TopToBottom = None
  VLine = None

  class ViewMode(object):

    IconMode = None
    ListMode = None
    name = property(None, None, None,
                    )

    values = {}

  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def batchSize():
    pass

  def clearPropertyFlags():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def contentsSize():
    pass

  def currentChanged():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def dataChanged():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doItemsLayout():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def flow():
    pass

  def gridSize():
    pass

  def horizontalOffset():
    pass

  def indexAt():
    pass

  def indexesMoved():
    """ Signal """
    pass

  def internalDrag():
    pass

  def internalDrop():
    pass

  def isIndexHidden():
    pass

  def isRowHidden():
    pass

  def isSelectionRectVisible():
    pass

  def isWrapping():
    pass

  def keyboardGrabber():
    pass

  def layoutMode():
    pass

  def modelColumn():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveCursor():
    pass

  def movement():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def rectForIndex():
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def resizeContents():
    pass

  def resizeEvent():
    pass

  def resizeMode():
    pass

  def rowsAboutToBeRemoved():
    pass

  def rowsInserted():
    pass

  def scrollContentsBy():
    pass

  def scrollTo():
    pass

  def selectedIndexes():
    pass

  def selectionChanged():
    pass

  def setBatchSize():
    pass

  def setFlow():
    pass

  def setGridSize():
    pass

  def setLayoutMode():
    pass

  def setModelColumn():
    pass

  def setMovement():
    pass

  def setPositionForIndex():
    pass

  def setResizeMode():
    pass

  def setRootIndex():
    pass

  def setRowHidden():
    pass

  def setSelection():
    pass

  def setSelectionRectVisible():
    pass

  def setSpacing():
    pass

  def setTabOrder():
    pass

  def setUniformItemSizes():
    pass

  def setViewMode():
    pass

  def setWordWrap():
    pass

  def setWrapping():
    pass

  def spacing():
    pass

  def startDrag():
    pass

  staticMetaObject = None

  def timerEvent():
    pass

  def uniformItemSizes():
    pass

  def updateGeometries():
    pass

  def verticalOffset():
    pass

  def viewMode():
    pass

  def viewOptions():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def visualRect():
    pass

  def visualRegionForSelection():
    pass

  def wordWrap():
    pass

class QListWidget(QListView):

  AboveItem = None
  Adjust = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  Batched = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  Fixed = None
  Free = None
  HLine = None
  IconMode = None
  IgnoreMask = None
  InternalMove = None
  LeftToRight = None
  ListMode = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SinglePass = None
  SingleSelection = None
  Snap = None
  Static = None
  StyledPanel = None
  Sunken = None
  TopToBottom = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def addItem():
    pass

  def addItems():
    pass

  def clear():
    pass

  def clicked():
    """ Signal """
    pass

  def closePersistentEditor():
    pass

  def connect():
    pass

  def count():
    pass

  def currentItem():
    pass

  def currentItemChanged():
    """ Signal """
    pass

  def currentRow():
    pass

  def currentRowChanged():
    """ Signal """
    pass

  def currentTextChanged():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def dropEvent():
    pass

  def dropMimeData():
    pass

  def editItem():
    pass

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def findItems():
    pass

  def indexFromItem():
    pass

  def indexesMoved():
    """ Signal """
    pass

  def insertItem():
    pass

  def insertItems():
    pass

  def isSortingEnabled():
    pass

  def item():
    pass

  def itemActivated():
    """ Signal """
    pass

  def itemAt():
    pass

  def itemChanged():
    """ Signal """
    pass

  def itemClicked():
    """ Signal """
    pass

  def itemDoubleClicked():
    """ Signal """
    pass

  def itemEntered():
    """ Signal """
    pass

  def itemFromIndex():
    pass

  def itemPressed():
    """ Signal """
    pass

  def itemSelectionChanged():
    """ Signal """
    pass

  def itemWidget():
    pass

  def items():
    pass

  def keyboardGrabber():
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def mouseGrabber():
    pass

  def openPersistentEditor():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeItemWidget():
    pass

  def row():
    pass

  def scrollToItem():
    pass

  def selectedItems():
    pass

  def setCurrentItem():
    pass

  def setCurrentRow():
    pass

  def setItemWidget():
    pass

  def setModel():
    pass

  def setSortingEnabled():
    pass

  def setTabOrder():
    pass

  def sortItems():
    pass

  staticMetaObject = None

  def supportedDropActions():
    pass

  def takeItem():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def visualItemRect():
    pass

class QListWidgetItem(Object):

  class ItemType(object):

    Type = None
    UserType = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  UserType = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def background():
    pass

  def checkState():
    pass

  def clone():
    pass

  def data():
    pass

  def flags():
    pass

  def font():
    pass

  def foreground():
    pass

  def icon():
    pass

  def isHidden():
    pass

  def isSelected():
    pass

  def listWidget():
    pass

  def read():
    pass

  def setBackground():
    pass

  def setCheckState():
    pass

  def setData():
    pass

  def setFlags():
    pass

  def setFont():
    pass

  def setForeground():
    pass

  def setHidden():
    pass

  def setIcon():
    pass

  def setSelected():
    pass

  def setSizeHint():
    pass

  def setStatusTip():
    pass

  def setText():
    pass

  def setTextAlignment():
    pass

  def setToolTip():
    pass

  def setWhatsThis():
    pass

  def sizeHint():
    pass

  def statusTip():
    pass

  def text():
    pass

  def textAlignment():
    pass

  def toolTip():
    pass

  def type():
    pass

  def whatsThis():
    pass

  def write():
    pass

class QMainWindow(QWidget):

  AllowNestedDocks = None
  AllowTabbedDocks = None
  AnimatedDocks = None

  class DockOption(object):

    AllowNestedDocks = None
    AllowTabbedDocks = None
    AnimatedDocks = None
    ForceTabbedDocks = None
    VerticalTabs = None
    name = property(None, None, None,
                    )

    values = {}

  class DockOptions(object):

    pass

  DrawChildren = None
  DrawWindowBackground = None
  ForceTabbedDocks = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  VerticalTabs = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addDockWidget():
    pass

  def addToolBar():
    pass

  def addToolBarBreak():
    pass

  def centralWidget():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def corner():
    pass

  def createPopupMenu():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dockOptions():
    pass

  def dockWidgetArea():
    pass

  def documentMode():
    pass

  def event():
    pass

  def iconSize():
    pass

  def iconSizeChanged():
    """ Signal """
    pass

  def insertToolBar():
    pass

  def insertToolBarBreak():
    pass

  def isAnimated():
    pass

  def isDockNestingEnabled():
    pass

  def isSeparator():
    pass

  def keyboardGrabber():
    pass

  def menuBar():
    pass

  def menuWidget():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def removeDockWidget():
    pass

  def removeToolBar():
    pass

  def removeToolBarBreak():
    pass

  def restoreDockWidget():
    pass

  def restoreState():
    pass

  def saveState():
    pass

  def setAnimated():
    pass

  def setCentralWidget():
    pass

  def setCorner():
    pass

  def setDockNestingEnabled():
    pass

  def setDockOptions():
    pass

  def setDocumentMode():
    pass

  def setIconSize():
    pass

  def setMenuBar():
    pass

  def setMenuWidget():
    pass

  def setStatusBar():
    pass

  def setTabOrder():
    pass

  def setTabPosition():
    pass

  def setTabShape():
    pass

  def setToolButtonStyle():
    pass

  def setUnifiedTitleAndToolBarOnMac():
    pass

  def splitDockWidget():
    pass

  staticMetaObject = None

  def statusBar():
    pass

  def tabPosition():
    pass

  def tabShape():
    pass

  def tabifiedDockWidgets():
    pass

  def tabifyDockWidget():
    pass

  def toolBarArea():
    pass

  def toolBarBreak():
    pass

  def toolButtonStyle():
    pass

  def toolButtonStyleChanged():
    """ Signal """
    pass

  def unifiedTitleAndToolBarOnMac():
    pass

class QMdiArea(QAbstractScrollArea):

  ActivationHistoryOrder = None

  class AreaOption(object):

    DontMaximizeSubWindowOnActivation = None
    name = property(None, None, None,
                    )

    values = {}

  class AreaOptions(object):

    pass

  Box = None
  CreationOrder = None
  DontMaximizeSubWindowOnActivation = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StackingOrder = None
  StyledPanel = None
  SubWindowView = None
  Sunken = None
  TabbedView = None
  VLine = None

  class ViewMode(object):

    SubWindowView = None
    TabbedView = None
    name = property(None, None, None,
                    )

    values = {}

  WinPanel = None

  class WindowOrder(object):

    ActivationHistoryOrder = None
    CreationOrder = None
    StackingOrder = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activateNextSubWindow():
    pass

  def activatePreviousSubWindow():
    pass

  def activationOrder():
    pass

  def activeSubWindow():
    pass

  def addSubWindow():
    pass

  def background():
    pass

  def cascadeSubWindows():
    pass

  def childEvent():
    pass

  def closeActiveSubWindow():
    pass

  def closeAllSubWindows():
    pass

  def connect():
    pass

  def currentSubWindow():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def documentMode():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def removeSubWindow():
    pass

  def resizeEvent():
    pass

  def scrollContentsBy():
    pass

  def setActivationOrder():
    pass

  def setActiveSubWindow():
    pass

  def setBackground():
    pass

  def setDocumentMode():
    pass

  def setOption():
    pass

  def setTabOrder():
    pass

  def setTabPosition():
    pass

  def setTabShape():
    pass

  def setTabsClosable():
    pass

  def setTabsMovable():
    pass

  def setViewMode():
    pass

  def setupViewport():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def subWindowActivated():
    """ Signal """
    pass

  def subWindowList():
    pass

  def tabPosition():
    pass

  def tabShape():
    pass

  def tabsClosable():
    pass

  def tabsMovable():
    pass

  def testOption():
    pass

  def tileSubWindows():
    pass

  def timerEvent():
    pass

  def viewMode():
    pass

  def viewportEvent():
    pass

class QMdiSubWindow(QWidget):

  AllowOutsideAreaHorizontally = None
  AllowOutsideAreaVertically = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  RubberBandMove = None
  RubberBandResize = None

  class SubWindowOption(object):

    AllowOutsideAreaHorizontally = None
    AllowOutsideAreaVertically = None
    RubberBandMove = None
    RubberBandResize = None
    name = property(None, None, None,
                    )

    values = {}

  class SubWindowOptions(object):

    pass

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToActivate():
    """ Signal """
    pass

  def changeEvent():
    pass

  def childEvent():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def hideEvent():
    pass

  def isShaded():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def keyboardPageStep():
    pass

  def keyboardSingleStep():
    pass

  def leaveEvent():
    pass

  def maximizedButtonsWidget():
    pass

  def maximizedSystemMenuIconWidget():
    pass

  def mdiArea():
    pass

  def minimumSizeHint():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def setKeyboardPageStep():
    pass

  def setKeyboardSingleStep():
    pass

  def setOption():
    pass

  def setSystemMenu():
    pass

  def setTabOrder():
    pass

  def setWidget():
    pass

  def showEvent():
    pass

  def showShaded():
    pass

  def showSystemMenu():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def systemMenu():
    pass

  def testOption():
    pass

  def timerEvent():
    pass

  def widget():
    pass

  def windowStateChanged():
    """ Signal """
    pass

class QMenu(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToHide():
    """ Signal """
    pass

  def aboutToShow():
    """ Signal """
    pass

  def actionAt():
    pass

  def actionEvent():
    pass

  def actionGeometry():
    pass

  def activated():
    """ Signal """
    pass

  def activeAction():
    pass

  def addAction():
    pass

  def addMenu():
    pass

  def addSeparator():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def columnCount():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def defaultAction():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def enterEvent():
    pass

  def event():
    pass

  def exec_():
    pass

  def focusNextPrevChild():
    pass

  def hideEvent():
    pass

  def hideTearOffMenu():
    pass

  def highlighted():
    """ Signal """
    pass

  def hovered():
    """ Signal """
    pass

  def icon():
    pass

  def initStyleOption():
    pass

  def insertMenu():
    pass

  def insertSeparator():
    pass

  def isEmpty():
    pass

  def isTearOffEnabled():
    pass

  def isTearOffMenuVisible():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def leaveEvent():
    pass

  def menuAction():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def popup():
    pass

  def registerUserData():
    pass

  def separatorsCollapsible():
    pass

  def setActiveAction():
    pass

  def setDefaultAction():
    pass

  def setIcon():
    pass

  def setSeparatorsCollapsible():
    pass

  def setTabOrder():
    pass

  def setTearOffEnabled():
    pass

  def setTitle():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def timerEvent():
    pass

  def title():
    pass

  def triggered():
    """ Signal """
    pass

  def wheelEvent():
    pass

class QMenuBar(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionAt():
    pass

  def actionEvent():
    pass

  def actionGeometry():
    pass

  def activated():
    """ Signal """
    pass

  def activeAction():
    pass

  def addAction():
    pass

  def addMenu():
    pass

  def addSeparator():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def connect():
    pass

  def cornerWidget():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def heightForWidth():
    pass

  def highlighted():
    """ Signal """
    pass

  def hovered():
    """ Signal """
    pass

  def initStyleOption():
    pass

  def insertMenu():
    pass

  def insertSeparator():
    pass

  def isDefaultUp():
    pass

  def isNativeMenuBar():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def leaveEvent():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def setActiveAction():
    pass

  def setCornerWidget():
    pass

  def setDefaultUp():
    pass

  def setNativeMenuBar():
    pass

  def setTabOrder():
    pass

  def setVisible():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def timerEvent():
    pass

  def triggered():
    """ Signal """
    pass

class QMessageBox(QDialog):

  Abort = None
  AcceptRole = None
  Accepted = None
  ActionRole = None
  Apply = None
  ApplyRole = None
  ButtonMask = None

  class ButtonRole(object):

    AcceptRole = None
    ActionRole = None
    ApplyRole = None
    DestructiveRole = None
    HelpRole = None
    InvalidRole = None
    NRoles = None
    NoRole = None
    RejectRole = None
    ResetRole = None
    YesRole = None
    name = property(None, None, None,
                    )

    values = {}

  Cancel = None
  Close = None
  Critical = None
  Default = None
  DestructiveRole = None
  Discard = None
  DrawChildren = None
  DrawWindowBackground = None
  Escape = None
  FirstButton = None
  FlagMask = None
  Help = None
  HelpRole = None

  class Icon(object):

    Critical = None
    Information = None
    NoIcon = None
    Question = None
    Warning = None
    name = property(None, None, None,
                    )

    values = {}

  Ignore = None
  IgnoreMask = None
  Information = None
  InvalidRole = None
  LastButton = None
  NRoles = None
  No = None
  NoAll = None
  NoButton = None
  NoIcon = None
  NoRole = None
  NoToAll = None
  Ok = None
  Open = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Question = None
  RejectRole = None
  Rejected = None
  Reset = None
  ResetRole = None
  RestoreDefaults = None
  Retry = None
  Save = None
  SaveAll = None

  class StandardButton(object):

    Abort = None
    Apply = None
    ButtonMask = None
    Cancel = None
    Close = None
    Default = None
    Discard = None
    Escape = None
    FirstButton = None
    FlagMask = None
    Help = None
    Ignore = None
    LastButton = None
    No = None
    NoAll = None
    NoButton = None
    NoToAll = None
    Ok = None
    Open = None
    Reset = None
    RestoreDefaults = None
    Retry = None
    Save = None
    SaveAll = None
    Yes = None
    YesAll = None
    YesToAll = None
    name = property(None, None, None,
                    )

    values = {}

  class StandardButtons(object):

    pass

  Warning = None
  Yes = None
  YesAll = None
  YesRole = None
  YesToAll = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def about():
    pass

  def aboutQt():
    pass

  def accepted():
    """ Signal """
    pass

  def addButton():
    pass

  def button():
    pass

  def buttonClicked():
    """ Signal """
    pass

  def buttonRole():
    pass

  def buttons():
    pass

  def changeEvent():
    pass

  def clickedButton():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def critical():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def defaultButton():
    pass

  def destroyed():
    """ Signal """
    pass

  def detailedText():
    pass

  def disconnect():
    pass

  def escapeButton():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def icon():
    pass

  def iconPixmap():
    pass

  def information():
    pass

  def informativeText():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def open():
    pass

  def question():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def removeButton():
    pass

  def resizeEvent():
    pass

  def setDefaultButton():
    pass

  def setDetailedText():
    pass

  def setEscapeButton():
    pass

  def setIcon():
    pass

  def setIconPixmap():
    pass

  def setInformativeText():
    pass

  def setStandardButtons():
    pass

  def setTabOrder():
    pass

  def setText():
    pass

  def setTextFormat():
    pass

  def setWindowModality():
    pass

  def setWindowTitle():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  def standardButton():
    pass

  def standardButtons():
    pass

  staticMetaObject = None

  def text():
    pass

  def textFormat():
    pass

  def warning():
    pass

class QMouseEventTransition(QEventTransition):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def button():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def eventTest():
    pass

  def hitTestPath():
    pass

  def modifierMask():
    pass

  def onTransition():
    pass

  def registerUserData():
    pass

  def setButton():
    pass

  def setHitTestPath():
    pass

  def setModifierMask():
    pass

  staticMetaObject = None

  def triggered():
    """ Signal """
    pass

class QPanGesture(QGesture):

  CancelAllInContext = None
  CancelNone = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def acceleration():
    pass

  def connect():
    pass

  def delta():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def lastOffset():
    pass

  def offset():
    pass

  def registerUserData():
    pass

  def setAcceleration():
    pass

  def setLastOffset():
    pass

  def setOffset():
    pass

  staticMetaObject = None

class QPinchGesture(QGesture):

  CancelAllInContext = None
  CancelNone = None
  CenterPointChanged = None

  class ChangeFlag(object):

    CenterPointChanged = None
    RotationAngleChanged = None
    ScaleFactorChanged = None
    name = property(None, None, None,
                    )

    values = {}

  class ChangeFlags(object):

    pass

  RotationAngleChanged = None
  ScaleFactorChanged = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def centerPoint():
    pass

  def changeFlags():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def lastCenterPoint():
    pass

  def lastRotationAngle():
    pass

  def lastScaleFactor():
    pass

  def registerUserData():
    pass

  def rotationAngle():
    pass

  def scaleFactor():
    pass

  def setCenterPoint():
    pass

  def setChangeFlags():
    pass

  def setLastCenterPoint():
    pass

  def setLastRotationAngle():
    pass

  def setLastScaleFactor():
    pass

  def setRotationAngle():
    pass

  def setScaleFactor():
    pass

  def setStartCenterPoint():
    pass

  def setTotalChangeFlags():
    pass

  def setTotalRotationAngle():
    pass

  def setTotalScaleFactor():
    pass

  def startCenterPoint():
    pass

  staticMetaObject = None

  def totalChangeFlags():
    pass

  def totalRotationAngle():
    pass

  def totalScaleFactor():
    pass

class QPlainTextDocumentLayout(QAbstractTextDocumentLayout):

  class PaintContext(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    clip = property(None, None, None,
                    )

    cursorPosition = property(None, None, None,
                              )

    palette = property(None, None, None,
                       )


  class Selection(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    cursor = property(None, None, None,
                      )

    format = property(None, None, None,
                      )


  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def blockBoundingRect():
    pass

  def connect():
    pass

  def cursorWidth():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def documentChanged():
    pass

  def documentSize():
    pass

  def documentSizeChanged():
    """ Signal """
    pass

  def draw():
    pass

  def ensureBlockLayout():
    pass

  def frameBoundingRect():
    pass

  def hitTest():
    pass

  def pageCount():
    pass

  def pageCountChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def requestUpdate():
    pass

  def setCursorWidth():
    pass

  staticMetaObject = None

  def update():
    """ Signal """
    pass

  def updateBlock():
    """ Signal """
    pass

class QPlainTextEdit(QAbstractScrollArea):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None

  class LineWrapMode(object):

    NoWrap = None
    WidgetWidth = None
    name = property(None, None, None,
                    )

    values = {}

  NoFrame = None
  NoWrap = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WidgetWidth = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def anchorAt():
    pass

  def appendHtml():
    pass

  def appendPlainText():
    pass

  def backgroundVisible():
    pass

  def blockBoundingGeometry():
    pass

  def blockBoundingRect():
    pass

  def blockCount():
    pass

  def blockCountChanged():
    """ Signal """
    pass

  def canInsertFromMimeData():
    pass

  def canPaste():
    pass

  def centerCursor():
    pass

  def centerOnScroll():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def connect():
    pass

  def contentOffset():
    pass

  def contextMenuEvent():
    pass

  def copy():
    pass

  def copyAvailable():
    """ Signal """
    pass

  def createMimeDataFromSelection():
    pass

  def createStandardContextMenu():
    pass

  def currentCharFormat():
    pass

  def cursorForPosition():
    pass

  def cursorPositionChanged():
    """ Signal """
    pass

  def cursorRect():
    pass

  def cursorWidth():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def cut():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def document():
    pass

  def documentTitle():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def ensureCursorVisible():
    pass

  def event():
    pass

  def extraSelections():
    pass

  def find():
    pass

  def firstVisibleBlock():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def getPaintContext():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def insertFromMimeData():
    pass

  def insertPlainText():
    pass

  def isReadOnly():
    pass

  def isUndoRedoEnabled():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def keyboardGrabber():
    pass

  def lineWrapMode():
    pass

  def loadResource():
    pass

  def maximumBlockCount():
    pass

  def mergeCurrentCharFormat():
    pass

  def modificationChanged():
    """ Signal """
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveCursor():
    pass

  def overwriteMode():
    pass

  def paintEvent():
    pass

  def paste():
    pass

  def print_():
    pass

  def redo():
    pass

  def redoAvailable():
    """ Signal """
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def scrollContentsBy():
    pass

  def selectAll():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def setBackgroundVisible():
    pass

  def setCenterOnScroll():
    pass

  def setCurrentCharFormat():
    pass

  def setCursorWidth():
    pass

  def setDocument():
    pass

  def setDocumentTitle():
    pass

  def setExtraSelections():
    pass

  def setLineWrapMode():
    pass

  def setMaximumBlockCount():
    pass

  def setOverwriteMode():
    pass

  def setPlainText():
    pass

  def setReadOnly():
    pass

  def setTabChangesFocus():
    pass

  def setTabOrder():
    pass

  def setTabStopWidth():
    pass

  def setTextCursor():
    pass

  def setTextInteractionFlags():
    pass

  def setUndoRedoEnabled():
    pass

  def setWordWrapMode():
    pass

  def showEvent():
    pass

  staticMetaObject = None

  def tabChangesFocus():
    pass

  def tabStopWidth():
    pass

  def textChanged():
    """ Signal """
    pass

  def textCursor():
    pass

  def textInteractionFlags():
    pass

  def timerEvent():
    pass

  def toPlainText():
    pass

  def undo():
    pass

  def undoAvailable():
    """ Signal """
    pass

  def updateRequest():
    """ Signal """
    pass

  def wheelEvent():
    pass

  def wordWrapMode():
    pass

class QProgressBar(QWidget):

  BottomToTop = None

  class Direction(object):

    BottomToTop = None
    TopToBottom = None
    name = property(None, None, None,
                    )

    values = {}

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  TopToBottom = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def format():
    pass

  def initStyleOption():
    pass

  def invertedAppearance():
    pass

  def isTextVisible():
    pass

  def keyboardGrabber():
    pass

  def maximum():
    pass

  def minimum():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def orientation():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def setAlignment():
    pass

  def setFormat():
    pass

  def setInvertedAppearance():
    pass

  def setMaximum():
    pass

  def setMinimum():
    pass

  def setOrientation():
    pass

  def setRange():
    pass

  def setTabOrder():
    pass

  def setTextDirection():
    pass

  def setTextVisible():
    pass

  def setValue():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def text():
    pass

  def textDirection():
    pass

  def value():
    pass

  def valueChanged():
    """ Signal """
    pass

class QProgressDialog(QDialog):

  Accepted = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rejected = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def autoClose():
    pass

  def autoReset():
    pass

  def cancel():
    pass

  def canceled():
    """ Signal """
    pass

  def changeEvent():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def finished():
    """ Signal """
    pass

  def forceShow():
    pass

  def keyboardGrabber():
    pass

  def labelText():
    pass

  def maximum():
    pass

  def minimum():
    pass

  def minimumDuration():
    pass

  def mouseGrabber():
    pass

  def open():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def reset():
    pass

  def resizeEvent():
    pass

  def setAutoClose():
    pass

  def setAutoReset():
    pass

  def setBar():
    pass

  def setCancelButton():
    pass

  def setCancelButtonText():
    pass

  def setLabel():
    pass

  def setLabelText():
    pass

  def setMaximum():
    pass

  def setMinimum():
    pass

  def setMinimumDuration():
    pass

  def setRange():
    pass

  def setTabOrder():
    pass

  def setValue():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def value():
    pass

  def wasCanceled():
    pass

class QPushButton(QAbstractButton):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def autoDefault():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def focusInEvent():
    pass

  def focusOutEvent():
    pass

  def initStyleOption():
    pass

  def isDefault():
    pass

  def isFlat():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def menu():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def released():
    """ Signal """
    pass

  def setAutoDefault():
    pass

  def setDefault():
    pass

  def setFlat():
    pass

  def setMenu():
    pass

  def setTabOrder():
    pass

  def showMenu():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def toggled():
    """ Signal """
    pass

class QRadioButton(QAbstractButton):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def hitButton():
    pass

  def initStyleOption():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def released():
    """ Signal """
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def toggled():
    """ Signal """
    pass

class QRubberBand(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  Line = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rectangle = None
  class Shape(object):

    Line = None
    Rectangle = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def changeEvent():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def initStyleOption():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def move():
    pass

  def moveEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resize():
    pass

  def resizeEvent():
    pass

  def setGeometry():
    pass

  def setTabOrder():
    pass

  def shape():
    pass

  def showEvent():
    pass

  staticMetaObject = None

class QScrollArea(QAbstractScrollArea):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def ensureVisible():
    pass

  def ensureWidgetVisible():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def focusNextPrevChild():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def scrollContentsBy():
    pass

  def setAlignment():
    pass

  def setTabOrder():
    pass

  def setWidget():
    pass

  def setWidgetResizable():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def takeWidget():
    pass

  def widget():
    pass

  def widgetResizable():
    pass

class QScrollBar(QAbstractSlider):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  SliderMove = None
  SliderNoAction = None
  SliderOrientationChange = None
  SliderPageStepAdd = None
  SliderPageStepSub = None
  SliderRangeChange = None
  SliderSingleStepAdd = None
  SliderSingleStepSub = None
  SliderStepsChange = None
  SliderToMaximum = None
  SliderToMinimum = None
  SliderValueChange = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionTriggered():
    """ Signal """
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def hideEvent():
    pass

  def initStyleOption():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def rangeChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  def sliderChange():
    pass

  def sliderMoved():
    """ Signal """
    pass

  def sliderPressed():
    """ Signal """
    pass

  def sliderReleased():
    """ Signal """
    pass

  staticMetaObject = None

  def valueChanged():
    """ Signal """
    pass

class QShortcut(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def activatedAmbiguously():
    """ Signal """
    pass

  def autoRepeat():
    pass

  def connect():
    pass

  def context():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def id():
    pass

  def isEnabled():
    pass

  def key():
    pass

  def parentWidget():
    pass

  def registerUserData():
    pass

  def setAutoRepeat():
    pass

  def setContext():
    pass

  def setEnabled():
    pass

  def setKey():
    pass

  def setWhatsThis():
    pass

  staticMetaObject = None

  def whatsThis():
    pass

class QSizeGrip(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def hideEvent():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveEvent():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  def setVisible():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def winEvent():
    pass

class QSizePolicy(Object):

  ButtonBox = None
  CheckBox = None
  ComboBox = None

  class ControlType(object):

    ButtonBox = None
    CheckBox = None
    ComboBox = None
    DefaultType = None
    Frame = None
    GroupBox = None
    Label = None
    Line = None
    LineEdit = None
    PushButton = None
    RadioButton = None
    Slider = None
    SpinBox = None
    TabWidget = None
    ToolButton = None
    name = property(None, None, None,
                    )

    values = {}

  class ControlTypes(object):

    pass

  DefaultType = None
  ExpandFlag = None
  Expanding = None
  Fixed = None
  Frame = None
  GroupBox = None
  GrowFlag = None
  IgnoreFlag = None
  Ignored = None
  Label = None
  Line = None
  LineEdit = None
  Maximum = None
  Minimum = None
  MinimumExpanding = None

  class Policy(object):

    Expanding = None
    Fixed = None
    Ignored = None
    Maximum = None
    Minimum = None
    MinimumExpanding = None
    Preferred = None
    name = property(None, None, None,
                    )

    values = {}

  class PolicyFlag(object):

    ExpandFlag = None
    GrowFlag = None
    IgnoreFlag = None
    ShrinkFlag = None
    name = property(None, None, None,
                    )

    values = {}

  Preferred = None
  PushButton = None
  RadioButton = None
  ShrinkFlag = None
  Slider = None
  SpinBox = None
  TabWidget = None
  ToolButton = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def controlType():
    pass

  def expandingDirections():
    pass

  def hasHeightForWidth():
    pass

  def hasWidthForHeight():
    pass

  def horizontalPolicy():
    pass

  def horizontalStretch():
    pass

  def setControlType():
    pass

  def setHeightForWidth():
    pass

  def setHorizontalPolicy():
    pass

  def setHorizontalStretch():
    pass

  def setVerticalPolicy():
    pass

  def setVerticalStretch():
    pass

  def setWidthForHeight():
    pass

  def transpose():
    pass

  def verticalPolicy():
    pass

  def verticalStretch():
    pass

class QSlider(QAbstractSlider):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  NoTicks = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  SliderMove = None
  SliderNoAction = None
  SliderOrientationChange = None
  SliderPageStepAdd = None
  SliderPageStepSub = None
  SliderRangeChange = None
  SliderSingleStepAdd = None
  SliderSingleStepSub = None
  SliderStepsChange = None
  SliderToMaximum = None
  SliderToMinimum = None
  SliderValueChange = None

  class TickPosition(object):

    NoTicks = None
    TicksAbove = None
    TicksBelow = None
    TicksBothSides = None
    TicksLeft = None
    TicksRight = None
    name = property(None, None, None,
                    )

    values = {}

  TicksAbove = None
  TicksBelow = None
  TicksBothSides = None
  TicksLeft = None
  TicksRight = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionTriggered():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def initStyleOption():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def paintEvent():
    pass

  def rangeChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  def setTickInterval():
    pass

  def setTickPosition():
    pass

  def sizeHint():
    pass

  def sliderMoved():
    """ Signal """
    pass

  def sliderPressed():
    """ Signal """
    pass

  def sliderReleased():
    """ Signal """
    pass

  staticMetaObject = None

  def tickInterval():
    pass

  def tickPosition():
    pass

  def valueChanged():
    """ Signal """
    pass

class QSpacerItem(QLayoutItem):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def changeSize():
    pass

  def expandingDirections():
    pass

  def geometry():
    pass

  def isEmpty():
    pass

  def maximumSize():
    pass

  def minimumSize():
    pass

  def setGeometry():
    pass

  def sizeHint():
    pass

  def spacerItem():
    pass

class QSpinBox(QAbstractSpinBox):

  CorrectToNearestValue = None
  CorrectToPreviousValue = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  NoButtons = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  PlusMinus = None
  StepDownEnabled = None
  StepNone = None
  StepUpEnabled = None
  UpDownArrows = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cleanText():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editingFinished():
    """ Signal """
    pass

  def event():
    pass

  def fixup():
    pass

  def keyboardGrabber():
    pass

  def maximum():
    pass

  def minimum():
    pass

  def mouseGrabber():
    pass

  def prefix():
    pass

  def registerUserData():
    pass

  def setMaximum():
    pass

  def setMinimum():
    pass

  def setPrefix():
    pass

  def setRange():
    pass

  def setSingleStep():
    pass

  def setSuffix():
    pass

  def setTabOrder():
    pass

  def setValue():
    pass

  def singleStep():
    pass

  staticMetaObject = None

  def suffix():
    pass

  def textFromValue():
    pass

  def validate():
    pass

  def value():
    pass

  def valueChanged():
    """ Signal """
    pass

  def valueFromText():
    pass

class QSplashScreen(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clearMessage():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def drawContents():
    pass

  def event():
    pass

  def finish():
    pass

  def keyboardGrabber():
    pass

  def messageChanged():
    """ Signal """
    pass

  def mouseGrabber():
    pass

  def mousePressEvent():
    pass

  def pixmap():
    pass

  def registerUserData():
    pass

  def setPixmap():
    pass

  def setTabOrder():
    pass

  def showMessage():
    pass

  staticMetaObject = None

class QSplitter(QFrame):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addWidget():
    pass

  def changeEvent():
    pass

  def childEvent():
    pass

  def childrenCollapsible():
    pass

  def closestLegalPosition():
    pass

  def connect():
    pass

  def count():
    pass

  def createHandle():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def getRange():
    pass

  def handle():
    pass

  def handleWidth():
    pass

  def indexOf():
    pass

  def insertWidget():
    pass

  def isCollapsible():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def moveSplitter():
    pass

  def opaqueResize():
    pass

  def orientation():
    pass

  def refresh():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def restoreState():
    pass

  def saveState():
    pass

  def setChildrenCollapsible():
    pass

  def setCollapsible():
    pass

  def setHandleWidth():
    pass

  def setOpaqueResize():
    pass

  def setOrientation():
    pass

  def setRubberBand():
    pass

  def setSizes():
    pass

  def setStretchFactor():
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  def sizes():
    pass

  def splitterMoved():
    """ Signal """
    pass

  staticMetaObject = None

  def widget():
    pass

class QSplitterHandle(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def closestLegalPosition():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveSplitter():
    pass

  def opaqueResize():
    pass

  def orientation():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def setOrientation():
    pass

  def setTabOrder():
    pass

  def sizeHint():
    pass

  def splitter():
    pass

  staticMetaObject = None

class QStackedLayout(QLayout):

  SetDefaultConstraint = None
  SetFixedSize = None
  SetMaximumSize = None
  SetMinAndMaxSize = None
  SetMinimumSize = None
  SetNoConstraint = None
  StackAll = None
  StackOne = None

  class StackingMode(object):

    StackAll = None
    StackOne = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addItem():
    pass

  def addWidget():
    pass

  def closestAcceptableSize():
    pass

  def connect():
    pass

  def count():
    pass

  def currentChanged():
    """ Signal """
    pass

  def currentIndex():
    pass

  def currentWidget():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def insertWidget():
    pass

  def itemAt():
    pass

  def minimumSize():
    pass

  def registerUserData():
    pass

  def setCurrentIndex():
    pass

  def setCurrentWidget():
    pass

  def setGeometry():
    pass

  def setStackingMode():
    pass

  def sizeHint():
    pass

  def stackingMode():
    pass

  staticMetaObject = None

  def takeAt():
    pass

  def widget():
    pass

  def widgetRemoved():
    """ Signal """
    pass

class QStackedWidget(QFrame):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addWidget():
    pass

  def connect():
    pass

  def count():
    pass

  def currentChanged():
    """ Signal """
    pass

  def currentIndex():
    pass

  def currentWidget():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def indexOf():
    pass

  def insertWidget():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def removeWidget():
    pass

  def setCurrentIndex():
    pass

  def setCurrentWidget():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def widget():
    pass

  def widgetRemoved():
    """ Signal """
    pass

class QStatusBar(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addPermanentWidget():
    pass

  def addWidget():
    pass

  def clearMessage():
    pass

  def connect():
    pass

  def currentMessage():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def hideOrShow():
    pass

  def insertPermanentWidget():
    pass

  def insertWidget():
    pass

  def isSizeGripEnabled():
    pass

  def keyboardGrabber():
    pass

  def messageChanged():
    """ Signal """
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def reformat():
    pass

  def registerUserData():
    pass

  def removeWidget():
    pass

  def resizeEvent():
    pass

  def setSizeGripEnabled():
    pass

  def setTabOrder():
    pass

  def showEvent():
    pass

  def showMessage():
    pass

  staticMetaObject = None

class QStyle(QObject):

  CC_ComboBox = None
  CC_CustomBase = None
  CC_Dial = None
  CC_GroupBox = None
  CC_MdiControls = None
  CC_Q3ListView = None
  CC_ScrollBar = None
  CC_Slider = None
  CC_SpinBox = None
  CC_TitleBar = None
  CC_ToolButton = None
  CE_CheckBox = None
  CE_CheckBoxLabel = None
  CE_ColumnViewGrip = None
  CE_ComboBoxLabel = None
  CE_CustomBase = None
  CE_DockWidgetTitle = None
  CE_FocusFrame = None
  CE_Header = None
  CE_HeaderEmptyArea = None
  CE_HeaderLabel = None
  CE_HeaderSection = None
  CE_ItemViewItem = None
  CE_MenuBarEmptyArea = None
  CE_MenuBarItem = None
  CE_MenuEmptyArea = None
  CE_MenuHMargin = None
  CE_MenuItem = None
  CE_MenuScroller = None
  CE_MenuTearoff = None
  CE_MenuVMargin = None
  CE_ProgressBar = None
  CE_ProgressBarContents = None
  CE_ProgressBarGroove = None
  CE_ProgressBarLabel = None
  CE_PushButton = None
  CE_PushButtonBevel = None
  CE_PushButtonLabel = None
  CE_Q3DockWindowEmptyArea = None
  CE_RadioButton = None
  CE_RadioButtonLabel = None
  CE_RubberBand = None
  CE_ScrollBarAddLine = None
  CE_ScrollBarAddPage = None
  CE_ScrollBarFirst = None
  CE_ScrollBarLast = None
  CE_ScrollBarSlider = None
  CE_ScrollBarSubLine = None
  CE_ScrollBarSubPage = None
  CE_ShapedFrame = None
  CE_SizeGrip = None
  CE_Splitter = None
  CE_TabBarTab = None
  CE_TabBarTabLabel = None
  CE_TabBarTabShape = None
  CE_ToolBar = None
  CE_ToolBoxTab = None
  CE_ToolBoxTabLabel = None
  CE_ToolBoxTabShape = None
  CE_ToolButtonLabel = None
  CT_CheckBox = None
  CT_ComboBox = None
  CT_CustomBase = None
  CT_DialogButtons = None
  CT_GroupBox = None
  CT_HeaderSection = None
  CT_ItemViewItem = None
  CT_LineEdit = None
  CT_MdiControls = None
  CT_Menu = None
  CT_MenuBar = None
  CT_MenuBarItem = None
  CT_MenuItem = None
  CT_ProgressBar = None
  CT_PushButton = None
  CT_Q3DockWindow = None
  CT_Q3Header = None
  CT_RadioButton = None
  CT_ScrollBar = None
  CT_SizeGrip = None
  CT_Slider = None
  CT_SpinBox = None
  CT_Splitter = None
  CT_TabBarTab = None
  CT_TabWidget = None
  CT_ToolButton = None
  PE_CustomBase = None
  PE_Frame = None
  PE_FrameButtonBevel = None
  PE_FrameButtonTool = None
  PE_FrameDefaultButton = None
  PE_FrameDockWidget = None
  PE_FrameFocusRect = None
  PE_FrameGroupBox = None
  PE_FrameLineEdit = None
  PE_FrameMenu = None
  PE_FrameStatusBar = None
  PE_FrameStatusBarItem = None
  PE_FrameTabBarBase = None
  PE_FrameTabWidget = None
  PE_FrameWindow = None
  PE_IndicatorArrowDown = None
  PE_IndicatorArrowLeft = None
  PE_IndicatorArrowRight = None
  PE_IndicatorArrowUp = None
  PE_IndicatorBranch = None
  PE_IndicatorButtonDropDown = None
  PE_IndicatorCheckBox = None
  PE_IndicatorColumnViewArrow = None
  PE_IndicatorDockWidgetResizeHandle = None
  PE_IndicatorHeaderArrow = None
  PE_IndicatorItemViewItemCheck = None
  PE_IndicatorItemViewItemDrop = None
  PE_IndicatorMenuCheckMark = None
  PE_IndicatorProgressChunk = None
  PE_IndicatorRadioButton = None
  PE_IndicatorSpinDown = None
  PE_IndicatorSpinMinus = None
  PE_IndicatorSpinPlus = None
  PE_IndicatorSpinUp = None
  PE_IndicatorTabClose = None
  PE_IndicatorTabTear = None
  PE_IndicatorToolBarHandle = None
  PE_IndicatorToolBarSeparator = None
  PE_IndicatorViewItemCheck = None
  PE_PanelButtonBevel = None
  PE_PanelButtonCommand = None
  PE_PanelButtonTool = None
  PE_PanelItemViewItem = None
  PE_PanelItemViewRow = None
  PE_PanelLineEdit = None
  PE_PanelMenu = None
  PE_PanelMenuBar = None
  PE_PanelScrollAreaCorner = None
  PE_PanelStatusBar = None
  PE_PanelTipLabel = None
  PE_PanelToolBar = None
  PE_Q3CheckListController = None
  PE_Q3CheckListExclusiveIndicator = None
  PE_Q3CheckListIndicator = None
  PE_Q3DockWindowSeparator = None
  PE_Q3Separator = None
  PE_Widget = None
  PM_ButtonDefaultIndicator = None
  PM_ButtonIconSize = None
  PM_ButtonMargin = None
  PM_ButtonShiftHorizontal = None
  PM_ButtonShiftVertical = None
  PM_CheckBoxLabelSpacing = None
  PM_CheckListButtonSize = None
  PM_CheckListControllerSize = None
  PM_ComboBoxFrameWidth = None
  PM_CustomBase = None
  PM_DefaultChildMargin = None
  PM_DefaultFrameWidth = None
  PM_DefaultLayoutSpacing = None
  PM_DefaultTopLevelMargin = None
  PM_DialogButtonsButtonHeight = None
  PM_DialogButtonsButtonWidth = None
  PM_DialogButtonsSeparator = None
  PM_DockWidgetFrameWidth = None
  PM_DockWidgetHandleExtent = None
  PM_DockWidgetSeparatorExtent = None
  PM_DockWidgetTitleBarButtonMargin = None
  PM_DockWidgetTitleMargin = None
  PM_ExclusiveIndicatorHeight = None
  PM_ExclusiveIndicatorWidth = None
  PM_FocusFrameHMargin = None
  PM_FocusFrameVMargin = None
  PM_HeaderGripMargin = None
  PM_HeaderMargin = None
  PM_HeaderMarkSize = None
  PM_IconViewIconSize = None
  PM_IndicatorHeight = None
  PM_IndicatorWidth = None
  PM_LargeIconSize = None
  PM_LayoutBottomMargin = None
  PM_LayoutHorizontalSpacing = None
  PM_LayoutLeftMargin = None
  PM_LayoutRightMargin = None
  PM_LayoutTopMargin = None
  PM_LayoutVerticalSpacing = None
  PM_ListViewIconSize = None
  PM_MDIFrameWidth = None
  PM_MDIMinimizedWidth = None
  PM_MaximumDragDistance = None
  PM_MdiSubWindowFrameWidth = None
  PM_MdiSubWindowMinimizedWidth = None
  PM_MenuBarHMargin = None
  PM_MenuBarItemSpacing = None
  PM_MenuBarPanelWidth = None
  PM_MenuBarVMargin = None
  PM_MenuButtonIndicator = None
  PM_MenuDesktopFrameWidth = None
  PM_MenuHMargin = None
  PM_MenuPanelWidth = None
  PM_MenuScrollerHeight = None
  PM_MenuTearoffHeight = None
  PM_MenuVMargin = None
  PM_MessageBoxIconSize = None
  PM_ProgressBarChunkWidth = None
  PM_RadioButtonLabelSpacing = None
  PM_ScrollBarExtent = None
  PM_ScrollBarSliderMin = None
  PM_ScrollView_ScrollBarSpacing = None
  PM_SizeGripSize = None
  PM_SliderControlThickness = None
  PM_SliderLength = None
  PM_SliderSpaceAvailable = None
  PM_SliderThickness = None
  PM_SliderTickmarkOffset = None
  PM_SmallIconSize = None
  PM_SpinBoxFrameWidth = None
  PM_SpinBoxSliderHeight = None
  PM_SplitterWidth = None
  PM_SubMenuOverlap = None
  PM_TabBarBaseHeight = None
  PM_TabBarBaseOverlap = None
  PM_TabBarIconSize = None
  PM_TabBarScrollButtonWidth = None
  PM_TabBarTabHSpace = None
  PM_TabBarTabOverlap = None
  PM_TabBarTabShiftHorizontal = None
  PM_TabBarTabShiftVertical = None
  PM_TabBarTabVSpace = None
  PM_TabBar_ScrollButtonOverlap = None
  PM_TabCloseIndicatorHeight = None
  PM_TabCloseIndicatorWidth = None
  PM_TextCursorWidth = None
  PM_TitleBarHeight = None
  PM_ToolBarExtensionExtent = None
  PM_ToolBarFrameWidth = None
  PM_ToolBarHandleExtent = None
  PM_ToolBarIconSize = None
  PM_ToolBarItemMargin = None
  PM_ToolBarItemSpacing = None
  PM_ToolBarSeparatorExtent = None
  PM_ToolTipLabelFrameWidth = None
  RSIP_OnMouseClick = None
  RSIP_OnMouseClickAndAlreadyFocused = None
  SC_All = None
  SC_ComboBoxArrow = None
  SC_ComboBoxEditField = None
  SC_ComboBoxFrame = None
  SC_ComboBoxListBoxPopup = None
  SC_CustomBase = None
  SC_DialGroove = None
  SC_DialHandle = None
  SC_DialTickmarks = None
  SC_GroupBoxCheckBox = None
  SC_GroupBoxContents = None
  SC_GroupBoxFrame = None
  SC_GroupBoxLabel = None
  SC_MdiCloseButton = None
  SC_MdiMinButton = None
  SC_MdiNormalButton = None
  SC_None = None
  SC_Q3ListView = None
  SC_Q3ListViewBranch = None
  SC_Q3ListViewExpand = None
  SC_ScrollBarAddLine = None
  SC_ScrollBarAddPage = None
  SC_ScrollBarFirst = None
  SC_ScrollBarGroove = None
  SC_ScrollBarLast = None
  SC_ScrollBarSlider = None
  SC_ScrollBarSubLine = None
  SC_ScrollBarSubPage = None
  SC_SliderGroove = None
  SC_SliderHandle = None
  SC_SliderTickmarks = None
  SC_SpinBoxDown = None
  SC_SpinBoxEditField = None
  SC_SpinBoxFrame = None
  SC_SpinBoxUp = None
  SC_TitleBarCloseButton = None
  SC_TitleBarContextHelpButton = None
  SC_TitleBarLabel = None
  SC_TitleBarMaxButton = None
  SC_TitleBarMinButton = None
  SC_TitleBarNormalButton = None
  SC_TitleBarShadeButton = None
  SC_TitleBarSysMenu = None
  SC_TitleBarUnshadeButton = None
  SC_ToolButton = None
  SC_ToolButtonMenu = None
  SE_CheckBoxClickRect = None
  SE_CheckBoxContents = None
  SE_CheckBoxFocusRect = None
  SE_CheckBoxIndicator = None
  SE_CheckBoxLayoutItem = None
  SE_ComboBoxFocusRect = None
  SE_ComboBoxLayoutItem = None
  SE_CustomBase = None
  SE_DateTimeEditLayoutItem = None
  SE_DialogButtonAbort = None
  SE_DialogButtonAccept = None
  SE_DialogButtonAll = None
  SE_DialogButtonApply = None
  SE_DialogButtonBoxLayoutItem = None
  SE_DialogButtonCustom = None
  SE_DialogButtonHelp = None
  SE_DialogButtonIgnore = None
  SE_DialogButtonReject = None
  SE_DialogButtonRetry = None
  SE_DockWidgetCloseButton = None
  SE_DockWidgetFloatButton = None
  SE_DockWidgetIcon = None
  SE_DockWidgetTitleBarText = None
  SE_FrameContents = None
  SE_FrameLayoutItem = None
  SE_GroupBoxLayoutItem = None
  SE_HeaderArrow = None
  SE_HeaderLabel = None
  SE_ItemViewItemCheckIndicator = None
  SE_ItemViewItemDecoration = None
  SE_ItemViewItemFocusRect = None
  SE_ItemViewItemText = None
  SE_LabelLayoutItem = None
  SE_LineEditContents = None
  SE_ProgressBarContents = None
  SE_ProgressBarGroove = None
  SE_ProgressBarLabel = None
  SE_ProgressBarLayoutItem = None
  SE_PushButtonContents = None
  SE_PushButtonFocusRect = None
  SE_PushButtonLayoutItem = None
  SE_Q3DockWindowHandleRect = None
  SE_RadioButtonClickRect = None
  SE_RadioButtonContents = None
  SE_RadioButtonFocusRect = None
  SE_RadioButtonIndicator = None
  SE_RadioButtonLayoutItem = None
  SE_ShapedFrameContents = None
  SE_SliderFocusRect = None
  SE_SliderLayoutItem = None
  SE_SpinBoxLayoutItem = None
  SE_TabBarTabLeftButton = None
  SE_TabBarTabRightButton = None
  SE_TabBarTabText = None
  SE_TabBarTearIndicator = None
  SE_TabWidgetLayoutItem = None
  SE_TabWidgetLeftCorner = None
  SE_TabWidgetRightCorner = None
  SE_TabWidgetTabBar = None
  SE_TabWidgetTabContents = None
  SE_TabWidgetTabPane = None
  SE_ToolBarHandle = None
  SE_ToolBoxTabContents = None
  SE_ToolButtonLayoutItem = None
  SE_TreeViewDisclosureItem = None
  SE_ViewItemCheckIndicator = None
  SH_BlinkCursorWhenTextSelected = None
  SH_Button_FocusPolicy = None
  SH_ComboBox_LayoutDirection = None
  SH_ComboBox_ListMouseTracking = None
  SH_ComboBox_Popup = None
  SH_ComboBox_PopupFrameStyle = None
  SH_CustomBase = None
  SH_Dial_BackgroundRole = None
  SH_DialogButtonBox_ButtonsHaveIcons = None
  SH_DialogButtonLayout = None
  SH_DialogButtons_DefaultButton = None
  SH_DitherDisabledText = None
  SH_DockWidget_ButtonsHaveFrame = None
  SH_DrawMenuBarSeparator = None
  SH_EtchDisabledText = None
  SH_FocusFrame_AboveWidget = None
  SH_FocusFrame_Mask = None
  SH_FontDialog_SelectAssociatedText = None
  SH_FormLayoutFieldGrowthPolicy = None
  SH_FormLayoutFormAlignment = None
  SH_FormLayoutLabelAlignment = None
  SH_FormLayoutWrapPolicy = None
  SH_GroupBox_TextLabelColor = None
  SH_GroupBox_TextLabelVerticalAlignment = None
  SH_Header_ArrowAlignment = None
  SH_ItemView_ActivateItemOnSingleClick = None
  SH_ItemView_ArrowKeysNavigateIntoChildren = None
  SH_ItemView_ChangeHighlightOnFocus = None
  SH_ItemView_DrawDelegateFrame = None
  SH_ItemView_EllipsisLocation = None
  SH_ItemView_MovementWithoutUpdatingSelection = None
  SH_ItemView_PaintAlternatingRowColorsForEmptyArea = None
  SH_ItemView_ShowDecorationSelected = None
  SH_LineEdit_PasswordCharacter = None
  SH_MainWindow_SpaceBelowMenuBar = None
  SH_MenuBar_AltKeyNavigation = None
  SH_MenuBar_DismissOnSecondClick = None
  SH_MenuBar_MouseTracking = None
  SH_Menu_AllowActiveAndDisabled = None
  SH_Menu_FadeOutOnHide = None
  SH_Menu_FillScreenWithScroll = None
  SH_Menu_FlashTriggeredItem = None
  SH_Menu_KeyboardSearch = None
  SH_Menu_Mask = None
  SH_Menu_MouseTracking = None
  SH_Menu_Scrollable = None
  SH_Menu_SelectionWrap = None
  SH_Menu_SloppySubMenus = None
  SH_Menu_SpaceActivatesItem = None
  SH_Menu_SubMenuPopupDelay = None
  SH_MessageBox_CenterButtons = None
  SH_MessageBox_TextInteractionFlags = None
  SH_MessageBox_UseBorderForButtonSpacing = None
  SH_PrintDialog_RightAlignButtons = None
  SH_ProgressDialog_CenterCancelButton = None
  SH_ProgressDialog_TextLabelAlignment = None
  SH_Q3ListViewExpand_SelectMouseType = None
  SH_RequestSoftwareInputPanel = None
  SH_RichText_FullWidthSelection = None
  SH_RubberBand_Mask = None
  SH_ScrollBar_ContextMenu = None
  SH_ScrollBar_LeftClickAbsolutePosition = None
  SH_ScrollBar_MiddleClickAbsolutePosition = None
  SH_ScrollBar_RollBetweenButtons = None
  SH_ScrollBar_ScrollWhenPointerLeavesControl = None
  SH_ScrollBar_StopMouseOverSlider = None
  SH_ScrollView_FrameOnlyAroundContents = None
  SH_Slider_AbsoluteSetButtons = None
  SH_Slider_PageSetButtons = None
  SH_Slider_SloppyKeyEvents = None
  SH_Slider_SnapToValue = None
  SH_Slider_StopMouseOverSlider = None
  SH_SpellCheckUnderlineStyle = None
  SH_SpinBox_AnimateButton = None
  SH_SpinBox_ClickAutoRepeatRate = None
  SH_SpinBox_ClickAutoRepeatThreshold = None
  SH_SpinBox_KeyPressAutoRepeatRate = None
  SH_SpinControls_DisableOnBounds = None
  SH_TabBar_Alignment = None
  SH_TabBar_CloseButtonPosition = None
  SH_TabBar_ElideMode = None
  SH_TabBar_PreferNoArrows = None
  SH_TabBar_SelectMouseType = None
  SH_TabWidget_DefaultTabPosition = None
  SH_Table_GridLineColor = None
  SH_TextControl_FocusIndicatorTextCharFormat = None
  SH_TitleBar_AutoRaise = None
  SH_TitleBar_ModifyNotification = None
  SH_TitleBar_NoBorder = None
  SH_ToolBar_Movable = None
  SH_ToolBox_SelectedPageTitleBold = None
  SH_ToolButtonStyle = None
  SH_ToolButton_PopupDelay = None
  SH_ToolTipLabel_Opacity = None
  SH_ToolTip_Mask = None
  SH_UnderlineShortcut = None
  SH_Widget_ShareActivation = None
  SH_WindowFrame_Mask = None
  SH_WizardStyle = None
  SH_Workspace_FillSpaceOnMaximize = None
  SP_ArrowBack = None
  SP_ArrowDown = None
  SP_ArrowForward = None
  SP_ArrowLeft = None
  SP_ArrowRight = None
  SP_ArrowUp = None
  SP_BrowserReload = None
  SP_BrowserStop = None
  SP_CommandLink = None
  SP_ComputerIcon = None
  SP_CustomBase = None
  SP_DesktopIcon = None
  SP_DialogApplyButton = None
  SP_DialogCancelButton = None
  SP_DialogCloseButton = None
  SP_DialogDiscardButton = None
  SP_DialogHelpButton = None
  SP_DialogNoButton = None
  SP_DialogOkButton = None
  SP_DialogOpenButton = None
  SP_DialogResetButton = None
  SP_DialogSaveButton = None
  SP_DialogYesButton = None
  SP_DirClosedIcon = None
  SP_DirHomeIcon = None
  SP_DirIcon = None
  SP_DirLinkIcon = None
  SP_DirOpenIcon = None
  SP_DockWidgetCloseButton = None
  SP_DriveCDIcon = None
  SP_DriveDVDIcon = None
  SP_DriveFDIcon = None
  SP_DriveHDIcon = None
  SP_DriveNetIcon = None
  SP_FileDialogBack = None
  SP_FileDialogContentsView = None
  SP_FileDialogDetailedView = None
  SP_FileDialogEnd = None
  SP_FileDialogInfoView = None
  SP_FileDialogListView = None
  SP_FileDialogNewFolder = None
  SP_FileDialogStart = None
  SP_FileDialogToParent = None
  SP_FileIcon = None
  SP_FileLinkIcon = None
  SP_MediaPause = None
  SP_MediaPlay = None
  SP_MediaSeekBackward = None
  SP_MediaSeekForward = None
  SP_MediaSkipBackward = None
  SP_MediaSkipForward = None
  SP_MediaStop = None
  SP_MediaVolume = None
  SP_MediaVolumeMuted = None
  SP_MessageBoxCritical = None
  SP_MessageBoxInformation = None
  SP_MessageBoxQuestion = None
  SP_MessageBoxWarning = None
  SP_TitleBarCloseButton = None
  SP_TitleBarContextHelpButton = None
  SP_TitleBarMaxButton = None
  SP_TitleBarMenuButton = None
  SP_TitleBarMinButton = None
  SP_TitleBarNormalButton = None
  SP_TitleBarShadeButton = None
  SP_TitleBarUnshadeButton = None
  SP_ToolBarHorizontalExtensionButton = None
  SP_ToolBarVerticalExtensionButton = None
  SP_TrashIcon = None
  SP_VistaShield = None
  State_Active = None
  State_AutoRaise = None
  State_Bottom = None
  State_Children = None
  State_DownArrow = None
  State_Editing = None
  State_Enabled = None
  State_FocusAtBorder = None
  State_HasFocus = None
  State_Horizontal = None
  State_Item = None
  State_KeyboardFocusChange = None
  State_Mini = None
  State_MouseOver = None
  State_NoChange = None
  State_None = None
  State_Off = None
  State_On = None
  State_Open = None
  State_Raised = None
  State_ReadOnly = None
  State_Selected = None
  State_Sibling = None
  State_Small = None
  State_Sunken = None
  State_Top = None
  State_UpArrow = None
  State_Window = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignedRect():
    pass

  def combinedLayoutSpacing():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def drawComplexControl():
    pass

  def drawControl():
    pass

  def drawItemPixmap():
    pass

  def drawItemText():
    pass

  def drawPrimitive():
    pass

  def generatedIconPixmap():
    pass

  def hitTestComplexControl():
    pass

  def itemPixmapRect():
    pass

  def itemTextRect():
    pass

  def layoutSpacing():
    pass

  def layoutSpacingImplementation():
    pass

  def pixelMetric():
    pass

  def polish():
    pass

  def proxy():
    pass

  def registerUserData():
    pass

  def sizeFromContents():
    pass

  def sliderPositionFromValue():
    pass

  def sliderValueFromPosition():
    pass

  def standardIcon():
    pass

  def standardIconImplementation():
    pass

  def standardPalette():
    pass

  def standardPixmap():
    pass

  staticMetaObject = None

  def styleHint():
    pass

  def subControlRect():
    pass

  def subElementRect():
    pass

  def unpolish():
    pass

  def visualAlignment():
    pass

  def visualPos():
    pass

  def visualRect():
    pass

class QStyleFactory(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def create():
    pass

  def keys():
    pass

class QStyleHintReturn(Object):

  class HintReturnType(object):

    SH_Default = None
    SH_Mask = None
    SH_Variant = None
    name = property(None, None, None,
                    )

    values = {}

  SH_Default = None
  SH_Mask = None
  SH_Variant = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  type = property(None, None, None,
                  )

  version = property(None, None, None,
                     )


class QStyleHintReturnMask(QStyleHintReturn):

  SH_Default = None
  SH_Mask = None
  SH_Variant = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  region = property(None, None, None,
                    )


class QStyleHintReturnVariant(QStyleHintReturn):

  SH_Default = None
  SH_Mask = None
  SH_Variant = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  variant = property(None, None, None,
                     )


class QStyleOption(Object):

  class OptionType(object):

    SO_Button = None
    SO_ComboBox = None
    SO_Complex = None
    SO_ComplexCustomBase = None
    SO_CustomBase = None
    SO_Default = None
    SO_DockWidget = None
    SO_FocusRect = None
    SO_Frame = None
    SO_GraphicsItem = None
    SO_GroupBox = None
    SO_Header = None
    SO_MenuItem = None
    SO_ProgressBar = None
    SO_Q3DockWindow = None
    SO_Q3ListView = None
    SO_Q3ListViewItem = None
    SO_RubberBand = None
    SO_SizeGrip = None
    SO_Slider = None
    SO_SpinBox = None
    SO_Tab = None
    SO_TabBarBase = None
    SO_TabWidgetFrame = None
    SO_TitleBar = None
    SO_ToolBar = None
    SO_ToolBox = None
    SO_ToolButton = None
    SO_ViewItem = None
    name = property(None, None, None,
                    )

    values = {}

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  direction = property(None, None, None,
                       )

  fontMetrics = property(None, None, None,
                         )


  def initFrom():
    pass

  palette = property(None, None, None,
                     )

  rect = property(None, None, None,
                  )

  state = property(None, None, None,
                   )

  type = property(None, None, None,
                  )

  version = property(None, None, None,
                     )


class QStyleOptionButton(QStyleOption):

  AutoDefaultButton = None

  class ButtonFeature(object):

    AutoDefaultButton = None
    CommandLinkButton = None
    DefaultButton = None
    Flat = None
    HasMenu = None
    None = None
    name = property(None, None, None,
                    )

    values = {}

  class ButtonFeatures(object):

    pass

  CommandLinkButton = None
  DefaultButton = None
  Flat = None
  HasMenu = None
  None = None
  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  features = property(None, None, None,
                      )

  icon = property(None, None, None,
                  )

  iconSize = property(None, None, None,
                      )

  text = property(None, None, None,
                  )


class QStyleOptionComboBox(QStyleOptionComplex):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  currentIcon = property(None, None, None,
                         )

  currentText = property(None, None, None,
                         )

  editable = property(None, None, None,
                      )

  frame = property(None, None, None,
                   )

  iconSize = property(None, None, None,
                      )

  popupRect = property(None, None, None,
                       )


class QStyleOptionComplex(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  activeSubControls = property(None, None, None,
                               )

  subControls = property(None, None, None,
                         )


class QStyleOptionDockWidget(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  closable = property(None, None, None,
                      )

  floatable = property(None, None, None,
                       )

  movable = property(None, None, None,
                     )

  title = property(None, None, None,
                   )


class QStyleOptionFocusRect(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  backgroundColor = property(None, None, None,
                             )


class QStyleOptionFrame(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  lineWidth = property(None, None, None,
                       )

  midLineWidth = property(None, None, None,
                          )


class QStyleOptionGraphicsItem(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  exposedRect = property(None, None, None,
                         )

  levelOfDetail = property(None, None, None,
                           )


  def levelOfDetailFromTransform():
    pass

  matrix = property(None, None, None,
                    )


class QStyleOptionGroupBox(QStyleOptionComplex):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  features = property(None, None, None,
                      )

  lineWidth = property(None, None, None,
                       )

  midLineWidth = property(None, None, None,
                          )

  text = property(None, None, None,
                  )

  textAlignment = property(None, None, None,
                           )

  textColor = property(None, None, None,
                       )


class QStyleOptionHeader(QStyleOption):

  Beginning = None
  End = None
  Middle = None
  NextAndPreviousAreSelected = None
  NextIsSelected = None
  None = None
  NotAdjacent = None
  OnlyOneSection = None
  PreviousIsSelected = None
  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class SectionPosition(object):

    Beginning = None
    End = None
    Middle = None
    OnlyOneSection = None
    name = property(None, None, None,
                    )

    values = {}

  class SelectedPosition(object):

    NextAndPreviousAreSelected = None
    NextIsSelected = None
    NotAdjacent = None
    PreviousIsSelected = None
    name = property(None, None, None,
                    )

    values = {}

  SortDown = None

  class SortIndicator(object):

    None = None
    SortDown = None
    SortUp = None
    name = property(None, None, None,
                    )

    values = {}

  SortUp = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  icon = property(None, None, None,
                  )

  iconAlignment = property(None, None, None,
                           )

  orientation = property(None, None, None,
                         )

  position = property(None, None, None,
                      )

  section = property(None, None, None,
                     )

  selectedPosition = property(None, None, None,
                              )

  sortIndicator = property(None, None, None,
                           )

  text = property(None, None, None,
                  )

  textAlignment = property(None, None, None,
                           )


class QStyleOptionMenuItem(QStyleOption):

  class CheckType(object):

    Exclusive = None
    NonExclusive = None
    NotCheckable = None
    name = property(None, None, None,
                    )

    values = {}

  DefaultItem = None
  EmptyArea = None
  Exclusive = None
  Margin = None

  class MenuItemType(object):

    DefaultItem = None
    EmptyArea = None
    Margin = None
    Normal = None
    Scroller = None
    Separator = None
    SubMenu = None
    TearOff = None
    name = property(None, None, None,
                    )

    values = {}

  NonExclusive = None
  Normal = None
  NotCheckable = None
  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None
  Scroller = None
  Separator = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  SubMenu = None
  TearOff = None
  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  checkType = property(None, None, None,
                       )

  checked = property(None, None, None,
                     )

  font = property(None, None, None,
                  )

  icon = property(None, None, None,
                  )

  maxIconWidth = property(None, None, None,
                          )

  menuHasCheckableItems = property(None, None, None,
                                   )

  menuItemType = property(None, None, None,
                          )

  menuRect = property(None, None, None,
                      )

  tabWidth = property(None, None, None,
                      )

  text = property(None, None, None,
                  )


class QStyleOptionProgressBar(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  maximum = property(None, None, None,
                     )

  minimum = property(None, None, None,
                     )

  progress = property(None, None, None,
                      )

  text = property(None, None, None,
                  )

  textAlignment = property(None, None, None,
                           )

  textVisible = property(None, None, None,
                         )


class QStyleOptionRubberBand(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  opaque = property(None, None, None,
                    )

  shape = property(None, None, None,
                   )


class QStyleOptionSizeGrip(QStyleOptionComplex):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  corner = property(None, None, None,
                    )


class QStyleOptionSlider(QStyleOptionComplex):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  dialWrapping = property(None, None, None,
                          )

  maximum = property(None, None, None,
                     )

  minimum = property(None, None, None,
                     )

  notchTarget = property(None, None, None,
                         )

  orientation = property(None, None, None,
                         )

  pageStep = property(None, None, None,
                      )

  singleStep = property(None, None, None,
                        )

  sliderPosition = property(None, None, None,
                            )

  sliderValue = property(None, None, None,
                         )

  tickInterval = property(None, None, None,
                          )

  tickPosition = property(None, None, None,
                          )

  upsideDown = property(None, None, None,
                        )


class QStyleOptionSpinBox(QStyleOptionComplex):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  buttonSymbols = property(None, None, None,
                           )

  frame = property(None, None, None,
                   )

  stepEnabled = property(None, None, None,
                         )


class QStyleOptionTab(QStyleOption):

  Beginning = None

  class CornerWidget(object):

    LeftCornerWidget = None
    NoCornerWidgets = None
    RightCornerWidget = None
    name = property(None, None, None,
                    )

    values = {}

  class CornerWidgets(object):

    pass

  End = None
  LeftCornerWidget = None
  Middle = None
  NextIsSelected = None
  NoCornerWidgets = None
  NotAdjacent = None
  OnlyOneTab = None
  PreviousIsSelected = None
  RightCornerWidget = None
  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class SelectedPosition(object):

    NextIsSelected = None
    NotAdjacent = None
    PreviousIsSelected = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  class TabPosition(object):

    Beginning = None
    End = None
    Middle = None
    OnlyOneTab = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  cornerWidgets = property(None, None, None,
                           )

  icon = property(None, None, None,
                  )

  position = property(None, None, None,
                      )

  row = property(None, None, None,
                 )

  selectedPosition = property(None, None, None,
                              )

  shape = property(None, None, None,
                   )

  text = property(None, None, None,
                  )


class QStyleOptionTabBarBase(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  selectedTabRect = property(None, None, None,
                             )

  shape = property(None, None, None,
                   )

  tabBarRect = property(None, None, None,
                        )


class QStyleOptionTabWidgetFrame(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  leftCornerWidgetSize = property(None, None, None,
                                  )

  lineWidth = property(None, None, None,
                       )

  midLineWidth = property(None, None, None,
                          )

  rightCornerWidgetSize = property(None, None, None,
                                   )

  shape = property(None, None, None,
                   )

  tabBarSize = property(None, None, None,
                        )


class QStyleOptionTitleBar(QStyleOptionComplex):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  icon = property(None, None, None,
                  )

  text = property(None, None, None,
                  )

  titleBarFlags = property(None, None, None,
                           )

  titleBarState = property(None, None, None,
                           )


class QStyleOptionToolBar(QStyleOption):

  Beginning = None
  End = None
  Middle = None
  Movable = None
  None = None
  OnlyOne = None
  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  class ToolBarFeature(object):

    Movable = None
    None = None
    name = property(None, None, None,
                    )

    values = {}

  class ToolBarFeatures(object):

    pass

  class ToolBarPosition(object):

    Beginning = None
    End = None
    Middle = None
    OnlyOne = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  features = property(None, None, None,
                      )

  lineWidth = property(None, None, None,
                       )

  midLineWidth = property(None, None, None,
                          )

  positionOfLine = property(None, None, None,
                            )

  positionWithinLine = property(None, None, None,
                                )

  toolBarArea = property(None, None, None,
                         )


class QStyleOptionToolBox(QStyleOption):

  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  icon = property(None, None, None,
                  )

  text = property(None, None, None,
                  )


class QStyleOptionToolButton(QStyleOptionComplex):

  Arrow = None
  HasMenu = None
  Menu = None
  MenuButtonPopup = None
  None = None
  PopupDelay = None
  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  class ToolButtonFeature(object):

    Arrow = None
    HasMenu = None
    Menu = None
    MenuButtonPopup = None
    None = None
    PopupDelay = None
    name = property(None, None, None,
                    )

    values = {}

  class ToolButtonFeatures(object):

    pass

  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  arrowType = property(None, None, None,
                       )

  features = property(None, None, None,
                      )

  font = property(None, None, None,
                  )

  icon = property(None, None, None,
                  )

  iconSize = property(None, None, None,
                      )

  pos = property(None, None, None,
                 )

  text = property(None, None, None,
                  )

  toolButtonStyle = property(None, None, None,
                             )


class QStyleOptionViewItem(QStyleOption):

  Bottom = None
  Left = None
  class Position(object):

    Bottom = None
    Left = None
    Right = None
    Top = None
    name = property(None, None, None,
                    )

    values = {}

  Right = None
  SO_Button = None
  SO_ComboBox = None
  SO_Complex = None
  SO_ComplexCustomBase = None
  SO_CustomBase = None
  SO_Default = None
  SO_DockWidget = None
  SO_FocusRect = None
  SO_Frame = None
  SO_GraphicsItem = None
  SO_GroupBox = None
  SO_Header = None
  SO_MenuItem = None
  SO_ProgressBar = None
  SO_Q3DockWindow = None
  SO_Q3ListView = None
  SO_Q3ListViewItem = None
  SO_RubberBand = None
  SO_SizeGrip = None
  SO_Slider = None
  SO_SpinBox = None
  SO_Tab = None
  SO_TabBarBase = None
  SO_TabWidgetFrame = None
  SO_TitleBar = None
  SO_ToolBar = None
  SO_ToolBox = None
  SO_ToolButton = None
  SO_ViewItem = None

  class StyleOptionType(object):

    Type = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleOptionVersion(object):

    Version = None
    name = property(None, None, None,
                    )

    values = {}

  Top = None
  Type = None
  Version = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  decorationAlignment = property(None, None, None,
                                 )

  decorationPosition = property(None, None, None,
                                )

  decorationSize = property(None, None, None,
                            )

  displayAlignment = property(None, None, None,
                              )

  font = property(None, None, None,
                  )

  showDecorationSelected = property(None, None, None,
                                    )

  textElideMode = property(None, None, None,
                           )


class QStylePainter(QPainter):

  Antialiasing = None

  class CompositionMode(object):

    CompositionMode_Clear = None
    CompositionMode_ColorBurn = None
    CompositionMode_ColorDodge = None
    CompositionMode_Darken = None
    CompositionMode_Destination = None
    CompositionMode_DestinationAtop = None
    CompositionMode_DestinationIn = None
    CompositionMode_DestinationOut = None
    CompositionMode_DestinationOver = None
    CompositionMode_Difference = None
    CompositionMode_Exclusion = None
    CompositionMode_HardLight = None
    CompositionMode_Lighten = None
    CompositionMode_Multiply = None
    CompositionMode_Overlay = None
    CompositionMode_Plus = None
    CompositionMode_Screen = None
    CompositionMode_SoftLight = None
    CompositionMode_Source = None
    CompositionMode_SourceAtop = None
    CompositionMode_SourceIn = None
    CompositionMode_SourceOut = None
    CompositionMode_SourceOver = None
    CompositionMode_Xor = None
    RasterOp_NotSource = None
    RasterOp_NotSourceAndDestination = None
    RasterOp_NotSourceAndNotDestination = None
    RasterOp_NotSourceOrNotDestination = None
    RasterOp_NotSourceXorDestination = None
    RasterOp_SourceAndDestination = None
    RasterOp_SourceAndNotDestination = None
    RasterOp_SourceOrDestination = None
    RasterOp_SourceXorDestination = None
    name = property(None, None, None,
                    )

    values = {}

  CompositionMode_Clear = None
  CompositionMode_ColorBurn = None
  CompositionMode_ColorDodge = None
  CompositionMode_Darken = None
  CompositionMode_Destination = None
  CompositionMode_DestinationAtop = None
  CompositionMode_DestinationIn = None
  CompositionMode_DestinationOut = None
  CompositionMode_DestinationOver = None
  CompositionMode_Difference = None
  CompositionMode_Exclusion = None
  CompositionMode_HardLight = None
  CompositionMode_Lighten = None
  CompositionMode_Multiply = None
  CompositionMode_Overlay = None
  CompositionMode_Plus = None
  CompositionMode_Screen = None
  CompositionMode_SoftLight = None
  CompositionMode_Source = None
  CompositionMode_SourceAtop = None
  CompositionMode_SourceIn = None
  CompositionMode_SourceOut = None
  CompositionMode_SourceOver = None
  CompositionMode_Xor = None
  HighQualityAntialiasing = None
  NonCosmeticDefaultPen = None
  OpaqueHint = None

  class PixmapFragment(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    def create():
      pass

    height = property(None, None, None,
                      )

    opacity = property(None, None, None,
                       )

    rotation = property(None, None, None,
                        )

    scaleX = property(None, None, None,
                      )

    scaleY = property(None, None, None,
                      )

    sourceLeft = property(None, None, None,
                          )

    sourceTop = property(None, None, None,
                         )

    width = property(None, None, None,
                     )

    x = property(None, None, None,
                 )

    y = property(None, None, None,
                 )


  class PixmapFragmentHint(object):

    OpaqueHint = None
    name = property(None, None, None,
                    )

    values = {}

  class PixmapFragmentHints(object):

    pass

  RasterOp_NotSource = None
  RasterOp_NotSourceAndDestination = None
  RasterOp_NotSourceAndNotDestination = None
  RasterOp_NotSourceOrNotDestination = None
  RasterOp_NotSourceXorDestination = None
  RasterOp_SourceAndDestination = None
  RasterOp_SourceAndNotDestination = None
  RasterOp_SourceOrDestination = None
  RasterOp_SourceXorDestination = None

  class RenderHint(object):

    Antialiasing = None
    HighQualityAntialiasing = None
    NonCosmeticDefaultPen = None
    SmoothPixmapTransform = None
    TextAntialiasing = None
    name = property(None, None, None,
                    )

    values = {}

  class RenderHints(object):

    pass

  SmoothPixmapTransform = None
  TextAntialiasing = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def begin():
    pass

  def drawComplexControl():
    pass

  def drawControl():
    pass

  def drawItemPixmap():
    pass

  def drawItemText():
    pass

  def drawPrimitive():
    pass

  def restoreRedirected():
    pass

  def setRedirected():
    pass

  def style():
    pass

class QStyledItemDelegate(QAbstractItemDelegate):

  EditNextItem = None
  EditPreviousItem = None
  NoHint = None
  RevertModelCache = None
  SubmitModelCache = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def closeEditor():
    """ Signal """
    pass

  def commitData():
    """ Signal """
    pass

  def connect():
    pass

  def createEditor():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def displayText():
    pass

  def editorEvent():
    pass

  def eventFilter():
    pass

  def initStyleOption():
    pass

  def itemEditorFactory():
    pass

  def paint():
    pass

  def registerUserData():
    pass

  def setEditorData():
    pass

  def setItemEditorFactory():
    pass

  def setModelData():
    pass

  def sizeHint():
    pass

  def sizeHintChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def updateEditorGeometry():
    pass

class QSwipeGesture(QGesture):

  CancelAllInContext = None
  CancelNone = None
  Down = None
  Left = None
  NoDirection = None
  Right = None

  class SwipeDirection(object):

    Down = None
    Left = None
    NoDirection = None
    Right = None
    Up = None
    name = property(None, None, None,
                    )

    values = {}

  Up = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def horizontalDirection():
    pass

  def registerUserData():
    pass

  def setSwipeAngle():
    pass

  staticMetaObject = None

  def swipeAngle():
    pass

  def verticalDirection():
    pass

class QSystemTrayIcon(QObject):

  class ActivationReason(object):

    Context = None
    DoubleClick = None
    MiddleClick = None
    Trigger = None
    Unknown = None
    name = property(None, None, None,
                    )

    values = {}

  Context = None
  Critical = None
  DoubleClick = None
  Information = None

  class MessageIcon(object):

    Critical = None
    Information = None
    NoIcon = None
    Warning = None
    name = property(None, None, None,
                    )

    values = {}

  MiddleClick = None
  NoIcon = None
  Trigger = None
  Unknown = None
  Warning = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def connect():
    pass

  def contextMenu():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def geometry():
    pass

  def hide():
    pass

  def icon():
    pass

  def isSystemTrayAvailable():
    pass

  def isVisible():
    pass

  def messageClicked():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setContextMenu():
    pass

  def setIcon():
    pass

  def setToolTip():
    pass

  def setVisible():
    pass

  def show():
    pass

  def showMessage():
    pass

  staticMetaObject = None

  def supportsMessages():
    pass

  def toolTip():
    pass

class QTabBar(QWidget):

  class ButtonPosition(object):

    LeftSide = None
    RightSide = None
    name = property(None, None, None,
                    )

    values = {}

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  LeftSide = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  RightSide = None
  RoundedEast = None
  RoundedNorth = None
  RoundedSouth = None
  RoundedWest = None
  SelectLeftTab = None
  SelectPreviousTab = None
  SelectRightTab = None

  class SelectionBehavior(object):

    SelectLeftTab = None
    SelectPreviousTab = None
    SelectRightTab = None
    name = property(None, None, None,
                    )

    values = {}

  class Shape(object):

    RoundedEast = None
    RoundedNorth = None
    RoundedSouth = None
    RoundedWest = None
    TriangularEast = None
    TriangularNorth = None
    TriangularSouth = None
    TriangularWest = None
    name = property(None, None, None,
                    )

    values = {}

  TriangularEast = None
  TriangularNorth = None
  TriangularSouth = None
  TriangularWest = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addTab():
    pass

  def changeEvent():
    pass

  def connect():
    pass

  def count():
    pass

  def currentChanged():
    """ Signal """
    pass

  def currentIndex():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def documentMode():
    pass

  def drawBase():
    pass

  def elideMode():
    pass

  def event():
    pass

  def expanding():
    pass

  def hideEvent():
    pass

  def iconSize():
    pass

  def initStyleOption():
    pass

  def insertTab():
    pass

  def isMovable():
    pass

  def isTabEnabled():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveTab():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def removeTab():
    pass

  def resizeEvent():
    pass

  def selected():
    """ Signal """
    pass

  def selectionBehaviorOnRemove():
    pass

  def setCurrentIndex():
    pass

  def setDocumentMode():
    pass

  def setDrawBase():
    pass

  def setElideMode():
    pass

  def setExpanding():
    pass

  def setIconSize():
    pass

  def setMovable():
    pass

  def setSelectionBehaviorOnRemove():
    pass

  def setShape():
    pass

  def setTabButton():
    pass

  def setTabData():
    pass

  def setTabEnabled():
    pass

  def setTabIcon():
    pass

  def setTabOrder():
    pass

  def setTabText():
    pass

  def setTabTextColor():
    pass

  def setTabToolTip():
    pass

  def setTabWhatsThis():
    pass

  def setTabsClosable():
    pass

  def setUsesScrollButtons():
    pass

  def shape():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def tabAt():
    pass

  def tabButton():
    pass

  def tabCloseRequested():
    """ Signal """
    pass

  def tabData():
    pass

  def tabIcon():
    pass

  def tabInserted():
    pass

  def tabLayoutChange():
    pass

  def tabMoved():
    """ Signal """
    pass

  def tabRect():
    pass

  def tabRemoved():
    pass

  def tabSizeHint():
    pass

  def tabText():
    pass

  def tabTextColor():
    pass

  def tabToolTip():
    pass

  def tabWhatsThis():
    pass

  def tabsClosable():
    pass

  def usesScrollButtons():
    pass

  def wheelEvent():
    pass

class QTabWidget(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  East = None
  IgnoreMask = None
  North = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rounded = None
  South = None

  class TabPosition(object):

    East = None
    North = None
    South = None
    West = None
    name = property(None, None, None,
                    )

    values = {}

  class TabShape(object):

    Rounded = None
    Triangular = None
    name = property(None, None, None,
                    )

    values = {}

  Triangular = None
  West = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addTab():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def connect():
    pass

  def cornerWidget():
    pass

  def count():
    pass

  def currentChanged():
    """ Signal """
    pass

  def currentIndex():
    pass

  def currentWidget():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def documentMode():
    pass

  def elideMode():
    pass

  def event():
    pass

  def heightForWidth():
    pass

  def iconSize():
    pass

  def indexOf():
    pass

  def initStyleOption():
    pass

  def insertTab():
    pass

  def isMovable():
    pass

  def isTabEnabled():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def removeTab():
    pass

  def resizeEvent():
    pass

  def selected():
    """ Signal """
    pass

  def setCornerWidget():
    pass

  def setCurrentIndex():
    pass

  def setCurrentWidget():
    pass

  def setDocumentMode():
    pass

  def setElideMode():
    pass

  def setIconSize():
    pass

  def setMovable():
    pass

  def setTabBar():
    pass

  def setTabEnabled():
    pass

  def setTabIcon():
    pass

  def setTabOrder():
    pass

  def setTabPosition():
    pass

  def setTabShape():
    pass

  def setTabText():
    pass

  def setTabToolTip():
    pass

  def setTabWhatsThis():
    pass

  def setTabsClosable():
    pass

  def setUsesScrollButtons():
    pass

  def showEvent():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def tabBar():
    pass

  def tabCloseRequested():
    """ Signal """
    pass

  def tabIcon():
    pass

  def tabInserted():
    pass

  def tabPosition():
    pass

  def tabRemoved():
    pass

  def tabShape():
    pass

  def tabText():
    pass

  def tabToolTip():
    pass

  def tabWhatsThis():
    pass

  def tabsClosable():
    pass

  def usesScrollButtons():
    pass

  def widget():
    pass

class QTableView(QAbstractItemView):

  AboveItem = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  HLine = None
  IgnoreMask = None
  InternalMove = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SingleSelection = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def clearSpans():
    pass

  def clicked():
    """ Signal """
    pass

  def columnAt():
    pass

  def columnCountChanged():
    pass

  def columnMoved():
    pass

  def columnResized():
    pass

  def columnSpan():
    pass

  def columnViewportPosition():
    pass

  def columnWidth():
    pass

  def connect():
    pass

  def currentChanged():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doItemsLayout():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def entered():
    """ Signal """
    pass

  def gridStyle():
    pass

  def hideColumn():
    pass

  def hideRow():
    pass

  def horizontalHeader():
    pass

  def horizontalOffset():
    pass

  def horizontalScrollbarAction():
    pass

  def indexAt():
    pass

  def isColumnHidden():
    pass

  def isCornerButtonEnabled():
    pass

  def isIndexHidden():
    pass

  def isRowHidden():
    pass

  def isSortingEnabled():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def moveCursor():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def resizeColumnToContents():
    pass

  def resizeColumnsToContents():
    pass

  def resizeRowToContents():
    pass

  def resizeRowsToContents():
    pass

  def rowAt():
    pass

  def rowCountChanged():
    pass

  def rowHeight():
    pass

  def rowMoved():
    pass

  def rowResized():
    pass

  def rowSpan():
    pass

  def rowViewportPosition():
    pass

  def scrollContentsBy():
    pass

  def scrollTo():
    pass

  def selectColumn():
    pass

  def selectRow():
    pass

  def selectedIndexes():
    pass

  def selectionChanged():
    pass

  def setColumnHidden():
    pass

  def setColumnWidth():
    pass

  def setCornerButtonEnabled():
    pass

  def setGridStyle():
    pass

  def setHorizontalHeader():
    pass

  def setModel():
    pass

  def setRootIndex():
    pass

  def setRowHeight():
    pass

  def setRowHidden():
    pass

  def setSelection():
    pass

  def setSelectionModel():
    pass

  def setShowGrid():
    pass

  def setSortingEnabled():
    pass

  def setSpan():
    pass

  def setTabOrder():
    pass

  def setVerticalHeader():
    pass

  def setWordWrap():
    pass

  def showColumn():
    pass

  def showGrid():
    pass

  def showRow():
    pass

  def sizeHintForColumn():
    pass

  def sizeHintForRow():
    pass

  def sortByColumn():
    pass

  staticMetaObject = None

  def timerEvent():
    pass

  def updateGeometries():
    pass

  def verticalHeader():
    pass

  def verticalOffset():
    pass

  def verticalScrollbarAction():
    pass

  def viewOptions():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def visualRect():
    pass

  def visualRegionForSelection():
    pass

  def wordWrap():
    pass

class QTableWidget(QTableView):

  AboveItem = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  HLine = None
  IgnoreMask = None
  InternalMove = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SingleSelection = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def cellActivated():
    """ Signal """
    pass

  def cellChanged():
    """ Signal """
    pass

  def cellClicked():
    """ Signal """
    pass

  def cellDoubleClicked():
    """ Signal """
    pass

  def cellEntered():
    """ Signal """
    pass

  def cellPressed():
    """ Signal """
    pass

  def cellWidget():
    pass

  def clear():
    pass

  def clearContents():
    pass

  def clicked():
    """ Signal """
    pass

  def closePersistentEditor():
    pass

  def column():
    pass

  def columnCount():
    pass

  def connect():
    pass

  def currentCellChanged():
    """ Signal """
    pass

  def currentColumn():
    pass

  def currentItem():
    pass

  def currentItemChanged():
    """ Signal """
    pass

  def currentRow():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def dropEvent():
    pass

  def dropMimeData():
    pass

  def editItem():
    pass

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def findItems():
    pass

  def horizontalHeaderItem():
    pass

  def indexFromItem():
    pass

  def insertColumn():
    pass

  def insertRow():
    pass

  def isSortingEnabled():
    pass

  def item():
    pass

  def itemActivated():
    """ Signal """
    pass

  def itemAt():
    pass

  def itemChanged():
    """ Signal """
    pass

  def itemClicked():
    """ Signal """
    pass

  def itemDoubleClicked():
    """ Signal """
    pass

  def itemEntered():
    """ Signal """
    pass

  def itemFromIndex():
    pass

  def itemPressed():
    """ Signal """
    pass

  def itemPrototype():
    pass

  def itemSelectionChanged():
    """ Signal """
    pass

  def items():
    pass

  def keyboardGrabber():
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def mouseGrabber():
    pass

  def openPersistentEditor():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeCellWidget():
    pass

  def removeColumn():
    pass

  def removeRow():
    pass

  def row():
    pass

  def rowCount():
    pass

  def scrollToItem():
    pass

  def selectedItems():
    pass

  def selectedRanges():
    pass

  def setCellWidget():
    pass

  def setColumnCount():
    pass

  def setCurrentCell():
    pass

  def setCurrentItem():
    pass

  def setHorizontalHeaderItem():
    pass

  def setHorizontalHeaderLabels():
    pass

  def setItem():
    pass

  def setItemPrototype():
    pass

  def setModel():
    pass

  def setRangeSelected():
    pass

  def setRowCount():
    pass

  def setSortingEnabled():
    pass

  def setTabOrder():
    pass

  def setVerticalHeaderItem():
    pass

  def setVerticalHeaderLabels():
    pass

  def sortItems():
    pass

  staticMetaObject = None

  def supportedDropActions():
    pass

  def takeHorizontalHeaderItem():
    pass

  def takeItem():
    pass

  def takeVerticalHeaderItem():
    pass

  def verticalHeaderItem():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def visualColumn():
    pass

  def visualItemRect():
    pass

  def visualRow():
    pass

class QTableWidgetItem(Object):

  class ItemType(object):

    Type = None
    UserType = None
    name = property(None, None, None,
                    )

    values = {}

  Type = None
  UserType = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def background():
    pass

  def checkState():
    pass

  def clone():
    pass

  def column():
    pass

  def data():
    pass

  def flags():
    pass

  def font():
    pass

  def foreground():
    pass

  def icon():
    pass

  def isSelected():
    pass

  def read():
    pass

  def row():
    pass

  def setBackground():
    pass

  def setCheckState():
    pass

  def setData():
    pass

  def setFlags():
    pass

  def setFont():
    pass

  def setForeground():
    pass

  def setIcon():
    pass

  def setSelected():
    pass

  def setSizeHint():
    pass

  def setStatusTip():
    pass

  def setText():
    pass

  def setTextAlignment():
    pass

  def setToolTip():
    pass

  def setWhatsThis():
    pass

  def sizeHint():
    pass

  def statusTip():
    pass

  def tableWidget():
    pass

  def text():
    pass

  def textAlignment():
    pass

  def toolTip():
    pass

  def type():
    pass

  def whatsThis():
    pass

  def write():
    pass

class QTableWidgetSelectionRange(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bottomRow():
    pass

  def columnCount():
    pass

  def leftColumn():
    pass

  def rightColumn():
    pass

  def rowCount():
    pass

  def topRow():
    pass

class QTapAndHoldGesture(QGesture):

  CancelAllInContext = None
  CancelNone = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def position():
    pass

  def registerUserData():
    pass

  def setPosition():
    pass

  def setTimeout():
    pass

  staticMetaObject = None

  def timeout():
    pass

class QTapGesture(QGesture):

  CancelAllInContext = None
  CancelNone = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def position():
    pass

  def registerUserData():
    pass

  def setPosition():
    pass

  staticMetaObject = None

class QTextBrowser(QTextEdit):

  AutoAll = None
  AutoBulletList = None

  class AutoFormatting(object):

    pass

  class AutoFormattingFlag(object):

    AutoAll = None
    AutoBulletList = None
    AutoNone = None
    name = property(None, None, None,
                    )

    values = {}

  AutoNone = None
  Box = None
  DrawChildren = None
  DrawWindowBackground = None

  class ExtraSelection(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    cursor = property(None, None, None,
                      )

    format = property(None, None, None,
                      )


  FixedColumnWidth = None
  FixedPixelWidth = None
  HLine = None
  IgnoreMask = None

  class LineWrapMode(object):

    FixedColumnWidth = None
    FixedPixelWidth = None
    NoWrap = None
    WidgetWidth = None
    name = property(None, None, None,
                    )

    values = {}

  NoFrame = None
  NoWrap = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WidgetWidth = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def anchorClicked():
    """ Signal """
    pass

  def backward():
    pass

  def backwardAvailable():
    """ Signal """
    pass

  def backwardHistoryCount():
    pass

  def clearHistory():
    pass

  def connect():
    pass

  def copyAvailable():
    """ Signal """
    pass

  def currentCharFormatChanged():
    """ Signal """
    pass

  def currentColorChanged():
    """ Signal """
    pass

  def currentFontChanged():
    """ Signal """
    pass

  def cursorPositionChanged():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def forward():
    pass

  def forwardAvailable():
    """ Signal """
    pass

  def forwardHistoryCount():
    pass

  def highlighted():
    """ Signal """
    pass

  def historyChanged():
    """ Signal """
    pass

  def historyTitle():
    pass

  def historyUrl():
    pass

  def home():
    pass

  def isBackwardAvailable():
    pass

  def isForwardAvailable():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def loadResource():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def openExternalLinks():
    pass

  def openLinks():
    pass

  def paintEvent():
    pass

  def redoAvailable():
    """ Signal """
    pass

  def registerUserData():
    pass

  def reload():
    pass

  def searchPaths():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def setOpenExternalLinks():
    pass

  def setOpenLinks():
    pass

  def setSearchPaths():
    pass

  def setSource():
    pass

  def setTabOrder():
    pass

  def source():
    pass

  def sourceChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def textChanged():
    """ Signal """
    pass

  def undoAvailable():
    """ Signal """
    pass

class QTextEdit(QAbstractScrollArea):

  AutoAll = None
  AutoBulletList = None
  AutoNone = None
  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  FixedColumnWidth = None
  FixedPixelWidth = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  NoWrap = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WidgetWidth = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def acceptRichText():
    pass

  def alignment():
    pass

  def anchorAt():
    pass

  def append():
    pass

  def autoFormatting():
    pass

  def canInsertFromMimeData():
    pass

  def canPaste():
    pass

  def changeEvent():
    pass

  def clear():
    pass

  def connect():
    pass

  def contextMenuEvent():
    pass

  def copy():
    pass

  def copyAvailable():
    """ Signal """
    pass

  def createMimeDataFromSelection():
    pass

  def createStandardContextMenu():
    pass

  def currentCharFormat():
    pass

  def currentCharFormatChanged():
    """ Signal """
    pass

  def currentColorChanged():
    """ Signal """
    pass

  def currentFont():
    pass

  def currentFontChanged():
    """ Signal """
    pass

  def cursorForPosition():
    pass

  def cursorPositionChanged():
    """ Signal """
    pass

  def cursorRect():
    pass

  def cursorWidth():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def cut():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def document():
    pass

  def documentTitle():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def ensureCursorVisible():
    pass

  def event():
    pass

  def extraSelections():
    pass

  def find():
    pass

  def focusInEvent():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def fontFamily():
    pass

  def fontItalic():
    pass

  def fontPointSize():
    pass

  def fontUnderline():
    pass

  def fontWeight():
    pass

  def inputMethodEvent():
    pass

  def inputMethodQuery():
    pass

  def insertFromMimeData():
    pass

  def insertHtml():
    pass

  def insertPlainText():
    pass

  def isReadOnly():
    pass

  def isUndoRedoEnabled():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def keyboardGrabber():
    pass

  def lineWrapColumnOrWidth():
    pass

  def lineWrapMode():
    pass

  def loadResource():
    pass

  def mergeCurrentCharFormat():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveCursor():
    pass

  def overwriteMode():
    pass

  def paintEvent():
    pass

  def paste():
    pass

  def print_():
    pass

  def redo():
    pass

  def redoAvailable():
    """ Signal """
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def scrollContentsBy():
    pass

  def scrollToAnchor():
    pass

  def selectAll():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def setAcceptRichText():
    pass

  def setAlignment():
    pass

  def setAutoFormatting():
    pass

  def setCurrentCharFormat():
    pass

  def setCurrentFont():
    pass

  def setCursorWidth():
    pass

  def setDocument():
    pass

  def setDocumentTitle():
    pass

  def setExtraSelections():
    pass

  def setFontFamily():
    pass

  def setFontItalic():
    pass

  def setFontPointSize():
    pass

  def setFontUnderline():
    pass

  def setFontWeight():
    pass

  def setHtml():
    pass

  def setLineWrapColumnOrWidth():
    pass

  def setLineWrapMode():
    pass

  def setOverwriteMode():
    pass

  def setPlainText():
    pass

  def setReadOnly():
    pass

  def setTabChangesFocus():
    pass

  def setTabOrder():
    pass

  def setTabStopWidth():
    pass

  def setText():
    pass

  def setTextBackgroundColor():
    pass

  def setTextColor():
    pass

  def setTextCursor():
    pass

  def setTextInteractionFlags():
    pass

  def setUndoRedoEnabled():
    pass

  def setWordWrapMode():
    pass

  def showEvent():
    pass

  staticMetaObject = None

  def tabChangesFocus():
    pass

  def tabStopWidth():
    pass

  def textBackgroundColor():
    pass

  def textChanged():
    """ Signal """
    pass

  def textColor():
    pass

  def textCursor():
    pass

  def textInteractionFlags():
    pass

  def timerEvent():
    pass

  def toHtml():
    pass

  def toPlainText():
    pass

  def undo():
    pass

  def undoAvailable():
    """ Signal """
    pass

  def wheelEvent():
    pass

  def wordWrapMode():
    pass

  def zoomIn():
    pass

  def zoomOut():
    pass

class QTimeEdit(QDateTimeEdit):

  AmPmSection = None
  CorrectToNearestValue = None
  CorrectToPreviousValue = None
  DateSections_Mask = None
  DaySection = None
  DrawChildren = None
  DrawWindowBackground = None
  HourSection = None
  IgnoreMask = None
  MSecSection = None
  MinuteSection = None
  MonthSection = None
  NoButtons = None
  NoSection = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  PlusMinus = None
  SecondSection = None
  StepDownEnabled = None
  StepNone = None
  StepUpEnabled = None
  TimeSections_Mask = None
  UpDownArrows = None
  YearSection = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def dateChanged():
    """ Signal """
    pass

  def dateTimeChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editingFinished():
    """ Signal """
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def timeChanged():
    """ Signal """
    pass

class QToolBar(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionAt():
    pass

  def actionEvent():
    pass

  def actionGeometry():
    pass

  def actionTriggered():
    """ Signal """
    pass

  def addAction():
    pass

  def addSeparator():
    pass

  def addWidget():
    pass

  def allowedAreas():
    pass

  def allowedAreasChanged():
    """ Signal """
    pass

  def changeEvent():
    pass

  def childEvent():
    pass

  def clear():
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def iconSize():
    pass

  def iconSizeChanged():
    """ Signal """
    pass

  def initStyleOption():
    pass

  def insertSeparator():
    pass

  def insertWidget():
    pass

  def isAreaAllowed():
    pass

  def isFloatable():
    pass

  def isFloating():
    pass

  def isMovable():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def movableChanged():
    """ Signal """
    pass

  def orientation():
    pass

  def orientationChanged():
    """ Signal """
    pass

  def paintEvent():
    pass

  def registerUserData():
    pass

  def resizeEvent():
    pass

  def setAllowedAreas():
    pass

  def setFloatable():
    pass

  def setIconSize():
    pass

  def setMovable():
    pass

  def setOrientation():
    pass

  def setTabOrder():
    pass

  def setToolButtonStyle():
    pass

  staticMetaObject = None

  def toggleViewAction():
    pass

  def toolButtonStyle():
    pass

  def toolButtonStyleChanged():
    """ Signal """
    pass

  def topLevelChanged():
    """ Signal """
    pass

  def visibilityChanged():
    """ Signal """
    pass

  def widgetForAction():
    pass

class QToolBox(QFrame):

  Box = None
  DrawChildren = None
  DrawWindowBackground = None
  HLine = None
  IgnoreMask = None
  NoFrame = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  Raised = None
  Shadow_Mask = None
  Shape_Mask = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addItem():
    pass

  def changeEvent():
    pass

  def connect():
    pass

  def count():
    pass

  def currentChanged():
    """ Signal """
    pass

  def currentIndex():
    pass

  def currentWidget():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def indexOf():
    pass

  def insertItem():
    pass

  def isItemEnabled():
    pass

  def itemIcon():
    pass

  def itemInserted():
    pass

  def itemRemoved():
    pass

  def itemText():
    pass

  def itemToolTip():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def removeItem():
    pass

  def setCurrentIndex():
    pass

  def setCurrentWidget():
    pass

  def setItemEnabled():
    pass

  def setItemIcon():
    pass

  def setItemText():
    pass

  def setItemToolTip():
    pass

  def setTabOrder():
    pass

  def showEvent():
    pass

  staticMetaObject = None

  def widget():
    pass

class QToolButton(QAbstractButton):

  DelayedPopup = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  InstantPopup = None
  MenuButtonPopup = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  class ToolButtonPopupMode(object):

    DelayedPopup = None
    InstantPopup = None
    MenuButtonPopup = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionEvent():
    pass

  def arrowType():
    pass

  def autoRaise():
    pass

  def changeEvent():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def defaultAction():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def enterEvent():
    pass

  def event():
    pass

  def hitButton():
    pass

  def initStyleOption():
    pass

  def keyboardGrabber():
    pass

  def leaveEvent():
    pass

  def menu():
    pass

  def minimumSizeHint():
    pass

  def mouseGrabber():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def nextCheckState():
    pass

  def paintEvent():
    pass

  def popupMode():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def released():
    """ Signal """
    pass

  def setArrowType():
    pass

  def setAutoRaise():
    pass

  def setDefaultAction():
    pass

  def setMenu():
    pass

  def setPopupMode():
    pass

  def setTabOrder():
    pass

  def setToolButtonStyle():
    pass

  def showMenu():
    pass

  def sizeHint():
    pass

  staticMetaObject = None

  def timerEvent():
    pass

  def toggled():
    """ Signal """
    pass

  def toolButtonStyle():
    pass

  def triggered():
    """ Signal """
    pass

class QToolTip(Object):

  def font():
    pass

  def hideText():
    pass

  def isVisible():
    pass

  def palette():
    pass

  def setFont():
    pass

  def setPalette():
    pass

  def showText():
    pass

  def text():
    pass

class QTreeView(QAbstractItemView):

  AboveItem = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  HLine = None
  IgnoreMask = None
  InternalMove = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SingleSelection = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def allColumnsShowFocus():
    pass

  def autoExpandDelay():
    pass

  def clicked():
    """ Signal """
    pass

  def collapse():
    pass

  def collapseAll():
    pass

  def collapsed():
    """ Signal """
    pass

  def columnAt():
    pass

  def columnCountChanged():
    pass

  def columnMoved():
    pass

  def columnResized():
    pass

  def columnViewportPosition():
    pass

  def columnWidth():
    pass

  def connect():
    pass

  def currentChanged():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def dataChanged():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doItemsLayout():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def dragMoveEvent():
    pass

  def drawBranches():
    pass

  def drawRow():
    pass

  def drawTree():
    pass

  def entered():
    """ Signal """
    pass

  def expand():
    pass

  def expandAll():
    pass

  def expandToDepth():
    pass

  def expanded():
    """ Signal """
    pass

  def expandsOnDoubleClick():
    pass

  def header():
    pass

  def hideColumn():
    pass

  def horizontalOffset():
    pass

  def horizontalScrollbarAction():
    pass

  def indentation():
    pass

  def indexAbove():
    pass

  def indexAt():
    pass

  def indexBelow():
    pass

  def indexRowSizeHint():
    pass

  def isAnimated():
    pass

  def isColumnHidden():
    pass

  def isExpanded():
    pass

  def isFirstColumnSpanned():
    pass

  def isHeaderHidden():
    pass

  def isIndexHidden():
    pass

  def isRowHidden():
    pass

  def isSortingEnabled():
    pass

  def itemsExpandable():
    pass

  def keyPressEvent():
    pass

  def keyboardGrabber():
    pass

  def keyboardSearch():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def moveCursor():
    pass

  def paintEvent():
    pass

  def pressed():
    """ Signal """
    pass

  def reexpand():
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def resizeColumnToContents():
    pass

  def rootIsDecorated():
    pass

  def rowHeight():
    pass

  def rowsAboutToBeRemoved():
    pass

  def rowsInserted():
    pass

  def rowsRemoved():
    pass

  def scrollContentsBy():
    pass

  def scrollTo():
    pass

  def selectAll():
    pass

  def selectedIndexes():
    pass

  def selectionChanged():
    pass

  def setAllColumnsShowFocus():
    pass

  def setAnimated():
    pass

  def setAutoExpandDelay():
    pass

  def setColumnHidden():
    pass

  def setColumnWidth():
    pass

  def setExpanded():
    pass

  def setExpandsOnDoubleClick():
    pass

  def setFirstColumnSpanned():
    pass

  def setHeader():
    pass

  def setHeaderHidden():
    pass

  def setIndentation():
    pass

  def setItemsExpandable():
    pass

  def setModel():
    pass

  def setRootIndex():
    pass

  def setRootIsDecorated():
    pass

  def setRowHidden():
    pass

  def setSelection():
    pass

  def setSelectionModel():
    pass

  def setSortingEnabled():
    pass

  def setTabOrder():
    pass

  def setUniformRowHeights():
    pass

  def setWordWrap():
    pass

  def showColumn():
    pass

  def sizeHintForColumn():
    pass

  def sortByColumn():
    pass

  staticMetaObject = None

  def timerEvent():
    pass

  def uniformRowHeights():
    pass

  def updateGeometries():
    pass

  def verticalOffset():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def viewportEvent():
    pass

  def visualRect():
    pass

  def visualRegionForSelection():
    pass

  def wordWrap():
    pass

class QTreeWidget(QTreeView):

  AboveItem = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  HLine = None
  IgnoreMask = None
  InternalMove = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SingleSelection = None
  StyledPanel = None
  Sunken = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def addTopLevelItem():
    pass

  def addTopLevelItems():
    pass

  def clear():
    pass

  def clicked():
    """ Signal """
    pass

  def closePersistentEditor():
    pass

  def collapseItem():
    pass

  def collapsed():
    """ Signal """
    pass

  def columnCount():
    pass

  def connect():
    pass

  def currentColumn():
    pass

  def currentItem():
    pass

  def currentItemChanged():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def dropEvent():
    pass

  def dropMimeData():
    pass

  def editItem():
    pass

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def expandItem():
    pass

  def expanded():
    """ Signal """
    pass

  def findItems():
    pass

  def headerItem():
    pass

  def indexFromItem():
    pass

  def indexOfTopLevelItem():
    pass

  def insertTopLevelItem():
    pass

  def insertTopLevelItems():
    pass

  def invisibleRootItem():
    pass

  def isFirstItemColumnSpanned():
    pass

  def isItemExpanded():
    pass

  def isItemHidden():
    pass

  def isItemSelected():
    pass

  def isSortingEnabled():
    pass

  def itemAbove():
    pass

  def itemActivated():
    """ Signal """
    pass

  def itemAt():
    pass

  def itemBelow():
    pass

  def itemChanged():
    """ Signal """
    pass

  def itemClicked():
    """ Signal """
    pass

  def itemCollapsed():
    """ Signal """
    pass

  def itemDoubleClicked():
    """ Signal """
    pass

  def itemEntered():
    """ Signal """
    pass

  def itemExpanded():
    """ Signal """
    pass

  def itemFromIndex():
    pass

  def itemPressed():
    """ Signal """
    pass

  def itemSelectionChanged():
    """ Signal """
    pass

  def itemWidget():
    pass

  def keyboardGrabber():
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def mouseGrabber():
    pass

  def openPersistentEditor():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeItemWidget():
    pass

  def scrollToItem():
    pass

  def selectedItems():
    pass

  def setColumnCount():
    pass

  def setCurrentItem():
    pass

  def setFirstItemColumnSpanned():
    pass

  def setHeaderItem():
    pass

  def setHeaderLabel():
    pass

  def setHeaderLabels():
    pass

  def setItemExpanded():
    pass

  def setItemHidden():
    pass

  def setItemSelected():
    pass

  def setItemWidget():
    pass

  def setModel():
    pass

  def setSelectionModel():
    pass

  def setSortingEnabled():
    pass

  def setTabOrder():
    pass

  def sortColumn():
    pass

  def sortItems():
    pass

  staticMetaObject = None

  def supportedDropActions():
    pass

  def takeTopLevelItem():
    pass

  def topLevelItem():
    pass

  def topLevelItemCount():
    pass

  def viewportEntered():
    """ Signal """
    pass

  def visualItemRect():
    pass

class QTreeWidgetItem(Object):

  class ChildIndicatorPolicy(object):

    DontShowIndicator = None
    DontShowIndicatorWhenChildless = None
    ShowIndicator = None
    name = property(None, None, None,
                    )

    values = {}

  DontShowIndicator = None
  DontShowIndicatorWhenChildless = None

  class ItemType(object):

    Type = None
    UserType = None
    name = property(None, None, None,
                    )

    values = {}

  ShowIndicator = None
  Type = None
  UserType = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addChild():
    pass

  def addChildren():
    pass

  def background():
    pass

  def checkState():
    pass

  def child():
    pass

  def childCount():
    pass

  def childIndicatorPolicy():
    pass

  def clone():
    pass

  def columnCount():
    pass

  def data():
    pass

  def emitDataChanged():
    pass

  def flags():
    pass

  def font():
    pass

  def foreground():
    pass

  def icon():
    pass

  def indexOfChild():
    pass

  def insertChild():
    pass

  def insertChildren():
    pass

  def isDisabled():
    pass

  def isExpanded():
    pass

  def isFirstColumnSpanned():
    pass

  def isHidden():
    pass

  def isSelected():
    pass

  def parent():
    pass

  def read():
    pass

  def removeChild():
    pass

  def setBackground():
    pass

  def setCheckState():
    pass

  def setChildIndicatorPolicy():
    pass

  def setData():
    pass

  def setDisabled():
    pass

  def setExpanded():
    pass

  def setFirstColumnSpanned():
    pass

  def setFlags():
    pass

  def setFont():
    pass

  def setForeground():
    pass

  def setHidden():
    pass

  def setIcon():
    pass

  def setSelected():
    pass

  def setSizeHint():
    pass

  def setStatusTip():
    pass

  def setText():
    pass

  def setTextAlignment():
    pass

  def setToolTip():
    pass

  def setWhatsThis():
    pass

  def sizeHint():
    pass

  def sortChildren():
    pass

  def statusTip():
    pass

  def takeChild():
    pass

  def takeChildren():
    pass

  def text():
    pass

  def textAlignment():
    pass

  def toolTip():
    pass

  def treeWidget():
    pass

  def type():
    pass

  def whatsThis():
    pass

  def write():
    pass

class QTreeWidgetItemIterator(Object):

  All = None
  Checked = None
  Disabled = None
  DragDisabled = None
  DragEnabled = None
  DropDisabled = None
  DropEnabled = None
  Editable = None
  Enabled = None
  HasChildren = None
  Hidden = None

  class IteratorFlag(object):

    All = None
    Checked = None
    Disabled = None
    DragDisabled = None
    DragEnabled = None
    DropDisabled = None
    DropEnabled = None
    Editable = None
    Enabled = None
    HasChildren = None
    Hidden = None
    NoChildren = None
    NotChecked = None
    NotEditable = None
    NotHidden = None
    NotSelectable = None
    Selectable = None
    Selected = None
    Unselected = None
    UserFlag = None
    name = property(None, None, None,
                    )

    values = {}

  class IteratorFlags(object):

    pass

  NoChildren = None
  NotChecked = None
  NotEditable = None
  NotHidden = None
  NotSelectable = None
  Selectable = None
  Selected = None
  Unselected = None
  UserFlag = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def next():
    """ x.next() -> the next value, or raise StopIteration """
    return None

  def value():
    pass

class QUndoCommand(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionText():
    pass

  def child():
    pass

  def childCount():
    pass

  def id():
    pass

  def mergeWith():
    pass

  def redo():
    pass

  def setText():
    pass

  def text():
    pass

  def undo():
    pass

class QUndoGroup(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activeStack():
    pass

  def activeStackChanged():
    """ Signal """
    pass

  def addStack():
    pass

  def canRedo():
    pass

  def canRedoChanged():
    """ Signal """
    pass

  def canUndo():
    pass

  def canUndoChanged():
    """ Signal """
    pass

  def cleanChanged():
    """ Signal """
    pass

  def connect():
    pass

  def createRedoAction():
    pass

  def createUndoAction():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def indexChanged():
    """ Signal """
    pass

  def isClean():
    pass

  def redo():
    pass

  def redoText():
    pass

  def redoTextChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeStack():
    pass

  def setActiveStack():
    pass

  def stacks():
    pass

  staticMetaObject = None

  def undo():
    pass

  def undoText():
    pass

  def undoTextChanged():
    """ Signal """
    pass

class QUndoStack(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def beginMacro():
    pass

  def canRedo():
    pass

  def canRedoChanged():
    """ Signal """
    pass

  def canUndo():
    pass

  def canUndoChanged():
    """ Signal """
    pass

  def cleanChanged():
    """ Signal """
    pass

  def cleanIndex():
    pass

  def clear():
    pass

  def command():
    pass

  def connect():
    pass

  def count():
    pass

  def createRedoAction():
    pass

  def createUndoAction():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def endMacro():
    pass

  def index():
    pass

  def indexChanged():
    """ Signal """
    pass

  def isActive():
    pass

  def isClean():
    pass

  def push():
    pass

  def redo():
    pass

  def redoText():
    pass

  def redoTextChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setActive():
    pass

  def setClean():
    pass

  def setIndex():
    pass

  def setUndoLimit():
    pass

  staticMetaObject = None

  def text():
    pass

  def undo():
    pass

  def undoLimit():
    pass

  def undoText():
    pass

  def undoTextChanged():
    """ Signal """
    pass

class QUndoView(QListView):

  AboveItem = None
  Adjust = None
  AllEditTriggers = None
  AnimatingState = None
  AnyKeyPressed = None
  Batched = None
  BelowItem = None
  Box = None
  CollapsingState = None
  ContiguousSelection = None
  CurrentChanged = None
  DoubleClicked = None
  DragDrop = None
  DragOnly = None
  DragSelectingState = None
  DraggingState = None
  DrawChildren = None
  DrawWindowBackground = None
  DropOnly = None
  EditKeyPressed = None
  EditingState = None
  EnsureVisible = None
  ExpandingState = None
  ExtendedSelection = None
  Fixed = None
  Free = None
  HLine = None
  IconMode = None
  IgnoreMask = None
  InternalMove = None
  LeftToRight = None
  ListMode = None
  MoveDown = None
  MoveEnd = None
  MoveHome = None
  MoveLeft = None
  MoveNext = None
  MovePageDown = None
  MovePageUp = None
  MovePrevious = None
  MoveRight = None
  MoveUp = None
  MultiSelection = None
  NoDragDrop = None
  NoEditTriggers = None
  NoFrame = None
  NoSelection = None
  NoState = None
  OnItem = None
  OnViewport = None
  Panel = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Plain = None
  PositionAtBottom = None
  PositionAtCenter = None
  PositionAtTop = None
  Raised = None
  ScrollPerItem = None
  ScrollPerPixel = None
  SelectColumns = None
  SelectItems = None
  SelectRows = None
  SelectedClicked = None
  Shadow_Mask = None
  Shape_Mask = None
  SinglePass = None
  SingleSelection = None
  Snap = None
  Static = None
  StyledPanel = None
  Sunken = None
  TopToBottom = None
  VLine = None
  WinPanel = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def cleanIcon():
    pass

  def clicked():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doubleClicked():
    """ Signal """
    pass

  def emptyLabel():
    pass

  def entered():
    """ Signal """
    pass

  def group():
    pass

  def indexesMoved():
    """ Signal """
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setCleanIcon():
    pass

  def setEmptyLabel():
    pass

  def setGroup():
    pass

  def setStack():
    pass

  def setTabOrder():
    pass

  def stack():
    pass

  staticMetaObject = None

  def viewportEntered():
    """ Signal """
    pass

class QVBoxLayout(QBoxLayout):

  BottomToTop = None
  Down = None
  LeftToRight = None
  RightToLeft = None
  SetDefaultConstraint = None
  SetFixedSize = None
  SetMaximumSize = None
  SetMinAndMaxSize = None
  SetMinimumSize = None
  SetNoConstraint = None
  TopToBottom = None
  Up = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def closestAcceptableSize():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

class QWhatsThis(Object):

  def createAction():
    pass

  def enterWhatsThisMode():
    pass

  def hideText():
    pass

  def inWhatsThisMode():
    pass

  def leaveWhatsThisMode():
    pass

  def showText():
    pass

class QWidget(QObject):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def acceptDrops():
    pass

  def accessibleDescription():
    pass

  def accessibleName():
    pass

  def actionEvent():
    pass

  def actions():
    pass

  def activateWindow():
    pass

  def addAction():
    pass

  def addActions():
    pass

  def adjustSize():
    pass

  def autoFillBackground():
    pass

  def backgroundRole():
    pass

  def baseSize():
    pass

  def changeEvent():
    pass

  def childAt():
    pass

  def childrenRect():
    pass

  def childrenRegion():
    pass

  def clearFocus():
    pass

  def clearMask():
    pass

  def close():
    pass

  def closeEvent():
    pass

  def connect():
    pass

  def contentsMargins():
    pass

  def contentsRect():
    pass

  def contextMenuEvent():
    pass

  def contextMenuPolicy():
    pass

  def createWinId():
    pass

  def cursor():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroy():
    pass

  def destroyed():
    """ Signal """
    pass

  def devType():
    pass

  def disconnect():
    pass

  def dragEnterEvent():
    pass

  def dragLeaveEvent():
    pass

  def dragMoveEvent():
    pass

  def dropEvent():
    pass

  def effectiveWinId():
    pass

  def ensurePolished():
    pass

  def enterEvent():
    pass

  def event():
    pass

  def focusInEvent():
    pass

  def focusNextChild():
    pass

  def focusNextPrevChild():
    pass

  def focusOutEvent():
    pass

  def focusPolicy():
    pass

  def focusPreviousChild():
    pass

  def focusProxy():
    pass

  def focusWidget():
    pass

  def font():
    pass

  def fontInfo():
    pass

  def fontMetrics():
    pass

  def foregroundRole():
    pass

  def frameGeometry():
    pass

  def frameSize():
    pass

  def geometry():
    pass

  def getContentsMargins():
    pass

  def grabGesture():
    pass

  def grabKeyboard():
    pass

  def grabMouse():
    pass

  def grabShortcut():
    pass

  def graphicsEffect():
    pass

  def graphicsProxyWidget():
    pass

  def hasFocus():
    pass

  def hasMouseTracking():
    pass

  def height():
    pass

  def heightForWidth():
    pass

  def hide():
    pass

  def hideEvent():
    pass

  def inputContext():
    pass

  def inputMethodEvent():
    pass

  def inputMethodHints():
    pass

  def inputMethodQuery():
    pass

  def insertAction():
    pass

  def insertActions():
    pass

  def isActiveWindow():
    pass

  def isAncestorOf():
    pass

  def isEnabled():
    pass

  def isEnabledTo():
    pass

  def isFullScreen():
    pass

  def isHidden():
    pass

  def isLeftToRight():
    pass

  def isMaximized():
    pass

  def isMinimized():
    pass

  def isModal():
    pass

  def isRightToLeft():
    pass

  def isVisible():
    pass

  def isVisibleTo():
    pass

  def isWindow():
    pass

  def isWindowModified():
    pass

  def keyPressEvent():
    pass

  def keyReleaseEvent():
    pass

  def keyboardGrabber():
    pass

  def languageChange():
    pass

  def layout():
    pass

  def layoutDirection():
    pass

  def leaveEvent():
    pass

  def locale():
    pass

  def lower():
    pass

  def mapFrom():
    pass

  def mapFromGlobal():
    pass

  def mapFromParent():
    pass

  def mapTo():
    pass

  def mapToGlobal():
    pass

  def mapToParent():
    pass

  def mask():
    pass

  def maximumHeight():
    pass

  def maximumSize():
    pass

  def maximumWidth():
    pass

  def metric():
    pass

  def minimumHeight():
    pass

  def minimumSize():
    pass

  def minimumSizeHint():
    pass

  def minimumWidth():
    pass

  def mouseDoubleClickEvent():
    pass

  def mouseGrabber():
    pass

  def mouseMoveEvent():
    pass

  def mousePressEvent():
    pass

  def mouseReleaseEvent():
    pass

  def move():
    pass

  def moveEvent():
    pass

  def nativeParentWidget():
    pass

  def nextInFocusChain():
    pass

  def normalGeometry():
    pass

  def overrideWindowFlags():
    pass

  def overrideWindowState():
    pass

  def paintEngine():
    pass

  def paintEvent():
    pass

  def palette():
    pass

  def parentWidget():
    pass

  def pos():
    pass

  def previousInFocusChain():
    pass

  def raise_():
    pass

  def rect():
    pass

  def registerUserData():
    pass

  def releaseKeyboard():
    pass

  def releaseMouse():
    pass

  def releaseShortcut():
    pass

  def removeAction():
    pass

  def render():
    pass

  def repaint():
    pass

  def resetInputContext():
    pass

  def resize():
    pass

  def resizeEvent():
    pass

  def restoreGeometry():
    pass

  def saveGeometry():
    pass

  def scroll():
    pass

  def setAcceptDrops():
    pass

  def setAccessibleDescription():
    pass

  def setAccessibleName():
    pass

  def setAttribute():
    pass

  def setAutoFillBackground():
    pass

  def setBackgroundRole():
    pass

  def setBaseSize():
    pass

  def setContentsMargins():
    pass

  def setContextMenuPolicy():
    pass

  def setCursor():
    pass

  def setDisabled():
    pass

  def setEnabled():
    pass

  def setFixedHeight():
    pass

  def setFixedSize():
    pass

  def setFixedWidth():
    pass

  def setFocus():
    pass

  def setFocusPolicy():
    pass

  def setFocusProxy():
    pass

  def setFont():
    pass

  def setForegroundRole():
    pass

  def setGeometry():
    pass

  def setGraphicsEffect():
    pass

  def setHidden():
    pass

  def setInputContext():
    pass

  def setInputMethodHints():
    pass

  def setLayout():
    pass

  def setLayoutDirection():
    pass

  def setLocale():
    pass

  def setMask():
    pass

  def setMaximumHeight():
    pass

  def setMaximumSize():
    pass

  def setMaximumWidth():
    pass

  def setMinimumHeight():
    pass

  def setMinimumSize():
    pass

  def setMinimumWidth():
    pass

  def setMouseTracking():
    pass

  def setPalette():
    pass

  def setParent():
    pass

  def setShortcutAutoRepeat():
    pass

  def setShortcutEnabled():
    pass

  def setSizeIncrement():
    pass

  def setSizePolicy():
    pass

  def setStatusTip():
    pass

  def setStyle():
    pass

  def setStyleSheet():
    pass

  def setTabOrder():
    pass

  def setToolTip():
    pass

  def setUpdatesEnabled():
    pass

  def setVisible():
    pass

  def setWhatsThis():
    pass

  def setWindowFilePath():
    pass

  def setWindowFlags():
    pass

  def setWindowIcon():
    pass

  def setWindowIconText():
    pass

  def setWindowModality():
    pass

  def setWindowModified():
    pass

  def setWindowOpacity():
    pass

  def setWindowRole():
    pass

  def setWindowState():
    pass

  def setWindowTitle():
    pass

  def show():
    pass

  def showEvent():
    pass

  def showFullScreen():
    pass

  def showMaximized():
    pass

  def showMinimized():
    pass

  def showNormal():
    pass

  def size():
    pass

  def sizeHint():
    pass

  def sizeIncrement():
    pass

  def sizePolicy():
    pass

  def stackUnder():
    pass

  staticMetaObject = None

  def statusTip():
    pass

  def style():
    pass

  def styleSheet():
    pass

  def tabletEvent():
    pass

  def testAttribute():
    pass

  def toolTip():
    pass

  def underMouse():
    pass

  def ungrabGesture():
    pass

  def unsetCursor():
    pass

  def unsetLayoutDirection():
    pass

  def unsetLocale():
    pass

  def update():
    pass

  def updateGeometry():
    pass

  def updateMicroFocus():
    pass

  def updatesEnabled():
    pass

  def visibleRegion():
    pass

  def whatsThis():
    pass

  def wheelEvent():
    pass

  def width():
    pass

  def winEvent():
    pass

  def winId():
    pass

  def window():
    pass

  def windowFilePath():
    pass

  def windowFlags():
    pass

  def windowIcon():
    pass

  def windowIconText():
    pass

  def windowModality():
    pass

  def windowOpacity():
    pass

  def windowRole():
    pass

  def windowState():
    pass

  def windowTitle():
    pass

  def windowType():
    pass

  def x():
    pass

  def y():
    pass

class QWidgetAction(QAction):

  AboutQtRole = None
  AboutRole = None
  ApplicationSpecificRole = None
  HighPriority = None
  Hover = None
  LowPriority = None
  NegativeSoftKey = None
  NoRole = None
  NoSoftKey = None
  NormalPriority = None
  PositiveSoftKey = None
  PreferencesRole = None
  QuitRole = None
  SelectSoftKey = None
  TextHeuristicRole = None
  Trigger = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def changed():
    """ Signal """
    pass

  def connect():
    pass

  def createWidget():
    pass

  def createdWidgets():
    pass

  def defaultWidget():
    pass

  def deleteWidget():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def hovered():
    """ Signal """
    pass

  def registerUserData():
    pass

  def releaseWidget():
    pass

  def requestWidget():
    pass

  def setDefaultWidget():
    pass

  staticMetaObject = None

  def toggled():
    """ Signal """
    pass

  def triggered():
    """ Signal """
    pass

class QWidgetItem(QLayoutItem):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def expandingDirections():
    pass

  def geometry():
    pass

  def hasHeightForWidth():
    pass

  def heightForWidth():
    pass

  def isEmpty():
    pass

  def maximumSize():
    pass

  def minimumSize():
    pass

  def setGeometry():
    pass

  def sizeHint():
    pass

  def widget():
    pass

class QWizard(QDialog):

  Accepted = None
  AeroStyle = None
  BackButton = None
  BackgroundPixmap = None
  BannerPixmap = None
  CancelButton = None
  CancelButtonOnLeft = None
  ClassicStyle = None
  CommitButton = None
  CustomButton1 = None
  CustomButton2 = None
  CustomButton3 = None
  DisabledBackButtonOnLastPage = None
  DrawChildren = None
  DrawWindowBackground = None
  ExtendedWatermarkPixmap = None
  FinishButton = None
  HaveCustomButton1 = None
  HaveCustomButton2 = None
  HaveCustomButton3 = None
  HaveFinishButtonOnEarlyPages = None
  HaveHelpButton = None
  HaveNextButtonOnLastPage = None
  HelpButton = None
  HelpButtonOnRight = None
  IgnoreMask = None
  IgnoreSubTitles = None
  IndependentPages = None
  LogoPixmap = None
  MacStyle = None
  ModernStyle = None
  NButtons = None
  NPixmaps = None
  NStandardButtons = None
  NStyles = None
  NextButton = None
  NoBackButtonOnLastPage = None
  NoBackButtonOnStartPage = None
  NoButton = None
  NoCancelButton = None
  NoDefaultButton = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  Rejected = None
  Stretch = None
  WatermarkPixmap = None

  class WizardButton(object):

    BackButton = None
    CancelButton = None
    CommitButton = None
    CustomButton1 = None
    CustomButton2 = None
    CustomButton3 = None
    FinishButton = None
    HelpButton = None
    NButtons = None
    NStandardButtons = None
    NextButton = None
    NoButton = None
    Stretch = None
    name = property(None, None, None,
                    )

    values = {}

  class WizardOption(object):

    CancelButtonOnLeft = None
    DisabledBackButtonOnLastPage = None
    ExtendedWatermarkPixmap = None
    HaveCustomButton1 = None
    HaveCustomButton2 = None
    HaveCustomButton3 = None
    HaveFinishButtonOnEarlyPages = None
    HaveHelpButton = None
    HaveNextButtonOnLastPage = None
    HelpButtonOnRight = None
    IgnoreSubTitles = None
    IndependentPages = None
    NoBackButtonOnLastPage = None
    NoBackButtonOnStartPage = None
    NoCancelButton = None
    NoDefaultButton = None
    name = property(None, None, None,
                    )

    values = {}

  class WizardOptions(object):

    pass

  class WizardPixmap(object):

    BackgroundPixmap = None
    BannerPixmap = None
    LogoPixmap = None
    NPixmaps = None
    WatermarkPixmap = None
    name = property(None, None, None,
                    )

    values = {}

  class WizardStyle(object):

    AeroStyle = None
    ClassicStyle = None
    MacStyle = None
    ModernStyle = None
    NStyles = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def addPage():
    pass

  def back():
    pass

  def button():
    pass

  def buttonText():
    pass

  def cleanupPage():
    pass

  def connect():
    pass

  def currentId():
    pass

  def currentIdChanged():
    """ Signal """
    pass

  def currentPage():
    pass

  def customButtonClicked():
    """ Signal """
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def done():
    pass

  def event():
    pass

  def field():
    pass

  def finished():
    """ Signal """
    pass

  def hasVisitedPage():
    pass

  def helpRequested():
    """ Signal """
    pass

  def initializePage():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def next():
    pass

  def nextId():
    pass

  def options():
    pass

  def page():
    pass

  def pageAdded():
    """ Signal """
    pass

  def pageIds():
    pass

  def pageRemoved():
    """ Signal """
    pass

  def paintEvent():
    pass

  def pixmap():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def removePage():
    pass

  def resizeEvent():
    pass

  def restart():
    pass

  def setButton():
    pass

  def setButtonLayout():
    pass

  def setButtonText():
    pass

  def setDefaultProperty():
    pass

  def setField():
    pass

  def setOption():
    pass

  def setOptions():
    pass

  def setPage():
    pass

  def setPixmap():
    pass

  def setSideWidget():
    pass

  def setStartId():
    pass

  def setSubTitleFormat():
    pass

  def setTabOrder():
    pass

  def setTitleFormat():
    pass

  def setVisible():
    pass

  def setWizardStyle():
    pass

  def sideWidget():
    pass

  def sizeHint():
    pass

  def startId():
    pass

  staticMetaObject = None

  def subTitleFormat():
    pass

  def testOption():
    pass

  def titleFormat():
    pass

  def validateCurrentPage():
    pass

  def visitedPages():
    pass

  def winEvent():
    pass

  def wizardStyle():
    pass

class QWizardPage(QWidget):

  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  PdmDepth = None
  PdmDpiX = None
  PdmDpiY = None
  PdmHeight = None
  PdmHeightMM = None
  PdmNumColors = None
  PdmPhysicalDpiX = None
  PdmPhysicalDpiY = None
  PdmWidth = None
  PdmWidthMM = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def buttonText():
    pass

  def cleanupPage():
    pass

  def completeChanged():
    """ Signal """
    pass

  def connect():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def field():
    pass

  def initializePage():
    pass

  def isCommitPage():
    pass

  def isComplete():
    pass

  def isFinalPage():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def nextId():
    pass

  def pixmap():
    pass

  def registerField():
    pass

  def registerUserData():
    pass

  def setButtonText():
    pass

  def setCommitPage():
    pass

  def setField():
    pass

  def setFinalPage():
    pass

  def setPixmap():
    pass

  def setSubTitle():
    pass

  def setTabOrder():
    pass

  def setTitle():
    pass

  staticMetaObject = None

  def subTitle():
    pass

  def title():
    pass

  def validatePage():
    pass

  def wizard():
    pass

__doc__ = None
__name__ = 'Qt.QtWidgets'

