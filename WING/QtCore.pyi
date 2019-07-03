# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class Property(object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def getter(self):
    pass

  def read(self):
    pass

  def setter(self):
    pass

  def write(self):
    pass

class QAbstractAnimation(QObject):

  Backward = None
  DeleteWhenStopped = None

  class DeletionPolicy(object):

    DeleteWhenStopped = None
    KeepWhenStopped = None
    name = property(None, None, None,
                    )

    values = {}

  class Direction(object):

    Backward = None
    Forward = None
    name = property(None, None, None,
                    )

    values = {}

  Forward = None
  KeepWhenStopped = None
  Paused = None
  Running = None

  class State(object):

    Paused = None
    Running = None
    Stopped = None
    name = property(None, None, None,
                    )

    values = {}

  Stopped = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentLoop():
    pass

  def currentLoopChanged():
    """ Signal """
    pass

  def currentLoopTime():
    pass

  def currentTime():
    pass

  def destroyed():
    """ Signal """
    pass

  def direction():
    pass

  def directionChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def duration():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def group():
    pass

  def loopCount():
    pass

  def pause():
    pass

  def registerUserData():
    pass

  def resume():
    pass

  def setCurrentTime():
    pass

  def setDirection():
    pass

  def setLoopCount():
    pass

  def setPaused():
    pass

  def start():
    pass

  def state():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def stop():
    pass

  def totalDuration():
    pass

  def updateCurrentTime():
    pass

  def updateDirection():
    pass

  def updateState():
    pass

class QAbstractEventDispatcher(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToBlock():
    """ Signal """
    pass

  def awake():
    """ Signal """
    pass

  def closingDown():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def flush():
    pass

  def hasPendingEvents():
    pass

  def instance():
    pass

  def interrupt():
    pass

  def processEvents():
    pass

  def registerSocketNotifier():
    pass

  def registerTimer():
    pass

  def registerUserData():
    pass

  def registeredTimers():
    pass

  def startingUp():
    pass

  staticMetaObject = None

  def unregisterSocketNotifier():
    pass

  def unregisterTimer():
    pass

  def unregisterTimers():
    pass

  def wakeUp():
    pass

class QAbstractItemModel(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def beginInsertColumns():
    pass

  def beginInsertRows():
    pass

  def beginMoveColumns():
    pass

  def beginMoveRows():
    pass

  def beginRemoveColumns():
    pass

  def beginRemoveRows():
    pass

  def beginResetModel():
    pass

  def buddy():
    pass

  def canFetchMore():
    pass

  def changePersistentIndex():
    pass

  def changePersistentIndexList():
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

  def createIndex():
    pass

  def data():
    pass

  def dataChanged():
    """ Signal """
    pass

  def decodeData():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def dropMimeData():
    pass

  def encodeData():
    pass

  def endInsertColumns():
    pass

  def endInsertRows():
    pass

  def endMoveColumns():
    pass

  def endMoveRows():
    pass

  def endRemoveColumns():
    pass

  def endRemoveRows():
    pass

  def endResetModel():
    pass

  def fetchMore():
    pass

  def flags():
    pass

  def hasChildren():
    pass

  def hasIndex():
    pass

  def headerData():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def index():
    pass

  def insertColumn():
    pass

  def insertColumns():
    pass

  def insertRow():
    pass

  def insertRows():
    pass

  def itemData():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def match():
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def parent():
    pass

  def persistentIndexList():
    pass

  def registerUserData():
    pass

  def removeColumn():
    pass

  def removeColumns():
    pass

  def removeRow():
    pass

  def removeRows():
    pass

  def reset():
    pass

  def resetInternalData():
    pass

  def revert():
    pass

  def roleNames():
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

  def setHeaderData():
    pass

  def setItemData():
    pass

  def setRoleNames():
    pass

  def setSupportedDragActions():
    pass

  def sibling():
    pass

  def sort():
    pass

  def span():
    pass

  staticMetaObject = None

  def submit():
    pass

  def supportedDragActions():
    pass

  def supportedDropActions():
    pass

class QAbstractListModel(QAbstractItemModel):

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

  def hasChildren():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def index():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def parent():
    pass

  def registerUserData():
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

  staticMetaObject = None

class QAbstractProxyModel(QAbstractItemModel):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def buddy():
    pass

  def canFetchMore():
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

  def fetchMore():
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

  def itemData():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def mapFromSource():
    pass

  def mapSelectionFromSource():
    pass

  def mapSelectionToSource():
    pass

  def mapToSource():
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def registerUserData():
    pass

  def revert():
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

  def setHeaderData():
    pass

  def setItemData():
    pass

  def setSourceModel():
    pass

  def sort():
    pass

  def sourceModel():
    pass

  def span():
    pass

  staticMetaObject = None

  def submit():
    pass

  def supportedDropActions():
    pass

class QAbstractState(QObject):

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

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def exited():
    """ Signal """
    pass

  def machine():
    pass

  def onEntry():
    pass

  def onExit():
    pass

  def parentState():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

class QAbstractTableModel(QAbstractItemModel):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
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

  def hasChildren():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def index():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def parent():
    pass

  def registerUserData():
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

  staticMetaObject = None

class QAbstractTransition(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addAnimation():
    pass

  def animations():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def eventTest():
    pass

  def machine():
    pass

  def onTransition():
    pass

  def registerUserData():
    pass

  def removeAnimation():
    pass

  def setTargetState():
    pass

  def setTargetStates():
    pass

  def sourceState():
    pass

  staticMetaObject = None

  def targetState():
    pass

  def targetStates():
    pass

  def triggered():
    """ Signal """
    pass

class QAnimationGroup(QAbstractAnimation):

  Backward = None
  DeleteWhenStopped = None
  Forward = None
  KeepWhenStopped = None
  Paused = None
  Running = None
  Stopped = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addAnimation():
    pass

  def animationAt():
    pass

  def animationCount():
    pass

  def clear():
    pass

  def connect():
    pass

  def currentLoopChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def directionChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def indexOfAnimation():
    pass

  def insertAnimation():
    pass

  def registerUserData():
    pass

  def removeAnimation():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def takeAnimation():
    pass

class QBasicTimer(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def isActive():
    pass

  def start():
    pass

  def stop():
    pass

  def timerId():
    pass

class QBitArray(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def at():
    pass

  def clear():
    pass

  def clearBit():
    pass

  def count():
    pass

  def fill():
    pass

  def isEmpty():
    pass

  def isNull():
    pass

  def resize():
    pass

  def setBit():
    pass

  def size():
    pass

  def swap():
    pass

  def testBit():
    pass

  def toggleBit():
    pass

  def truncate():
    pass

class QBuffer(QIODevice):

  Append = None
  NotOpen = None

  class OpenMode(object):

    pass

  class OpenModeFlag(object):

    Append = None
    NotOpen = None
    ReadOnly = None
    ReadWrite = None
    Text = None
    Truncate = None
    Unbuffered = None
    WriteOnly = None
    name = property(None, None, None,
                    )

    values = {}

  ReadOnly = None
  ReadWrite = None
  Text = None
  Truncate = None
  Unbuffered = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToClose():
    """ Signal """
    pass

  def atEnd():
    pass

  def buffer():
    pass

  def bytesWritten():
    """ Signal """
    pass

  def canReadLine():
    pass

  def close():
    pass

  def connect():
    pass

  def connectNotify():
    pass

  def data():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def disconnectNotify():
    pass

  def open():
    pass

  def pos():
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readData():
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def seek():
    pass

  def setBuffer():
    pass

  def setData():
    pass

  def size():
    pass

  staticMetaObject = None

  def writeData():
    pass

class QByteArray(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def at():
    pass

  def capacity():
    pass

  def chop():
    pass

  def clear():
    pass

  def contains():
    pass

  def count():
    pass

  def data():
    pass

  def endsWith():
    pass

  def fill():
    pass

  def fromBase64():
    pass

  def fromHex():
    pass

  def fromPercentEncoding():
    pass

  def fromRawData():
    pass

  def indexOf():
    pass

  def insert():
    pass

  def isEmpty():
    pass

  def isNull():
    pass

  def isSharedWith():
    pass

  def lastIndexOf():
    pass

  def left():
    pass

  def leftJustified():
    pass

  def length():
    pass

  def mid():
    pass

  def number():
    pass

  def prepend():
    pass

  def remove():
    pass

  def repeated():
    pass

  def replace():
    pass

  def reserve():
    pass

  def resize():
    pass

  def right():
    pass

  def rightJustified():
    pass

  def setNum():
    pass

  def setRawData():
    pass

  def simplified():
    pass

  def size():
    pass

  def split():
    pass

  def squeeze():
    pass

  def startsWith():
    pass

  def swap():
    pass

  def toBase64():
    pass

  def toDouble():
    pass

  def toFloat():
    pass

  def toHex():
    pass

  def toInt():
    pass

  def toLong():
    pass

  def toLongLong():
    pass

  def toLower():
    pass

  def toPercentEncoding():
    pass

  def toShort():
    pass

  def toUInt():
    pass

  def toULong():
    pass

  def toULongLong():
    pass

  def toUShort():
    pass

  def toUpper():
    pass

  def trimmed():
    pass

  def truncate():
    pass

class QByteArrayMatcher(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def indexIn():
    pass

  def pattern():
    pass

  def setPattern():
    pass

class QChildEvent(QEvent):

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

  def added():
    pass

  def child():
    pass

  def polished():
    pass

  def registerEventType():
    pass

  def removed():
    pass

class QCoreApplication(QObject):

  ApplicationFlags = 17041413
  CodecForTr = None
  DefaultCodec = None

  class Encoding(object):

    CodecForTr = None
    DefaultCodec = None
    UnicodeUTF8 = None
    name = property(None, None, None,
                    )

    values = {}

  UnicodeUTF8 = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToQuit():
    """ Signal """
    pass

  def addLibraryPath():
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

  def closingDown():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def exec_():
    pass

  def exit():
    pass

  def flush():
    pass

  def hasPendingEvents():
    pass

  def installTranslator():
    pass

  def instance():
    pass

  def libraryPaths():
    pass

  def notify():
    pass

  def organizationDomain():
    pass

  def organizationName():
    pass

  def postEvent():
    pass

  def processEvents():
    pass

  def quit():
    pass

  def registerUserData():
    pass

  def removeLibraryPath():
    pass

  def removePostedEvents():
    pass

  def removeTranslator():
    pass

  def sendEvent():
    pass

  def sendPostedEvents():
    pass

  def setApplicationName():
    pass

  def setApplicationVersion():
    pass

  def setAttribute():
    pass

  def setLibraryPaths():
    pass

  def setOrganizationDomain():
    pass

  def setOrganizationName():
    pass

  def startingUp():
    pass

  staticMetaObject = None

  def testAttribute():
    pass

  def translate():
    pass

  def unixSignal():
    """ Signal """
    pass

  def winEventFilter():
    pass

class QCryptographicHash(Object):

  class Algorithm(object):

    Md4 = None
    Md5 = None
    Sha1 = None
    name = property(None, None, None,
                    )

    values = {}

  Md4 = None
  Md5 = None
  Sha1 = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addData():
    pass

  def hash():
    pass

  def reset():
    pass

  def result():
    pass

class QDataStream(Object):

  BigEndian = None

  class ByteOrder(object):

    BigEndian = None
    LittleEndian = None
    name = property(None, None, None,
                    )

    values = {}

  DoublePrecision = None

  class FloatingPointPrecision(object):

    DoublePrecision = None
    SinglePrecision = None
    name = property(None, None, None,
                    )

    values = {}

  LittleEndian = None
  Ok = None
  Qt_1_0 = None
  Qt_2_0 = None
  Qt_2_1 = None
  Qt_3_0 = None
  Qt_3_1 = None
  Qt_3_3 = None
  Qt_4_0 = None
  Qt_4_1 = None
  Qt_4_2 = None
  Qt_4_3 = None
  Qt_4_4 = None
  Qt_4_5 = None
  Qt_4_6 = None
  Qt_4_7 = None
  Qt_4_8 = None
  ReadCorruptData = None
  ReadPastEnd = None
  SinglePrecision = None

  class Status(object):

    Ok = None
    ReadCorruptData = None
    ReadPastEnd = None
    WriteFailed = None
    name = property(None, None, None,
                    )

    values = {}

  class Version(object):

    Qt_1_0 = None
    Qt_2_0 = None
    Qt_2_1 = None
    Qt_3_0 = None
    Qt_3_1 = None
    Qt_3_3 = None
    Qt_4_0 = None
    Qt_4_1 = None
    Qt_4_2 = None
    Qt_4_3 = None
    Qt_4_4 = None
    Qt_4_5 = None
    Qt_4_6 = None
    Qt_4_7 = None
    Qt_4_8 = None
    name = property(None, None, None,
                    )

    values = {}

  WriteFailed = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def atEnd():
    pass

  def byteOrder():
    pass

  def device():
    pass

  def floatingPointPrecision():
    pass

  def readBool():
    pass

  def readDouble():
    pass

  def readFloat():
    pass

  def readInt16():
    pass

  def readInt32():
    pass

  def readInt64():
    pass

  def readInt8():
    pass

  def readQChar():
    pass

  def readQString():
    pass

  def readQStringList():
    pass

  def readQVariant():
    pass

  def readRawData():
    pass

  def readString():
    pass

  def readUInt16():
    pass

  def readUInt32():
    pass

  def readUInt64():
    pass

  def readUInt8():
    pass

  def resetStatus():
    pass

  def setByteOrder():
    pass

  def setDevice():
    pass

  def setFloatingPointPrecision():
    pass

  def setStatus():
    pass

  def setVersion():
    pass

  def skipRawData():
    pass

  def status():
    pass

  def unsetDevice():
    pass

  def version():
    pass

  def writeBool():
    pass

  def writeDouble():
    pass

  def writeFloat():
    pass

  def writeInt16():
    pass

  def writeInt32():
    pass

  def writeInt64():
    pass

  def writeInt8():
    pass

  def writeQChar():
    pass

  def writeQString():
    pass

  def writeQStringList():
    pass

  def writeQVariant():
    pass

  def writeRawData():
    pass

  def writeString():
    pass

  def writeUInt16():
    pass

  def writeUInt32():
    pass

  def writeUInt64():
    pass

  def writeUInt8():
    pass

class QDate(Object):

  DateFormat = None

  class MonthNameType(object):

    DateFormat = None
    StandaloneFormat = None
    name = property(None, None, None,
                    )

    values = {}

  StandaloneFormat = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addDays():
    pass

  def addMonths():
    pass

  def addYears():
    pass

  def currentDate():
    pass

  def day():
    pass

  def dayOfWeek():
    pass

  def dayOfYear():
    pass

  def daysInMonth():
    pass

  def daysInYear():
    pass

  def daysTo():
    pass

  def fromJulianDay():
    pass

  def fromString():
    pass

  def getDate():
    pass

  def gregorianToJulian():
    pass

  def isLeapYear():
    pass

  def isNull():
    pass

  def isValid():
    pass

  def longDayName():
    pass

  def longMonthName():
    pass

  def month():
    pass

  def setDate():
    pass

  def setYMD():
    pass

  def shortDayName():
    pass

  def shortMonthName():
    pass

  def toJulianDay():
    pass

  def toPython():
    pass

  def toString():
    pass

  def weekNumber():
    pass

  def year():
    pass

class QDateTime(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addDays():
    pass

  def addMSecs():
    pass

  def addMonths():
    pass

  def addSecs():
    pass

  def addYears():
    pass

  def currentDateTime():
    pass

  def currentDateTimeUtc():
    pass

  def currentMSecsSinceEpoch():
    pass

  def date():
    pass

  def daysTo():
    pass

  def fromMSecsSinceEpoch():
    pass

  def fromString():
    pass

  def fromTime_t():
    pass

  def isNull():
    pass

  def isValid():
    pass

  def msecsTo():
    pass

  def secsTo():
    pass

  def setDate():
    pass

  def setMSecsSinceEpoch():
    pass

  def setTime():
    pass

  def setTimeSpec():
    pass

  def setTime_t():
    pass

  def setUtcOffset():
    pass

  def time():
    pass

  def timeSpec():
    pass

  def toLocalTime():
    pass

  def toMSecsSinceEpoch():
    pass

  def toPython():
    pass

  def toString():
    pass

  def toTimeSpec():
    pass

  def toTime_t():
    pass

  def toUTC():
    pass

  def utcOffset():
    pass

class QDir(Object):

  AccessMask = None
  AllDirs = None
  AllEntries = None
  CaseSensitive = None
  Dirs = None
  DirsFirst = None
  DirsLast = None
  Drives = None
  Executable = None
  Files = None

  class Filter(object):

    AccessMask = None
    AllDirs = None
    AllEntries = None
    CaseSensitive = None
    Dirs = None
    Drives = None
    Executable = None
    Files = None
    Hidden = None
    Modified = None
    NoDot = None
    NoDotAndDotDot = None
    NoDotDot = None
    NoFilter = None
    NoSymLinks = None
    PermissionMask = None
    Readable = None
    System = None
    TypeMask = None
    Writable = None
    name = property(None, None, None,
                    )

    values = {}

  class Filters(object):

    pass

  Hidden = None
  IgnoreCase = None
  LocaleAware = None
  Modified = None
  Name = None
  NoDot = None
  NoDotAndDotDot = None
  NoDotDot = None
  NoFilter = None
  NoSort = None
  NoSymLinks = None
  PermissionMask = None
  Readable = None
  Reversed = None
  Size = None
  SortByMask = None

  class SortFlag(object):

    DirsFirst = None
    DirsLast = None
    IgnoreCase = None
    LocaleAware = None
    Name = None
    NoSort = None
    Reversed = None
    Size = None
    SortByMask = None
    Time = None
    Type = None
    Unsorted = None
    name = property(None, None, None,
                    )

    values = {}

  class SortFlags(object):

    pass

  System = None
  Time = None
  Type = None
  TypeMask = None
  Unsorted = None
  Writable = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def absoluteFilePath():
    pass

  def absolutePath():
    pass

  def addResourceSearchPath():
    pass

  def addSearchPath():
    pass

  def canonicalPath():
    pass

  def cd():
    pass

  def cdUp():
    pass

  def cleanPath():
    pass

  def convertSeparators():
    pass

  def count():
    pass

  def current():
    pass

  def currentPath():
    pass

  def dirName():
    pass

  def drives():
    pass

  def entryInfoList():
    pass

  def entryList():
    pass

  def exists():
    pass

  def filePath():
    pass

  def filter():
    pass

  def fromNativeSeparators():
    pass

  def home():
    pass

  def homePath():
    pass

  def isAbsolute():
    pass

  def isAbsolutePath():
    pass

  def isReadable():
    pass

  def isRelative():
    pass

  def isRelativePath():
    pass

  def isRoot():
    pass

  def makeAbsolute():
    pass

  def match():
    pass

  def mkdir():
    pass

  def mkpath():
    pass

  def nameFilters():
    pass

  def nameFiltersFromString():
    pass

  def path():
    pass

  def refresh():
    pass

  def relativeFilePath():
    pass

  def remove():
    pass

  def rename():
    pass

  def rmdir():
    pass

  def rmpath():
    pass

  def root():
    pass

  def rootPath():
    pass

  def searchPaths():
    pass

  def separator():
    pass

  def setCurrent():
    pass

  def setFilter():
    pass

  def setNameFilters():
    pass

  def setPath():
    pass

  def setSearchPaths():
    pass

  def setSorting():
    pass

  def sorting():
    pass

  def temp():
    pass

  def tempPath():
    pass

  def toNativeSeparators():
    pass

class QDirIterator(Object):

  FollowSymlinks = None

  class IteratorFlag(object):

    FollowSymlinks = None
    NoIteratorFlags = None
    Subdirectories = None
    name = property(None, None, None,
                    )

    values = {}

  class IteratorFlags(object):

    pass

  NoIteratorFlags = None
  Subdirectories = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def fileInfo():
    pass

  def fileName():
    pass

  def filePath():
    pass

  def hasNext():
    pass

  def next():
    pass

  def path():
    pass

class QDynamicPropertyChangeEvent(QEvent):

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

  def propertyName():
    pass

  def registerEventType():
    pass

class QEasingCurve(Object):

  CosineCurve = None
  Custom = None
  InBack = None
  InBounce = None
  InCirc = None
  InCubic = None
  InCurve = None
  InElastic = None
  InExpo = None
  InOutBack = None
  InOutBounce = None
  InOutCirc = None
  InOutCubic = None
  InOutElastic = None
  InOutExpo = None
  InOutQuad = None
  InOutQuart = None
  InOutQuint = None
  InOutSine = None
  InQuad = None
  InQuart = None
  InQuint = None
  InSine = None
  Linear = None
  NCurveTypes = None
  OutBack = None
  OutBounce = None
  OutCirc = None
  OutCubic = None
  OutCurve = None
  OutElastic = None
  OutExpo = None
  OutInBack = None
  OutInBounce = None
  OutInCirc = None
  OutInCubic = None
  OutInElastic = None
  OutInExpo = None
  OutInQuad = None
  OutInQuart = None
  OutInQuint = None
  OutInSine = None
  OutQuad = None
  OutQuart = None
  OutQuint = None
  OutSine = None
  SineCurve = None

  class Type(object):

    CosineCurve = None
    Custom = None
    InBack = None
    InBounce = None
    InCirc = None
    InCubic = None
    InCurve = None
    InElastic = None
    InExpo = None
    InOutBack = None
    InOutBounce = None
    InOutCirc = None
    InOutCubic = None
    InOutElastic = None
    InOutExpo = None
    InOutQuad = None
    InOutQuart = None
    InOutQuint = None
    InOutSine = None
    InQuad = None
    InQuart = None
    InQuint = None
    InSine = None
    Linear = None
    NCurveTypes = None
    OutBack = None
    OutBounce = None
    OutCirc = None
    OutCubic = None
    OutCurve = None
    OutElastic = None
    OutExpo = None
    OutInBack = None
    OutInBounce = None
    OutInCirc = None
    OutInCubic = None
    OutInElastic = None
    OutInExpo = None
    OutInQuad = None
    OutInQuart = None
    OutInQuint = None
    OutInSine = None
    OutQuad = None
    OutQuart = None
    OutQuint = None
    OutSine = None
    SineCurve = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def amplitude():
    pass

  def customType():
    pass

  def overshoot():
    pass

  def period():
    pass

  def setAmplitude():
    pass

  def setCustomType():
    pass

  def setOvershoot():
    pass

  def setPeriod():
    pass

  def setType():
    pass

  def type():
    pass

  def valueForProgress():
    pass

class QElapsedTimer(Object):

  class ClockType(object):

    MachAbsoluteTime = None
    MonotonicClock = None
    PerformanceCounter = None
    SystemTime = None
    TickCounter = None
    name = property(None, None, None,
                    )

    values = {}

  MachAbsoluteTime = None
  MonotonicClock = None
  PerformanceCounter = None
  SystemTime = None
  TickCounter = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clockType():
    pass

  def elapsed():
    pass

  def hasExpired():
    pass

  def invalidate():
    pass

  def isMonotonic():
    pass

  def isValid():
    pass

  def msecsSinceReference():
    pass

  def msecsTo():
    pass

  def nsecsElapsed():
    pass

  def restart():
    pass

  def secsTo():
    pass

  def start():
    pass

class QEvent(Object):

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

  def accept():
    pass

  def ignore():
    pass

  def isAccepted():
    pass

  def registerEventType():
    pass

  def setAccepted():
    pass

  def spontaneous():
    pass

  def type():
    pass

class QEventLoop(QObject):

  AllEvents = None
  DeferredDeletion = None
  DialogExec = None
  EventLoopExec = None
  ExcludeSocketNotifiers = None
  ExcludeUserInputEvents = None

  class ProcessEventsFlag(object):

    AllEvents = None
    DeferredDeletion = None
    DialogExec = None
    EventLoopExec = None
    ExcludeSocketNotifiers = None
    ExcludeUserInputEvents = None
    WaitForMoreEvents = None
    X11ExcludeTimers = None
    name = property(None, None, None,
                    )

    values = {}

  class ProcessEventsFlags(object):

    pass

  WaitForMoreEvents = None
  X11ExcludeTimers = None

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

  def exec_():
    pass

  def exit():
    pass

  def isRunning():
    pass

  def processEvents():
    pass

  def quit():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

  def wakeUp():
    pass

class QEventTransition(QAbstractTransition):

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

  def event():
    pass

  def eventSource():
    pass

  def eventTest():
    pass

  def eventType():
    pass

  def onTransition():
    pass

  def registerUserData():
    pass

  def setEventSource():
    pass

  def setEventType():
    pass

  staticMetaObject = None

  def triggered():
    """ Signal """
    pass

class QFile(QIODevice):

  AbortError = None
  Append = None
  AutoCloseHandle = None
  CopyError = None
  DontCloseHandle = None
  ExeGroup = None
  ExeOther = None
  ExeOwner = None
  ExeUser = None
  FatalError = None

  class FileError(object):

    AbortError = None
    CopyError = None
    FatalError = None
    NoError = None
    OpenError = None
    PermissionsError = None
    PositionError = None
    ReadError = None
    RemoveError = None
    RenameError = None
    ResizeError = None
    ResourceError = None
    TimeOutError = None
    UnspecifiedError = None
    WriteError = None
    name = property(None, None, None,
                    )

    values = {}

  class FileHandleFlag(object):

    AutoCloseHandle = None
    DontCloseHandle = None
    name = property(None, None, None,
                    )

    values = {}

  class FileHandleFlags(object):

    pass

  class MemoryMapFlags(object):

    NoOptions = None
    name = property(None, None, None,
                    )

    values = {}

  NoError = None
  NoOptions = None
  NotOpen = None
  OpenError = None
  class Permission(object):

    ExeGroup = None
    ExeOther = None
    ExeOwner = None
    ExeUser = None
    ReadGroup = None
    ReadOther = None
    ReadOwner = None
    ReadUser = None
    WriteGroup = None
    WriteOther = None
    WriteOwner = None
    WriteUser = None
    name = property(None, None, None,
                    )

    values = {}

  class Permissions(object):

    pass

  PermissionsError = None
  PositionError = None
  ReadError = None
  ReadGroup = None
  ReadOnly = None
  ReadOther = None
  ReadOwner = None
  ReadUser = None
  ReadWrite = None
  RemoveError = None
  RenameError = None
  ResizeError = None
  ResourceError = None
  Text = None
  TimeOutError = None
  Truncate = None
  Unbuffered = None
  UnspecifiedError = None
  WriteError = None
  WriteGroup = None
  WriteOnly = None
  WriteOther = None
  WriteOwner = None
  WriteUser = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToClose():
    """ Signal """
    pass

  def atEnd():
    pass

  def bytesWritten():
    """ Signal """
    pass

  def close():
    pass

  def connect():
    pass

  def copy():
    pass

  def decodeName():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def encodeName():
    pass

  def error():
    pass

  def exists():
    pass

  def fileEngine():
    pass

  def fileName():
    pass

  def flush():
    pass

  def handle():
    pass

  def isSequential():
    pass

  def link():
    pass

  def map():
    pass

  def open():
    pass

  def permissions():
    pass

  def pos():
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readData():
    pass

  def readLineData():
    pass

  def readLink():
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def remove():
    pass

  def rename():
    pass

  def resize():
    pass

  def seek():
    pass

  def setFileName():
    pass

  def setPermissions():
    pass

  def size():
    pass

  staticMetaObject = None

  def symLinkTarget():
    pass

  def unmap():
    pass

  def unsetError():
    pass

  def writeData():
    pass

class QFileInfo(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def absoluteDir():
    pass

  def absoluteFilePath():
    pass

  def absolutePath():
    pass

  def baseName():
    pass

  def bundleName():
    pass

  def caching():
    pass

  def canonicalFilePath():
    pass

  def canonicalPath():
    pass

  def completeBaseName():
    pass

  def completeSuffix():
    pass

  def created():
    pass

  def dir():
    pass

  def exists():
    pass

  def fileName():
    pass

  def filePath():
    pass

  def group():
    pass

  def groupId():
    pass

  def isAbsolute():
    pass

  def isBundle():
    pass

  def isDir():
    pass

  def isExecutable():
    pass

  def isFile():
    pass

  def isHidden():
    pass

  def isReadable():
    pass

  def isRelative():
    pass

  def isRoot():
    pass

  def isSymLink():
    pass

  def isWritable():
    pass

  def lastModified():
    pass

  def lastRead():
    pass

  def makeAbsolute():
    pass

  def owner():
    pass

  def ownerId():
    pass

  def path():
    pass

  def permission():
    pass

  def permissions():
    pass

  def readLink():
    pass

  def refresh():
    pass

  def setCaching():
    pass

  def setFile():
    pass

  def size():
    pass

  def suffix():
    pass

  def symLinkTarget():
    pass

class QFileSystemWatcher(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addPath():
    pass

  def addPaths():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def directories():
    pass

  def directoryChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def fileChanged():
    """ Signal """
    pass

  def files():
    pass

  def registerUserData():
    pass

  def removePath():
    pass

  def removePaths():
    pass

  staticMetaObject = None

class QFinalState(QAbstractState):

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

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def exited():
    """ Signal """
    pass

  def onEntry():
    pass

  def onExit():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

class QGenericArgument(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def name():
    pass

class QGenericReturnArgument(QGenericArgument):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

class QHistoryState(QAbstractState):

  DeepHistory = None

  class HistoryType(object):

    DeepHistory = None
    ShallowHistory = None
    name = property(None, None, None,
                    )

    values = {}

  ShallowHistory = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def defaultState():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def entered():
    """ Signal """
    pass

  def event():
    pass

  def exited():
    """ Signal """
    pass

  def historyType():
    pass

  def onEntry():
    pass

  def onExit():
    pass

  def registerUserData():
    pass

  def setDefaultState():
    pass

  def setHistoryType():
    pass

  staticMetaObject = None

class QIODevice(QObject):

  Append = None
  NotOpen = None
  ReadOnly = None
  ReadWrite = None
  Text = None
  Truncate = None
  Unbuffered = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToClose():
    """ Signal """
    pass

  def atEnd():
    pass

  def bytesAvailable():
    pass

  def bytesToWrite():
    pass

  def bytesWritten():
    """ Signal """
    pass

  def canReadLine():
    pass

  def close():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def errorString():
    pass

  def getChar():
    pass

  def isOpen():
    pass

  def isReadable():
    pass

  def isSequential():
    pass

  def isTextModeEnabled():
    pass

  def isWritable():
    pass

  def open():
    pass

  def openMode():
    pass

  def peek():
    pass

  def pos():
    pass

  def putChar():
    pass

  def read():
    pass

  def readAll():
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readData():
    pass

  def readLine():
    pass

  def readLineData():
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def seek():
    pass

  def setErrorString():
    pass

  def setOpenMode():
    pass

  def setTextModeEnabled():
    pass

  def size():
    pass

  staticMetaObject = None

  def ungetChar():
    pass

  def waitForBytesWritten():
    pass

  def waitForReadyRead():
    pass

  def write():
    pass

  def writeData():
    pass

class QItemSelection(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def at():
    pass

  def back():
    pass

  def clear():
    pass

  def contains():
    pass

  def count():
    pass

  def detachShared():
    pass

  def empty():
    pass

  def endsWith():
    pass

  def first():
    pass

  def fromSet():
    pass

  def fromVector():
    pass

  def front():
    pass

  def indexOf():
    pass

  def indexes():
    pass

  def insert():
    pass

  def isEmpty():
    pass

  def isSharedWith():
    pass

  def last():
    pass

  def lastIndexOf():
    pass

  def length():
    pass

  def merge():
    pass

  def mid():
    pass

  def move():
    pass

  def pop_back():
    pass

  def pop_front():
    pass

  def prepend():
    pass

  def push_back():
    pass

  def push_front():
    pass

  def removeAll():
    pass

  def removeAt():
    pass

  def removeFirst():
    pass

  def removeLast():
    pass

  def removeOne():
    pass

  def replace():
    pass

  def reserve():
    pass

  def select():
    pass

  def setSharable():
    pass

  def size():
    pass

  def split():
    pass

  def startsWith():
    pass

  def swap():
    pass

  def takeAt():
    pass

  def takeFirst():
    pass

  def takeLast():
    pass

  def toSet():
    pass

  def toVector():
    pass

  def value():
    pass

class QItemSelectionModel(QObject):

  Clear = None
  ClearAndSelect = None
  Columns = None
  Current = None
  Deselect = None
  NoUpdate = None
  Rows = None
  Select = None
  SelectCurrent = None

  class SelectionFlag(object):

    Clear = None
    ClearAndSelect = None
    Columns = None
    Current = None
    Deselect = None
    NoUpdate = None
    Rows = None
    Select = None
    SelectCurrent = None
    Toggle = None
    ToggleCurrent = None
    name = property(None, None, None,
                    )

    values = {}

  class SelectionFlags(object):

    pass

  Toggle = None
  ToggleCurrent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clear():
    pass

  def clearSelection():
    pass

  def columnIntersectsSelection():
    pass

  def connect():
    pass

  def currentChanged():
    """ Signal """
    pass

  def currentColumnChanged():
    """ Signal """
    pass

  def currentIndex():
    pass

  def currentRowChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def emitSelectionChanged():
    pass

  def hasSelection():
    pass

  def isColumnSelected():
    pass

  def isRowSelected():
    pass

  def isSelected():
    pass

  def model():
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def rowIntersectsSelection():
    pass

  def select():
    pass

  def selectedColumns():
    pass

  def selectedIndexes():
    pass

  def selectedRows():
    pass

  def selection():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def setCurrentIndex():
    pass

  staticMetaObject = None

class QItemSelectionRange(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bottom():
    pass

  def bottomRight():
    pass

  def contains():
    pass

  def height():
    pass

  def indexes():
    pass

  def intersected():
    pass

  def intersects():
    pass

  def isEmpty():
    pass

  def isValid():
    pass

  def left():
    pass

  def model():
    pass

  def parent():
    pass

  def right():
    pass

  def top():
    pass

  def topLeft():
    pass

  def width():
    pass

class QLibraryInfo(Object):

  BinariesPath = None
  DataPath = None
  DemosPath = None
  DocumentationPath = None
  ExamplesPath = None
  HeadersPath = None
  ImportsPath = None
  LibrariesPath = None

  class LibraryLocation(object):

    BinariesPath = None
    DataPath = None
    DemosPath = None
    DocumentationPath = None
    ExamplesPath = None
    HeadersPath = None
    ImportsPath = None
    LibrariesPath = None
    PluginsPath = None
    PrefixPath = None
    SettingsPath = None
    TranslationsPath = None
    name = property(None, None, None,
                    )

    values = {}

  PluginsPath = None
  PrefixPath = None
  SettingsPath = None
  TranslationsPath = None

  def buildDate():
    pass

  def buildKey():
    pass

  def licensedProducts():
    pass

  def licensee():
    pass

  def location():
    pass

class QLine(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def dx():
    pass

  def dy():
    pass

  def isNull():
    pass

  def p1():
    pass

  def p2():
    pass

  def setLine():
    pass

  def setP1():
    pass

  def setP2():
    pass

  def setPoints():
    pass

  def toTuple():
    pass

  def translate():
    pass

  def translated():
    pass

  def x1():
    pass

  def x2():
    pass

  def y1():
    pass

  def y2():
    pass

class QLineF(Object):

  BoundedIntersection = None

  class IntersectType(object):

    BoundedIntersection = None
    NoIntersection = None
    UnboundedIntersection = None
    name = property(None, None, None,
                    )

    values = {}

  NoIntersection = None
  UnboundedIntersection = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def angle():
    pass

  def angleTo():
    pass

  def dx():
    pass

  def dy():
    pass

  def fromPolar():
    pass

  def intersect():
    pass

  def isNull():
    pass

  def length():
    pass

  def normalVector():
    pass

  def p1():
    pass

  def p2():
    pass

  def pointAt():
    pass

  def setAngle():
    pass

  def setLength():
    pass

  def setLine():
    pass

  def setP1():
    pass

  def setP2():
    pass

  def setPoints():
    pass

  def toLine():
    pass

  def toTuple():
    pass

  def translate():
    pass

  def translated():
    pass

  def unitVector():
    pass

  def x1():
    pass

  def x2():
    pass

  def y1():
    pass

  def y2():
    pass

class QLocale(Object):

  Abkhazian = None
  Afan = None
  Afar = None
  Afghanistan = None
  Afrikaans = None
  Aghem = None
  Akan = None
  Albania = None
  Albanian = None
  Algeria = None
  AlternateQuotation = None
  AmericanSamoa = None
  Amharic = None
  Andorra = None
  Angola = None
  Anguilla = None
  Antarctica = None
  AntiguaAndBarbuda = None
  AnyCountry = None
  AnyLanguage = None
  AnyScript = None
  Arabic = None
  ArabicScript = None
  Argentina = None
  Armenia = None
  Armenian = None
  Aruba = None
  Assamese = None
  Asu = None
  Atsam = None
  Australia = None
  Austria = None
  Aymara = None
  Azerbaijan = None
  Azerbaijani = None
  Bafia = None
  Bahamas = None
  Bahrain = None
  Bambara = None
  Bangladesh = None
  Barbados = None
  Basaa = None
  Bashkir = None
  Basque = None
  Belarus = None
  Belgium = None
  Belize = None
  Bemba = None
  Bena = None
  Bengali = None
  Benin = None
  Bermuda = None
  Bhutan = None
  Bhutani = None
  Bihari = None
  Bislama = None
  Blin = None
  Bodo = None
  Bolivia = None
  BosniaAndHerzegowina = None
  Bosnian = None
  Botswana = None
  BouvetIsland = None
  Brazil = None
  Breton = None
  BritishIndianOceanTerritory = None
  BritishVirginIslands = None
  BruneiDarussalam = None
  Bulgaria = None
  Bulgarian = None
  BurkinaFaso = None
  Burmese = None
  Burundi = None
  Byelorussian = None
  C = None
  Cambodia = None
  Cambodian = None
  Cameroon = None
  Canada = None
  CapeVerde = None
  Catalan = None
  CaymanIslands = None
  CentralAfricanRepublic = None
  CentralMoroccoTamazight = None
  Chad = None
  Cherokee = None
  Chewa = None
  Chiga = None
  Chile = None
  China = None
  Chinese = None
  ChristmasIsland = None
  CocosIslands = None
  Colognian = None
  Colombia = None
  Comoros = None
  CongoSwahili = None
  CookIslands = None
  Cornish = None
  Corsican = None
  CostaRica = None

  class Country(object):

    Afghanistan = None
    Albania = None
    Algeria = None
    AmericanSamoa = None
    Andorra = None
    Angola = None
    Anguilla = None
    Antarctica = None
    AntiguaAndBarbuda = None
    AnyCountry = None
    Argentina = None
    Armenia = None
    Aruba = None
    Australia = None
    Austria = None
    Azerbaijan = None
    Bahamas = None
    Bahrain = None
    Bangladesh = None
    Barbados = None
    Belarus = None
    Belgium = None
    Belize = None
    Benin = None
    Bermuda = None
    Bhutan = None
    Bolivia = None
    BosniaAndHerzegowina = None
    Botswana = None
    BouvetIsland = None
    Brazil = None
    BritishIndianOceanTerritory = None
    BritishVirginIslands = None
    BruneiDarussalam = None
    Bulgaria = None
    BurkinaFaso = None
    Burundi = None
    Cambodia = None
    Cameroon = None
    Canada = None
    CapeVerde = None
    CaymanIslands = None
    CentralAfricanRepublic = None
    Chad = None
    Chile = None
    China = None
    ChristmasIsland = None
    CocosIslands = None
    Colombia = None
    Comoros = None
    CookIslands = None
    CostaRica = None
    Croatia = None
    Cuba = None
    Cyprus = None
    CzechRepublic = None
    DemocraticRepublicOfCongo = None
    DemocraticRepublicOfKorea = None
    Denmark = None
    Djibouti = None
    Dominica = None
    DominicanRepublic = None
    EastTimor = None
    Ecuador = None
    Egypt = None
    ElSalvador = None
    EquatorialGuinea = None
    Eritrea = None
    Estonia = None
    Ethiopia = None
    FalklandIslands = None
    FaroeIslands = None
    FijiCountry = None
    Finland = None
    France = None
    FrenchGuiana = None
    FrenchPolynesia = None
    FrenchSouthernTerritories = None
    Gabon = None
    Gambia = None
    Georgia = None
    Germany = None
    Ghana = None
    Gibraltar = None
    Greece = None
    Greenland = None
    Grenada = None
    Guadeloupe = None
    Guam = None
    Guatemala = None
    Guinea = None
    GuineaBissau = None
    Guyana = None
    Haiti = None
    HeardAndMcDonaldIslands = None
    Honduras = None
    HongKong = None
    Hungary = None
    Iceland = None
    India = None
    Indonesia = None
    Iran = None
    Iraq = None
    Ireland = None
    Israel = None
    Italy = None
    IvoryCoast = None
    Jamaica = None
    Japan = None
    Jordan = None
    Kazakhstan = None
    Kenya = None
    Kiribati = None
    Kuwait = None
    Kyrgyzstan = None
    Lao = None
    LastCountry = None
    LatinAmericaAndTheCaribbean = None
    Latvia = None
    Lebanon = None
    Lesotho = None
    Liberia = None
    LibyanArabJamahiriya = None
    Liechtenstein = None
    Lithuania = None
    Luxembourg = None
    Macau = None
    Macedonia = None
    Madagascar = None
    Malawi = None
    Malaysia = None
    Maldives = None
    Mali = None
    Malta = None
    MarshallIslands = None
    Martinique = None
    Mauritania = None
    Mauritius = None
    Mayotte = None
    MetropolitanFrance = None
    Mexico = None
    Micronesia = None
    Moldova = None
    Monaco = None
    Mongolia = None
    Montenegro = None
    Montserrat = None
    Morocco = None
    Mozambique = None
    Myanmar = None
    Namibia = None
    NauruCountry = None
    Nepal = None
    Netherlands = None
    NetherlandsAntilles = None
    NewCaledonia = None
    NewZealand = None
    Nicaragua = None
    Niger = None
    Nigeria = None
    Niue = None
    NorfolkIsland = None
    NorthernMarianaIslands = None
    Norway = None
    Oman = None
    Pakistan = None
    Palau = None
    PalestinianTerritory = None
    Panama = None
    PapuaNewGuinea = None
    Paraguay = None
    PeoplesRepublicOfCongo = None
    Peru = None
    Philippines = None
    Pitcairn = None
    Poland = None
    Portugal = None
    PuertoRico = None
    Qatar = None
    RepublicOfKorea = None
    Reunion = None
    Romania = None
    RussianFederation = None
    Rwanda = None
    SaintBarthelemy = None
    SaintKittsAndNevis = None
    SaintMartin = None
    Samoa = None
    SanMarino = None
    SaoTomeAndPrincipe = None
    SaudiArabia = None
    Senegal = None
    Serbia = None
    SerbiaAndMontenegro = None
    Seychelles = None
    SierraLeone = None
    Singapore = None
    Slovakia = None
    Slovenia = None
    SolomonIslands = None
    Somalia = None
    SouthAfrica = None
    SouthGeorgiaAndTheSouthSandwichIslands = None
    Spain = None
    SriLanka = None
    StHelena = None
    StLucia = None
    StPierreAndMiquelon = None
    StVincentAndTheGrenadines = None
    Sudan = None
    Suriname = None
    SvalbardAndJanMayenIslands = None
    Swaziland = None
    Sweden = None
    Switzerland = None
    SyrianArabRepublic = None
    Taiwan = None
    Tajikistan = None
    Tanzania = None
    Thailand = None
    Togo = None
    Tokelau = None
    TongaCountry = None
    TrinidadAndTobago = None
    Tunisia = None
    Turkey = None
    Turkmenistan = None
    TurksAndCaicosIslands = None
    Tuvalu = None
    USVirginIslands = None
    Uganda = None
    Ukraine = None
    UnitedArabEmirates = None
    UnitedKingdom = None
    UnitedStates = None
    UnitedStatesMinorOutlyingIslands = None
    Uruguay = None
    Uzbekistan = None
    Vanuatu = None
    VaticanCityState = None
    Venezuela = None
    VietNam = None
    WallisAndFutunaIslands = None
    WesternSahara = None
    Yemen = None
    Yugoslavia = None
    Zambia = None
    Zimbabwe = None
    name = property(None, None, None,
                    )

    values = {}

  Croatia = None
  Croatian = None
  Cuba = None
  CurrencyDisplayName = None
  CurrencyIsoCode = None
  CurrencySymbol = None

  class CurrencySymbolFormat(object):

    CurrencyDisplayName = None
    CurrencyIsoCode = None
    CurrencySymbol = None
    name = property(None, None, None,
                    )

    values = {}

  Cyprus = None
  CyrillicScript = None
  Czech = None
  CzechRepublic = None
  Danish = None
  DemocraticRepublicOfCongo = None
  DemocraticRepublicOfKorea = None
  Denmark = None
  DeseretScript = None
  Divehi = None
  Djibouti = None
  Dominica = None
  DominicanRepublic = None
  Duala = None
  Dutch = None
  EastTimor = None
  Ecuador = None
  Egypt = None
  ElSalvador = None
  Embu = None
  English = None
  EquatorialGuinea = None
  Eritrea = None
  Esperanto = None
  Estonia = None
  Estonian = None
  Ethiopia = None
  Ewe = None
  Ewondo = None
  FalklandIslands = None
  FaroeIslands = None
  Faroese = None
  FijiCountry = None
  FijiLanguage = None
  Filipino = None
  Finland = None
  Finnish = None

  class FormatType(object):

    LongFormat = None
    NarrowFormat = None
    ShortFormat = None
    name = property(None, None, None,
                    )

    values = {}

  France = None
  French = None
  FrenchGuiana = None
  FrenchPolynesia = None
  FrenchSouthernTerritories = None
  Frisian = None
  Friulian = None
  Fulah = None
  Ga = None
  Gabon = None
  Gaelic = None
  Galician = None
  Gambia = None
  Ganda = None
  Geez = None
  Georgia = None
  Georgian = None
  German = None
  Germany = None
  Ghana = None
  Gibraltar = None
  Greece = None
  Greek = None
  Greenland = None
  Greenlandic = None
  Grenada = None
  Guadeloupe = None
  Guam = None
  Guarani = None
  Guatemala = None
  Guinea = None
  GuineaBissau = None
  Gujarati = None
  GurmukhiScript = None
  Gusii = None
  Guyana = None
  Haiti = None
  Hausa = None
  Hawaiian = None
  HeardAndMcDonaldIslands = None
  Hebrew = None
  Hindi = None
  Honduras = None
  HongKong = None
  Hungarian = None
  Hungary = None
  Iceland = None
  Icelandic = None
  Igbo = None
  ImperialSystem = None
  India = None
  Indonesia = None
  Indonesian = None
  Interlingua = None
  Interlingue = None
  Inuktitut = None
  Inupiak = None
  Iran = None
  Iraq = None
  Ireland = None
  Irish = None
  Israel = None
  Italian = None
  Italy = None
  IvoryCoast = None
  Jamaica = None
  Japan = None
  Japanese = None
  Javanese = None
  Jju = None
  JolaFonyi = None
  Jordan = None
  Kabuverdianu = None
  Kabyle = None
  Kalenjin = None
  Kamba = None
  Kannada = None
  Kashmiri = None
  Kazakh = None
  Kazakhstan = None
  Kenya = None
  Kikuyu = None
  Kinyarwanda = None
  Kirghiz = None
  Kiribati = None
  Konkani = None
  Korean = None
  Koro = None
  KoyraChiini = None
  KoyraboroSenni = None
  Kpelle = None
  Kurdish = None
  Kurundi = None
  Kuwait = None
  Kwasio = None
  Kyrgyzstan = None
  Langi = None

  class Language(object):

    Abkhazian = None
    Afan = None
    Afar = None
    Afrikaans = None
    Aghem = None
    Akan = None
    Albanian = None
    Amharic = None
    AnyLanguage = None
    Arabic = None
    Armenian = None
    Assamese = None
    Asu = None
    Atsam = None
    Aymara = None
    Azerbaijani = None
    Bafia = None
    Bambara = None
    Basaa = None
    Bashkir = None
    Basque = None
    Bemba = None
    Bena = None
    Bengali = None
    Bhutani = None
    Bihari = None
    Bislama = None
    Blin = None
    Bodo = None
    Bosnian = None
    Breton = None
    Bulgarian = None
    Burmese = None
    Byelorussian = None
    C = None
    Cambodian = None
    Catalan = None
    CentralMoroccoTamazight = None
    Cherokee = None
    Chewa = None
    Chiga = None
    Chinese = None
    Colognian = None
    CongoSwahili = None
    Cornish = None
    Corsican = None
    Croatian = None
    Czech = None
    Danish = None
    Divehi = None
    Duala = None
    Dutch = None
    Embu = None
    English = None
    Esperanto = None
    Estonian = None
    Ewe = None
    Ewondo = None
    Faroese = None
    FijiLanguage = None
    Filipino = None
    Finnish = None
    French = None
    Frisian = None
    Friulian = None
    Fulah = None
    Ga = None
    Gaelic = None
    Galician = None
    Ganda = None
    Geez = None
    Georgian = None
    German = None
    Greek = None
    Greenlandic = None
    Guarani = None
    Gujarati = None
    Gusii = None
    Hausa = None
    Hawaiian = None
    Hebrew = None
    Hindi = None
    Hungarian = None
    Icelandic = None
    Igbo = None
    Indonesian = None
    Interlingua = None
    Interlingue = None
    Inuktitut = None
    Inupiak = None
    Irish = None
    Italian = None
    Japanese = None
    Javanese = None
    Jju = None
    JolaFonyi = None
    Kabuverdianu = None
    Kabyle = None
    Kalenjin = None
    Kamba = None
    Kannada = None
    Kashmiri = None
    Kazakh = None
    Kikuyu = None
    Kinyarwanda = None
    Kirghiz = None
    Konkani = None
    Korean = None
    Koro = None
    KoyraChiini = None
    KoyraboroSenni = None
    Kpelle = None
    Kurdish = None
    Kurundi = None
    Kwasio = None
    Langi = None
    Laothian = None
    LastLanguage = None
    Latin = None
    Latvian = None
    Lingala = None
    Lithuanian = None
    LowGerman = None
    LubaKatanga = None
    Luo = None
    Luyia = None
    Macedonian = None
    Machame = None
    MakhuwaMeetto = None
    Makonde = None
    Malagasy = None
    Malay = None
    Malayalam = None
    Maltese = None
    Manx = None
    Maori = None
    Marathi = None
    Masai = None
    Meru = None
    Moldavian = None
    Mongolian = None
    Morisyen = None
    Mundang = None
    Nama = None
    NauruLanguage = None
    Nepali = None
    NorthNdebele = None
    NorthernSami = None
    NorthernSotho = None
    Norwegian = None
    NorwegianBokmal = None
    NorwegianNynorsk = None
    Nuer = None
    Nyankole = None
    Nynorsk = None
    Occitan = None
    Oriya = None
    Pashto = None
    Persian = None
    Polish = None
    Portuguese = None
    Punjabi = None
    Quechua = None
    RhaetoRomance = None
    Romanian = None
    Rombo = None
    Rundi = None
    Russian = None
    Rwa = None
    Saho = None
    Sakha = None
    Samburu = None
    Samoan = None
    Sangho = None
    Sangu = None
    Sanskrit = None
    Sena = None
    Serbian = None
    SerboCroatian = None
    Sesotho = None
    Setswana = None
    Shambala = None
    Shona = None
    SichuanYi = None
    Sidamo = None
    Sindhi = None
    Singhalese = None
    Siswati = None
    Slovak = None
    Slovenian = None
    Soga = None
    Somali = None
    SouthNdebele = None
    Spanish = None
    Sundanese = None
    Swahili = None
    Swedish = None
    SwissGerman = None
    Syriac = None
    Tachelhit = None
    Tagalog = None
    Taita = None
    Tajik = None
    Tamil = None
    Taroko = None
    Tasawaq = None
    Tatar = None
    Telugu = None
    Teso = None
    Thai = None
    Tibetan = None
    Tigre = None
    Tigrinya = None
    TongaLanguage = None
    Tsonga = None
    Turkish = None
    Turkmen = None
    Twi = None
    Tyap = None
    Uigur = None
    Ukrainian = None
    Urdu = None
    Uzbek = None
    Vai = None
    Venda = None
    Vietnamese = None
    Volapuk = None
    Vunjo = None
    Walamo = None
    Walser = None
    Welsh = None
    Wolof = None
    Xhosa = None
    Yangben = None
    Yiddish = None
    Yoruba = None
    Zarma = None
    Zhuang = None
    Zulu = None
    name = property(None, None, None,
                    )

    values = {}

  Lao = None
  Laothian = None
  LastCountry = None
  LastLanguage = None
  LastScript = None
  Latin = None
  LatinAmericaAndTheCaribbean = None
  LatinScript = None
  Latvia = None
  Latvian = None
  Lebanon = None
  Lesotho = None
  Liberia = None
  LibyanArabJamahiriya = None
  Liechtenstein = None
  Lingala = None
  Lithuania = None
  Lithuanian = None
  LongFormat = None
  LowGerman = None
  LubaKatanga = None
  Luo = None
  Luxembourg = None
  Luyia = None
  Macau = None
  Macedonia = None
  Macedonian = None
  Machame = None
  Madagascar = None
  MakhuwaMeetto = None
  Makonde = None
  Malagasy = None
  Malawi = None
  Malay = None
  Malayalam = None
  Malaysia = None
  Maldives = None
  Mali = None
  Malta = None
  Maltese = None
  Manx = None
  Maori = None
  Marathi = None
  MarshallIslands = None
  Martinique = None
  Masai = None
  Mauritania = None
  Mauritius = None
  Mayotte = None

  class MeasurementSystem(object):

    ImperialSystem = None
    MetricSystem = None
    name = property(None, None, None,
                    )

    values = {}

  Meru = None
  MetricSystem = None
  MetropolitanFrance = None
  Mexico = None
  Micronesia = None
  Moldavian = None
  Moldova = None
  Monaco = None
  Mongolia = None
  Mongolian = None
  MongolianScript = None
  Montenegro = None
  Montserrat = None
  Morisyen = None
  Morocco = None
  Mozambique = None
  Mundang = None
  Myanmar = None
  Nama = None
  Namibia = None
  NarrowFormat = None
  NauruCountry = None
  NauruLanguage = None
  Nepal = None
  Nepali = None
  Netherlands = None
  NetherlandsAntilles = None
  NewCaledonia = None
  NewZealand = None
  Nicaragua = None
  Niger = None
  Nigeria = None
  Niue = None
  NorfolkIsland = None
  NorthNdebele = None
  NorthernMarianaIslands = None
  NorthernSami = None
  NorthernSotho = None
  Norway = None
  Norwegian = None
  NorwegianBokmal = None
  NorwegianNynorsk = None
  Nuer = None

  class NumberOption(object):

    OmitGroupSeparator = None
    RejectGroupSeparator = None
    name = property(None, None, None,
                    )

    values = {}

  class NumberOptions(object):

    pass

  Nyankole = None
  Nynorsk = None
  Occitan = None
  Oman = None
  OmitGroupSeparator = None
  Oriya = None
  Pakistan = None
  Palau = None
  PalestinianTerritory = None
  Panama = None
  PapuaNewGuinea = None
  Paraguay = None
  Pashto = None
  PeoplesRepublicOfCongo = None
  Persian = None
  Peru = None
  Philippines = None
  Pitcairn = None
  Poland = None
  Polish = None
  Portugal = None
  Portuguese = None
  PuertoRico = None
  Punjabi = None
  Qatar = None
  Quechua = None

  class QuotationStyle(object):

    AlternateQuotation = None
    StandardQuotation = None
    name = property(None, None, None,
                    )

    values = {}

  RejectGroupSeparator = None
  RepublicOfKorea = None
  Reunion = None
  RhaetoRomance = None
  Romania = None
  Romanian = None
  Rombo = None
  Rundi = None
  Russian = None
  RussianFederation = None
  Rwa = None
  Rwanda = None
  Saho = None
  SaintBarthelemy = None
  SaintKittsAndNevis = None
  SaintMartin = None
  Sakha = None
  Samburu = None
  Samoa = None
  Samoan = None
  SanMarino = None
  Sangho = None
  Sangu = None
  Sanskrit = None
  SaoTomeAndPrincipe = None
  SaudiArabia = None

  class Script(object):

    AnyScript = None
    ArabicScript = None
    CyrillicScript = None
    DeseretScript = None
    GurmukhiScript = None
    LastScript = None
    LatinScript = None
    MongolianScript = None
    SimplifiedChineseScript = None
    SimplifiedHanScript = None
    TifinaghScript = None
    TraditionalChineseScript = None
    TraditionalHanScript = None
    name = property(None, None, None,
                    )

    values = {}

  Sena = None
  Senegal = None
  Serbia = None
  SerbiaAndMontenegro = None
  Serbian = None
  SerboCroatian = None
  Sesotho = None
  Setswana = None
  Seychelles = None
  Shambala = None
  Shona = None
  ShortFormat = None
  SichuanYi = None
  Sidamo = None
  SierraLeone = None
  SimplifiedChineseScript = None
  SimplifiedHanScript = None
  Sindhi = None
  Singapore = None
  Singhalese = None
  Siswati = None
  Slovak = None
  Slovakia = None
  Slovenia = None
  Slovenian = None
  Soga = None
  SolomonIslands = None
  Somali = None
  Somalia = None
  SouthAfrica = None
  SouthGeorgiaAndTheSouthSandwichIslands = None
  SouthNdebele = None
  Spain = None
  Spanish = None
  SriLanka = None
  StHelena = None
  StLucia = None
  StPierreAndMiquelon = None
  StVincentAndTheGrenadines = None
  StandardQuotation = None
  Sudan = None
  Sundanese = None
  Suriname = None
  SvalbardAndJanMayenIslands = None
  Swahili = None
  Swaziland = None
  Sweden = None
  Swedish = None
  SwissGerman = None
  Switzerland = None
  Syriac = None
  SyrianArabRepublic = None
  Tachelhit = None
  Tagalog = None
  Taita = None
  Taiwan = None
  Tajik = None
  Tajikistan = None
  Tamil = None
  Tanzania = None
  Taroko = None
  Tasawaq = None
  Tatar = None
  Telugu = None
  Teso = None
  Thai = None
  Thailand = None
  Tibetan = None
  TifinaghScript = None
  Tigre = None
  Tigrinya = None
  Togo = None
  Tokelau = None
  TongaCountry = None
  TongaLanguage = None
  TraditionalChineseScript = None
  TraditionalHanScript = None
  TrinidadAndTobago = None
  Tsonga = None
  Tunisia = None
  Turkey = None
  Turkish = None
  Turkmen = None
  Turkmenistan = None
  TurksAndCaicosIslands = None
  Tuvalu = None
  Twi = None
  Tyap = None
  USVirginIslands = None
  Uganda = None
  Uigur = None
  Ukraine = None
  Ukrainian = None
  UnitedArabEmirates = None
  UnitedKingdom = None
  UnitedStates = None
  UnitedStatesMinorOutlyingIslands = None
  Urdu = None
  Uruguay = None
  Uzbek = None
  Uzbekistan = None
  Vai = None
  Vanuatu = None
  VaticanCityState = None
  Venda = None
  Venezuela = None
  VietNam = None
  Vietnamese = None
  Volapuk = None
  Vunjo = None
  Walamo = None
  WallisAndFutunaIslands = None
  Walser = None
  Welsh = None
  WesternSahara = None
  Wolof = None
  Xhosa = None
  Yangben = None
  Yemen = None
  Yiddish = None
  Yoruba = None
  Yugoslavia = None
  Zambia = None
  Zarma = None
  Zhuang = None
  Zimbabwe = None
  Zulu = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def amText():
    pass

  def bcp47Name():
    pass

  def c():
    pass

  def countriesForLanguage():
    pass

  def country():
    pass

  def countryToString():
    pass

  def createSeparatedList():
    pass

  def currencySymbol():
    pass

  def dateFormat():
    pass

  def dateTimeFormat():
    pass

  def dayName():
    pass

  def decimalPoint():
    pass

  def exponential():
    pass

  def firstDayOfWeek():
    pass

  def groupSeparator():
    pass

  def language():
    pass

  def languageToString():
    pass

  def matchingLocales():
    pass

  def measurementSystem():
    pass

  def monthName():
    pass

  def name():
    pass

  def nativeCountryName():
    pass

  def nativeLanguageName():
    pass

  def negativeSign():
    pass

  def numberOptions():
    pass

  def percent():
    pass

  def pmText():
    pass

  def positiveSign():
    pass

  def quoteString():
    pass

  def script():
    pass

  def scriptToString():
    pass

  def setDefault():
    pass

  def setNumberOptions():
    pass

  def standaloneDayName():
    pass

  def standaloneMonthName():
    pass

  def system():
    pass

  def textDirection():
    pass

  def timeFormat():
    pass

  def toCurrencyString():
    pass

  def toDate():
    pass

  def toDateTime():
    pass

  def toDouble():
    pass

  def toFloat():
    pass

  def toInt():
    pass

  def toLongLong():
    pass

  def toLower():
    pass

  def toShort():
    pass

  def toString():
    pass

  def toTime():
    pass

  def toUInt():
    pass

  def toULongLong():
    pass

  def toUShort():
    pass

  def toUpper():
    pass

  def uiLanguages():
    pass

  def weekdays():
    pass

  def zeroDigit():
    pass

class QMargins(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bottom():
    pass

  def isNull():
    pass

  def left():
    pass

  def right():
    pass

  def setBottom():
    pass

  def setLeft():
    pass

  def setRight():
    pass

  def setTop():
    pass

  def top():
    pass

class QMetaClassInfo(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def name():
    pass

  def value():
    pass

class QMetaEnum(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def isFlag():
    pass

  def isValid():
    pass

  def key():
    pass

  def keyCount():
    pass

  def keyToValue():
    pass

  def keysToValue():
    pass

  def name():
    pass

  def scope():
    pass

  def value():
    pass

  def valueToKey():
    pass

  def valueToKeys():
    pass

class QMetaMethod(Object):

  class Access(object):

    Private = None
    Protected = None
    Public = None
    name = property(None, None, None,
                    )

    values = {}

  Constructor = None
  Method = None

  class MethodType(object):

    Constructor = None
    Method = None
    Signal = None
    Slot = None
    name = property(None, None, None,
                    )

    values = {}

  Private = None
  Protected = None
  Public = None
  Signal = None
  Slot = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def access():
    pass

  def enclosingMetaObject():
    pass

  def invoke():
    pass

  def methodIndex():
    pass

  def methodType():
    pass

  def parameterNames():
    pass

  def parameterTypes():
    pass

  def revision():
    pass

  def signature():
    pass

  def tag():
    pass

  def typeName():
    pass

class QMetaObject(Object):

  class Call(object):

    CreateInstance = None
    InvokeMetaMethod = None
    QueryPropertyDesignable = None
    QueryPropertyEditable = None
    QueryPropertyScriptable = None
    QueryPropertyStored = None
    QueryPropertyUser = None
    ReadProperty = None
    ResetProperty = None
    WriteProperty = None
    name = property(None, None, None,
                    )

    values = {}

  CreateInstance = None
  InvokeMetaMethod = None
  QueryPropertyDesignable = None
  QueryPropertyEditable = None
  QueryPropertyScriptable = None
  QueryPropertyStored = None
  QueryPropertyUser = None
  ReadProperty = None
  ResetProperty = None
  WriteProperty = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cast():
    pass

  def checkConnectArgs():
    pass

  def classInfo():
    pass

  def classInfoCount():
    pass

  def classInfoOffset():
    pass

  def className():
    pass

  def connectSlotsByName():
    pass

  def constructor():
    pass

  def constructorCount():
    pass

  def disconnect():
    pass

  def enumerator():
    pass

  def enumeratorCount():
    pass

  def enumeratorOffset():
    pass

  def indexOfClassInfo():
    pass

  def indexOfConstructor():
    pass

  def indexOfEnumerator():
    pass

  def indexOfMethod():
    pass

  def indexOfProperty():
    pass

  def indexOfSignal():
    pass

  def indexOfSlot():
    pass

  def invokeMethod():
    pass

  def method():
    pass

  def methodCount():
    pass

  def methodOffset():
    pass

  def newInstance():
    pass

  def normalizedSignature():
    pass

  def normalizedType():
    pass

  def property():
    pass

  def propertyCount():
    pass

  def propertyOffset():
    pass

  def superClass():
    pass

  def userProperty():
    pass

class QMetaProperty(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def enumerator():
    pass

  def hasNotifySignal():
    pass

  def hasStdCppSet():
    pass

  def isConstant():
    pass

  def isDesignable():
    pass

  def isEditable():
    pass

  def isEnumType():
    pass

  def isFinal():
    pass

  def isFlagType():
    pass

  def isReadable():
    pass

  def isResettable():
    pass

  def isScriptable():
    pass

  def isStored():
    pass

  def isUser():
    pass

  def isValid():
    pass

  def isWritable():
    pass

  def name():
    pass

  def notifySignal():
    pass

  def notifySignalIndex():
    pass

  def propertyIndex():
    pass

  def read():
    pass

  def reset():
    pass

  def revision():
    pass

  def type():
    pass

  def typeName():
    pass

  def userType():
    pass

  def write():
    pass

class QMimeData(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clear():
    pass

  def colorData():
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

  def formats():
    pass

  def hasColor():
    pass

  def hasFormat():
    pass

  def hasHtml():
    pass

  def hasImage():
    pass

  def hasText():
    pass

  def hasUrls():
    pass

  def html():
    pass

  def imageData():
    pass

  def registerUserData():
    pass

  def removeFormat():
    pass

  def retrieveData():
    pass

  def setColorData():
    pass

  def setData():
    pass

  def setHtml():
    pass

  def setImageData():
    pass

  def setText():
    pass

  def setUrls():
    pass

  staticMetaObject = None

  def text():
    pass

  def urls():
    pass

class QModelIndex(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def child():
    pass

  def column():
    pass

  def data():
    pass

  def flags():
    pass

  def internalId():
    pass

  def internalPointer():
    pass

  def isValid():
    pass

  def model():
    pass

  def parent():
    pass

  def row():
    pass

  def sibling():
    pass

class QMutex(Object):

  NonRecursive = None

  class RecursionMode(object):

    NonRecursive = None
    Recursive = None
    name = property(None, None, None,
                    )

    values = {}

  Recursive = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def lock():
    pass

  def lockInline():
    pass

  def tryLock():
    pass

  def tryLockInline():
    pass

  def unlock():
    pass

  def unlockInline():
    pass

class QMutexLocker(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def mutex():
    pass

  def relock():
    pass

  def unlock():
    pass

class QObject(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def blockSignals():
    pass

  def childEvent():
    pass

  def children():
    pass

  def connect():
    pass

  def connectNotify():
    pass

  def customEvent():
    pass

  def deleteLater():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def disconnectNotify():
    pass

  def dumpObjectInfo():
    pass

  def dumpObjectTree():
    pass

  def dynamicPropertyNames():
    pass

  def emit():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def findChild():
    pass

  def findChildren():
    pass

  def inherits():
    pass

  def installEventFilter():
    pass

  def isWidgetType():
    pass

  def killTimer():
    pass

  def metaObject():
    pass

  def moveToThread():
    pass

  def objectName():
    pass

  def parent():
    pass

  def property():
    pass

  def receivers():
    pass

  def registerUserData():
    pass

  def removeEventFilter():
    pass

  def sender():
    pass

  def senderSignalIndex():
    pass

  def setObjectName():
    pass

  def setParent():
    pass

  def setProperty():
    pass

  def signalsBlocked():
    pass

  def startTimer():
    pass

  staticMetaObject = None

  def thread():
    pass

  def timerEvent():
    pass

  def tr():
    pass

  def trUtf8():
    pass

class QParallelAnimationGroup(QAnimationGroup):

  Backward = None
  DeleteWhenStopped = None
  Forward = None
  KeepWhenStopped = None
  Paused = None
  Running = None
  Stopped = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentLoopChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def directionChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def duration():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def registerUserData():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def updateCurrentTime():
    pass

  def updateDirection():
    pass

  def updateState():
    pass

class QPauseAnimation(QAbstractAnimation):

  Backward = None
  DeleteWhenStopped = None
  Forward = None
  KeepWhenStopped = None
  Paused = None
  Running = None
  Stopped = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentLoopChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def directionChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def duration():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setDuration():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def updateCurrentTime():
    pass

class QPersistentModelIndex(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def child():
    pass

  def column():
    pass

  def data():
    pass

  def flags():
    pass

  def internalId():
    pass

  def internalPointer():
    pass

  def isValid():
    pass

  def model():
    pass

  def parent():
    pass

  def row():
    pass

  def sibling():
    pass

class QPluginLoader(QObject):

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

  def errorString():
    pass

  def fileName():
    pass

  def instance():
    pass

  def isLoaded():
    pass

  def load():
    pass

  def registerUserData():
    pass

  def setFileName():
    pass

  def staticInstances():
    pass

  staticMetaObject = None

  def unload():
    pass

class QPoint(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def isNull():
    pass

  def manhattanLength():
    pass

  def setX():
    pass

  def setY():
    pass

  def toTuple():
    pass

  def x():
    pass

  def y():
    pass

class QPointF(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def isNull():
    pass

  def manhattanLength():
    pass

  def setX():
    pass

  def setY():
    pass

  def toPoint():
    pass

  def toTuple():
    pass

  def x():
    pass

  def y():
    pass

class QProcess(QIODevice):

  Append = None
  CrashExit = None
  Crashed = None

  class ExitStatus(object):

    CrashExit = None
    NormalExit = None
    name = property(None, None, None,
                    )

    values = {}

  FailedToStart = None
  ForwardedChannels = None
  MergedChannels = None
  NormalExit = None
  NotOpen = None
  NotRunning = None
  class ProcessChannel(object):

    StandardError = None
    StandardOutput = None
    name = property(None, None, None,
                    )

    values = {}

  class ProcessChannelMode(object):

    ForwardedChannels = None
    MergedChannels = None
    SeparateChannels = None
    name = property(None, None, None,
                    )

    values = {}

  class ProcessError(object):

    Crashed = None
    FailedToStart = None
    ReadError = None
    Timedout = None
    UnknownError = None
    WriteError = None
    name = property(None, None, None,
                    )

    values = {}

  class ProcessState(object):

    NotRunning = None
    Running = None
    Starting = None
    name = property(None, None, None,
                    )

    values = {}

  ReadError = None
  ReadOnly = None
  ReadWrite = None
  Running = None
  SeparateChannels = None
  StandardError = None
  StandardOutput = None
  Starting = None
  Text = None
  Timedout = None
  Truncate = None
  Unbuffered = None
  UnknownError = None
  WriteError = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToClose():
    """ Signal """
    pass

  def atEnd():
    pass

  def bytesAvailable():
    pass

  def bytesToWrite():
    pass

  def bytesWritten():
    """ Signal """
    pass

  def canReadLine():
    pass

  def close():
    pass

  def closeReadChannel():
    pass

  def closeWriteChannel():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def environment():
    pass

  def error():
    """ Signal """
    pass

  def execute():
    pass

  def exitCode():
    pass

  def exitStatus():
    pass

  def finished():
    """ Signal """
    pass

  def isSequential():
    pass

  def kill():
    pass

  def pid():
    pass

  def processChannelMode():
    pass

  def processEnvironment():
    pass

  def readAllStandardError():
    pass

  def readAllStandardOutput():
    pass

  def readChannel():
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readData():
    pass

  def readyRead():
    """ Signal """
    pass

  def readyReadStandardError():
    """ Signal """
    pass

  def readyReadStandardOutput():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setEnvironment():
    pass

  def setProcessChannelMode():
    pass

  def setProcessEnvironment():
    pass

  def setProcessState():
    pass

  def setReadChannel():
    pass

  def setStandardErrorFile():
    pass

  def setStandardInputFile():
    pass

  def setStandardOutputFile():
    pass

  def setStandardOutputProcess():
    pass

  def setWorkingDirectory():
    pass

  def setupChildProcess():
    pass

  def start():
    pass

  def startDetached():
    pass

  def started():
    """ Signal """
    pass

  def state():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def systemEnvironment():
    pass

  def terminate():
    pass

  def waitForBytesWritten():
    pass

  def waitForFinished():
    pass

  def waitForReadyRead():
    pass

  def waitForStarted():
    pass

  def workingDirectory():
    pass

  def writeData():
    pass

class QProcessEnvironment(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clear():
    pass

  def contains():
    pass

  def insert():
    pass

  def isEmpty():
    pass

  def keys():
    pass

  def remove():
    pass

  def systemEnvironment():
    pass

  def toStringList():
    pass

  def value():
    pass

class QPropertyAnimation(QVariantAnimation):

  Backward = None
  DeleteWhenStopped = None
  Forward = None
  KeepWhenStopped = None
  Paused = None
  Running = None
  Stopped = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentLoopChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def directionChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def propertyName():
    pass

  def registerUserData():
    pass

  def setPropertyName():
    pass

  def setTargetObject():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def targetObject():
    pass

  def updateCurrentValue():
    pass

  def updateState():
    pass

  def valueChanged():
    """ Signal """
    pass

class QReadLocker(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def readWriteLock():
    pass

  def relock():
    pass

  def unlock():
    pass

class QReadWriteLock(Object):

  NonRecursive = None

  class RecursionMode(object):

    NonRecursive = None
    Recursive = None
    name = property(None, None, None,
                    )

    values = {}

  Recursive = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def lockForRead():
    pass

  def lockForWrite():
    pass

  def tryLockForRead():
    pass

  def tryLockForWrite():
    pass

  def unlock():
    pass

class QRect(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def adjust():
    pass

  def adjusted():
    pass

  def bottom():
    pass

  def bottomLeft():
    pass

  def bottomRight():
    pass

  def center():
    pass

  def contains():
    pass

  def getCoords():
    pass

  def getRect():
    pass

  def height():
    pass

  def intersect():
    pass

  def intersected():
    pass

  def intersects():
    pass

  def isEmpty():
    pass

  def isNull():
    pass

  def isValid():
    pass

  def left():
    pass

  def moveBottom():
    pass

  def moveBottomLeft():
    pass

  def moveBottomRight():
    pass

  def moveCenter():
    pass

  def moveLeft():
    pass

  def moveRight():
    pass

  def moveTo():
    pass

  def moveTop():
    pass

  def moveTopLeft():
    pass

  def moveTopRight():
    pass

  def normalized():
    pass

  def right():
    pass

  def setBottom():
    pass

  def setBottomLeft():
    pass

  def setBottomRight():
    pass

  def setCoords():
    pass

  def setHeight():
    pass

  def setLeft():
    pass

  def setRect():
    pass

  def setRight():
    pass

  def setSize():
    pass

  def setTop():
    pass

  def setTopLeft():
    pass

  def setTopRight():
    pass

  def setWidth():
    pass

  def setX():
    pass

  def setY():
    pass

  def size():
    pass

  def top():
    pass

  def topLeft():
    pass

  def topRight():
    pass

  def translate():
    pass

  def translated():
    pass

  def unite():
    pass

  def united():
    pass

  def width():
    pass

  def x():
    pass

  def y():
    pass

class QRectF(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def adjust():
    pass

  def adjusted():
    pass

  def bottom():
    pass

  def bottomLeft():
    pass

  def bottomRight():
    pass

  def center():
    pass

  def contains():
    pass

  def getCoords():
    pass

  def getRect():
    pass

  def height():
    pass

  def intersect():
    pass

  def intersected():
    pass

  def intersects():
    pass

  def isEmpty():
    pass

  def isNull():
    pass

  def isValid():
    pass

  def left():
    pass

  def moveBottom():
    pass

  def moveBottomLeft():
    pass

  def moveBottomRight():
    pass

  def moveCenter():
    pass

  def moveLeft():
    pass

  def moveRight():
    pass

  def moveTo():
    pass

  def moveTop():
    pass

  def moveTopLeft():
    pass

  def moveTopRight():
    pass

  def normalized():
    pass

  def right():
    pass

  def setBottom():
    pass

  def setBottomLeft():
    pass

  def setBottomRight():
    pass

  def setCoords():
    pass

  def setHeight():
    pass

  def setLeft():
    pass

  def setRect():
    pass

  def setRight():
    pass

  def setSize():
    pass

  def setTop():
    pass

  def setTopLeft():
    pass

  def setTopRight():
    pass

  def setWidth():
    pass

  def setX():
    pass

  def setY():
    pass

  def size():
    pass

  def toAlignedRect():
    pass

  def toRect():
    pass

  def top():
    pass

  def topLeft():
    pass

  def topRight():
    pass

  def translate():
    pass

  def translated():
    pass

  def unite():
    pass

  def united():
    pass

  def width():
    pass

  def x():
    pass

  def y():
    pass

class QRegExp(Object):

  CaretAtOffset = None
  CaretAtZero = None

  class CaretMode(object):

    CaretAtOffset = None
    CaretAtZero = None
    CaretWontMatch = None
    name = property(None, None, None,
                    )

    values = {}

  CaretWontMatch = None
  FixedString = None

  class PatternSyntax(object):

    FixedString = None
    RegExp = None
    RegExp2 = None
    W3CXmlSchema11 = None
    Wildcard = None
    WildcardUnix = None
    name = property(None, None, None,
                    )

    values = {}

  RegExp = None
  RegExp2 = None
  W3CXmlSchema11 = None
  Wildcard = None
  WildcardUnix = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cap():
    pass

  def captureCount():
    pass

  def capturedTexts():
    pass

  def caseSensitivity():
    pass

  def errorString():
    pass

  def escape():
    pass

  def exactMatch():
    pass

  def indexIn():
    pass

  def isEmpty():
    pass

  def isMinimal():
    pass

  def isValid():
    pass

  def lastIndexIn():
    pass

  def matchedLength():
    pass

  def numCaptures():
    pass

  def pattern():
    pass

  def patternSyntax():
    pass

  def pos():
    pass

  def replace():
    pass

  def setCaseSensitivity():
    pass

  def setMinimal():
    pass

  def setPattern():
    pass

  def setPatternSyntax():
    pass

  def swap():
    pass

class QResource(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def absoluteFilePath():
    pass

  def addSearchPath():
    pass

  def children():
    pass

  def data():
    pass

  def fileName():
    pass

  def isCompressed():
    pass

  def isDir():
    pass

  def isFile():
    pass

  def isValid():
    pass

  def locale():
    pass

  def registerResource():
    pass

  def registerResourceData():
    pass

  def searchPaths():
    pass

  def setFileName():
    pass

  def setLocale():
    pass

  def size():
    pass

  def unregisterResource():
    pass

  def unregisterResourceData():
    pass

class QRunnable(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def autoDelete():
    pass

  def run():
    pass

  def setAutoDelete():
    pass

class QSemaphore(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def acquire():
    pass

  def available():
    pass

  def release():
    pass

  def tryAcquire():
    pass

class QSequentialAnimationGroup(QAnimationGroup):

  Backward = None
  DeleteWhenStopped = None
  Forward = None
  KeepWhenStopped = None
  Paused = None
  Running = None
  Stopped = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addPause():
    pass

  def connect():
    pass

  def currentAnimation():
    pass

  def currentAnimationChanged():
    """ Signal """
    pass

  def currentLoopChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def directionChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def duration():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def insertPause():
    pass

  def registerUserData():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def updateCurrentTime():
    pass

  def updateDirection():
    pass

  def updateState():
    pass

class QSettings(QObject):

  AccessError = None
  CustomFormat1 = None
  CustomFormat10 = None
  CustomFormat11 = None
  CustomFormat12 = None
  CustomFormat13 = None
  CustomFormat14 = None
  CustomFormat15 = None
  CustomFormat16 = None
  CustomFormat2 = None
  CustomFormat3 = None
  CustomFormat4 = None
  CustomFormat5 = None
  CustomFormat6 = None
  CustomFormat7 = None
  CustomFormat8 = None
  CustomFormat9 = None

  class Format(object):

    CustomFormat1 = None
    CustomFormat10 = None
    CustomFormat11 = None
    CustomFormat12 = None
    CustomFormat13 = None
    CustomFormat14 = None
    CustomFormat15 = None
    CustomFormat16 = None
    CustomFormat2 = None
    CustomFormat3 = None
    CustomFormat4 = None
    CustomFormat5 = None
    CustomFormat6 = None
    CustomFormat7 = None
    CustomFormat8 = None
    CustomFormat9 = None
    IniFormat = None
    InvalidFormat = None
    NativeFormat = None
    name = property(None, None, None,
                    )

    values = {}

  FormatError = None
  IniFormat = None
  InvalidFormat = None
  NativeFormat = None
  NoError = None

  class Scope(object):

    SystemScope = None
    UserScope = None
    name = property(None, None, None,
                    )

    values = {}

  class Status(object):

    AccessError = None
    FormatError = None
    NoError = None
    name = property(None, None, None,
                    )

    values = {}

  SystemScope = None
  UserScope = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def allKeys():
    pass

  def applicationName():
    pass

  def beginGroup():
    pass

  def beginReadArray():
    pass

  def beginWriteArray():
    pass

  def childGroups():
    pass

  def childKeys():
    pass

  def clear():
    pass

  def connect():
    pass

  def contains():
    pass

  def defaultFormat():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def endArray():
    pass

  def endGroup():
    pass

  def event():
    pass

  def fallbacksEnabled():
    pass

  def fileName():
    pass

  def format():
    pass

  def group():
    pass

  def iniCodec():
    pass

  def isWritable():
    pass

  def organizationName():
    pass

  def registerUserData():
    pass

  def remove():
    pass

  def scope():
    pass

  def setArrayIndex():
    pass

  def setDefaultFormat():
    pass

  def setFallbacksEnabled():
    pass

  def setIniCodec():
    pass

  def setPath():
    pass

  def setValue():
    pass

  staticMetaObject = None

  def status():
    pass

  def sync():
    pass

  def value():
    pass

class QSignalMapper(QObject):

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

  def map():
    pass

  def mapped():
    """ Signal """
    pass

  def mapping():
    pass

  def registerUserData():
    pass

  def removeMappings():
    pass

  def setMapping():
    pass

  staticMetaObject = None

class QSignalTransition(QAbstractTransition):

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

  def event():
    pass

  def eventTest():
    pass

  def onTransition():
    pass

  def registerUserData():
    pass

  def senderObject():
    pass

  def setSenderObject():
    pass

  def setSignal():
    pass

  def signal():
    pass

  staticMetaObject = None

  def triggered():
    """ Signal """
    pass

class QSize(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundedTo():
    pass

  def expandedTo():
    pass

  def height():
    pass

  def isEmpty():
    pass

  def isNull():
    pass

  def isValid():
    pass

  def scale():
    pass

  def setHeight():
    pass

  def setWidth():
    pass

  def toTuple():
    pass

  def transpose():
    pass

  def width():
    pass

class QSizeF(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundedTo():
    pass

  def expandedTo():
    pass

  def height():
    pass

  def isEmpty():
    pass

  def isNull():
    pass

  def isValid():
    pass

  def scale():
    pass

  def setHeight():
    pass

  def setWidth():
    pass

  def toSize():
    pass

  def toTuple():
    pass

  def transpose():
    pass

  def width():
    pass

class QSocketNotifier(QObject):

  Exception = None
  Read = None

  class Type(object):

    Exception = None
    Read = None
    Write = None
    name = property(None, None, None,
                    )

    values = {}

  Write = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activated():
    """ Signal """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def isEnabled():
    pass

  def registerUserData():
    pass

  def setEnabled():
    pass

  def socket():
    pass

  staticMetaObject = None

  def type():
    pass

class QSortFilterProxyModel(QAbstractProxyModel):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def buddy():
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

  def disconnect():
    pass

  def dropMimeData():
    pass

  def dynamicSortFilter():
    pass

  def fetchMore():
    pass

  def filterAcceptsColumn():
    pass

  def filterAcceptsRow():
    pass

  def filterCaseSensitivity():
    pass

  def filterKeyColumn():
    pass

  def filterRegExp():
    pass

  def filterRole():
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

  def index():
    pass

  def insertColumns():
    pass

  def insertRows():
    pass

  def invalidate():
    pass

  def invalidateFilter():
    pass

  def isSortLocaleAware():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def lessThan():
    pass

  def mapFromSource():
    pass

  def mapSelectionFromSource():
    pass

  def mapSelectionToSource():
    pass

  def mapToSource():
    pass

  def match():
    pass

  def mimeData():
    pass

  def mimeTypes():
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def parent():
    pass

  def registerUserData():
    pass

  def removeColumns():
    pass

  def removeRows():
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

  def setDynamicSortFilter():
    pass

  def setFilterCaseSensitivity():
    pass

  def setFilterFixedString():
    pass

  def setFilterKeyColumn():
    pass

  def setFilterRegExp():
    pass

  def setFilterRole():
    pass

  def setFilterWildcard():
    pass

  def setHeaderData():
    pass

  def setSortCaseSensitivity():
    pass

  def setSortLocaleAware():
    pass

  def setSortRole():
    pass

  def setSourceModel():
    pass

  def sort():
    pass

  def sortCaseSensitivity():
    pass

  def sortColumn():
    pass

  def sortOrder():
    pass

  def sortRole():
    pass

  def span():
    pass

  staticMetaObject = None

  def supportedDropActions():
    pass

class QState(QAbstractState):

  class ChildMode(object):

    ExclusiveStates = None
    ParallelStates = None
    name = property(None, None, None,
                    )

    values = {}

  ExclusiveStates = None
  ParallelStates = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addTransition():
    pass

  def assignProperty():
    pass

  def childMode():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def entered():
    """ Signal """
    pass

  def errorState():
    pass

  def event():
    pass

  def exited():
    """ Signal """
    pass

  def finished():
    """ Signal """
    pass

  def initialState():
    pass

  def onEntry():
    pass

  def onExit():
    pass

  def propertiesAssigned():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeTransition():
    pass

  def setChildMode():
    pass

  def setErrorState():
    pass

  def setInitialState():
    pass

  staticMetaObject = None

  def transitions():
    pass

class QStateMachine(QState):

  DontRestoreProperties = None

  class Error(object):

    NoCommonAncestorForTransitionError = None
    NoDefaultStateInHistoryStateError = None
    NoError = None
    NoInitialStateError = None
    name = property(None, None, None,
                    )

    values = {}

  class EventPriority(object):

    HighPriority = None
    NormalPriority = None
    name = property(None, None, None,
                    )

    values = {}

  ExclusiveStates = None
  HighPriority = None
  NoCommonAncestorForTransitionError = None
  NoDefaultStateInHistoryStateError = None
  NoError = None
  NoInitialStateError = None
  NormalPriority = None
  ParallelStates = None

  class RestorePolicy(object):

    DontRestoreProperties = None
    RestoreProperties = None
    name = property(None, None, None,
                    )

    values = {}

  RestoreProperties = None

  class SignalEvent(QEvent):

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

    def arguments():
      pass

    def registerEventType():
      pass

    def sender():
      pass

    def signalIndex():
      pass

  class WrappedEvent(QEvent):

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

    def event():
      pass

    def object():
      pass

    def registerEventType():
      pass

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addDefaultAnimation():
    pass

  def addState():
    pass

  def beginMicrostep():
    pass

  def beginSelectTransitions():
    pass

  def cancelDelayedEvent():
    pass

  def clearError():
    pass

  def configuration():
    pass

  def connect():
    pass

  def defaultAnimations():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def endMicrostep():
    pass

  def endSelectTransitions():
    pass

  def entered():
    """ Signal """
    pass

  def error():
    pass

  def errorString():
    pass

  def event():
    pass

  def eventFilter():
    pass

  def exited():
    """ Signal """
    pass

  def finished():
    """ Signal """
    pass

  def globalRestorePolicy():
    pass

  def isAnimated():
    pass

  def isRunning():
    pass

  def onEntry():
    pass

  def onExit():
    pass

  def postDelayedEvent():
    pass

  def postEvent():
    pass

  def propertiesAssigned():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeDefaultAnimation():
    pass

  def removeState():
    pass

  def setAnimated():
    pass

  def setGlobalRestorePolicy():
    pass

  def start():
    pass

  def started():
    """ Signal """
    pass

  staticMetaObject = None

  def stop():
    pass

  def stopped():
    """ Signal """
    pass

class QStringListModel(QAbstractListModel):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
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

  def flags():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def insertRows():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeRows():
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

  def setStringList():
    pass

  def sort():
    pass

  staticMetaObject = None

  def stringList():
    pass

  def supportedDropActions():
    pass

class QSysInfo(Object):

  BigEndian = None
  ByteOrder = None

  class Endian(object):

    BigEndian = None
    ByteOrder = None
    LittleEndian = None
    name = property(None, None, None,
                    )

    values = {}

  LittleEndian = None

  class Sizes(object):

    WordSize = None
    name = property(None, None, None,
                    )

    values = {}

  WordSize = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

class QSystemSemaphore(Object):

  class AccessMode(object):

    Create = None
    Open = None
    name = property(None, None, None,
                    )

    values = {}

  AlreadyExists = None
  Create = None
  KeyError = None
  NoError = None
  NotFound = None
  Open = None
  OutOfResources = None
  PermissionDenied = None

  class SystemSemaphoreError(object):

    AlreadyExists = None
    KeyError = None
    NoError = None
    NotFound = None
    OutOfResources = None
    PermissionDenied = None
    UnknownError = None
    name = property(None, None, None,
                    )

    values = {}

  UnknownError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def acquire():
    pass

  def error():
    pass

  def errorString():
    pass

  def key():
    pass

  def release():
    pass

  def setKey():
    pass

def QT_TRANSLATE_NOOP():
  pass

def QT_TR_NOOP():
  pass

def QT_TR_NOOP_UTF8():
  pass

class QTemporaryFile(QFile):

  AbortError = None
  Append = None
  AutoCloseHandle = None
  CopyError = None
  DontCloseHandle = None
  ExeGroup = None
  ExeOther = None
  ExeOwner = None
  ExeUser = None
  FatalError = None
  NoError = None
  NoOptions = None
  NotOpen = None
  OpenError = None
  PermissionsError = None
  PositionError = None
  ReadError = None
  ReadGroup = None
  ReadOnly = None
  ReadOther = None
  ReadOwner = None
  ReadUser = None
  ReadWrite = None
  RemoveError = None
  RenameError = None
  ResizeError = None
  ResourceError = None
  Text = None
  TimeOutError = None
  Truncate = None
  Unbuffered = None
  UnspecifiedError = None
  WriteError = None
  WriteGroup = None
  WriteOnly = None
  WriteOther = None
  WriteOwner = None
  WriteUser = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToClose():
    """ Signal """
    pass

  def autoRemove():
    pass

  def bytesWritten():
    """ Signal """
    pass

  def connect():
    pass

  def copy():
    pass

  def createLocalFile():
    pass

  def decodeName():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def encodeName():
    pass

  def exists():
    pass

  def fileEngine():
    pass

  def fileName():
    pass

  def fileTemplate():
    pass

  def link():
    pass

  def open():
    pass

  def permissions():
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readLink():
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def remove():
    pass

  def rename():
    pass

  def resize():
    pass

  def setAutoRemove():
    pass

  def setFileTemplate():
    pass

  def setPermissions():
    pass

  staticMetaObject = None

  def symLinkTarget():
    pass

class QTextBoundaryFinder(Object):

  class BoundaryReason(object):

    EndWord = None
    NotAtBoundary = None
    StartWord = None
    name = property(None, None, None,
                    )

    values = {}

  class BoundaryReasons(object):

    pass

  class BoundaryType(object):

    Grapheme = None
    Line = None
    Sentence = None
    Word = None
    name = property(None, None, None,
                    )

    values = {}

  EndWord = None
  Grapheme = None
  Line = None
  NotAtBoundary = None
  Sentence = None
  StartWord = None
  Word = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundaryReasons():
    pass

  def isAtBoundary():
    pass

  def isValid():
    pass

  def position():
    pass

  def setPosition():
    pass

  def string():
    pass

  def toEnd():
    pass

  def toNextBoundary():
    pass

  def toPreviousBoundary():
    pass

  def toStart():
    pass

  def type():
    pass

class QTextCodec(Object):

  class ConversionFlag(object):

    ConvertInvalidToNull = None
    DefaultConversion = None
    FreeFunction = None
    IgnoreHeader = None
    name = property(None, None, None,
                    )

    values = {}

  class ConversionFlags(object):

    pass

  ConvertInvalidToNull = None

  class ConverterState(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    flags = property(None, None, None,
                     )

    invalidChars = property(None, None, None,
                            )

    remainingChars = property(None, None, None,
                              )


  DefaultConversion = None
  FreeFunction = None
  IgnoreHeader = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aliases():
    pass

  def availableCodecs():
    pass

  def availableMibs():
    pass

  def canEncode():
    pass

  def codecForCStrings():
    pass

  def codecForHtml():
    pass

  def codecForLocale():
    pass

  def codecForMib():
    pass

  def codecForName():
    pass

  def codecForTr():
    pass

  def codecForUtfText():
    pass

  def convertToUnicode():
    pass

  def fromUnicode():
    pass

  def makeDecoder():
    pass

  def makeEncoder():
    pass

  def mibEnum():
    pass

  def name():
    pass

  def setCodecForCStrings():
    pass

  def setCodecForLocale():
    pass

  def setCodecForTr():
    pass

  def toUnicode():
    pass

class QTextDecoder(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def hasFailure():
    pass

  def toUnicode():
    pass

class QTextEncoder(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def fromUnicode():
    pass

  def hasFailure():
    pass

class QTextStream(Object):

  AlignAccountingStyle = None
  AlignCenter = None
  AlignLeft = None
  AlignRight = None

  class FieldAlignment(object):

    AlignAccountingStyle = None
    AlignCenter = None
    AlignLeft = None
    AlignRight = None
    name = property(None, None, None,
                    )

    values = {}

  FixedNotation = None
  ForcePoint = None
  ForceSign = None

  class NumberFlag(object):

    ForcePoint = None
    ForceSign = None
    ShowBase = None
    UppercaseBase = None
    UppercaseDigits = None
    name = property(None, None, None,
                    )

    values = {}

  class NumberFlags(object):

    pass

  Ok = None
  ReadCorruptData = None
  ReadPastEnd = None

  class RealNumberNotation(object):

    FixedNotation = None
    ScientificNotation = None
    SmartNotation = None
    name = property(None, None, None,
                    )

    values = {}

  ScientificNotation = None
  ShowBase = None
  SmartNotation = None

  class Status(object):

    Ok = None
    ReadCorruptData = None
    ReadPastEnd = None
    WriteFailed = None
    name = property(None, None, None,
                    )

    values = {}

  UppercaseBase = None
  UppercaseDigits = None
  WriteFailed = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def atEnd():
    pass

  def autoDetectUnicode():
    pass

  def codec():
    pass

  def device():
    pass

  def fieldAlignment():
    pass

  def fieldWidth():
    pass

  def flush():
    pass

  def generateByteOrderMark():
    pass

  def integerBase():
    pass

  def locale():
    pass

  def numberFlags():
    pass

  def padChar():
    pass

  def pos():
    pass

  def read():
    pass

  def readAll():
    pass

  def readLine():
    pass

  def realNumberNotation():
    pass

  def realNumberPrecision():
    pass

  def reset():
    pass

  def resetStatus():
    pass

  def seek():
    pass

  def setAutoDetectUnicode():
    pass

  def setCodec():
    pass

  def setDevice():
    pass

  def setFieldAlignment():
    pass

  def setFieldWidth():
    pass

  def setGenerateByteOrderMark():
    pass

  def setIntegerBase():
    pass

  def setLocale():
    pass

  def setNumberFlags():
    pass

  def setPadChar():
    pass

  def setRealNumberNotation():
    pass

  def setRealNumberPrecision():
    pass

  def setStatus():
    pass

  def skipWhiteSpace():
    pass

  def status():
    pass

  def string():
    pass

class QTextStreamManipulator(Object):

  def exec_():
    pass

class QThread(QObject):

  HighPriority = None
  HighestPriority = None
  IdlePriority = None
  InheritPriority = None
  LowPriority = None
  LowestPriority = None
  NormalPriority = None

  class Priority(object):

    HighPriority = None
    HighestPriority = None
    IdlePriority = None
    InheritPriority = None
    LowPriority = None
    LowestPriority = None
    NormalPriority = None
    TimeCriticalPriority = None
    name = property(None, None, None,
                    )

    values = {}

  TimeCriticalPriority = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentThread():
    pass

  def currentThreadId():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def exec_():
    pass

  def exit():
    pass

  def finished():
    """ Signal """
    pass

  def idealThreadCount():
    pass

  def isFinished():
    pass

  def isRunning():
    pass

  def msleep():
    pass

  def priority():
    pass

  def quit():
    pass

  def registerUserData():
    pass

  def run():
    pass

  def setPriority():
    pass

  def setStackSize():
    pass

  def setTerminationEnabled():
    pass

  def sleep():
    pass

  def stackSize():
    pass

  def start():
    pass

  def started():
    """ Signal """
    pass

  staticMetaObject = None

  def terminate():
    pass

  def terminated():
    """ Signal """
    pass

  def usleep():
    pass

  def wait():
    pass

  def yieldCurrentThread():
    pass

class QThreadPool(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activeThreadCount():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def expiryTimeout():
    pass

  def globalInstance():
    pass

  def maxThreadCount():
    pass

  def registerUserData():
    pass

  def releaseThread():
    pass

  def reserveThread():
    pass

  def setExpiryTimeout():
    pass

  def setMaxThreadCount():
    pass

  def start():
    pass

  staticMetaObject = None

  def tryStart():
    pass

  def waitForDone():
    pass

class QTime(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addMSecs():
    pass

  def addSecs():
    pass

  def currentTime():
    pass

  def elapsed():
    pass

  def fromString():
    pass

  def hour():
    pass

  def isNull():
    pass

  def isValid():
    pass

  def minute():
    pass

  def msec():
    pass

  def msecsTo():
    pass

  def restart():
    pass

  def second():
    pass

  def secsTo():
    pass

  def setHMS():
    pass

  def start():
    pass

  def toPython():
    pass

  def toString():
    pass

class QTimeLine(QObject):

  Backward = None
  CosineCurve = None

  class CurveShape(object):

    CosineCurve = None
    EaseInCurve = None
    EaseInOutCurve = None
    EaseOutCurve = None
    LinearCurve = None
    SineCurve = None
    name = property(None, None, None,
                    )

    values = {}

  class Direction(object):

    Backward = None
    Forward = None
    name = property(None, None, None,
                    )

    values = {}

  EaseInCurve = None
  EaseInOutCurve = None
  EaseOutCurve = None
  Forward = None
  LinearCurve = None
  NotRunning = None
  Paused = None
  Running = None
  SineCurve = None

  class State(object):

    NotRunning = None
    Paused = None
    Running = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentFrame():
    pass

  def currentTime():
    pass

  def currentValue():
    pass

  def curveShape():
    pass

  def destroyed():
    """ Signal """
    pass

  def direction():
    pass

  def disconnect():
    pass

  def duration():
    pass

  def easingCurve():
    pass

  def endFrame():
    pass

  def finished():
    """ Signal """
    pass

  def frameChanged():
    """ Signal """
    pass

  def frameForTime():
    pass

  def loopCount():
    pass

  def registerUserData():
    pass

  def resume():
    pass

  def setCurrentTime():
    pass

  def setCurveShape():
    pass

  def setDirection():
    pass

  def setDuration():
    pass

  def setEasingCurve():
    pass

  def setEndFrame():
    pass

  def setFrameRange():
    pass

  def setLoopCount():
    pass

  def setPaused():
    pass

  def setStartFrame():
    pass

  def setUpdateInterval():
    pass

  def start():
    pass

  def startFrame():
    pass

  def state():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def stop():
    pass

  def timerEvent():
    pass

  def toggleDirection():
    pass

  def updateInterval():
    pass

  def valueChanged():
    """ Signal """
    pass

  def valueForTime():
    pass

class QTimer(QObject):

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

  def interval():
    pass

  def isActive():
    pass

  def isSingleShot():
    pass

  def killTimer():
    pass

  def registerUserData():
    pass

  def setInterval():
    pass

  def setSingleShot():
    pass

  def singleShot():
    pass

  def start():
    pass

  def startTimer():
    pass

  staticMetaObject = None

  def stop():
    pass

  def timeout():
    """ Signal """
    pass

  def timerEvent():
    pass

  def timerId():
    pass

class QTimerEvent(QEvent):

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

  def timerId():
    pass

class QTranslator(QObject):

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

  def isEmpty():
    pass

  def load():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

  def translate():
    pass

class QUrl(Object):

  class FormattingOption(object):

    None = None
    RemoveAuthority = None
    RemoveFragment = None
    RemovePassword = None
    RemovePath = None
    RemovePort = None
    RemoveQuery = None
    RemoveScheme = None
    RemoveUserInfo = None
    StripTrailingSlash = None
    name = property(None, None, None,
                    )

    values = {}

  class FormattingOptions(object):

    pass

  None = None

  class ParsingMode(object):

    StrictMode = None
    TolerantMode = None
    name = property(None, None, None,
                    )

    values = {}

  RemoveAuthority = None
  RemoveFragment = None
  RemovePassword = None
  RemovePath = None
  RemovePort = None
  RemoveQuery = None
  RemoveScheme = None
  RemoveUserInfo = None
  StrictMode = None
  StripTrailingSlash = None
  TolerantMode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addEncodedQueryItem():
    pass

  def addQueryItem():
    pass

  def allEncodedQueryItemValues():
    pass

  def allQueryItemValues():
    pass

  def authority():
    pass

  def clear():
    pass

  def encodedFragment():
    pass

  def encodedHost():
    pass

  def encodedPassword():
    pass

  def encodedPath():
    pass

  def encodedQuery():
    pass

  def encodedQueryItemValue():
    pass

  def encodedQueryItems():
    pass

  def encodedUserName():
    pass

  def errorString():
    pass

  def fragment():
    pass

  def fromAce():
    pass

  def fromEncoded():
    pass

  def fromLocalFile():
    pass

  def fromPercentEncoding():
    pass

  def fromPunycode():
    pass

  def fromUserInput():
    pass

  def hasEncodedQueryItem():
    pass

  def hasFragment():
    pass

  def hasQuery():
    pass

  def hasQueryItem():
    pass

  def host():
    pass

  def idnWhitelist():
    pass

  def isEmpty():
    pass

  def isLocalFile():
    pass

  def isParentOf():
    pass

  def isRelative():
    pass

  def isValid():
    pass

  def password():
    pass

  def path():
    pass

  def port():
    pass

  def queryItemValue():
    pass

  def queryItems():
    pass

  def queryPairDelimiter():
    pass

  def queryValueDelimiter():
    pass

  def removeAllEncodedQueryItems():
    pass

  def removeAllQueryItems():
    pass

  def removeEncodedQueryItem():
    pass

  def removeQueryItem():
    pass

  def resolved():
    pass

  def scheme():
    pass

  def setAuthority():
    pass

  def setEncodedFragment():
    pass

  def setEncodedHost():
    pass

  def setEncodedPassword():
    pass

  def setEncodedPath():
    pass

  def setEncodedQuery():
    pass

  def setEncodedQueryItems():
    pass

  def setEncodedUrl():
    pass

  def setEncodedUserName():
    pass

  def setFragment():
    pass

  def setHost():
    pass

  def setIdnWhitelist():
    pass

  def setPassword():
    pass

  def setPath():
    pass

  def setPort():
    pass

  def setQueryDelimiters():
    pass

  def setQueryItems():
    pass

  def setScheme():
    pass

  def setUrl():
    pass

  def setUserInfo():
    pass

  def setUserName():
    pass

  def swap():
    pass

  def toAce():
    pass

  def toEncoded():
    pass

  def toLocalFile():
    pass

  def toPercentEncoding():
    pass

  def toPunycode():
    pass

  def toString():
    pass

  def topLevelDomain():
    pass

  def userInfo():
    pass

  def userName():
    pass

class QVariantAnimation(QAbstractAnimation):

  Backward = None
  DeleteWhenStopped = None
  Forward = None
  KeepWhenStopped = None
  Paused = None
  Running = None
  Stopped = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentLoopChanged():
    """ Signal """
    pass

  def currentValue():
    pass

  def destroyed():
    """ Signal """
    pass

  def directionChanged():
    """ Signal """
    pass

  def disconnect():
    pass

  def duration():
    pass

  def easingCurve():
    pass

  def endValue():
    pass

  def event():
    pass

  def finished():
    """ Signal """
    pass

  def interpolated():
    pass

  def keyValueAt():
    pass

  def keyValues():
    pass

  def registerUserData():
    pass

  def setDuration():
    pass

  def setEasingCurve():
    pass

  def setEndValue():
    pass

  def setKeyValueAt():
    pass

  def setKeyValues():
    pass

  def setStartValue():
    pass

  def startValue():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def updateCurrentTime():
    pass

  def updateCurrentValue():
    pass

  def updateState():
    pass

  def valueChanged():
    """ Signal """
    pass

class QWaitCondition(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def wait():
    pass

  def wakeAll():
    pass

  def wakeOne():
    pass

class QWriteLocker(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def readWriteLock():
    pass

  def relock():
    pass

  def unlock():
    pass

class QXmlStreamAttribute(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def isDefault():
    pass

  def name():
    pass

  def namespaceUri():
    pass

  def prefix():
    pass

  def qualifiedName():
    pass

  def value():
    pass

class QXmlStreamAttributes(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def at():
    pass

  def capacity():
    pass

  def clear():
    pass

  def constData():
    pass

  def contains():
    pass

  def count():
    pass

  def data():
    pass

  def empty():
    pass

  def endsWith():
    pass

  def erase():
    pass

  def fill():
    pass

  def first():
    pass

  def front():
    pass

  def hasAttribute():
    pass

  def indexOf():
    pass

  def insert():
    pass

  def isEmpty():
    pass

  def isSharedWith():
    pass

  def last():
    pass

  def lastIndexOf():
    pass

  def mid():
    pass

  def prepend():
    pass

  def remove():
    pass

  def replace():
    pass

  def reserve():
    pass

  def resize():
    pass

  def setSharable():
    pass

  def size():
    pass

  def squeeze():
    pass

  def startsWith():
    pass

  def swap():
    pass

  def value():
    pass

class QXmlStreamEntityDeclaration(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def name():
    pass

  def notationName():
    pass

  def publicId():
    pass

  def systemId():
    pass

  def value():
    pass

class QXmlStreamEntityResolver(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def resolveEntity():
    pass

  def resolveUndeclaredEntity():
    pass

class QXmlStreamNamespaceDeclaration(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def namespaceUri():
    pass

  def prefix():
    pass

class QXmlStreamNotationDeclaration(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def name():
    pass

  def publicId():
    pass

  def systemId():
    pass

class QXmlStreamReader(Object):

  Characters = None
  Comment = None
  CustomError = None
  DTD = None
  EndDocument = None
  EndElement = None
  EntityReference = None

  class Error(object):

    CustomError = None
    NoError = None
    NotWellFormedError = None
    PrematureEndOfDocumentError = None
    UnexpectedElementError = None
    name = property(None, None, None,
                    )

    values = {}

  ErrorOnUnexpectedElement = None
  IncludeChildElements = None
  Invalid = None
  NoError = None
  NoToken = None
  NotWellFormedError = None
  PrematureEndOfDocumentError = None
  ProcessingInstruction = None

  class ReadElementTextBehaviour(object):

    ErrorOnUnexpectedElement = None
    IncludeChildElements = None
    SkipChildElements = None
    name = property(None, None, None,
                    )

    values = {}

  SkipChildElements = None
  StartDocument = None
  StartElement = None

  class TokenType(object):

    Characters = None
    Comment = None
    DTD = None
    EndDocument = None
    EndElement = None
    EntityReference = None
    Invalid = None
    NoToken = None
    ProcessingInstruction = None
    StartDocument = None
    StartElement = None
    name = property(None, None, None,
                    )

    values = {}

  UnexpectedElementError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addData():
    pass

  def addExtraNamespaceDeclaration():
    pass

  def addExtraNamespaceDeclarations():
    pass

  def atEnd():
    pass

  def attributes():
    pass

  def characterOffset():
    pass

  def clear():
    pass

  def columnNumber():
    pass

  def device():
    pass

  def documentEncoding():
    pass

  def documentVersion():
    pass

  def dtdName():
    pass

  def dtdPublicId():
    pass

  def dtdSystemId():
    pass

  def entityDeclarations():
    pass

  def entityResolver():
    pass

  def error():
    pass

  def errorString():
    pass

  def hasError():
    pass

  def isCDATA():
    pass

  def isCharacters():
    pass

  def isComment():
    pass

  def isDTD():
    pass

  def isEndDocument():
    pass

  def isEndElement():
    pass

  def isEntityReference():
    pass

  def isProcessingInstruction():
    pass

  def isStandaloneDocument():
    pass

  def isStartDocument():
    pass

  def isStartElement():
    pass

  def isWhitespace():
    pass

  def lineNumber():
    pass

  def name():
    pass

  def namespaceDeclarations():
    pass

  def namespaceProcessing():
    pass

  def namespaceUri():
    pass

  def notationDeclarations():
    pass

  def prefix():
    pass

  def processingInstructionData():
    pass

  def processingInstructionTarget():
    pass

  def qualifiedName():
    pass

  def raiseError():
    pass

  def readElementText():
    pass

  def readNext():
    pass

  def readNextStartElement():
    pass

  def setDevice():
    pass

  def setEntityResolver():
    pass

  def setNamespaceProcessing():
    pass

  def skipCurrentElement():
    pass

  def text():
    pass

  def tokenString():
    pass

  def tokenType():
    pass

class QXmlStreamWriter(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def autoFormatting():
    pass

  def autoFormattingIndent():
    pass

  def codec():
    pass

  def device():
    pass

  def hasError():
    pass

  def setAutoFormatting():
    pass

  def setAutoFormattingIndent():
    pass

  def setCodec():
    pass

  def setDevice():
    pass

  def writeAttribute():
    pass

  def writeAttributes():
    pass

  def writeCDATA():
    pass

  def writeCharacters():
    pass

  def writeComment():
    pass

  def writeCurrentToken():
    pass

  def writeDTD():
    pass

  def writeDefaultNamespace():
    pass

  def writeEmptyElement():
    pass

  def writeEndDocument():
    pass

  def writeEndElement():
    pass

  def writeEntityReference():
    pass

  def writeNamespace():
    pass

  def writeProcessingInstruction():
    pass

  def writeStartDocument():
    pass

  def writeStartElement():
    pass

  def writeTextElement():
    pass

class Qt(Object):

  AA_AttributeCount = None
  AA_CaptureMultimediaKeys = None
  AA_DontCreateNativeWidgetSiblings = None
  AA_DontShowIconsInMenus = None
  AA_DontUseNativeMenuBar = None
  AA_ImmediateWidgetCreation = None
  AA_MSWindowsUseDirect3DByDefault = None
  AA_MacDontSwapCtrlAndMeta = None
  AA_MacPluginApplication = None
  AA_NativeWindows = None
  AA_S60DisablePartialScreenInputMode = None
  AA_S60DontConstructApplicationPanes = None
  AA_X11InitThreads = None
  ALT = None
  AbsoluteSize = None
  AccessibleDescriptionRole = None
  AccessibleTextRole = None
  ActionMask = None
  ActionsContextMenu = None
  ActiveWindowFocusReason = None
  AlignAbsolute = None
  AlignBottom = None
  AlignCenter = None
  AlignHCenter = None
  AlignHorizontal_Mask = None
  AlignJustify = None
  AlignLeading = None
  AlignLeft = None
  AlignRight = None
  AlignTop = None
  AlignTrailing = None
  AlignVCenter = None
  AlignVertical_Mask = None

  class Alignment(object):

    pass

  class AlignmentFlag(object):

    AlignAbsolute = None
    AlignBottom = None
    AlignCenter = None
    AlignHCenter = None
    AlignHorizontal_Mask = None
    AlignJustify = None
    AlignLeading = None
    AlignLeft = None
    AlignRight = None
    AlignTop = None
    AlignTrailing = None
    AlignVCenter = None
    AlignVertical_Mask = None
    name = property(None, None, None,
                    )

    values = {}

  AllDockWidgetAreas = None
  AllToolBarAreas = None
  AlphaDither_Mask = None
  AltModifier = None

  class AnchorAttribute(object):

    AnchorHref = None
    AnchorName = None
    name = property(None, None, None,
                    )

    values = {}

  AnchorBottom = None
  AnchorHorizontalCenter = None
  AnchorHref = None
  AnchorLeft = None
  AnchorName = None

  class AnchorPoint(object):

    AnchorBottom = None
    AnchorHorizontalCenter = None
    AnchorLeft = None
    AnchorRight = None
    AnchorTop = None
    AnchorVerticalCenter = None
    name = property(None, None, None,
                    )

    values = {}

  AnchorRight = None
  AnchorTop = None
  AnchorVerticalCenter = None

  class ApplicationAttribute(object):

    AA_AttributeCount = None
    AA_CaptureMultimediaKeys = None
    AA_DontCreateNativeWidgetSiblings = None
    AA_DontShowIconsInMenus = None
    AA_DontUseNativeMenuBar = None
    AA_ImmediateWidgetCreation = None
    AA_MSWindowsUseDirect3DByDefault = None
    AA_MacDontSwapCtrlAndMeta = None
    AA_MacPluginApplication = None
    AA_NativeWindows = None
    AA_S60DisablePartialScreenInputMode = None
    AA_S60DontConstructApplicationPanes = None
    AA_X11InitThreads = None
    name = property(None, None, None,
                    )

    values = {}

  ApplicationModal = None
  ApplicationShortcut = None
  ArrowCursor = None

  class ArrowType(object):

    DownArrow = None
    LeftArrow = None
    NoArrow = None
    RightArrow = None
    UpArrow = None
    name = property(None, None, None,
                    )

    values = {}

  AscendingOrder = None

  class AspectRatioMode(object):

    IgnoreAspectRatio = None
    KeepAspectRatio = None
    KeepAspectRatioByExpanding = None
    name = property(None, None, None,
                    )

    values = {}

  AutoColor = None
  AutoCompatConnection = None
  AutoConnection = None
  AutoDither = None
  AutoText = None
  AvoidDither = None

  class Axis(object):

    XAxis = None
    YAxis = None
    ZAxis = None
    name = property(None, None, None,
                    )

    values = {}

  BDiagPattern = None

  class BGMode(object):

    OpaqueMode = None
    TransparentMode = None
    name = property(None, None, None,
                    )

    values = {}

  BackgroundColorRole = None
  BackgroundRole = None
  BacktabFocusReason = None
  BevelJoin = None
  BitmapCursor = None
  BlankCursor = None
  BlockingQueuedConnection = None
  BottomDockWidgetArea = None
  BottomLeftCorner = None
  BottomLeftSection = None
  BottomRightCorner = None
  BottomRightSection = None
  BottomSection = None
  BottomToolBarArea = None

  class BrushStyle(object):

    BDiagPattern = None
    ConicalGradientPattern = None
    CrossPattern = None
    Dense1Pattern = None
    Dense2Pattern = None
    Dense3Pattern = None
    Dense4Pattern = None
    Dense5Pattern = None
    Dense6Pattern = None
    Dense7Pattern = None
    DiagCrossPattern = None
    FDiagPattern = None
    HorPattern = None
    LinearGradientPattern = None
    NoBrush = None
    RadialGradientPattern = None
    SolidPattern = None
    TexturePattern = None
    VerPattern = None
    name = property(None, None, None,
                    )

    values = {}

  BusyCursor = None
  BypassGraphicsProxyWidget = None
  CTRL = None
  CaseInsensitive = None
  CaseSensitive = None

  class CaseSensitivity(object):

    CaseInsensitive = None
    CaseSensitive = None
    name = property(None, None, None,
                    )

    values = {}

  class CheckState(object):

    Checked = None
    PartiallyChecked = None
    Unchecked = None
    name = property(None, None, None,
                    )

    values = {}

  CheckStateRole = None
  Checked = None
  ClickFocus = None

  class ClipOperation(object):

    IntersectClip = None
    NoClip = None
    ReplaceClip = None
    UniteClip = None
    name = property(None, None, None,
                    )

    values = {}

  ClosedHandCursor = None
  ColorMode_Mask = None
  ColorOnly = None
  ConicalGradientPattern = None

  class ConnectionType(object):

    AutoCompatConnection = None
    AutoConnection = None
    BlockingQueuedConnection = None
    DirectConnection = None
    QueuedConnection = None
    UniqueConnection = None
    name = property(None, None, None,
                    )

    values = {}

  ContainsItemBoundingRect = None
  ContainsItemShape = None

  class ContextMenuPolicy(object):

    ActionsContextMenu = None
    CustomContextMenu = None
    DefaultContextMenu = None
    NoContextMenu = None
    PreventContextMenu = None
    name = property(None, None, None,
                    )

    values = {}

  ControlModifier = None

  class CoordinateSystem(object):

    DeviceCoordinates = None
    LogicalCoordinates = None
    name = property(None, None, None,
                    )

    values = {}

  CopyAction = None

  class Corner(object):

    BottomLeftCorner = None
    BottomRightCorner = None
    TopLeftCorner = None
    TopRightCorner = None
    name = property(None, None, None,
                    )

    values = {}

  CrossCursor = None
  CrossPattern = None

  class CursorMoveStyle(object):

    LogicalMoveStyle = None
    VisualMoveStyle = None
    name = property(None, None, None,
                    )

    values = {}

  class CursorShape(object):

    ArrowCursor = None
    BitmapCursor = None
    BlankCursor = None
    BusyCursor = None
    ClosedHandCursor = None
    CrossCursor = None
    CustomCursor = None
    DragCopyCursor = None
    DragLinkCursor = None
    DragMoveCursor = None
    ForbiddenCursor = None
    IBeamCursor = None
    LastCursor = None
    OpenHandCursor = None
    PointingHandCursor = None
    SizeAllCursor = None
    SizeBDiagCursor = None
    SizeFDiagCursor = None
    SizeHorCursor = None
    SizeVerCursor = None
    SplitHCursor = None
    SplitVCursor = None
    UpArrowCursor = None
    WaitCursor = None
    WhatsThisCursor = None
    name = property(None, None, None,
                    )

    values = {}

  CustomContextMenu = None
  CustomCursor = None
  CustomDashLine = None
  CustomGesture = None
  CustomizeWindowHint = None
  DashDotDotLine = None
  DashDotLine = None
  DashLine = None

  class DateFormat(object):

    DefaultLocaleLongDate = None
    DefaultLocaleShortDate = None
    ISODate = None
    LocalDate = None
    LocaleDate = None
    SystemLocaleDate = None
    SystemLocaleLongDate = None
    SystemLocaleShortDate = None
    TextDate = None
    name = property(None, None, None,
                    )

    values = {}

  class DayOfWeek(object):

    Friday = None
    Monday = None
    Saturday = None
    Sunday = None
    Thursday = None
    Tuesday = None
    Wednesday = None
    name = property(None, None, None,
                    )

    values = {}

  DecorationPropertyRole = None
  DecorationRole = None
  DefaultContextMenu = None
  DefaultLocaleLongDate = None
  DefaultLocaleShortDate = None
  Dense1Pattern = None
  Dense2Pattern = None
  Dense3Pattern = None
  Dense4Pattern = None
  Dense5Pattern = None
  Dense6Pattern = None
  Dense7Pattern = None
  DescendingOrder = None
  Desktop = None
  DeviceCoordinates = None
  DiagCrossPattern = None
  Dialog = None
  DiffuseAlphaDither = None
  DiffuseDither = None
  DirectConnection = None
  DisplayPropertyRole = None
  DisplayRole = None
  DitherMode_Mask = None
  Dither_Mask = None

  class DockWidgetArea(object):

    AllDockWidgetAreas = None
    BottomDockWidgetArea = None
    DockWidgetArea_Mask = None
    LeftDockWidgetArea = None
    NoDockWidgetArea = None
    RightDockWidgetArea = None
    TopDockWidgetArea = None
    name = property(None, None, None,
                    )

    values = {}

  class DockWidgetAreaSizes(object):

    NDockWidgetAreas = None
    name = property(None, None, None,
                    )

    values = {}

  DockWidgetArea_Mask = None

  class DockWidgetAreas(object):

    pass

  DontStartGestureOnChildren = None
  DotLine = None
  DownArrow = None
  DragCopyCursor = None
  DragLinkCursor = None
  DragMoveCursor = None
  Drawer = None

  class DropAction(object):

    ActionMask = None
    CopyAction = None
    IgnoreAction = None
    LinkAction = None
    MoveAction = None
    TargetMoveAction = None
    name = property(None, None, None,
                    )

    values = {}

  class DropActions(object):

    pass

  EditRole = None
  ElideLeft = None
  ElideMiddle = None
  ElideNone = None
  ElideRight = None

  class EventPriority(object):

    HighEventPriority = None
    LowEventPriority = None
    NormalEventPriority = None
    name = property(None, None, None,
                    )

    values = {}

  ExactHit = None
  FDiagPattern = None
  FastTransformation = None

  class FillRule(object):

    OddEvenFill = None
    WindingFill = None
    name = property(None, None, None,
                    )

    values = {}

  FlatCap = None

  class FocusPolicy(object):

    ClickFocus = None
    NoFocus = None
    StrongFocus = None
    TabFocus = None
    WheelFocus = None
    name = property(None, None, None,
                    )

    values = {}

  class FocusReason(object):

    ActiveWindowFocusReason = None
    BacktabFocusReason = None
    MenuBarFocusReason = None
    MouseFocusReason = None
    NoFocusReason = None
    OtherFocusReason = None
    PopupFocusReason = None
    ShortcutFocusReason = None
    TabFocusReason = None
    name = property(None, None, None,
                    )

    values = {}

  FontRole = None
  ForbiddenCursor = None
  ForegroundRole = None
  FramelessWindowHint = None
  Friday = None
  FuzzyHit = None
  GestureCanceled = None
  GestureFinished = None

  class GestureFlag(object):

    DontStartGestureOnChildren = None
    IgnoredGesturesPropagateToParent = None
    ReceivePartialGestures = None
    name = property(None, None, None,
                    )

    values = {}

  class GestureFlags(object):

    pass

  GestureStarted = None

  class GestureState(object):

    GestureCanceled = None
    GestureFinished = None
    GestureStarted = None
    GestureUpdated = None
    NoGesture = None
    name = property(None, None, None,
                    )

    values = {}

  class GestureType(object):

    CustomGesture = None
    LastGestureType = None
    PanGesture = None
    PinchGesture = None
    SwipeGesture = None
    TapAndHoldGesture = None
    TapGesture = None
    name = property(None, None, None,
                    )

    values = {}

  GestureUpdated = None

  class GlobalColor(object):

    black = None
    blue = None
    color0 = None
    color1 = None
    cyan = None
    darkBlue = None
    darkCyan = None
    darkGray = None
    darkGreen = None
    darkMagenta = None
    darkRed = None
    darkYellow = None
    gray = None
    green = None
    lightGray = None
    magenta = None
    name = property(None, None, None,
                    )

    red = None
    transparent = None
    values = {}
    white = None
    yellow = None

  GroupSwitchModifier = None
  HighEventPriority = None

  class HitTestAccuracy(object):

    ExactHit = None
    FuzzyHit = None
    name = property(None, None, None,
                    )

    values = {}

  HorPattern = None
  Horizontal = None
  IBeamCursor = None
  ISODate = None
  IgnoreAction = None
  IgnoreAspectRatio = None
  IgnoredGesturesPropagateToParent = None
  ImAnchorPosition = None
  ImCurrentSelection = None
  ImCursorPosition = None
  ImFont = None
  ImMaximumTextLength = None
  ImMicroFocus = None
  ImSurroundingText = None

  class ImageConversionFlag(object):

    AlphaDither_Mask = None
    AutoColor = None
    AutoDither = None
    AvoidDither = None
    ColorMode_Mask = None
    ColorOnly = None
    DiffuseAlphaDither = None
    DiffuseDither = None
    DitherMode_Mask = None
    Dither_Mask = None
    MonoOnly = None
    NoAlpha = None
    NoFormatConversion = None
    NoOpaqueDetection = None
    OrderedAlphaDither = None
    OrderedDither = None
    PreferDither = None
    ThresholdAlphaDither = None
    ThresholdDither = None
    name = property(None, None, None,
                    )

    values = {}

  class ImageConversionFlags(object):

    pass

  ImhDialableCharactersOnly = None
  ImhDigitsOnly = None
  ImhEmailCharactersOnly = None
  ImhExclusiveInputMask = None
  ImhFormattedNumbersOnly = None
  ImhHiddenText = None
  ImhLowercaseOnly = None
  ImhNoAutoUppercase = None
  ImhNoPredictiveText = None
  ImhNone = None
  ImhPreferLowercase = None
  ImhPreferNumbers = None
  ImhPreferUppercase = None
  ImhUppercaseOnly = None
  ImhUrlCharactersOnly = None
  InitialSortOrderRole = None

  class InputMethodHint(object):

    ImhDialableCharactersOnly = None
    ImhDigitsOnly = None
    ImhEmailCharactersOnly = None
    ImhExclusiveInputMask = None
    ImhFormattedNumbersOnly = None
    ImhHiddenText = None
    ImhLowercaseOnly = None
    ImhNoAutoUppercase = None
    ImhNoPredictiveText = None
    ImhNone = None
    ImhPreferLowercase = None
    ImhPreferNumbers = None
    ImhPreferUppercase = None
    ImhUppercaseOnly = None
    ImhUrlCharactersOnly = None
    name = property(None, None, None,
                    )

    values = {}

  class InputMethodHints(object):

    pass

  class InputMethodQuery(object):

    ImAnchorPosition = None
    ImCurrentSelection = None
    ImCursorPosition = None
    ImFont = None
    ImMaximumTextLength = None
    ImMicroFocus = None
    ImSurroundingText = None
    name = property(None, None, None,
                    )

    values = {}

  IntersectClip = None
  IntersectsItemBoundingRect = None
  IntersectsItemShape = None

  class ItemDataRole(object):

    AccessibleDescriptionRole = None
    AccessibleTextRole = None
    BackgroundColorRole = None
    BackgroundRole = None
    CheckStateRole = None
    DecorationPropertyRole = None
    DecorationRole = None
    DisplayPropertyRole = None
    DisplayRole = None
    EditRole = None
    FontRole = None
    ForegroundRole = None
    InitialSortOrderRole = None
    SizeHintRole = None
    StatusTipPropertyRole = None
    StatusTipRole = None
    TextAlignmentRole = None
    TextColorRole = None
    ToolTipPropertyRole = None
    ToolTipRole = None
    UserRole = None
    WhatsThisPropertyRole = None
    WhatsThisRole = None
    name = property(None, None, None,
                    )

    values = {}

  class ItemFlag(object):

    ItemIsDragEnabled = None
    ItemIsDropEnabled = None
    ItemIsEditable = None
    ItemIsEnabled = None
    ItemIsSelectable = None
    ItemIsTristate = None
    ItemIsUserCheckable = None
    NoItemFlags = None
    name = property(None, None, None,
                    )

    values = {}

  class ItemFlags(object):

    pass

  ItemIsDragEnabled = None
  ItemIsDropEnabled = None
  ItemIsEditable = None
  ItemIsEnabled = None
  ItemIsSelectable = None
  ItemIsTristate = None
  ItemIsUserCheckable = None

  class ItemSelectionMode(object):

    ContainsItemBoundingRect = None
    ContainsItemShape = None
    IntersectsItemBoundingRect = None
    IntersectsItemShape = None
    name = property(None, None, None,
                    )

    values = {}

  KeepAspectRatio = None
  KeepAspectRatioByExpanding = None

  class Key(object):

    Key_0 = None
    Key_1 = None
    Key_2 = None
    Key_3 = None
    Key_4 = None
    Key_5 = None
    Key_6 = None
    Key_7 = None
    Key_8 = None
    Key_9 = None
    Key_A = None
    Key_AE = None
    Key_Aacute = None
    Key_Acircumflex = None
    Key_AddFavorite = None
    Key_Adiaeresis = None
    Key_Agrave = None
    Key_Alt = None
    Key_AltGr = None
    Key_Ampersand = None
    Key_Any = None
    Key_Apostrophe = None
    Key_ApplicationLeft = None
    Key_ApplicationRight = None
    Key_Aring = None
    Key_AsciiCircum = None
    Key_AsciiTilde = None
    Key_Asterisk = None
    Key_At = None
    Key_Atilde = None
    Key_AudioCycleTrack = None
    Key_AudioForward = None
    Key_AudioRandomPlay = None
    Key_AudioRepeat = None
    Key_AudioRewind = None
    Key_Away = None
    Key_B = None
    Key_Back = None
    Key_BackForward = None
    Key_Backslash = None
    Key_Backspace = None
    Key_Backtab = None
    Key_Bar = None
    Key_BassBoost = None
    Key_BassDown = None
    Key_BassUp = None
    Key_Battery = None
    Key_Bluetooth = None
    Key_Book = None
    Key_BraceLeft = None
    Key_BraceRight = None
    Key_BracketLeft = None
    Key_BracketRight = None
    Key_BrightnessAdjust = None
    Key_C = None
    Key_CD = None
    Key_Calculator = None
    Key_Calendar = None
    Key_Call = None
    Key_Camera = None
    Key_CameraFocus = None
    Key_Cancel = None
    Key_CapsLock = None
    Key_Ccedilla = None
    Key_Clear = None
    Key_ClearGrab = None
    Key_Close = None
    Key_Codeinput = None
    Key_Colon = None
    Key_Comma = None
    Key_Community = None
    Key_Context1 = None
    Key_Context2 = None
    Key_Context3 = None
    Key_Context4 = None
    Key_ContrastAdjust = None
    Key_Control = None
    Key_Copy = None
    Key_Cut = None
    Key_D = None
    Key_DOS = None
    Key_Dead_Abovedot = None
    Key_Dead_Abovering = None
    Key_Dead_Acute = None
    Key_Dead_Belowdot = None
    Key_Dead_Breve = None
    Key_Dead_Caron = None
    Key_Dead_Cedilla = None
    Key_Dead_Circumflex = None
    Key_Dead_Diaeresis = None
    Key_Dead_Doubleacute = None
    Key_Dead_Grave = None
    Key_Dead_Hook = None
    Key_Dead_Horn = None
    Key_Dead_Iota = None
    Key_Dead_Macron = None
    Key_Dead_Ogonek = None
    Key_Dead_Semivoiced_Sound = None
    Key_Dead_Tilde = None
    Key_Dead_Voiced_Sound = None
    Key_Delete = None
    Key_Direction_L = None
    Key_Direction_R = None
    Key_Display = None
    Key_Documents = None
    Key_Dollar = None
    Key_Down = None
    Key_E = None
    Key_ETH = None
    Key_Eacute = None
    Key_Ecircumflex = None
    Key_Ediaeresis = None
    Key_Egrave = None
    Key_Eisu_Shift = None
    Key_Eisu_toggle = None
    Key_Eject = None
    Key_End = None
    Key_Enter = None
    Key_Equal = None
    Key_Escape = None
    Key_Excel = None
    Key_Exclam = None
    Key_Execute = None
    Key_Explorer = None
    Key_F = None
    Key_F1 = None
    Key_F10 = None
    Key_F11 = None
    Key_F12 = None
    Key_F13 = None
    Key_F14 = None
    Key_F15 = None
    Key_F16 = None
    Key_F17 = None
    Key_F18 = None
    Key_F19 = None
    Key_F2 = None
    Key_F20 = None
    Key_F21 = None
    Key_F22 = None
    Key_F23 = None
    Key_F24 = None
    Key_F25 = None
    Key_F26 = None
    Key_F27 = None
    Key_F28 = None
    Key_F29 = None
    Key_F3 = None
    Key_F30 = None
    Key_F31 = None
    Key_F32 = None
    Key_F33 = None
    Key_F34 = None
    Key_F35 = None
    Key_F4 = None
    Key_F5 = None
    Key_F6 = None
    Key_F7 = None
    Key_F8 = None
    Key_F9 = None
    Key_Favorites = None
    Key_Finance = None
    Key_Flip = None
    Key_Forward = None
    Key_G = None
    Key_Game = None
    Key_Go = None
    Key_Greater = None
    Key_H = None
    Key_Hangul = None
    Key_Hangul_Banja = None
    Key_Hangul_End = None
    Key_Hangul_Hanja = None
    Key_Hangul_Jamo = None
    Key_Hangul_Jeonja = None
    Key_Hangul_PostHanja = None
    Key_Hangul_PreHanja = None
    Key_Hangul_Romaja = None
    Key_Hangul_Special = None
    Key_Hangul_Start = None
    Key_Hangup = None
    Key_Hankaku = None
    Key_Help = None
    Key_Henkan = None
    Key_Hibernate = None
    Key_Hiragana = None
    Key_Hiragana_Katakana = None
    Key_History = None
    Key_Home = None
    Key_HomePage = None
    Key_HotLinks = None
    Key_Hyper_L = None
    Key_Hyper_R = None
    Key_I = None
    Key_Iacute = None
    Key_Icircumflex = None
    Key_Idiaeresis = None
    Key_Igrave = None
    Key_Insert = None
    Key_J = None
    Key_K = None
    Key_Kana_Lock = None
    Key_Kana_Shift = None
    Key_Kanji = None
    Key_Katakana = None
    Key_KeyboardBrightnessDown = None
    Key_KeyboardBrightnessUp = None
    Key_KeyboardLightOnOff = None
    Key_L = None
    Key_LastNumberRedial = None
    Key_Launch0 = None
    Key_Launch1 = None
    Key_Launch2 = None
    Key_Launch3 = None
    Key_Launch4 = None
    Key_Launch5 = None
    Key_Launch6 = None
    Key_Launch7 = None
    Key_Launch8 = None
    Key_Launch9 = None
    Key_LaunchA = None
    Key_LaunchB = None
    Key_LaunchC = None
    Key_LaunchD = None
    Key_LaunchE = None
    Key_LaunchF = None
    Key_LaunchG = None
    Key_LaunchH = None
    Key_LaunchMail = None
    Key_LaunchMedia = None
    Key_Left = None
    Key_Less = None
    Key_LightBulb = None
    Key_LogOff = None
    Key_M = None
    Key_MailForward = None
    Key_Market = None
    Key_Massyo = None
    Key_MediaLast = None
    Key_MediaNext = None
    Key_MediaPause = None
    Key_MediaPlay = None
    Key_MediaPrevious = None
    Key_MediaRecord = None
    Key_MediaStop = None
    Key_MediaTogglePlayPause = None
    Key_Meeting = None
    Key_Memo = None
    Key_Menu = None
    Key_MenuKB = None
    Key_MenuPB = None
    Key_Messenger = None
    Key_Meta = None
    Key_Minus = None
    Key_Mode_switch = None
    Key_MonBrightnessDown = None
    Key_MonBrightnessUp = None
    Key_Muhenkan = None
    Key_Multi_key = None
    Key_MultipleCandidate = None
    Key_Music = None
    Key_MySites = None
    Key_N = None
    Key_News = None
    Key_No = None
    Key_Ntilde = None
    Key_NumLock = None
    Key_NumberSign = None
    Key_O = None
    Key_Oacute = None
    Key_Ocircumflex = None
    Key_Odiaeresis = None
    Key_OfficeHome = None
    Key_Ograve = None
    Key_Ooblique = None
    Key_OpenUrl = None
    Key_Option = None
    Key_Otilde = None
    Key_P = None
    Key_PageDown = None
    Key_PageUp = None
    Key_ParenLeft = None
    Key_ParenRight = None
    Key_Paste = None
    Key_Pause = None
    Key_Percent = None
    Key_Period = None
    Key_Phone = None
    Key_Pictures = None
    Key_Play = None
    Key_Plus = None
    Key_PowerDown = None
    Key_PowerOff = None
    Key_PreviousCandidate = None
    Key_Print = None
    Key_Printer = None
    Key_Q = None
    Key_Question = None
    Key_QuoteDbl = None
    Key_QuoteLeft = None
    Key_R = None
    Key_Refresh = None
    Key_Reload = None
    Key_Reply = None
    Key_Return = None
    Key_Right = None
    Key_Romaji = None
    Key_RotateWindows = None
    Key_RotationKB = None
    Key_RotationPB = None
    Key_S = None
    Key_Save = None
    Key_ScreenSaver = None
    Key_ScrollLock = None
    Key_Search = None
    Key_Select = None
    Key_Semicolon = None
    Key_Send = None
    Key_Shift = None
    Key_Shop = None
    Key_SingleCandidate = None
    Key_Slash = None
    Key_Sleep = None
    Key_Space = None
    Key_Spell = None
    Key_SplitScreen = None
    Key_Standby = None
    Key_Stop = None
    Key_Subtitle = None
    Key_Super_L = None
    Key_Super_R = None
    Key_Support = None
    Key_Suspend = None
    Key_SysReq = None
    Key_T = None
    Key_THORN = None
    Key_Tab = None
    Key_TaskPane = None
    Key_Terminal = None
    Key_Time = None
    Key_ToDoList = None
    Key_ToggleCallHangup = None
    Key_Tools = None
    Key_TopMenu = None
    Key_Touroku = None
    Key_Travel = None
    Key_TrebleDown = None
    Key_TrebleUp = None
    Key_U = None
    Key_UWB = None
    Key_Uacute = None
    Key_Ucircumflex = None
    Key_Udiaeresis = None
    Key_Ugrave = None
    Key_Underscore = None
    Key_Up = None
    Key_V = None
    Key_Video = None
    Key_View = None
    Key_VoiceDial = None
    Key_VolumeDown = None
    Key_VolumeMute = None
    Key_VolumeUp = None
    Key_W = None
    Key_WLAN = None
    Key_WWW = None
    Key_WakeUp = None
    Key_WebCam = None
    Key_Word = None
    Key_X = None
    Key_Xfer = None
    Key_Y = None
    Key_Yacute = None
    Key_Yes = None
    Key_Z = None
    Key_Zenkaku = None
    Key_Zenkaku_Hankaku = None
    Key_Zoom = None
    Key_ZoomIn = None
    Key_ZoomOut = None
    Key_acute = None
    Key_brokenbar = None
    Key_cedilla = None
    Key_cent = None
    Key_copyright = None
    Key_currency = None
    Key_degree = None
    Key_diaeresis = None
    Key_division = None
    Key_exclamdown = None
    Key_guillemotleft = None
    Key_guillemotright = None
    Key_hyphen = None
    Key_iTouch = None
    Key_macron = None
    Key_masculine = None
    Key_mu = None
    Key_multiply = None
    Key_nobreakspace = None
    Key_notsign = None
    Key_onehalf = None
    Key_onequarter = None
    Key_onesuperior = None
    Key_ordfeminine = None
    Key_paragraph = None
    Key_periodcentered = None
    Key_plusminus = None
    Key_questiondown = None
    Key_registered = None
    Key_section = None
    Key_ssharp = None
    Key_sterling = None
    Key_threequarters = None
    Key_threesuperior = None
    Key_twosuperior = None
    Key_unknown = None
    Key_ydiaeresis = None
    Key_yen = None
    name = property(None, None, None,
                    )

    values = {}

  Key_0 = None
  Key_1 = None
  Key_2 = None
  Key_3 = None
  Key_4 = None
  Key_5 = None
  Key_6 = None
  Key_7 = None
  Key_8 = None
  Key_9 = None
  Key_A = None
  Key_AE = None
  Key_Aacute = None
  Key_Acircumflex = None
  Key_AddFavorite = None
  Key_Adiaeresis = None
  Key_Agrave = None
  Key_Alt = None
  Key_AltGr = None
  Key_Ampersand = None
  Key_Any = None
  Key_Apostrophe = None
  Key_ApplicationLeft = None
  Key_ApplicationRight = None
  Key_Aring = None
  Key_AsciiCircum = None
  Key_AsciiTilde = None
  Key_Asterisk = None
  Key_At = None
  Key_Atilde = None
  Key_AudioCycleTrack = None
  Key_AudioForward = None
  Key_AudioRandomPlay = None
  Key_AudioRepeat = None
  Key_AudioRewind = None
  Key_Away = None
  Key_B = None
  Key_Back = None
  Key_BackForward = None
  Key_Backslash = None
  Key_Backspace = None
  Key_Backtab = None
  Key_Bar = None
  Key_BassBoost = None
  Key_BassDown = None
  Key_BassUp = None
  Key_Battery = None
  Key_Bluetooth = None
  Key_Book = None
  Key_BraceLeft = None
  Key_BraceRight = None
  Key_BracketLeft = None
  Key_BracketRight = None
  Key_BrightnessAdjust = None
  Key_C = None
  Key_CD = None
  Key_Calculator = None
  Key_Calendar = None
  Key_Call = None
  Key_Camera = None
  Key_CameraFocus = None
  Key_Cancel = None
  Key_CapsLock = None
  Key_Ccedilla = None
  Key_Clear = None
  Key_ClearGrab = None
  Key_Close = None
  Key_Codeinput = None
  Key_Colon = None
  Key_Comma = None
  Key_Community = None
  Key_Context1 = None
  Key_Context2 = None
  Key_Context3 = None
  Key_Context4 = None
  Key_ContrastAdjust = None
  Key_Control = None
  Key_Copy = None
  Key_Cut = None
  Key_D = None
  Key_DOS = None
  Key_Dead_Abovedot = None
  Key_Dead_Abovering = None
  Key_Dead_Acute = None
  Key_Dead_Belowdot = None
  Key_Dead_Breve = None
  Key_Dead_Caron = None
  Key_Dead_Cedilla = None
  Key_Dead_Circumflex = None
  Key_Dead_Diaeresis = None
  Key_Dead_Doubleacute = None
  Key_Dead_Grave = None
  Key_Dead_Hook = None
  Key_Dead_Horn = None
  Key_Dead_Iota = None
  Key_Dead_Macron = None
  Key_Dead_Ogonek = None
  Key_Dead_Semivoiced_Sound = None
  Key_Dead_Tilde = None
  Key_Dead_Voiced_Sound = None
  Key_Delete = None
  Key_Direction_L = None
  Key_Direction_R = None
  Key_Display = None
  Key_Documents = None
  Key_Dollar = None
  Key_Down = None
  Key_E = None
  Key_ETH = None
  Key_Eacute = None
  Key_Ecircumflex = None
  Key_Ediaeresis = None
  Key_Egrave = None
  Key_Eisu_Shift = None
  Key_Eisu_toggle = None
  Key_Eject = None
  Key_End = None
  Key_Enter = None
  Key_Equal = None
  Key_Escape = None
  Key_Excel = None
  Key_Exclam = None
  Key_Execute = None
  Key_Explorer = None
  Key_F = None
  Key_F1 = None
  Key_F10 = None
  Key_F11 = None
  Key_F12 = None
  Key_F13 = None
  Key_F14 = None
  Key_F15 = None
  Key_F16 = None
  Key_F17 = None
  Key_F18 = None
  Key_F19 = None
  Key_F2 = None
  Key_F20 = None
  Key_F21 = None
  Key_F22 = None
  Key_F23 = None
  Key_F24 = None
  Key_F25 = None
  Key_F26 = None
  Key_F27 = None
  Key_F28 = None
  Key_F29 = None
  Key_F3 = None
  Key_F30 = None
  Key_F31 = None
  Key_F32 = None
  Key_F33 = None
  Key_F34 = None
  Key_F35 = None
  Key_F4 = None
  Key_F5 = None
  Key_F6 = None
  Key_F7 = None
  Key_F8 = None
  Key_F9 = None
  Key_Favorites = None
  Key_Finance = None
  Key_Flip = None
  Key_Forward = None
  Key_G = None
  Key_Game = None
  Key_Go = None
  Key_Greater = None
  Key_H = None
  Key_Hangul = None
  Key_Hangul_Banja = None
  Key_Hangul_End = None
  Key_Hangul_Hanja = None
  Key_Hangul_Jamo = None
  Key_Hangul_Jeonja = None
  Key_Hangul_PostHanja = None
  Key_Hangul_PreHanja = None
  Key_Hangul_Romaja = None
  Key_Hangul_Special = None
  Key_Hangul_Start = None
  Key_Hangup = None
  Key_Hankaku = None
  Key_Help = None
  Key_Henkan = None
  Key_Hibernate = None
  Key_Hiragana = None
  Key_Hiragana_Katakana = None
  Key_History = None
  Key_Home = None
  Key_HomePage = None
  Key_HotLinks = None
  Key_Hyper_L = None
  Key_Hyper_R = None
  Key_I = None
  Key_Iacute = None
  Key_Icircumflex = None
  Key_Idiaeresis = None
  Key_Igrave = None
  Key_Insert = None
  Key_J = None
  Key_K = None
  Key_Kana_Lock = None
  Key_Kana_Shift = None
  Key_Kanji = None
  Key_Katakana = None
  Key_KeyboardBrightnessDown = None
  Key_KeyboardBrightnessUp = None
  Key_KeyboardLightOnOff = None
  Key_L = None
  Key_LastNumberRedial = None
  Key_Launch0 = None
  Key_Launch1 = None
  Key_Launch2 = None
  Key_Launch3 = None
  Key_Launch4 = None
  Key_Launch5 = None
  Key_Launch6 = None
  Key_Launch7 = None
  Key_Launch8 = None
  Key_Launch9 = None
  Key_LaunchA = None
  Key_LaunchB = None
  Key_LaunchC = None
  Key_LaunchD = None
  Key_LaunchE = None
  Key_LaunchF = None
  Key_LaunchG = None
  Key_LaunchH = None
  Key_LaunchMail = None
  Key_LaunchMedia = None
  Key_Left = None
  Key_Less = None
  Key_LightBulb = None
  Key_LogOff = None
  Key_M = None
  Key_MailForward = None
  Key_Market = None
  Key_Massyo = None
  Key_MediaLast = None
  Key_MediaNext = None
  Key_MediaPause = None
  Key_MediaPlay = None
  Key_MediaPrevious = None
  Key_MediaRecord = None
  Key_MediaStop = None
  Key_MediaTogglePlayPause = None
  Key_Meeting = None
  Key_Memo = None
  Key_Menu = None
  Key_MenuKB = None
  Key_MenuPB = None
  Key_Messenger = None
  Key_Meta = None
  Key_Minus = None
  Key_Mode_switch = None
  Key_MonBrightnessDown = None
  Key_MonBrightnessUp = None
  Key_Muhenkan = None
  Key_Multi_key = None
  Key_MultipleCandidate = None
  Key_Music = None
  Key_MySites = None
  Key_N = None
  Key_News = None
  Key_No = None
  Key_Ntilde = None
  Key_NumLock = None
  Key_NumberSign = None
  Key_O = None
  Key_Oacute = None
  Key_Ocircumflex = None
  Key_Odiaeresis = None
  Key_OfficeHome = None
  Key_Ograve = None
  Key_Ooblique = None
  Key_OpenUrl = None
  Key_Option = None
  Key_Otilde = None
  Key_P = None
  Key_PageDown = None
  Key_PageUp = None
  Key_ParenLeft = None
  Key_ParenRight = None
  Key_Paste = None
  Key_Pause = None
  Key_Percent = None
  Key_Period = None
  Key_Phone = None
  Key_Pictures = None
  Key_Play = None
  Key_Plus = None
  Key_PowerDown = None
  Key_PowerOff = None
  Key_PreviousCandidate = None
  Key_Print = None
  Key_Printer = None
  Key_Q = None
  Key_Question = None
  Key_QuoteDbl = None
  Key_QuoteLeft = None
  Key_R = None
  Key_Refresh = None
  Key_Reload = None
  Key_Reply = None
  Key_Return = None
  Key_Right = None
  Key_Romaji = None
  Key_RotateWindows = None
  Key_RotationKB = None
  Key_RotationPB = None
  Key_S = None
  Key_Save = None
  Key_ScreenSaver = None
  Key_ScrollLock = None
  Key_Search = None
  Key_Select = None
  Key_Semicolon = None
  Key_Send = None
  Key_Shift = None
  Key_Shop = None
  Key_SingleCandidate = None
  Key_Slash = None
  Key_Sleep = None
  Key_Space = None
  Key_Spell = None
  Key_SplitScreen = None
  Key_Standby = None
  Key_Stop = None
  Key_Subtitle = None
  Key_Super_L = None
  Key_Super_R = None
  Key_Support = None
  Key_Suspend = None
  Key_SysReq = None
  Key_T = None
  Key_THORN = None
  Key_Tab = None
  Key_TaskPane = None
  Key_Terminal = None
  Key_Time = None
  Key_ToDoList = None
  Key_ToggleCallHangup = None
  Key_Tools = None
  Key_TopMenu = None
  Key_Touroku = None
  Key_Travel = None
  Key_TrebleDown = None
  Key_TrebleUp = None
  Key_U = None
  Key_UWB = None
  Key_Uacute = None
  Key_Ucircumflex = None
  Key_Udiaeresis = None
  Key_Ugrave = None
  Key_Underscore = None
  Key_Up = None
  Key_V = None
  Key_Video = None
  Key_View = None
  Key_VoiceDial = None
  Key_VolumeDown = None
  Key_VolumeMute = None
  Key_VolumeUp = None
  Key_W = None
  Key_WLAN = None
  Key_WWW = None
  Key_WakeUp = None
  Key_WebCam = None
  Key_Word = None
  Key_X = None
  Key_Xfer = None
  Key_Y = None
  Key_Yacute = None
  Key_Yes = None
  Key_Z = None
  Key_Zenkaku = None
  Key_Zenkaku_Hankaku = None
  Key_Zoom = None
  Key_ZoomIn = None
  Key_ZoomOut = None
  Key_acute = None
  Key_brokenbar = None
  Key_cedilla = None
  Key_cent = None
  Key_copyright = None
  Key_currency = None
  Key_degree = None
  Key_diaeresis = None
  Key_division = None
  Key_exclamdown = None
  Key_guillemotleft = None
  Key_guillemotright = None
  Key_hyphen = None
  Key_iTouch = None
  Key_macron = None
  Key_masculine = None
  Key_mu = None
  Key_multiply = None
  Key_nobreakspace = None
  Key_notsign = None
  Key_onehalf = None
  Key_onequarter = None
  Key_onesuperior = None
  Key_ordfeminine = None
  Key_paragraph = None
  Key_periodcentered = None
  Key_plusminus = None
  Key_questiondown = None
  Key_registered = None
  Key_section = None
  Key_ssharp = None
  Key_sterling = None
  Key_threequarters = None
  Key_threesuperior = None
  Key_twosuperior = None
  Key_unknown = None
  Key_ydiaeresis = None
  Key_yen = None

  class KeyboardModifier(object):

    AltModifier = None
    ControlModifier = None
    GroupSwitchModifier = None
    KeyboardModifierMask = None
    KeypadModifier = None
    MetaModifier = None
    NoModifier = None
    ShiftModifier = None
    name = property(None, None, None,
                    )

    values = {}

  KeyboardModifierMask = None

  class KeyboardModifiers(object):

    pass

  KeypadModifier = None
  LastCursor = None
  LastGestureType = None

  class LayoutDirection(object):

    LayoutDirectionAuto = None
    LeftToRight = None
    RightToLeft = None
    name = property(None, None, None,
                    )

    values = {}

  LayoutDirectionAuto = None
  LeftArrow = None
  LeftButton = None
  LeftDockWidgetArea = None
  LeftSection = None
  LeftToRight = None
  LeftToolBarArea = None
  LinearGradientPattern = None
  LinkAction = None
  LinksAccessibleByKeyboard = None
  LinksAccessibleByMouse = None
  LocalDate = None
  LocalTime = None
  LocaleDate = None
  LogText = None
  LogicalCoordinates = None
  LogicalMoveStyle = None
  LowEventPriority = None
  META = None
  MODIFIER_MASK = None
  MPenCapStyle = None
  MPenJoinStyle = None
  MPenStyle = None
  MSWindowsFixedSizeDialogHint = None
  MSWindowsOwnDC = None
  MacWindowToolBarButtonHint = None
  MaskInColor = None

  class MaskMode(object):

    MaskInColor = None
    MaskOutColor = None
    name = property(None, None, None,
                    )

    values = {}

  MaskOutColor = None
  MatchCaseSensitive = None
  MatchContains = None
  MatchEndsWith = None
  MatchExactly = None
  MatchFixedString = None

  class MatchFlag(object):

    MatchCaseSensitive = None
    MatchContains = None
    MatchEndsWith = None
    MatchExactly = None
    MatchFixedString = None
    MatchRecursive = None
    MatchRegExp = None
    MatchStartsWith = None
    MatchWildcard = None
    MatchWrap = None
    name = property(None, None, None,
                    )

    values = {}

  class MatchFlags(object):

    pass

  MatchRecursive = None
  MatchRegExp = None
  MatchStartsWith = None
  MatchWildcard = None
  MatchWrap = None
  MaximumSize = None
  MenuBarFocusReason = None
  MetaModifier = None
  MidButton = None
  MiddleButton = None
  MinimumDescent = None
  MinimumSize = None
  MiterJoin = None

  class Modifier(object):

    ALT = None
    CTRL = None
    META = None
    MODIFIER_MASK = None
    SHIFT = None
    UNICODE_ACCEL = None
    name = property(None, None, None,
                    )

    values = {}

  Monday = None
  MonoOnly = None

  class MouseButton(object):

    LeftButton = None
    MidButton = None
    MiddleButton = None
    MouseButtonMask = None
    NoButton = None
    RightButton = None
    XButton1 = None
    XButton2 = None
    name = property(None, None, None,
                    )

    values = {}

  MouseButtonMask = None

  class MouseButtons(object):

    pass

  MouseFocusReason = None
  MoveAction = None
  NDockWidgetAreas = None
  NSizeHints = None
  NToolBarAreas = None

  class NavigationMode(object):

    NavigationModeCursorAuto = None
    NavigationModeCursorForceVisible = None
    NavigationModeKeypadDirectional = None
    NavigationModeKeypadTabOrder = None
    NavigationModeNone = None
    name = property(None, None, None,
                    )

    values = {}

  NavigationModeCursorAuto = None
  NavigationModeCursorForceVisible = None
  NavigationModeKeypadDirectional = None
  NavigationModeKeypadTabOrder = None
  NavigationModeNone = None
  NoAlpha = None
  NoArrow = None
  NoBrush = None
  NoButton = None
  NoClip = None
  NoContextMenu = None
  NoDockWidgetArea = None
  NoFocus = None
  NoFocusReason = None
  NoFormatConversion = None
  NoGesture = None
  NoItemFlags = None
  NoModifier = None
  NoOpaqueDetection = None
  NoPen = None
  NoSection = None
  NoTextInteraction = None
  NoToolBarArea = None
  NonModal = None
  NormalEventPriority = None
  OddEvenFill = None
  OffsetFromUTC = None
  OpaqueMode = None
  OpenHandCursor = None
  OrderedAlphaDither = None
  OrderedDither = None

  class Orientation(object):

    Horizontal = None
    Vertical = None
    name = property(None, None, None,
                    )

    values = {}

  class Orientations(object):

    pass

  OtherFocusReason = None
  PanGesture = None
  PartiallyChecked = None

  class PenCapStyle(object):

    FlatCap = None
    MPenCapStyle = None
    RoundCap = None
    SquareCap = None
    name = property(None, None, None,
                    )

    values = {}

  class PenJoinStyle(object):

    BevelJoin = None
    MPenJoinStyle = None
    MiterJoin = None
    RoundJoin = None
    SvgMiterJoin = None
    name = property(None, None, None,
                    )

    values = {}

  class PenStyle(object):

    CustomDashLine = None
    DashDotDotLine = None
    DashDotLine = None
    DashLine = None
    DotLine = None
    MPenStyle = None
    NoPen = None
    SolidLine = None
    name = property(None, None, None,
                    )

    values = {}

  PinchGesture = None
  PlainText = None
  PointingHandCursor = None
  Popup = None
  PopupFocusReason = None
  PreferDither = None
  PreferredSize = None
  PreventContextMenu = None
  QueuedConnection = None
  RadialGradientPattern = None
  ReceivePartialGestures = None
  RelativeSize = None
  RepeatTile = None
  ReplaceClip = None
  RichText = None
  RightArrow = None
  RightButton = None
  RightDockWidgetArea = None
  RightSection = None
  RightToLeft = None
  RightToolBarArea = None
  RoundCap = None
  RoundJoin = None
  RoundTile = None
  SHIFT = None
  Saturday = None
  ScrollBarAlwaysOff = None
  ScrollBarAlwaysOn = None
  ScrollBarAsNeeded = None

  class ScrollBarPolicy(object):

    ScrollBarAlwaysOff = None
    ScrollBarAlwaysOn = None
    ScrollBarAsNeeded = None
    name = property(None, None, None,
                    )

    values = {}

  Sheet = None
  ShiftModifier = None

  class ShortcutContext(object):

    ApplicationShortcut = None
    WidgetShortcut = None
    WidgetWithChildrenShortcut = None
    WindowShortcut = None
    name = property(None, None, None,
                    )

    values = {}

  ShortcutFocusReason = None
  SizeAllCursor = None
  SizeBDiagCursor = None
  SizeFDiagCursor = None

  class SizeHint(object):

    MaximumSize = None
    MinimumDescent = None
    MinimumSize = None
    NSizeHints = None
    PreferredSize = None
    name = property(None, None, None,
                    )

    values = {}

  SizeHintRole = None
  SizeHorCursor = None

  class SizeMode(object):

    AbsoluteSize = None
    RelativeSize = None
    name = property(None, None, None,
                    )

    values = {}

  SizeVerCursor = None
  SmoothTransformation = None
  SolidLine = None
  SolidPattern = None

  class SortOrder(object):

    AscendingOrder = None
    DescendingOrder = None
    name = property(None, None, None,
                    )

    values = {}

  SplashScreen = None
  SplitHCursor = None
  SplitVCursor = None
  SquareCap = None
  StatusTipPropertyRole = None
  StatusTipRole = None
  StretchTile = None
  StrongFocus = None
  SubWindow = None
  Sunday = None
  SvgMiterJoin = None
  SwipeGesture = None
  SystemLocaleDate = None
  SystemLocaleLongDate = None
  SystemLocaleShortDate = None
  TabFocus = None
  TabFocusReason = None
  TapAndHoldGesture = None
  TapGesture = None
  TargetMoveAction = None
  TextAlignmentRole = None
  TextBrowserInteraction = None
  TextBypassShaping = None
  TextColorRole = None
  TextDate = None
  TextDontClip = None
  TextDontPrint = None
  TextEditable = None
  TextEditorInteraction = None

  class TextElideMode(object):

    ElideLeft = None
    ElideMiddle = None
    ElideNone = None
    ElideRight = None
    name = property(None, None, None,
                    )

    values = {}

  TextExpandTabs = None

  class TextFlag(object):

    TextBypassShaping = None
    TextDontClip = None
    TextDontPrint = None
    TextExpandTabs = None
    TextForceLeftToRight = None
    TextForceRightToLeft = None
    TextHideMnemonic = None
    TextIncludeTrailingSpaces = None
    TextJustificationForced = None
    TextLongestVariant = None
    TextShowMnemonic = None
    TextSingleLine = None
    TextWordWrap = None
    TextWrapAnywhere = None
    name = property(None, None, None,
                    )

    values = {}

  TextForceLeftToRight = None
  TextForceRightToLeft = None

  class TextFormat(object):

    AutoText = None
    LogText = None
    PlainText = None
    RichText = None
    name = property(None, None, None,
                    )

    values = {}

  TextHideMnemonic = None
  TextIncludeTrailingSpaces = None

  class TextInteractionFlag(object):

    LinksAccessibleByKeyboard = None
    LinksAccessibleByMouse = None
    NoTextInteraction = None
    TextBrowserInteraction = None
    TextEditable = None
    TextEditorInteraction = None
    TextSelectableByKeyboard = None
    TextSelectableByMouse = None
    name = property(None, None, None,
                    )

    values = {}

  class TextInteractionFlags(object):

    pass

  TextJustificationForced = None
  TextLongestVariant = None
  TextSelectableByKeyboard = None
  TextSelectableByMouse = None
  TextShowMnemonic = None
  TextSingleLine = None
  TextWordWrap = None
  TextWrapAnywhere = None
  TexturePattern = None
  ThresholdAlphaDither = None
  ThresholdDither = None
  Thursday = None

  class TileRule(object):

    RepeatTile = None
    RoundTile = None
    StretchTile = None
    name = property(None, None, None,
                    )

    values = {}

  class TimeSpec(object):

    LocalTime = None
    OffsetFromUTC = None
    UTC = None
    name = property(None, None, None,
                    )

    values = {}

  TitleBarArea = None
  Tool = None

  class ToolBarArea(object):

    AllToolBarAreas = None
    BottomToolBarArea = None
    LeftToolBarArea = None
    NoToolBarArea = None
    RightToolBarArea = None
    ToolBarArea_Mask = None
    TopToolBarArea = None
    name = property(None, None, None,
                    )

    values = {}

  class ToolBarAreaSizes(object):

    NToolBarAreas = None
    name = property(None, None, None,
                    )

    values = {}

  ToolBarArea_Mask = None

  class ToolBarAreas(object):

    pass

  ToolButtonFollowStyle = None
  ToolButtonIconOnly = None

  class ToolButtonStyle(object):

    ToolButtonFollowStyle = None
    ToolButtonIconOnly = None
    ToolButtonTextBesideIcon = None
    ToolButtonTextOnly = None
    ToolButtonTextUnderIcon = None
    name = property(None, None, None,
                    )

    values = {}

  ToolButtonTextBesideIcon = None
  ToolButtonTextOnly = None
  ToolButtonTextUnderIcon = None
  ToolTip = None
  ToolTipPropertyRole = None
  ToolTipRole = None
  TopDockWidgetArea = None
  TopLeftCorner = None
  TopLeftSection = None
  TopRightCorner = None
  TopRightSection = None
  TopSection = None
  TopToolBarArea = None
  TouchPointMoved = None
  TouchPointPressed = None
  TouchPointPrimary = None
  TouchPointReleased = None

  class TouchPointState(object):

    TouchPointMoved = None
    TouchPointPressed = None
    TouchPointPrimary = None
    TouchPointReleased = None
    TouchPointStateMask = None
    TouchPointStationary = None
    name = property(None, None, None,
                    )

    values = {}

  TouchPointStateMask = None
  TouchPointStationary = None

  class TransformationMode(object):

    FastTransformation = None
    SmoothTransformation = None
    name = property(None, None, None,
                    )

    values = {}

  TransparentMode = None
  Tuesday = None

  class UIEffect(object):

    UI_AnimateCombo = None
    UI_AnimateMenu = None
    UI_AnimateToolBox = None
    UI_AnimateTooltip = None
    UI_FadeMenu = None
    UI_FadeTooltip = None
    UI_General = None
    name = property(None, None, None,
                    )

    values = {}

  UI_AnimateCombo = None
  UI_AnimateMenu = None
  UI_AnimateToolBox = None
  UI_AnimateTooltip = None
  UI_FadeMenu = None
  UI_FadeTooltip = None
  UI_General = None
  UNICODE_ACCEL = None
  UTC = None
  Unchecked = None
  UniqueConnection = None
  UniteClip = None
  UpArrow = None
  UpArrowCursor = None
  UserRole = None
  VerPattern = None
  Vertical = None
  VisualMoveStyle = None
  WA_AcceptDrops = None
  WA_AcceptTouchEvents = None
  WA_AlwaysShowToolTips = None
  WA_AttributeCount = None
  WA_AutoOrientation = None
  WA_CanHostQMdiSubWindowTitleBar = None
  WA_ContentsPropagated = None
  WA_CustomWhatsThis = None
  WA_DeleteOnClose = None
  WA_Disabled = None
  WA_DontCreateNativeAncestors = None
  WA_DontShowOnScreen = None
  WA_DropSiteRegistered = None
  WA_ForceAcceptDrops = None
  WA_ForceDisabled = None
  WA_ForceUpdatesDisabled = None
  WA_GrabbedShortcut = None
  WA_GroupLeader = None
  WA_Hover = None
  WA_InputMethodEnabled = None
  WA_InputMethodTransparent = None
  WA_InvalidSize = None
  WA_KeyCompression = None
  WA_KeyboardFocusChange = None
  WA_LaidOut = None
  WA_LayoutOnEntireRect = None
  WA_LayoutUsesWidgetRect = None
  WA_LockLandscapeOrientation = None
  WA_LockPortraitOrientation = None
  WA_MSWindowsUseDirect3D = None
  WA_MacAlwaysShowToolWindow = None
  WA_MacBrushedMetal = None
  WA_MacFrameworkScaled = None
  WA_MacMetalStyle = None
  WA_MacMiniSize = None
  WA_MacNoClickThrough = None
  WA_MacNoShadow = None
  WA_MacNormalSize = None
  WA_MacOpaqueSizeGrip = None
  WA_MacShowFocusRect = None
  WA_MacSmallSize = None
  WA_MacVariableSize = None
  WA_Mapped = None
  WA_MergeSoftkeys = None
  WA_MergeSoftkeysRecursively = None
  WA_MouseNoMask = None
  WA_MouseTracking = None
  WA_Moved = None
  WA_NativeWindow = None
  WA_NoBackground = None
  WA_NoChildEventsForParent = None
  WA_NoChildEventsFromChildren = None
  WA_NoMousePropagation = None
  WA_NoMouseReplay = None
  WA_NoSystemBackground = None
  WA_NoX11EventCompression = None
  WA_OpaquePaintEvent = None
  WA_OutsideWSRange = None
  WA_PaintOnScreen = None
  WA_PaintOutsidePaintEvent = None
  WA_PaintUnclipped = None
  WA_PendingMoveEvent = None
  WA_PendingResizeEvent = None
  WA_PendingUpdate = None
  WA_QuitOnClose = None
  WA_Resized = None
  WA_RightToLeft = None
  WA_SetCursor = None
  WA_SetFont = None
  WA_SetLayoutDirection = None
  WA_SetLocale = None
  WA_SetPalette = None
  WA_SetStyle = None
  WA_SetWindowIcon = None
  WA_SetWindowModality = None
  WA_ShowModal = None
  WA_ShowWithoutActivating = None
  WA_StaticContents = None
  WA_StyleSheet = None
  WA_StyledBackground = None
  WA_SymbianNoSystemRotation = None
  WA_TintedBackground = None
  WA_TouchPadAcceptSingleTouchEvents = None
  WA_TranslucentBackground = None
  WA_TransparentForMouseEvents = None
  WA_UnderMouse = None
  WA_UpdatesDisabled = None
  WA_WState_AcceptedTouchBeginEvent = None
  WA_WState_CompressKeys = None
  WA_WState_ConfigPending = None
  WA_WState_Created = None
  WA_WState_DND = None
  WA_WState_ExplicitShowHide = None
  WA_WState_Hidden = None
  WA_WState_InPaintEvent = None
  WA_WState_OwnSizePolicy = None
  WA_WState_Polished = None
  WA_WState_Reparented = None
  WA_WState_Visible = None
  WA_WState_WindowOpacitySet = None
  WA_WindowModified = None
  WA_WindowPropagation = None
  WA_X11BypassTransientForHint = None
  WA_X11DoNotAcceptFocus = None
  WA_X11NetWmWindowTypeCombo = None
  WA_X11NetWmWindowTypeDND = None
  WA_X11NetWmWindowTypeDesktop = None
  WA_X11NetWmWindowTypeDialog = None
  WA_X11NetWmWindowTypeDock = None
  WA_X11NetWmWindowTypeDropDownMenu = None
  WA_X11NetWmWindowTypeMenu = None
  WA_X11NetWmWindowTypeNotification = None
  WA_X11NetWmWindowTypePopupMenu = None
  WA_X11NetWmWindowTypeSplash = None
  WA_X11NetWmWindowTypeToolBar = None
  WA_X11NetWmWindowTypeToolTip = None
  WA_X11NetWmWindowTypeUtility = None
  WA_X11OpenGLOverlay = None
  WaitCursor = None
  Wednesday = None
  WhatsThisCursor = None
  WhatsThisPropertyRole = None
  WhatsThisRole = None
  WheelFocus = None

  class WhiteSpaceMode(object):

    WhiteSpaceModeUndefined = None
    WhiteSpaceNoWrap = None
    WhiteSpaceNormal = None
    WhiteSpacePre = None
    name = property(None, None, None,
                    )

    values = {}

  WhiteSpaceModeUndefined = None
  WhiteSpaceNoWrap = None
  WhiteSpaceNormal = None
  WhiteSpacePre = None
  Widget = None

  class WidgetAttribute(object):

    WA_AcceptDrops = None
    WA_AcceptTouchEvents = None
    WA_AlwaysShowToolTips = None
    WA_AttributeCount = None
    WA_AutoOrientation = None
    WA_CanHostQMdiSubWindowTitleBar = None
    WA_ContentsPropagated = None
    WA_CustomWhatsThis = None
    WA_DeleteOnClose = None
    WA_Disabled = None
    WA_DontCreateNativeAncestors = None
    WA_DontShowOnScreen = None
    WA_DropSiteRegistered = None
    WA_ForceAcceptDrops = None
    WA_ForceDisabled = None
    WA_ForceUpdatesDisabled = None
    WA_GrabbedShortcut = None
    WA_GroupLeader = None
    WA_Hover = None
    WA_InputMethodEnabled = None
    WA_InputMethodTransparent = None
    WA_InvalidSize = None
    WA_KeyCompression = None
    WA_KeyboardFocusChange = None
    WA_LaidOut = None
    WA_LayoutOnEntireRect = None
    WA_LayoutUsesWidgetRect = None
    WA_LockLandscapeOrientation = None
    WA_LockPortraitOrientation = None
    WA_MSWindowsUseDirect3D = None
    WA_MacAlwaysShowToolWindow = None
    WA_MacBrushedMetal = None
    WA_MacFrameworkScaled = None
    WA_MacMetalStyle = None
    WA_MacMiniSize = None
    WA_MacNoClickThrough = None
    WA_MacNoShadow = None
    WA_MacNormalSize = None
    WA_MacOpaqueSizeGrip = None
    WA_MacShowFocusRect = None
    WA_MacSmallSize = None
    WA_MacVariableSize = None
    WA_Mapped = None
    WA_MergeSoftkeys = None
    WA_MergeSoftkeysRecursively = None
    WA_MouseNoMask = None
    WA_MouseTracking = None
    WA_Moved = None
    WA_NativeWindow = None
    WA_NoBackground = None
    WA_NoChildEventsForParent = None
    WA_NoChildEventsFromChildren = None
    WA_NoMousePropagation = None
    WA_NoMouseReplay = None
    WA_NoSystemBackground = None
    WA_NoX11EventCompression = None
    WA_OpaquePaintEvent = None
    WA_OutsideWSRange = None
    WA_PaintOnScreen = None
    WA_PaintOutsidePaintEvent = None
    WA_PaintUnclipped = None
    WA_PendingMoveEvent = None
    WA_PendingResizeEvent = None
    WA_PendingUpdate = None
    WA_QuitOnClose = None
    WA_Resized = None
    WA_RightToLeft = None
    WA_SetCursor = None
    WA_SetFont = None
    WA_SetLayoutDirection = None
    WA_SetLocale = None
    WA_SetPalette = None
    WA_SetStyle = None
    WA_SetWindowIcon = None
    WA_SetWindowModality = None
    WA_ShowModal = None
    WA_ShowWithoutActivating = None
    WA_StaticContents = None
    WA_StyleSheet = None
    WA_StyledBackground = None
    WA_SymbianNoSystemRotation = None
    WA_TintedBackground = None
    WA_TouchPadAcceptSingleTouchEvents = None
    WA_TranslucentBackground = None
    WA_TransparentForMouseEvents = None
    WA_UnderMouse = None
    WA_UpdatesDisabled = None
    WA_WState_AcceptedTouchBeginEvent = None
    WA_WState_CompressKeys = None
    WA_WState_ConfigPending = None
    WA_WState_Created = None
    WA_WState_DND = None
    WA_WState_ExplicitShowHide = None
    WA_WState_Hidden = None
    WA_WState_InPaintEvent = None
    WA_WState_OwnSizePolicy = None
    WA_WState_Polished = None
    WA_WState_Reparented = None
    WA_WState_Visible = None
    WA_WState_WindowOpacitySet = None
    WA_WindowModified = None
    WA_WindowPropagation = None
    WA_X11BypassTransientForHint = None
    WA_X11DoNotAcceptFocus = None
    WA_X11NetWmWindowTypeCombo = None
    WA_X11NetWmWindowTypeDND = None
    WA_X11NetWmWindowTypeDesktop = None
    WA_X11NetWmWindowTypeDialog = None
    WA_X11NetWmWindowTypeDock = None
    WA_X11NetWmWindowTypeDropDownMenu = None
    WA_X11NetWmWindowTypeMenu = None
    WA_X11NetWmWindowTypeNotification = None
    WA_X11NetWmWindowTypePopupMenu = None
    WA_X11NetWmWindowTypeSplash = None
    WA_X11NetWmWindowTypeToolBar = None
    WA_X11NetWmWindowTypeToolTip = None
    WA_X11NetWmWindowTypeUtility = None
    WA_X11OpenGLOverlay = None
    name = property(None, None, None,
                    )

    values = {}

  WidgetShortcut = None
  WidgetWithChildrenShortcut = None
  WindingFill = None
  Window = None
  WindowActive = None
  WindowCancelButtonHint = None
  WindowCloseButtonHint = None
  WindowContextHelpButtonHint = None

  class WindowFlags(object):

    pass

  class WindowFrameSection(object):

    BottomLeftSection = None
    BottomRightSection = None
    BottomSection = None
    LeftSection = None
    NoSection = None
    RightSection = None
    TitleBarArea = None
    TopLeftSection = None
    TopRightSection = None
    TopSection = None
    name = property(None, None, None,
                    )

    values = {}

  WindowFullScreen = None
  WindowMaximizeButtonHint = None
  WindowMaximized = None
  WindowMinMaxButtonsHint = None
  WindowMinimizeButtonHint = None
  WindowMinimized = None
  WindowModal = None

  class WindowModality(object):

    ApplicationModal = None
    NonModal = None
    WindowModal = None
    name = property(None, None, None,
                    )

    values = {}

  WindowNoState = None
  WindowOkButtonHint = None
  WindowShadeButtonHint = None
  WindowShortcut = None
  WindowSoftkeysRespondHint = None
  WindowSoftkeysVisibleHint = None

  class WindowState(object):

    WindowActive = None
    WindowFullScreen = None
    WindowMaximized = None
    WindowMinimized = None
    WindowNoState = None
    name = property(None, None, None,
                    )

    values = {}

  class WindowStates(object):

    pass

  WindowStaysOnBottomHint = None
  WindowStaysOnTopHint = None
  WindowSystemMenuHint = None
  WindowTitleHint = None

  class WindowType(object):

    BypassGraphicsProxyWidget = None
    CustomizeWindowHint = None
    Desktop = None
    Dialog = None
    Drawer = None
    FramelessWindowHint = None
    MSWindowsFixedSizeDialogHint = None
    MSWindowsOwnDC = None
    MacWindowToolBarButtonHint = None
    Popup = None
    Sheet = None
    SplashScreen = None
    SubWindow = None
    Tool = None
    ToolTip = None
    Widget = None
    Window = None
    WindowCancelButtonHint = None
    WindowCloseButtonHint = None
    WindowContextHelpButtonHint = None
    WindowMaximizeButtonHint = None
    WindowMinMaxButtonsHint = None
    WindowMinimizeButtonHint = None
    WindowOkButtonHint = None
    WindowShadeButtonHint = None
    WindowSoftkeysRespondHint = None
    WindowSoftkeysVisibleHint = None
    WindowStaysOnBottomHint = None
    WindowStaysOnTopHint = None
    WindowSystemMenuHint = None
    WindowTitleHint = None
    WindowType_Mask = None
    X11BypassWindowManagerHint = None
    name = property(None, None, None,
                    )

    values = {}

  WindowType_Mask = None
  X11BypassWindowManagerHint = None
  XAxis = None
  XButton1 = None
  XButton2 = None
  YAxis = None
  ZAxis = None
  black = None
  blue = None
  color0 = None
  color1 = None
  cyan = None
  darkBlue = None
  darkCyan = None
  darkGray = None
  darkGreen = None
  darkMagenta = None
  darkRed = None
  darkYellow = None
  gray = None
  green = None
  lightGray = None
  magenta = None
  red = None
  transparent = None
  white = None
  yellow = None

QtCriticalMsg = None
QtDebugMsg = None
QtFatalMsg = None

class QtMsgType(object):

  QtCriticalMsg = None
  QtDebugMsg = None
  QtFatalMsg = None
  QtSystemMsg = None
  QtWarningMsg = None
  name = property(None, None, None,
                  )

  values = {}

QtSystemMsg = None
QtWarningMsg = None

class Signal(object):
  """ Signal """

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

class Slot(object):
  """ Slot """

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

__doc__ = None
__name__ = 'Qt.QtCore'

def qAbs():
  pass

def qAddPostRoutine():
  pass

def qChecksum():
  pass

def qCritical():
  pass

def qDebug():
  pass

def qFatal():
  pass

def qFuzzyCompare():
  pass

def qIsFinite():
  pass

def qIsInf():
  pass

def qIsNaN():
  pass

def qIsNull():
  pass

def qRegisterResourceData():
  pass

def qUnregisterResourceData():
  pass

def qVersion():
  pass

def qWarning():
  pass

def qrand():
  pass

def qsrand():
  pass

