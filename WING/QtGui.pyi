# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QAbstractTextDocumentLayout(QObject):

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

  def anchorAt():
    pass

  def blockBoundingRect():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def document():
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

  def drawInlineObject():
    pass

  def format():
    pass

  def formatIndex():
    pass

  def frameBoundingRect():
    pass

  def handlerForObject():
    pass

  def hitTest():
    pass

  def pageCount():
    pass

  def pageCountChanged():
    """ Signal """
    pass

  def paintDevice():
    pass

  def positionInlineObject():
    pass

  def registerHandler():
    pass

  def registerUserData():
    pass

  def resizeInlineObject():
    pass

  def setPaintDevice():
    pass

  staticMetaObject = None

  def update():
    """ Signal """
    pass

  def updateBlock():
    """ Signal """
    pass

class QActionEvent(QEvent):

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

  def action():
    pass

  def before():
    pass

  def registerEventType():
    pass

class QBitmap(QPixmap):

  Alpha = None

  class HBitmapFormat(object):

    Alpha = None
    NoAlpha = None
    PremultipliedAlpha = None
    name = property(None, None, None,
                    )

    values = {}

  NoAlpha = None

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
  PremultipliedAlpha = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clear():
    pass

  def defaultDepth():
    pass

  def fromData():
    pass

  def fromImage():
    pass

  def fromImageReader():
    pass

  def grabWidget():
    pass

  def grabWindow():
    pass

  def swap():
    pass

  def transformed():
    pass

  def trueMatrix():
    pass

class QBrush(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def color():
    pass

  def gradient():
    pass

  def isOpaque():
    pass

  def matrix():
    pass

  def setColor():
    pass

  def setMatrix():
    pass

  def setStyle():
    pass

  def setTexture():
    pass

  def setTextureImage():
    pass

  def setTransform():
    pass

  def style():
    pass

  def swap():
    pass

  def texture():
    pass

  def textureImage():
    pass

  def transform():
    pass

class QClipboard(QObject):

  Clipboard = None
  FindBuffer = None
  LastMode = None

  class Mode(object):

    Clipboard = None
    FindBuffer = None
    LastMode = None
    Selection = None
    name = property(None, None, None,
                    )

    values = {}

  Selection = None

  def changed():
    """ Signal """
    pass

  def clear():
    pass

  def connect():
    pass

  def connectNotify():
    pass

  def dataChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def event():
    pass

  def findBufferChanged():
    """ Signal """
    pass

  def image():
    pass

  def mimeData():
    pass

  def ownsClipboard():
    pass

  def ownsFindBuffer():
    pass

  def ownsSelection():
    pass

  def pixmap():
    pass

  def registerUserData():
    pass

  def selectionChanged():
    """ Signal """
    pass

  def setImage():
    pass

  def setMimeData():
    pass

  def setPixmap():
    pass

  def setText():
    pass

  staticMetaObject = None

  def supportsFindBuffer():
    pass

  def supportsSelection():
    pass

  def text():
    pass

class QCloseEvent(QEvent):

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

class QColor(Object):

  Cmyk = None
  Hsl = None
  Hsv = None
  Invalid = None
  Rgb = None

  class Spec(object):

    Cmyk = None
    Hsl = None
    Hsv = None
    Invalid = None
    Rgb = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alpha():
    pass

  def alphaF():
    pass

  def black():
    pass

  def blackF():
    pass

  def blue():
    pass

  def blueF():
    pass

  def colorNames():
    pass

  def convertTo():
    pass

  def cyan():
    pass

  def cyanF():
    pass

  def darker():
    pass

  def fromCmyk():
    pass

  def fromCmykF():
    pass

  def fromHsl():
    pass

  def fromHslF():
    pass

  def fromHsv():
    pass

  def fromHsvF():
    pass

  def fromRgb():
    pass

  def fromRgbF():
    pass

  def fromRgba():
    pass

  def getCmyk():
    pass

  def getCmykF():
    pass

  def getHsl():
    pass

  def getHslF():
    pass

  def getHsv():
    pass

  def getHsvF():
    pass

  def getRgb():
    pass

  def getRgbF():
    pass

  def green():
    pass

  def greenF():
    pass

  def hslHue():
    pass

  def hslHueF():
    pass

  def hslSaturation():
    pass

  def hslSaturationF():
    pass

  def hsvHue():
    pass

  def hsvHueF():
    pass

  def hsvSaturation():
    pass

  def hsvSaturationF():
    pass

  def hue():
    pass

  def hueF():
    pass

  def isValid():
    pass

  def isValidColor():
    pass

  def lighter():
    pass

  def lightness():
    pass

  def lightnessF():
    pass

  def magenta():
    pass

  def magentaF():
    pass

  def name():
    pass

  def red():
    pass

  def redF():
    pass

  def rgb():
    pass

  def rgba():
    pass

  def saturation():
    pass

  def saturationF():
    pass

  def setAlpha():
    pass

  def setAlphaF():
    pass

  def setBlue():
    pass

  def setBlueF():
    pass

  def setCmyk():
    pass

  def setCmykF():
    pass

  def setGreen():
    pass

  def setGreenF():
    pass

  def setHsl():
    pass

  def setHslF():
    pass

  def setHsv():
    pass

  def setHsvF():
    pass

  def setNamedColor():
    pass

  def setRed():
    pass

  def setRedF():
    pass

  def setRgb():
    pass

  def setRgbF():
    pass

  def setRgba():
    pass

  def spec():
    pass

  def toCmyk():
    pass

  def toHsl():
    pass

  def toHsv():
    pass

  def toRgb():
    pass

  def toTuple():
    pass

  def value():
    pass

  def valueF():
    pass

  def yellow():
    pass

  def yellowF():
    pass

class QConicalGradient(QGradient):

  ColorInterpolation = None
  ComponentInterpolation = None
  ConicalGradient = None

  class CoordinateMode(object):

    LogicalMode = None
    ObjectBoundingMode = None
    StretchToDeviceMode = None
    name = property(None, None, None,
                    )

    values = {}

  class InterpolationMode(object):

    ColorInterpolation = None
    ComponentInterpolation = None
    name = property(None, None, None,
                    )

    values = {}

  LinearGradient = None
  LogicalMode = None
  NoGradient = None
  ObjectBoundingMode = None
  PadSpread = None
  RadialGradient = None
  ReflectSpread = None
  RepeatSpread = None

  class Spread(object):

    PadSpread = None
    ReflectSpread = None
    RepeatSpread = None
    name = property(None, None, None,
                    )

    values = {}

  StretchToDeviceMode = None

  class Type(object):

    ConicalGradient = None
    LinearGradient = None
    NoGradient = None
    RadialGradient = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def angle():
    pass

  def center():
    pass

  def setAngle():
    pass

  def setCenter():
    pass

class QContextMenuEvent(QInputEvent):

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

  def globalPos():
    pass

  def globalX():
    pass

  def globalY():
    pass

  def pos():
    pass

  def reason():
    pass

  def registerEventType():
    pass

  def x():
    pass

  def y():
    pass

class QCursor(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bitmap():
    pass

  def hotSpot():
    pass

  def mask():
    pass

  def pixmap():
    pass

  def pos():
    pass

  def setPos():
    pass

  def setShape():
    pass

  def shape():
    pass

class QDesktopServices(Object):

  ApplicationsLocation = None
  CacheLocation = None
  DataLocation = None
  DesktopLocation = None
  DocumentsLocation = None
  FontsLocation = None
  HomeLocation = None
  MoviesLocation = None
  MusicLocation = None
  PicturesLocation = None

  class StandardLocation(object):

    ApplicationsLocation = None
    CacheLocation = None
    DataLocation = None
    DesktopLocation = None
    DocumentsLocation = None
    FontsLocation = None
    HomeLocation = None
    MoviesLocation = None
    MusicLocation = None
    PicturesLocation = None
    TempLocation = None
    name = property(None, None, None,
                    )

    values = {}

  TempLocation = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def displayName():
    pass

  def openUrl():
    pass

  def setUrlHandler():
    pass

  def storageLocation():
    pass

  def unsetUrlHandler():
    pass

class QDoubleValidator(QValidator):

  Acceptable = None
  Intermediate = None
  Invalid = None

  class Notation(object):

    ScientificNotation = None
    StandardNotation = None
    name = property(None, None, None,
                    )

    values = {}

  ScientificNotation = None
  StandardNotation = None

  class State(object):

    Acceptable = None
    Intermediate = None
    Invalid = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bottom():
    pass

  def connect():
    pass

  def decimals():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def notation():
    pass

  def registerUserData():
    pass

  def setBottom():
    pass

  def setDecimals():
    pass

  def setNotation():
    pass

  def setRange():
    pass

  def setTop():
    pass

  staticMetaObject = None

  def top():
    pass

  def validate():
    pass

class QDrag(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actionChanged():
    """ Signal """
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

  def hotSpot():
    pass

  def mimeData():
    pass

  def pixmap():
    pass

  def registerUserData():
    pass

  def setDragCursor():
    pass

  def setHotSpot():
    pass

  def setMimeData():
    pass

  def setPixmap():
    pass

  def source():
    pass

  def start():
    pass

  staticMetaObject = None

  def target():
    pass

  def targetChanged():
    """ Signal """
    pass

class QDragEnterEvent(QDragMoveEvent):

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

class QDragLeaveEvent(QEvent):

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

class QDragMoveEvent(QDropEvent):

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

  def answerRect():
    pass

  def ignore():
    pass

  def registerEventType():
    pass

class QDropEvent(QEvent):

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

  def dropAction():
    pass

  def keyboardModifiers():
    pass

  def mimeData():
    pass

  def mouseButtons():
    pass

  def pos():
    pass

  def possibleActions():
    pass

  def proposedAction():
    pass

  def registerEventType():
    pass

  def setDropAction():
    pass

  def source():
    pass

class QFileOpenEvent(QEvent):

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

  def file():
    pass

  def openFile():
    pass

  def registerEventType():
    pass

  def url():
    pass

class QFocusEvent(QEvent):

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

  def gotFocus():
    pass

  def lostFocus():
    pass

  def reason():
    pass

  def registerEventType():
    pass

class QFont(Object):

  AbsoluteSpacing = None
  AllLowercase = None
  AllUppercase = None
  AnyStyle = None
  Black = None
  Bold = None

  class Capitalization(object):

    AllLowercase = None
    AllUppercase = None
    Capitalize = None
    MixedCase = None
    SmallCaps = None
    name = property(None, None, None,
                    )

    values = {}

  Capitalize = None
  Condensed = None
  Courier = None
  Cursive = None
  Decorative = None
  DemiBold = None
  Expanded = None
  ExtraCondensed = None
  ExtraExpanded = None
  Fantasy = None
  ForceIntegerMetrics = None
  ForceOutline = None
  Helvetica = None

  class HintingPreference(object):

    PreferDefaultHinting = None
    PreferFullHinting = None
    PreferNoHinting = None
    PreferVerticalHinting = None
    name = property(None, None, None,
                    )

    values = {}

  Light = None
  MixedCase = None
  Monospace = None
  NoAntialias = None
  NoFontMerging = None
  Normal = None
  OldEnglish = None
  OpenGLCompatible = None
  PercentageSpacing = None
  PreferAntialias = None
  PreferBitmap = None
  PreferDefault = None
  PreferDefaultHinting = None
  PreferDevice = None
  PreferFullHinting = None
  PreferMatch = None
  PreferNoHinting = None
  PreferOutline = None
  PreferQuality = None
  PreferVerticalHinting = None
  SansSerif = None
  SemiCondensed = None
  SemiExpanded = None
  Serif = None
  SmallCaps = None

  class SpacingType(object):

    AbsoluteSpacing = None
    PercentageSpacing = None
    name = property(None, None, None,
                    )

    values = {}

  class Stretch(object):

    Condensed = None
    Expanded = None
    ExtraCondensed = None
    ExtraExpanded = None
    SemiCondensed = None
    SemiExpanded = None
    UltraCondensed = None
    UltraExpanded = None
    Unstretched = None
    name = property(None, None, None,
                    )

    values = {}

  class Style(object):

    StyleItalic = None
    StyleNormal = None
    StyleOblique = None
    name = property(None, None, None,
                    )

    values = {}

  class StyleHint(object):

    AnyStyle = None
    Courier = None
    Cursive = None
    Decorative = None
    Fantasy = None
    Helvetica = None
    Monospace = None
    OldEnglish = None
    SansSerif = None
    Serif = None
    System = None
    Times = None
    TypeWriter = None
    name = property(None, None, None,
                    )

    values = {}

  StyleItalic = None
  StyleNormal = None
  StyleOblique = None

  class StyleStrategy(object):

    ForceIntegerMetrics = None
    ForceOutline = None
    NoAntialias = None
    NoFontMerging = None
    OpenGLCompatible = None
    PreferAntialias = None
    PreferBitmap = None
    PreferDefault = None
    PreferDevice = None
    PreferMatch = None
    PreferOutline = None
    PreferQuality = None
    name = property(None, None, None,
                    )

    values = {}

  System = None
  Times = None
  TypeWriter = None
  UltraCondensed = None
  UltraExpanded = None
  Unstretched = None

  class Weight(object):

    Black = None
    Bold = None
    DemiBold = None
    Light = None
    Normal = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bold():
    pass

  def cacheStatistics():
    pass

  def capitalization():
    pass

  def cleanup():
    pass

  def defaultFamily():
    pass

  def exactMatch():
    pass

  def family():
    pass

  def fixedPitch():
    pass

  def fromString():
    pass

  def hintingPreference():
    pass

  def initialize():
    pass

  def insertSubstitution():
    pass

  def insertSubstitutions():
    pass

  def isCopyOf():
    pass

  def italic():
    pass

  def kerning():
    pass

  def key():
    pass

  def lastResortFamily():
    pass

  def lastResortFont():
    pass

  def letterSpacing():
    pass

  def letterSpacingType():
    pass

  def overline():
    pass

  def pixelSize():
    pass

  def pointSize():
    pass

  def pointSizeF():
    pass

  def rawMode():
    pass

  def rawName():
    pass

  def removeSubstitution():
    pass

  def resolve():
    pass

  def setBold():
    pass

  def setCapitalization():
    pass

  def setFamily():
    pass

  def setFixedPitch():
    pass

  def setHintingPreference():
    pass

  def setItalic():
    pass

  def setKerning():
    pass

  def setLetterSpacing():
    pass

  def setOverline():
    pass

  def setPixelSize():
    pass

  def setPointSize():
    pass

  def setPointSizeF():
    pass

  def setRawMode():
    pass

  def setRawName():
    pass

  def setStretch():
    pass

  def setStrikeOut():
    pass

  def setStyle():
    pass

  def setStyleHint():
    pass

  def setStyleName():
    pass

  def setStyleStrategy():
    pass

  def setUnderline():
    pass

  def setWeight():
    pass

  def setWordSpacing():
    pass

  def stretch():
    pass

  def strikeOut():
    pass

  def style():
    pass

  def styleHint():
    pass

  def styleName():
    pass

  def styleStrategy():
    pass

  def substitute():
    pass

  def substitutes():
    pass

  def substitutions():
    pass

  def toString():
    pass

  def underline():
    pass

  def weight():
    pass

  def wordSpacing():
    pass

class QFontDatabase(Object):

  Any = None
  Arabic = None
  Armenian = None
  Bengali = None
  Cyrillic = None
  Devanagari = None
  Georgian = None
  Greek = None
  Gujarati = None
  Gurmukhi = None
  Hebrew = None
  Japanese = None
  Kannada = None
  Khmer = None
  Korean = None
  Lao = None
  Latin = None
  Malayalam = None
  Myanmar = None
  Nko = None
  Ogham = None
  Oriya = None
  Other = None
  Runic = None
  SimplifiedChinese = None
  Sinhala = None
  Symbol = None
  Syriac = None
  Tamil = None
  Telugu = None
  Thaana = None
  Thai = None
  Tibetan = None
  TraditionalChinese = None
  Vietnamese = None

  class WritingSystem(object):

    Any = None
    Arabic = None
    Armenian = None
    Bengali = None
    Cyrillic = None
    Devanagari = None
    Georgian = None
    Greek = None
    Gujarati = None
    Gurmukhi = None
    Hebrew = None
    Japanese = None
    Kannada = None
    Khmer = None
    Korean = None
    Lao = None
    Latin = None
    Malayalam = None
    Myanmar = None
    Nko = None
    Ogham = None
    Oriya = None
    Other = None
    Runic = None
    SimplifiedChinese = None
    Sinhala = None
    Symbol = None
    Syriac = None
    Tamil = None
    Telugu = None
    Thaana = None
    Thai = None
    Tibetan = None
    TraditionalChinese = None
    Vietnamese = None
    WritingSystemsCount = None
    name = property(None, None, None,
                    )

    values = {}

  WritingSystemsCount = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addApplicationFont():
    pass

  def addApplicationFontFromData():
    pass

  def applicationFontFamilies():
    pass

  def bold():
    pass

  def families():
    pass

  def font():
    pass

  def hasFamily():
    pass

  def isBitmapScalable():
    pass

  def isFixedPitch():
    pass

  def isScalable():
    pass

  def isSmoothlyScalable():
    pass

  def italic():
    pass

  def pointSizes():
    pass

  def removeAllApplicationFonts():
    pass

  def removeApplicationFont():
    pass

  def smoothSizes():
    pass

  def standardSizes():
    pass

  def styleString():
    pass

  def styles():
    pass

  def supportsThreadedFontRendering():
    pass

  def weight():
    pass

  def writingSystemName():
    pass

  def writingSystemSample():
    pass

  def writingSystems():
    pass

class QFontInfo(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bold():
    pass

  def exactMatch():
    pass

  def family():
    pass

  def fixedPitch():
    pass

  def italic():
    pass

  def overline():
    pass

  def pixelSize():
    pass

  def pointSize():
    pass

  def pointSizeF():
    pass

  def rawMode():
    pass

  def strikeOut():
    pass

  def style():
    pass

  def styleHint():
    pass

  def styleName():
    pass

  def underline():
    pass

  def weight():
    pass

class QFontMetrics(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def ascent():
    pass

  def averageCharWidth():
    pass

  def boundingRect():
    pass

  def boundingRectChar():
    pass

  def charWidth():
    pass

  def descent():
    pass

  def elidedText():
    pass

  def height():
    pass

  def inFont():
    pass

  def inFontUcs4():
    pass

  def leading():
    pass

  def leftBearing():
    pass

  def lineSpacing():
    pass

  def lineWidth():
    pass

  def maxWidth():
    pass

  def minLeftBearing():
    pass

  def minRightBearing():
    pass

  def overlinePos():
    pass

  def rightBearing():
    pass

  def size():
    pass

  def strikeOutPos():
    pass

  def tightBoundingRect():
    pass

  def underlinePos():
    pass

  def width():
    pass

  def widthChar():
    pass

  def xHeight():
    pass

class QFontMetricsF(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def ascent():
    pass

  def averageCharWidth():
    pass

  def boundingRect():
    pass

  def boundingRectChar():
    pass

  def descent():
    pass

  def elidedText():
    pass

  def height():
    pass

  def inFont():
    pass

  def inFontUcs4():
    pass

  def leading():
    pass

  def leftBearing():
    pass

  def lineSpacing():
    pass

  def lineWidth():
    pass

  def maxWidth():
    pass

  def minLeftBearing():
    pass

  def minRightBearing():
    pass

  def overlinePos():
    pass

  def rightBearing():
    pass

  def size():
    pass

  def strikeOutPos():
    pass

  def tightBoundingRect():
    pass

  def underlinePos():
    pass

  def width():
    pass

  def widthChar():
    pass

  def xHeight():
    pass

class QGradient(Object):

  ColorInterpolation = None
  ComponentInterpolation = None
  ConicalGradient = None
  LinearGradient = None
  LogicalMode = None
  NoGradient = None
  ObjectBoundingMode = None
  PadSpread = None
  RadialGradient = None
  ReflectSpread = None
  RepeatSpread = None
  StretchToDeviceMode = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def coordinateMode():
    pass

  def interpolationMode():
    pass

  def setColorAt():
    pass

  def setCoordinateMode():
    pass

  def setInterpolationMode():
    pass

  def setSpread():
    pass

  def setStops():
    pass

  def spread():
    pass

  def stops():
    pass

  def type():
    pass

class QHelpEvent(QEvent):

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

  def globalPos():
    pass

  def globalX():
    pass

  def globalY():
    pass

  def pos():
    pass

  def registerEventType():
    pass

  def x():
    pass

  def y():
    pass

class QHideEvent(QEvent):

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

class QHoverEvent(QEvent):

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

  def oldPos():
    pass

  def pos():
    pass

  def registerEventType():
    pass

class QIcon(Object):

  Active = None
  Disabled = None

  class Mode(object):

    Active = None
    Disabled = None
    Normal = None
    Selected = None
    name = property(None, None, None,
                    )

    values = {}

  Normal = None
  Off = None
  On = None
  Selected = None

  class State(object):

    Off = None
    On = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actualSize():
    pass

  def addFile():
    pass

  def addPixmap():
    pass

  def availableSizes():
    pass

  def cacheKey():
    pass

  def fromTheme():
    pass

  def hasThemeIcon():
    pass

  def isNull():
    pass

  def name():
    pass

  def paint():
    pass

  def pixmap():
    pass

  def setThemeName():
    pass

  def setThemeSearchPaths():
    pass

  def swap():
    pass

  def themeName():
    pass

  def themeSearchPaths():
    pass

class QIconDragEvent(QEvent):

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

class QIconEngine(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def actualSize():
    pass

  def addFile():
    pass

  def addPixmap():
    pass

  def paint():
    pass

  def pixmap():
    pass

class QImage(QPaintDevice):

  class Format(object):

    Format_ARGB32 = None
    Format_ARGB32_Premultiplied = None
    Format_ARGB4444_Premultiplied = None
    Format_ARGB6666_Premultiplied = None
    Format_ARGB8555_Premultiplied = None
    Format_ARGB8565_Premultiplied = None
    Format_Indexed8 = None
    Format_Invalid = None
    Format_Mono = None
    Format_MonoLSB = None
    Format_RGB16 = None
    Format_RGB32 = None
    Format_RGB444 = None
    Format_RGB555 = None
    Format_RGB666 = None
    Format_RGB888 = None
    NImageFormats = None
    name = property(None, None, None,
                    )

    values = {}

  Format_ARGB32 = None
  Format_ARGB32_Premultiplied = None
  Format_ARGB4444_Premultiplied = None
  Format_ARGB6666_Premultiplied = None
  Format_ARGB8555_Premultiplied = None
  Format_ARGB8565_Premultiplied = None
  Format_Indexed8 = None
  Format_Invalid = None
  Format_Mono = None
  Format_MonoLSB = None
  Format_RGB16 = None
  Format_RGB32 = None
  Format_RGB444 = None
  Format_RGB555 = None
  Format_RGB666 = None
  Format_RGB888 = None

  class InvertMode(object):

    InvertRgb = None
    InvertRgba = None
    name = property(None, None, None,
                    )

    values = {}

  InvertRgb = None
  InvertRgba = None
  NImageFormats = None
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

  def allGray():
    pass

  def alphaChannel():
    pass

  def bitPlaneCount():
    pass

  def bits():
    pass

  def byteCount():
    pass

  def bytesPerLine():
    pass

  def cacheKey():
    pass

  def color():
    pass

  def colorCount():
    pass

  def colorTable():
    pass

  def constBits():
    pass

  def constScanLine():
    pass

  def convertToFormat():
    pass

  def copy():
    pass

  def createAlphaMask():
    pass

  def createHeuristicMask():
    pass

  def createMaskFromColor():
    pass

  def depth():
    pass

  def devType():
    pass

  def dotsPerMeterX():
    pass

  def dotsPerMeterY():
    pass

  def fill():
    pass

  def format():
    pass

  def fromData():
    pass

  def hasAlphaChannel():
    pass

  def height():
    pass

  def invertPixels():
    pass

  def isGrayscale():
    pass

  def isNull():
    pass

  def load():
    pass

  def loadFromData():
    pass

  def metric():
    pass

  def mirrored():
    pass

  def numBytes():
    pass

  def numColors():
    pass

  def offset():
    pass

  def paintEngine():
    pass

  def pixel():
    pass

  def pixelIndex():
    pass

  def rect():
    pass

  def rgbSwapped():
    pass

  def save():
    pass

  def scaled():
    pass

  def scaledToHeight():
    pass

  def scaledToWidth():
    pass

  def scanLine():
    pass

  def setAlphaChannel():
    pass

  def setColor():
    pass

  def setColorCount():
    pass

  def setColorTable():
    pass

  def setDotsPerMeterX():
    pass

  def setDotsPerMeterY():
    pass

  def setNumColors():
    pass

  def setOffset():
    pass

  def setPixel():
    pass

  def setText():
    pass

  def size():
    pass

  def swap():
    pass

  def text():
    pass

  def textKeys():
    pass

  def transformed():
    pass

  def trueMatrix():
    pass

  def valid():
    pass

  def width():
    pass

class QImageIOHandler(Object):

  Animation = None
  BackgroundColor = None
  ClipRect = None
  CompressionRatio = None
  Description = None
  Endianness = None
  Gamma = None
  ImageFormat = None

  class ImageOption(object):

    Animation = None
    BackgroundColor = None
    ClipRect = None
    CompressionRatio = None
    Description = None
    Endianness = None
    Gamma = None
    ImageFormat = None
    IncrementalReading = None
    Name = None
    Quality = None
    ScaledClipRect = None
    ScaledSize = None
    Size = None
    SubType = None
    name = property(None, None, None,
                    )

    values = {}

  IncrementalReading = None
  Name = None
  Quality = None
  ScaledClipRect = None
  ScaledSize = None
  Size = None
  SubType = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def canRead():
    pass

  def currentImageNumber():
    pass

  def currentImageRect():
    pass

  def device():
    pass

  def format():
    pass

  def imageCount():
    pass

  def jumpToImage():
    pass

  def jumpToNextImage():
    pass

  def loopCount():
    pass

  def nextImageDelay():
    pass

  def option():
    pass

  def read():
    pass

  def setDevice():
    pass

  def setFormat():
    pass

  def setOption():
    pass

  def supportsOption():
    pass

  def write():
    pass

class QImageReader(Object):

  DeviceError = None
  FileNotFoundError = None

  class ImageReaderError(object):

    DeviceError = None
    FileNotFoundError = None
    InvalidDataError = None
    UnknownError = None
    UnsupportedFormatError = None
    name = property(None, None, None,
                    )

    values = {}

  InvalidDataError = None
  UnknownError = None
  UnsupportedFormatError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def autoDetectImageFormat():
    pass

  def backgroundColor():
    pass

  def canRead():
    pass

  def clipRect():
    pass

  def currentImageNumber():
    pass

  def currentImageRect():
    pass

  def decideFormatFromContent():
    pass

  def device():
    pass

  def error():
    pass

  def errorString():
    pass

  def fileName():
    pass

  def format():
    pass

  def imageCount():
    pass

  def imageFormat():
    pass

  def jumpToImage():
    pass

  def jumpToNextImage():
    pass

  def loopCount():
    pass

  def nextImageDelay():
    pass

  def quality():
    pass

  def read():
    pass

  def scaledClipRect():
    pass

  def scaledSize():
    pass

  def setAutoDetectImageFormat():
    pass

  def setBackgroundColor():
    pass

  def setClipRect():
    pass

  def setDecideFormatFromContent():
    pass

  def setDevice():
    pass

  def setFileName():
    pass

  def setFormat():
    pass

  def setQuality():
    pass

  def setScaledClipRect():
    pass

  def setScaledSize():
    pass

  def size():
    pass

  def supportedImageFormats():
    pass

  def supportsAnimation():
    pass

  def supportsOption():
    pass

  def text():
    pass

  def textKeys():
    pass

class QImageWriter(Object):

  DeviceError = None

  class ImageWriterError(object):

    DeviceError = None
    UnknownError = None
    UnsupportedFormatError = None
    name = property(None, None, None,
                    )

    values = {}

  UnknownError = None
  UnsupportedFormatError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def canWrite():
    pass

  def compression():
    pass

  def device():
    pass

  def error():
    pass

  def errorString():
    pass

  def fileName():
    pass

  def format():
    pass

  def gamma():
    pass

  def quality():
    pass

  def setCompression():
    pass

  def setDevice():
    pass

  def setFileName():
    pass

  def setFormat():
    pass

  def setGamma():
    pass

  def setQuality():
    pass

  def setText():
    pass

  def supportedImageFormats():
    pass

  def supportsOption():
    pass

  def write():
    pass

class QInputEvent(QEvent):

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

  def modifiers():
    pass

  def registerEventType():
    pass

  def setModifiers():
    pass

class QInputMethodEvent(QEvent):

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

  class Attribute(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    length = property(None, None, None,
                      )

    start = property(None, None, None,
                     )

    type = property(None, None, None,
                    )

    value = property(None, None, None,
                     )


  class AttributeType(object):

    Cursor = None
    Language = None
    Ruby = None
    Selection = None
    TextFormat = None
    name = property(None, None, None,
                    )

    values = {}

  ChildAdded = None
  ChildPolished = None
  ChildRemoved = None
  Clipboard = None
  Close = None
  CloseSoftwareInputPanel = None
  ContentsRectChange = None
  ContextMenu = None
  Create = None
  Cursor = None
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
  Language = None
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
  Ruby = None
  Selection = None
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
  TextFormat = None
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

  def attributes():
    pass

  def commitString():
    pass

  def preeditString():
    pass

  def registerEventType():
    pass

  def replacementLength():
    pass

  def replacementStart():
    pass

  def setCommitString():
    pass

class QIntValidator(QValidator):

  Acceptable = None
  Intermediate = None
  Invalid = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bottom():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def fixup():
    pass

  def registerUserData():
    pass

  def setBottom():
    pass

  def setRange():
    pass

  def setTop():
    pass

  staticMetaObject = None

  def top():
    pass

  def validate():
    pass

class QKeyEvent(QInputEvent):

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

  autor = property(None, None, None,
                   )


  def count():
    pass

  def createExtendedKeyEvent():
    pass

  def hasExtendedInfo():
    pass

  def isAutoRepeat():
    pass

  def key():
    pass

  def matches():
    pass

  def modifiers():
    pass

  def nativeModifiers():
    pass

  def nativeScanCode():
    pass

  def nativeVirtualKey():
    pass

  def registerEventType():
    pass

  def text():
    pass

class QKeySequence(Object):

  AddTab = None
  Back = None
  Bold = None
  Close = None
  Copy = None
  Cut = None
  Delete = None
  DeleteEndOfLine = None
  DeleteEndOfWord = None
  DeleteStartOfWord = None
  ExactMatch = None
  Find = None
  FindNext = None
  FindPrevious = None
  Forward = None
  HelpContents = None
  InsertLineSeparator = None
  InsertParagraphSeparator = None
  Italic = None
  MoveToEndOfBlock = None
  MoveToEndOfDocument = None
  MoveToEndOfLine = None
  MoveToNextChar = None
  MoveToNextLine = None
  MoveToNextPage = None
  MoveToNextWord = None
  MoveToPreviousChar = None
  MoveToPreviousLine = None
  MoveToPreviousPage = None
  MoveToPreviousWord = None
  MoveToStartOfBlock = None
  MoveToStartOfDocument = None
  MoveToStartOfLine = None
  NativeText = None
  New = None
  NextChild = None
  NoMatch = None
  Open = None
  PartialMatch = None
  Paste = None
  PortableText = None
  Preferences = None
  PreviousChild = None
  Print = None
  Quit = None
  Redo = None
  Refresh = None
  Replace = None
  Save = None
  SaveAs = None
  SelectAll = None
  SelectEndOfBlock = None
  SelectEndOfDocument = None
  SelectEndOfLine = None
  SelectNextChar = None
  SelectNextLine = None
  SelectNextPage = None
  SelectNextWord = None
  SelectPreviousChar = None
  SelectPreviousLine = None
  SelectPreviousPage = None
  SelectPreviousWord = None
  SelectStartOfBlock = None
  SelectStartOfDocument = None
  SelectStartOfLine = None

  class SequenceFormat(object):

    NativeText = None
    PortableText = None
    name = property(None, None, None,
                    )

    values = {}

  class SequenceMatch(object):

    ExactMatch = None
    NoMatch = None
    PartialMatch = None
    name = property(None, None, None,
                    )

    values = {}

  class StandardKey(object):

    AddTab = None
    Back = None
    Bold = None
    Close = None
    Copy = None
    Cut = None
    Delete = None
    DeleteEndOfLine = None
    DeleteEndOfWord = None
    DeleteStartOfWord = None
    Find = None
    FindNext = None
    FindPrevious = None
    Forward = None
    HelpContents = None
    InsertLineSeparator = None
    InsertParagraphSeparator = None
    Italic = None
    MoveToEndOfBlock = None
    MoveToEndOfDocument = None
    MoveToEndOfLine = None
    MoveToNextChar = None
    MoveToNextLine = None
    MoveToNextPage = None
    MoveToNextWord = None
    MoveToPreviousChar = None
    MoveToPreviousLine = None
    MoveToPreviousPage = None
    MoveToPreviousWord = None
    MoveToStartOfBlock = None
    MoveToStartOfDocument = None
    MoveToStartOfLine = None
    New = None
    NextChild = None
    Open = None
    Paste = None
    Preferences = None
    PreviousChild = None
    Print = None
    Quit = None
    Redo = None
    Refresh = None
    Replace = None
    Save = None
    SaveAs = None
    SelectAll = None
    SelectEndOfBlock = None
    SelectEndOfDocument = None
    SelectEndOfLine = None
    SelectNextChar = None
    SelectNextLine = None
    SelectNextPage = None
    SelectNextWord = None
    SelectPreviousChar = None
    SelectPreviousLine = None
    SelectPreviousPage = None
    SelectPreviousWord = None
    SelectStartOfBlock = None
    SelectStartOfDocument = None
    SelectStartOfLine = None
    Underline = None
    Undo = None
    UnknownKey = None
    WhatsThis = None
    ZoomIn = None
    ZoomOut = None
    name = property(None, None, None,
                    )

    values = {}

  Underline = None
  Undo = None
  UnknownKey = None
  WhatsThis = None
  ZoomIn = None
  ZoomOut = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def count():
    pass

  def fromString():
    pass

  def isEmpty():
    pass

  def keyBindings():
    pass

  def matches():
    pass

  def mnemonic():
    pass

  def swap():
    pass

  def toString():
    pass

class QLinearGradient(QGradient):

  ColorInterpolation = None
  ComponentInterpolation = None
  ConicalGradient = None
  LinearGradient = None
  LogicalMode = None
  NoGradient = None
  ObjectBoundingMode = None
  PadSpread = None
  RadialGradient = None
  ReflectSpread = None
  RepeatSpread = None
  StretchToDeviceMode = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def finalStop():
    pass

  def setFinalStop():
    pass

  def setStart():
    pass

  def start():
    pass

class QMatrix2x2(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix2x3(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix2x4(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix3x2(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix3x3(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix3x4(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix4x2(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix4x3(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fill():
    pass

  def transposed():
    pass

class QMatrix4x4(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def column():
    pass

  def copyDataTo():
    pass

  def data():
    pass

  def determinant():
    pass

  def fill():
    pass

  def flipCoordinates():
    pass

  def frustum():
    pass

  def inverted():
    pass

  def isIdentity():
    pass

  def lookAt():
    pass

  def map():
    pass

  def mapRect():
    pass

  def mapVector():
    pass

  def normalMatrix():
    pass

  def optimize():
    pass

  def ortho():
    pass

  def perspective():
    pass

  def rotate():
    pass

  def row():
    pass

  def scale():
    pass

  def setColumn():
    pass

  def setRow():
    pass

  def setToIdentity():
    pass

  def toAffine():
    pass

  def toTransform():
    pass

  def translate():
    pass

  def transposed():
    pass

class QMouseEvent(QInputEvent):

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

  def buttons():
    pass

  def createExtendedMouseEvent():
    pass

  def globalPos():
    pass

  def globalX():
    pass

  def globalY():
    pass

  def hasExtendedInfo():
    pass

  def pos():
    pass

  def posF():
    pass

  def registerEventType():
    pass

  def x():
    pass

  def y():
    pass

class QMoveEvent(QEvent):

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

  def oldPos():
    pass

  def pos():
    pass

  def registerEventType():
    pass

class QMovie(QObject):

  CacheAll = None

  class CacheMode(object):

    CacheAll = None
    CacheNone = None
    name = property(None, None, None,
                    )

    values = {}

  CacheNone = None

  class MovieState(object):

    NotRunning = None
    Paused = None
    Running = None
    name = property(None, None, None,
                    )

    values = {}

  NotRunning = None
  Paused = None
  Running = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def backgroundColor():
    pass

  def cacheMode():
    pass

  def connect():
    pass

  def currentFrameNumber():
    pass

  def currentImage():
    pass

  def currentPixmap():
    pass

  def destroyed():
    """ Signal """
    pass

  def device():
    pass

  def disconnect():
    pass

  def error():
    """ Signal """
    pass

  def fileName():
    pass

  def finished():
    """ Signal """
    pass

  def format():
    pass

  def frameChanged():
    """ Signal """
    pass

  def frameCount():
    pass

  def frameRect():
    pass

  def isValid():
    pass

  def jumpToFrame():
    pass

  def jumpToNextFrame():
    pass

  def loopCount():
    pass

  def nextFrameDelay():
    pass

  def registerUserData():
    pass

  def resized():
    """ Signal """
    pass

  def scaledSize():
    pass

  def setBackgroundColor():
    pass

  def setCacheMode():
    pass

  def setDevice():
    pass

  def setFileName():
    pass

  def setFormat():
    pass

  def setPaused():
    pass

  def setScaledSize():
    pass

  def setSpeed():
    pass

  def speed():
    pass

  def start():
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

  def stop():
    pass

  def supportedFormats():
    pass

  def updated():
    """ Signal """
    pass

class QPaintDevice(Object):

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

  def colorCount():
    pass

  def depth():
    pass

  def devType():
    pass

  def height():
    pass

  def heightMM():
    pass

  def logicalDpiX():
    pass

  def logicalDpiY():
    pass

  def metric():
    pass

  def numColors():
    pass

  def paintEngine():
    pass

  painters = property(None, None, None,
                      )


  def paintingActive():
    pass

  def physicalDpiX():
    pass

  def physicalDpiY():
    pass

  def width():
    pass

  def widthMM():
    pass

class QPaintEngine(Object):

  AllDirty = None
  AllFeatures = None
  AlphaBlend = None
  Antialiasing = None
  BlendModes = None
  Blitter = None
  BrushStroke = None
  ConicalGradientFill = None
  ConstantOpacity = None
  ConvexMode = None
  CoreGraphics = None
  Direct3D = None
  DirtyBackground = None
  DirtyBackgroundMode = None
  DirtyBrush = None
  DirtyBrushOrigin = None
  DirtyClipEnabled = None
  DirtyClipPath = None
  DirtyClipRegion = None
  DirtyCompositionMode = None

  class DirtyFlag(object):

    AllDirty = None
    DirtyBackground = None
    DirtyBackgroundMode = None
    DirtyBrush = None
    DirtyBrushOrigin = None
    DirtyClipEnabled = None
    DirtyClipPath = None
    DirtyClipRegion = None
    DirtyCompositionMode = None
    DirtyFont = None
    DirtyHints = None
    DirtyOpacity = None
    DirtyPen = None
    DirtyTransform = None
    name = property(None, None, None,
                    )

    values = {}

  class DirtyFlags(object):

    pass

  DirtyFont = None
  DirtyHints = None
  DirtyOpacity = None
  DirtyPen = None
  DirtyTransform = None
  LinearGradientFill = None
  MacPrinter = None
  MaskedBrush = None
  MaxUser = None
  ObjectBoundingModeGradients = None
  OddEvenMode = None
  OpenGL = None
  OpenGL2 = None
  OpenVG = None
  PaintBuffer = None

  class PaintEngineFeature(object):

    AllFeatures = None
    AlphaBlend = None
    Antialiasing = None
    BlendModes = None
    BrushStroke = None
    ConicalGradientFill = None
    ConstantOpacity = None
    LinearGradientFill = None
    MaskedBrush = None
    ObjectBoundingModeGradients = None
    PaintOutsidePaintEvent = None
    PainterPaths = None
    PatternBrush = None
    PatternTransform = None
    PerspectiveTransform = None
    PixmapTransform = None
    PorterDuff = None
    PrimitiveTransform = None
    RadialGradientFill = None
    RasterOpModes = None
    name = property(None, None, None,
                    )

    values = {}

  class PaintEngineFeatures(object):

    pass

  PaintOutsidePaintEvent = None
  PainterPaths = None
  PatternBrush = None
  PatternTransform = None
  Pdf = None
  PerspectiveTransform = None
  Picture = None
  PixmapTransform = None

  class PolygonDrawMode(object):

    ConvexMode = None
    OddEvenMode = None
    PolylineMode = None
    WindingMode = None
    name = property(None, None, None,
                    )

    values = {}

  PolylineMode = None
  PorterDuff = None
  PostScript = None
  PrimitiveTransform = None
  QWindowSystem = None
  QuickDraw = None
  RadialGradientFill = None
  Raster = None
  RasterOpModes = None
  SVG = None

  class Type(object):

    Blitter = None
    CoreGraphics = None
    Direct3D = None
    MacPrinter = None
    MaxUser = None
    OpenGL = None
    OpenGL2 = None
    OpenVG = None
    PaintBuffer = None
    Pdf = None
    Picture = None
    PostScript = None
    QWindowSystem = None
    QuickDraw = None
    Raster = None
    SVG = None
    User = None
    Windows = None
    X11 = None
    name = property(None, None, None,
                    )

    values = {}

  User = None
  WindingMode = None
  Windows = None
  X11 = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  active = property(None, None, None,
                    )


  def begin():
    pass

  def clearDirty():
    pass

  def coordinateOffset():
    pass

  def drawEllipse():
    pass

  def drawImage():
    pass

  def drawLines():
    pass

  def drawPath():
    pass

  def drawPixmap():
    pass

  def drawPoints():
    pass

  def drawPolygon():
    pass

  def drawRects():
    pass

  def drawTextItem():
    pass

  def drawTiledPixmap():
    pass

  def end():
    pass

  extended = property(None, None, None,
                      )

  gccaps = property(None, None, None,
                    )


  def hasFeature():
    pass

  def isActive():
    pass

  def isExtended():
    pass

  def paintDevice():
    pass

  def painter():
    pass

  selfDestruct = property(None, None, None,
                          )


  def setActive():
    pass

  def setDirty():
    pass

  def setSystemClip():
    pass

  def setSystemRect():
    pass

  state = property(None, None, None,
                   )


  def syncState():
    pass

  def systemClip():
    pass

  def systemRect():
    pass

  def testDirty():
    pass

  def type():
    pass

  def updateState():
    pass

class QPaintEngineState(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def backgroundBrush():
    pass

  def backgroundMode():
    pass

  def brush():
    pass

  def brushNeedsResolving():
    pass

  def brushOrigin():
    pass

  def clipOperation():
    pass

  def clipPath():
    pass

  def clipRegion():
    pass

  def compositionMode():
    pass

  dirtyFlags = property(None, None, None,
                        )


  def font():
    pass

  def isClipEnabled():
    pass

  def matrix():
    pass

  def opacity():
    pass

  def painter():
    pass

  def pen():
    pass

  def penNeedsResolving():
    pass

  def renderHints():
    pass

  def state():
    pass

  def transform():
    pass

class QPaintEvent(QEvent):

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

  def rect():
    pass

  def region():
    pass

  def registerEventType():
    pass

class QPainter(Object):

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

  def background():
    pass

  def backgroundMode():
    pass

  def begin():
    pass

  def beginNativePainting():
    pass

  def boundingRect():
    pass

  def brush():
    pass

  def brushOrigin():
    pass

  def clipBoundingRect():
    pass

  def clipPath():
    pass

  def clipRegion():
    pass

  def combinedMatrix():
    pass

  def combinedTransform():
    pass

  def compositionMode():
    pass

  def device():
    pass

  def deviceMatrix():
    pass

  def deviceTransform():
    pass

  def drawArc():
    pass

  def drawChord():
    pass

  def drawConvexPolygon():
    pass

  def drawEllipse():
    pass

  def drawImage():
    pass

  def drawLine():
    pass

  def drawLines():
    pass

  def drawPath():
    pass

  def drawPicture():
    pass

  def drawPie():
    pass

  def drawPixmap():
    pass

  def drawPixmapFragments():
    pass

  def drawPoint():
    pass

  def drawPoints():
    pass

  def drawPolygon():
    pass

  def drawPolyline():
    pass

  def drawRect():
    pass

  def drawRects():
    pass

  def drawRoundRect():
    pass

  def drawRoundedRect():
    pass

  def drawText():
    pass

  def drawTextItem():
    pass

  def drawTiledPixmap():
    pass

  def end():
    pass

  def endNativePainting():
    pass

  def eraseRect():
    pass

  def fillPath():
    pass

  def fillRect():
    pass

  def font():
    pass

  def fontInfo():
    pass

  def fontMetrics():
    pass

  def hasClipping():
    pass

  def initFrom():
    pass

  def isActive():
    pass

  def layoutDirection():
    pass

  def opacity():
    pass

  def paintEngine():
    pass

  def pen():
    pass

  def renderHints():
    pass

  def resetMatrix():
    pass

  def resetTransform():
    pass

  def restore():
    pass

  def restoreRedirected():
    pass

  def rotate():
    pass

  def save():
    pass

  def scale():
    pass

  def setBackground():
    pass

  def setBackgroundMode():
    pass

  def setBrush():
    pass

  def setBrushOrigin():
    pass

  def setClipPath():
    pass

  def setClipRect():
    pass

  def setClipRegion():
    pass

  def setClipping():
    pass

  def setCompositionMode():
    pass

  def setFont():
    pass

  def setLayoutDirection():
    pass

  def setOpacity():
    pass

  def setPen():
    pass

  def setRedirected():
    pass

  def setRenderHint():
    pass

  def setRenderHints():
    pass

  def setTransform():
    pass

  def setViewTransformEnabled():
    pass

  def setViewport():
    pass

  def setWindow():
    pass

  def setWorldMatrix():
    pass

  def setWorldMatrixEnabled():
    pass

  def setWorldTransform():
    pass

  def shear():
    pass

  def strokePath():
    pass

  def testRenderHint():
    pass

  def transform():
    pass

  def translate():
    pass

  def viewTransformEnabled():
    pass

  def viewport():
    pass

  def window():
    pass

  def worldMatrix():
    pass

  def worldMatrixEnabled():
    pass

  def worldTransform():
    pass

class QPainterPath(Object):

  CurveToDataElement = None
  CurveToElement = None

  class Element(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    def isCurveTo():
      pass

    def isLineTo():
      pass

    def isMoveTo():
      pass

    type = property(None, None, None,
                    )

    x = property(None, None, None,
                 )

    y = property(None, None, None,
                 )


  class ElementType(object):

    CurveToDataElement = None
    CurveToElement = None
    LineToElement = None
    MoveToElement = None
    name = property(None, None, None,
                    )

    values = {}

  LineToElement = None
  MoveToElement = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addEllipse():
    pass

  def addPath():
    pass

  def addPolygon():
    pass

  def addRect():
    pass

  def addRegion():
    pass

  def addRoundRect():
    pass

  def addRoundedRect():
    pass

  def addText():
    pass

  def angleAtPercent():
    pass

  def arcMoveTo():
    pass

  def arcTo():
    pass

  def boundingRect():
    pass

  def closeSubpath():
    pass

  def connectPath():
    pass

  def contains():
    pass

  def controlPointRect():
    pass

  def cubicTo():
    pass

  def currentPosition():
    pass

  def elementAt():
    pass

  def elementCount():
    pass

  def fillRule():
    pass

  def intersected():
    pass

  def intersects():
    pass

  def isEmpty():
    pass

  def length():
    pass

  def lineTo():
    pass

  def moveTo():
    pass

  def percentAtLength():
    pass

  def pointAtPercent():
    pass

  def quadTo():
    pass

  def setElementPositionAt():
    pass

  def setFillRule():
    pass

  def simplified():
    pass

  def slopeAtPercent():
    pass

  def subtracted():
    pass

  def subtractedInverted():
    pass

  def swap():
    pass

  def toFillPolygon():
    pass

  def toFillPolygons():
    pass

  def toReversed():
    pass

  def toSubpathPolygons():
    pass

  def translate():
    pass

  def translated():
    pass

  def united():
    pass

class QPainterPathStroker(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def capStyle():
    pass

  def createStroke():
    pass

  def curveThreshold():
    pass

  def dashOffset():
    pass

  def dashPattern():
    pass

  def joinStyle():
    pass

  def miterLimit():
    pass

  def setCapStyle():
    pass

  def setCurveThreshold():
    pass

  def setDashOffset():
    pass

  def setDashPattern():
    pass

  def setJoinStyle():
    pass

  def setMiterLimit():
    pass

  def setWidth():
    pass

  def width():
    pass

class QPalette(Object):

  Active = None
  All = None
  AlternateBase = None
  Background = None
  Base = None
  BrightText = None
  Button = None
  ButtonText = None

  class ColorGroup(object):

    Active = None
    All = None
    Current = None
    Disabled = None
    Inactive = None
    NColorGroups = None
    Normal = None
    name = property(None, None, None,
                    )

    values = {}

  class ColorRole(object):

    AlternateBase = None
    Background = None
    Base = None
    BrightText = None
    Button = None
    ButtonText = None
    Dark = None
    Foreground = None
    Highlight = None
    HighlightedText = None
    Light = None
    Link = None
    LinkVisited = None
    Mid = None
    Midlight = None
    NColorRoles = None
    NoRole = None
    Shadow = None
    Text = None
    ToolTipBase = None
    ToolTipText = None
    Window = None
    WindowText = None
    name = property(None, None, None,
                    )

    values = {}

  Current = None
  Dark = None
  Disabled = None
  Foreground = None
  Highlight = None
  HighlightedText = None
  Inactive = None
  Light = None
  Link = None
  LinkVisited = None
  Mid = None
  Midlight = None
  NColorGroups = None
  NColorRoles = None
  NoRole = None
  Normal = None
  Shadow = None
  Text = None
  ToolTipBase = None
  ToolTipText = None
  Window = None
  WindowText = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alternateBase():
    pass

  def base():
    pass

  def brightText():
    pass

  def brush():
    pass

  def button():
    pass

  def buttonText():
    pass

  def cacheKey():
    pass

  def color():
    pass

  def currentColorGroup():
    pass

  def dark():
    pass

  def highlight():
    pass

  def highlightedText():
    pass

  def isBrushSet():
    pass

  def isCopyOf():
    pass

  def isEqual():
    pass

  def light():
    pass

  def link():
    pass

  def linkVisited():
    pass

  def mid():
    pass

  def midlight():
    pass

  def resolve():
    pass

  def setBrush():
    pass

  def setColor():
    pass

  def setColorGroup():
    pass

  def setCurrentColorGroup():
    pass

  def shadow():
    pass

  def text():
    pass

  def toolTipBase():
    pass

  def toolTipText():
    pass

  def window():
    pass

  def windowText():
    pass

class QPen(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def brush():
    pass

  def capStyle():
    pass

  def color():
    pass

  def dashOffset():
    pass

  def dashPattern():
    pass

  def isCosmetic():
    pass

  def isSolid():
    pass

  def joinStyle():
    pass

  def miterLimit():
    pass

  def setBrush():
    pass

  def setCapStyle():
    pass

  def setColor():
    pass

  def setCosmetic():
    pass

  def setDashOffset():
    pass

  def setDashPattern():
    pass

  def setJoinStyle():
    pass

  def setMiterLimit():
    pass

  def setStyle():
    pass

  def setWidth():
    pass

  def setWidthF():
    pass

  def style():
    pass

  def swap():
    pass

  def width():
    pass

  def widthF():
    pass

class QPicture(QPaintDevice):

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

  def boundingRect():
    pass

  def data():
    pass

  def devType():
    pass

  def isNull():
    pass

  def load():
    pass

  def metric():
    pass

  def paintEngine():
    pass

  def play():
    pass

  def save():
    pass

  def setBoundingRect():
    pass

  def setData():
    pass

  def size():
    pass

  def swap():
    pass

class QPictureIO(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def description():
    pass

  def fileName():
    pass

  def format():
    pass

  def gamma():
    pass

  def inputFormats():
    pass

  def ioDevice():
    pass

  def outputFormats():
    pass

  def parameters():
    pass

  def picture():
    pass

  def pictureFormat():
    pass

  def quality():
    pass

  def read():
    pass

  def setDescription():
    pass

  def setFileName():
    pass

  def setFormat():
    pass

  def setGamma():
    pass

  def setIODevice():
    pass

  def setParameters():
    pass

  def setPicture():
    pass

  def setQuality():
    pass

  def setStatus():
    pass

  def status():
    pass

  def write():
    pass

class QPixmap(QPaintDevice):

  Alpha = None
  NoAlpha = None
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
  PremultipliedAlpha = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alphaChannel():
    pass

  def cacheKey():
    pass

  def convertFromImage():
    pass

  def copy():
    pass

  def createHeuristicMask():
    pass

  def createMaskFromColor():
    pass

  def defaultDepth():
    pass

  def depth():
    pass

  def devType():
    pass

  def fill():
    pass

  def fromImage():
    pass

  def fromImageReader():
    pass

  def grabWidget():
    pass

  def grabWindow():
    pass

  def hasAlpha():
    pass

  def hasAlphaChannel():
    pass

  def height():
    pass

  def isNull():
    pass

  def isQBitmap():
    pass

  def load():
    pass

  def loadFromData():
    pass

  def mask():
    pass

  def metric():
    pass

  def paintEngine():
    pass

  def rect():
    pass

  def save():
    pass

  def scaled():
    pass

  def scaledToHeight():
    pass

  def scaledToWidth():
    pass

  def scroll():
    pass

  def setAlphaChannel():
    pass

  def setMask():
    pass

  def size():
    pass

  def swap():
    pass

  def toImage():
    pass

  def transformed():
    pass

  def trueMatrix():
    pass

  def width():
    pass

class QPixmapCache(Object):

  class Key(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cacheLimit():
    pass

  def clear():
    pass

  def find():
    pass

  def insert():
    pass

  def remove():
    pass

  def replace():
    pass

  def setCacheLimit():
    pass

class QPolygon(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def at():
    pass

  def boundingRect():
    pass

  def capacity():
    pass

  def clear():
    pass

  def constData():
    pass

  def contains():
    pass

  def containsPoint():
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

  def fromList():
    pass

  def front():
    pass

  def indexOf():
    pass

  def insert():
    pass

  def intersected():
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

  def subtracted():
    pass

  def swap():
    pass

  def toList():
    pass

  def translate():
    pass

  def translated():
    pass

  def united():
    pass

  def value():
    pass

class QPolygonF(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def at():
    pass

  def boundingRect():
    pass

  def capacity():
    pass

  def clear():
    pass

  def constData():
    pass

  def contains():
    pass

  def containsPoint():
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

  def fromList():
    pass

  def front():
    pass

  def indexOf():
    pass

  def insert():
    pass

  def intersected():
    pass

  def isClosed():
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

  def subtracted():
    pass

  def swap():
    pass

  def toList():
    pass

  def toPolygon():
    pass

  def translate():
    pass

  def translated():
    pass

  def united():
    pass

  def value():
    pass

class QQuaternion(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def conjugate():
    pass

  def fromAxisAndAngle():
    pass

  def isIdentity():
    pass

  def isNull():
    pass

  def length():
    pass

  def lengthSquared():
    pass

  def nlerp():
    pass

  def normalize():
    pass

  def normalized():
    pass

  def rotatedVector():
    pass

  def scalar():
    pass

  def setScalar():
    pass

  def setVector():
    pass

  def setX():
    pass

  def setY():
    pass

  def setZ():
    pass

  def slerp():
    pass

  def toVector4D():
    pass

  def vector():
    pass

  def x():
    pass

  def y():
    pass

  def z():
    pass

class QRadialGradient(QGradient):

  ColorInterpolation = None
  ComponentInterpolation = None
  ConicalGradient = None
  LinearGradient = None
  LogicalMode = None
  NoGradient = None
  ObjectBoundingMode = None
  PadSpread = None
  RadialGradient = None
  ReflectSpread = None
  RepeatSpread = None
  StretchToDeviceMode = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def center():
    pass

  def centerRadius():
    pass

  def focalPoint():
    pass

  def focalRadius():
    pass

  def radius():
    pass

  def setCenter():
    pass

  def setCenterRadius():
    pass

  def setFocalPoint():
    pass

  def setFocalRadius():
    pass

  def setRadius():
    pass

class QRegExpValidator(QValidator):

  Acceptable = None
  Intermediate = None
  Invalid = None
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

  def regExp():
    pass

  def registerUserData():
    pass

  def setRegExp():
    pass

  staticMetaObject = None

  def validate():
    pass

class QRegion(Object):

  Ellipse = None
  Rectangle = None

  class RegionType(object):

    Ellipse = None
    Rectangle = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def boundingRect():
    pass

  def contains():
    pass

  def intersected():
    pass

  def intersects():
    pass

  def isEmpty():
    pass

  def numRects():
    pass

  def rectCount():
    pass

  def rects():
    pass

  def setRects():
    pass

  def subtracted():
    pass

  def swap():
    pass

  def translate():
    pass

  def translated():
    pass

  def united():
    pass

  def xored():
    pass

class QResizeEvent(QEvent):

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

  def oldSize():
    pass

  def registerEventType():
    pass

  def size():
    pass

class QSessionManager(QObject):

  RestartAnyway = None

  class RestartHint(object):

    RestartAnyway = None
    RestartIfRunning = None
    RestartImmediately = None
    RestartNever = None
    name = property(None, None, None,
                    )

    values = {}

  RestartIfRunning = None
  RestartImmediately = None
  RestartNever = None

  def allowsErrorInteraction():
    pass

  def allowsInteraction():
    pass

  def cancel():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def discardCommand():
    pass

  def disconnect():
    pass

  def isPhase2():
    pass

  def registerUserData():
    pass

  def release():
    pass

  def requestPhase2():
    pass

  def restartCommand():
    pass

  def restartHint():
    pass

  def sessionId():
    pass

  def sessionKey():
    pass

  def setDiscardCommand():
    pass

  def setManagerProperty():
    pass

  def setRestartCommand():
    pass

  def setRestartHint():
    pass

  staticMetaObject = None

class QShortcutEvent(QEvent):

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

  def isAmbiguous():
    pass

  def key():
    pass

  def registerEventType():
    pass

  def shortcutId():
    pass

class QShowEvent(QEvent):

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

class QStandardItem(Object):

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

  def accessibleDescription():
    pass

  def accessibleText():
    pass

  def appendColumn():
    pass

  def appendRow():
    pass

  def appendRows():
    pass

  def background():
    pass

  def checkState():
    pass

  def child():
    pass

  def clone():
    pass

  def column():
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

  def hasChildren():
    pass

  def icon():
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

  def isCheckable():
    pass

  def isDragEnabled():
    pass

  def isDropEnabled():
    pass

  def isEditable():
    pass

  def isEnabled():
    pass

  def isSelectable():
    pass

  def isTristate():
    pass

  def model():
    pass

  def parent():
    pass

  def read():
    pass

  def removeColumn():
    pass

  def removeColumns():
    pass

  def removeRow():
    pass

  def removeRows():
    pass

  def row():
    pass

  def rowCount():
    pass

  def setAccessibleDescription():
    pass

  def setAccessibleText():
    pass

  def setBackground():
    pass

  def setCheckState():
    pass

  def setCheckable():
    pass

  def setChild():
    pass

  def setColumnCount():
    pass

  def setData():
    pass

  def setDragEnabled():
    pass

  def setDropEnabled():
    pass

  def setEditable():
    pass

  def setEnabled():
    pass

  def setFlags():
    pass

  def setFont():
    pass

  def setForeground():
    pass

  def setIcon():
    pass

  def setRowCount():
    pass

  def setSelectable():
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

  def setTristate():
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

  def takeColumn():
    pass

  def takeRow():
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

class QStandardItemModel(QAbstractItemModel):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def appendColumn():
    pass

  def appendRow():
    pass

  def clear():
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

  def findItems():
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

  def horizontalHeaderItem():
    pass

  def index():
    pass

  def indexFromItem():
    pass

  def insertColumn():
    pass

  def insertColumns():
    pass

  def insertRow():
    pass

  def insertRows():
    pass

  def invisibleRootItem():
    pass

  def item():
    pass

  def itemChanged():
    """ Signal """
    pass

  def itemData():
    pass

  def itemFromIndex():
    pass

  def itemPrototype():
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

  def setColumnCount():
    pass

  def setData():
    pass

  def setHeaderData():
    pass

  def setHorizontalHeaderItem():
    pass

  def setHorizontalHeaderLabels():
    pass

  def setItem():
    pass

  def setItemData():
    pass

  def setItemPrototype():
    pass

  def setRowCount():
    pass

  def setSortRole():
    pass

  def setVerticalHeaderItem():
    pass

  def setVerticalHeaderLabels():
    pass

  def sort():
    pass

  def sortRole():
    pass

  staticMetaObject = None

  def supportedDropActions():
    pass

  def takeColumn():
    pass

  def takeHorizontalHeaderItem():
    pass

  def takeItem():
    pass

  def takeRow():
    pass

  def takeVerticalHeaderItem():
    pass

  def verticalHeaderItem():
    pass

class QStatusTipEvent(QEvent):

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

  def tip():
    pass

class QSyntaxHighlighter(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentBlock():
    pass

  def currentBlockState():
    pass

  def currentBlockUserData():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def document():
    pass

  def format():
    pass

  def highlightBlock():
    pass

  def previousBlockState():
    pass

  def registerUserData():
    pass

  def rehighlight():
    pass

  def rehighlightBlock():
    pass

  def setCurrentBlockState():
    pass

  def setCurrentBlockUserData():
    pass

  def setDocument():
    pass

  def setFormat():
    pass

  staticMetaObject = None

class QTabletEvent(QInputEvent):

  AcceptDropsChange = None
  AccessibilityDescription = None
  AccessibilityHelp = None
  AccessibilityPrepare = None
  ActionAdded = None
  ActionChanged = None
  ActionRemoved = None
  ActivateControl = None
  ActivationChange = None
  Airbrush = None
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
  Cursor = None
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
  Eraser = None
  FileOpen = None
  FocusIn = None
  FocusOut = None
  FontChange = None
  FourDMouse = None
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
  NoDevice = None
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
  Pen = None
  PlatformPanel = None

  class PointerType(object):

    Cursor = None
    Eraser = None
    Pen = None
    UnknownPointer = None
    name = property(None, None, None,
                    )

    values = {}

  Polish = None
  PolishRequest = None
  Puck = None
  QueryWhatsThis = None
  Quit = None
  RequestSoftwareInputPanel = None
  Resize = None
  RotationStylus = None
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
  Stylus = None

  class TabletDevice(object):

    Airbrush = None
    FourDMouse = None
    NoDevice = None
    Puck = None
    RotationStylus = None
    Stylus = None
    XFreeEraser = None
    name = property(None, None, None,
                    )

    values = {}

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
  UnknownPointer = None
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
  XFreeEraser = None
  ZOrderChange = None
  ZeroTimerEvent = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def device():
    pass

  def globalPos():
    pass

  def globalX():
    pass

  def globalY():
    pass

  def hiResGlobalPos():
    pass

  def hiResGlobalX():
    pass

  def hiResGlobalY():
    pass

  def pointerType():
    pass

  def pos():
    pass

  def pressure():
    pass

  def registerEventType():
    pass

  def rotation():
    pass

  def tangentialPressure():
    pass

  def uniqueId():
    pass

  def x():
    pass

  def xTilt():
    pass

  def y():
    pass

  def yTilt():
    pass

  def z():
    pass

class QTextBlock(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def begin():
    pass

  def blockFormat():
    pass

  def blockFormatIndex():
    pass

  def blockNumber():
    pass

  def charFormat():
    pass

  def charFormatIndex():
    pass

  def clearLayout():
    pass

  def contains():
    pass

  def document():
    pass

  def end():
    pass

  def firstLineNumber():
    pass

  def fragmentIndex():
    pass

  def isValid():
    pass

  def isVisible():
    pass

  class iterator(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    def atEnd():
      pass

    def fragment():
      pass

    def next():
      """ x.next() -> the next value, or raise StopIteration """
      return None

  def layout():
    pass

  def length():
    pass

  def lineCount():
    pass

  def next():
    pass

  def position():
    pass

  def previous():
    pass

  def revision():
    pass

  def setLineCount():
    pass

  def setRevision():
    pass

  def setUserData():
    pass

  def setUserState():
    pass

  def setVisible():
    pass

  def text():
    pass

  def textDirection():
    pass

  def textList():
    pass

  def userData():
    pass

  def userState():
    pass

class QTextBlockFormat(QTextFormat):

  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None
  CharFormat = None
  CssFloat = None
  FirstFontProperty = None
  FixedHeight = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None

  class FormatType(object):

    BlockFormat = None
    CharFormat = None
    FrameFormat = None
    InvalidFormat = None
    ListFormat = None
    TableFormat = None
    UserFormat = None
    name = property(None, None, None,
                    )

    values = {}

  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineDistanceHeight = None
  LineHeight = None
  LineHeightType = None

  class LineHeightTypes(object):

    FixedHeight = None
    LineDistanceHeight = None
    MinimumHeight = None
    ProportionalHeight = None
    SingleHeight = None
    name = property(None, None, None,
                    )

    values = {}

  ListFormat = None
  ListIndent = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListStyle = None
  MinimumHeight = None
  NoObject = None
  ObjectIndex = None
  ObjectType = None

  class ObjectTypes(object):

    ImageObject = None
    NoObject = None
    TableCellObject = None
    TableObject = None
    UserObject = None
    name = property(None, None, None,
                    )

    values = {}

  OutlinePen = None

  class PageBreakFlag(object):

    PageBreak_AlwaysAfter = None
    PageBreak_AlwaysBefore = None
    PageBreak_Auto = None
    name = property(None, None, None,
                    )

    values = {}

  class PageBreakFlags(object):

    pass

  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None

  class Property(object):

    AnchorHref = None
    AnchorName = None
    BackgroundBrush = None
    BackgroundImageUrl = None
    BlockAlignment = None
    BlockBottomMargin = None
    BlockIndent = None
    BlockLeftMargin = None
    BlockNonBreakableLines = None
    BlockRightMargin = None
    BlockTopMargin = None
    BlockTrailingHorizontalRulerWidth = None
    CssFloat = None
    FirstFontProperty = None
    FontCapitalization = None
    FontFamily = None
    FontFixedPitch = None
    FontHintingPreference = None
    FontItalic = None
    FontKerning = None
    FontLetterSpacing = None
    FontOverline = None
    FontPixelSize = None
    FontPointSize = None
    FontSizeAdjustment = None
    FontSizeIncrement = None
    FontStrikeOut = None
    FontStyleHint = None
    FontStyleStrategy = None
    FontUnderline = None
    FontWeight = None
    FontWordSpacing = None
    ForegroundBrush = None
    FrameBorder = None
    FrameBorderBrush = None
    FrameBorderStyle = None
    FrameBottomMargin = None
    FrameHeight = None
    FrameLeftMargin = None
    FrameMargin = None
    FramePadding = None
    FrameRightMargin = None
    FrameTopMargin = None
    FrameWidth = None
    FullWidthSelection = None
    ImageHeight = None
    ImageName = None
    ImageWidth = None
    IsAnchor = None
    LastFontProperty = None
    LayoutDirection = None
    LineHeight = None
    LineHeightType = None
    ListIndent = None
    ListNumberPrefix = None
    ListNumberSuffix = None
    ListStyle = None
    ObjectIndex = None
    ObjectType = None
    OutlinePen = None
    PageBreakPolicy = None
    TabPositions = None
    TableCellBottomPadding = None
    TableCellColumnSpan = None
    TableCellLeftPadding = None
    TableCellPadding = None
    TableCellRightPadding = None
    TableCellRowSpan = None
    TableCellSpacing = None
    TableCellTopPadding = None
    TableColumnWidthConstraints = None
    TableColumns = None
    TableHeaderRowCount = None
    TextIndent = None
    TextOutline = None
    TextToolTip = None
    TextUnderlineColor = None
    TextUnderlineStyle = None
    TextVerticalAlignment = None
    UserProperty = None
    name = property(None, None, None,
                    )

    values = {}

  ProportionalHeight = None
  SingleHeight = None
  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None
  UserFormat = None
  UserObject = None
  UserProperty = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def bottomMargin():
    pass

  def indent():
    pass

  def isValid():
    pass

  def leftMargin():
    pass

  def lineHeight():
    pass

  def lineHeightType():
    pass

  def nonBreakableLines():
    pass

  def pageBreakPolicy():
    pass

  def rightMargin():
    pass

  def setAlignment():
    pass

  def setBottomMargin():
    pass

  def setIndent():
    pass

  def setLeftMargin():
    pass

  def setLineHeight():
    pass

  def setNonBreakableLines():
    pass

  def setPageBreakPolicy():
    pass

  def setRightMargin():
    pass

  def setTabPositions():
    pass

  def setTextIndent():
    pass

  def setTopMargin():
    pass

  def tabPositions():
    pass

  def textIndent():
    pass

  def topMargin():
    pass

class QTextBlockGroup(QTextObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def blockFormatChanged():
    pass

  def blockInserted():
    pass

  def blockList():
    pass

  def blockRemoved():
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

class QTextBlockUserData(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

class QTextCharFormat(QTextFormat):

  AlignBaseline = None
  AlignBottom = None
  AlignMiddle = None
  AlignNormal = None
  AlignSubScript = None
  AlignSuperScript = None
  AlignTop = None
  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None
  CharFormat = None
  CssFloat = None
  DashDotDotLine = None
  DashDotLine = None
  DashUnderline = None
  DotLine = None
  FirstFontProperty = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None
  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineHeight = None
  LineHeightType = None
  ListFormat = None
  ListIndent = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListStyle = None
  NoObject = None
  NoUnderline = None
  ObjectIndex = None
  ObjectType = None
  OutlinePen = None
  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None
  SingleUnderline = None
  SpellCheckUnderline = None
  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None

  class UnderlineStyle(object):

    DashDotDotLine = None
    DashDotLine = None
    DashUnderline = None
    DotLine = None
    NoUnderline = None
    SingleUnderline = None
    SpellCheckUnderline = None
    WaveUnderline = None
    name = property(None, None, None,
                    )

    values = {}

  UserFormat = None
  UserObject = None
  UserProperty = None

  class VerticalAlignment(object):

    AlignBaseline = None
    AlignBottom = None
    AlignMiddle = None
    AlignNormal = None
    AlignSubScript = None
    AlignSuperScript = None
    AlignTop = None
    name = property(None, None, None,
                    )

    values = {}

  WaveUnderline = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def anchorHref():
    pass

  def anchorNames():
    pass

  def font():
    pass

  def fontCapitalization():
    pass

  def fontFamily():
    pass

  def fontFixedPitch():
    pass

  def fontHintingPreference():
    pass

  def fontItalic():
    pass

  def fontKerning():
    pass

  def fontLetterSpacing():
    pass

  def fontOverline():
    pass

  def fontPointSize():
    pass

  def fontStrikeOut():
    pass

  def fontStyleHint():
    pass

  def fontStyleStrategy():
    pass

  def fontUnderline():
    pass

  def fontWeight():
    pass

  def fontWordSpacing():
    pass

  def isAnchor():
    pass

  def isValid():
    pass

  def setAnchor():
    pass

  def setAnchorHref():
    pass

  def setAnchorNames():
    pass

  def setFont():
    pass

  def setFontCapitalization():
    pass

  def setFontFamily():
    pass

  def setFontFixedPitch():
    pass

  def setFontHintingPreference():
    pass

  def setFontItalic():
    pass

  def setFontKerning():
    pass

  def setFontLetterSpacing():
    pass

  def setFontOverline():
    pass

  def setFontPointSize():
    pass

  def setFontStrikeOut():
    pass

  def setFontStyleHint():
    pass

  def setFontStyleStrategy():
    pass

  def setFontUnderline():
    pass

  def setFontWeight():
    pass

  def setFontWordSpacing():
    pass

  def setTableCellColumnSpan():
    pass

  def setTableCellRowSpan():
    pass

  def setTextOutline():
    pass

  def setToolTip():
    pass

  def setUnderlineColor():
    pass

  def setUnderlineStyle():
    pass

  def setVerticalAlignment():
    pass

  def tableCellColumnSpan():
    pass

  def tableCellRowSpan():
    pass

  def textOutline():
    pass

  def toolTip():
    pass

  def underlineColor():
    pass

  def underlineStyle():
    pass

  def verticalAlignment():
    pass

class QTextCursor(Object):

  BlockUnderCursor = None
  Document = None
  Down = None
  End = None
  EndOfBlock = None
  EndOfLine = None
  EndOfWord = None
  KeepAnchor = None
  Left = None
  LineUnderCursor = None
  MoveAnchor = None

  class MoveMode(object):

    KeepAnchor = None
    MoveAnchor = None
    name = property(None, None, None,
                    )

    values = {}

  class MoveOperation(object):

    Down = None
    End = None
    EndOfBlock = None
    EndOfLine = None
    EndOfWord = None
    Left = None
    NextBlock = None
    NextCell = None
    NextCharacter = None
    NextRow = None
    NextWord = None
    NoMove = None
    PreviousBlock = None
    PreviousCell = None
    PreviousCharacter = None
    PreviousRow = None
    PreviousWord = None
    Right = None
    Start = None
    StartOfBlock = None
    StartOfLine = None
    StartOfWord = None
    Up = None
    WordLeft = None
    WordRight = None
    name = property(None, None, None,
                    )

    values = {}

  NextBlock = None
  NextCell = None
  NextCharacter = None
  NextRow = None
  NextWord = None
  NoMove = None
  PreviousBlock = None
  PreviousCell = None
  PreviousCharacter = None
  PreviousRow = None
  PreviousWord = None
  Right = None

  class SelectionType(object):

    BlockUnderCursor = None
    Document = None
    LineUnderCursor = None
    WordUnderCursor = None
    name = property(None, None, None,
                    )

    values = {}

  Start = None
  StartOfBlock = None
  StartOfLine = None
  StartOfWord = None
  Up = None
  WordLeft = None
  WordRight = None
  WordUnderCursor = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def anchor():
    pass

  def atBlockEnd():
    pass

  def atBlockStart():
    pass

  def atEnd():
    pass

  def atStart():
    pass

  def beginEditBlock():
    pass

  def block():
    pass

  def blockCharFormat():
    pass

  def blockFormat():
    pass

  def blockNumber():
    pass

  def charFormat():
    pass

  def clearSelection():
    pass

  def columnNumber():
    pass

  def createList():
    pass

  def currentFrame():
    pass

  def currentList():
    pass

  def currentTable():
    pass

  def deleteChar():
    pass

  def deletePreviousChar():
    pass

  def document():
    pass

  def endEditBlock():
    pass

  def hasComplexSelection():
    pass

  def hasSelection():
    pass

  def insertBlock():
    pass

  def insertFragment():
    pass

  def insertFrame():
    pass

  def insertHtml():
    pass

  def insertImage():
    pass

  def insertList():
    pass

  def insertTable():
    pass

  def insertText():
    pass

  def isCopyOf():
    pass

  def isNull():
    pass

  def joinPreviousEditBlock():
    pass

  def keepPositionOnInsert():
    pass

  def mergeBlockCharFormat():
    pass

  def mergeBlockFormat():
    pass

  def mergeCharFormat():
    pass

  def movePosition():
    pass

  def position():
    pass

  def positionInBlock():
    pass

  def removeSelectedText():
    pass

  def select():
    pass

  def selectedTableCells():
    pass

  def selectedText():
    pass

  def selection():
    pass

  def selectionEnd():
    pass

  def selectionStart():
    pass

  def setBlockCharFormat():
    pass

  def setBlockFormat():
    pass

  def setCharFormat():
    pass

  def setKeepPositionOnInsert():
    pass

  def setPosition():
    pass

  def setVerticalMovementX():
    pass

  def setVisualNavigation():
    pass

  def verticalMovementX():
    pass

  def visualNavigation():
    pass

class QTextDocument(QObject):

  DocumentTitle = None
  DocumentUrl = None
  FindBackward = None
  FindCaseSensitively = None

  class FindFlag(object):

    FindBackward = None
    FindCaseSensitively = None
    FindWholeWords = None
    name = property(None, None, None,
                    )

    values = {}

  class FindFlags(object):

    pass

  FindWholeWords = None
  HtmlResource = None
  ImageResource = None

  class MetaInformation(object):

    DocumentTitle = None
    DocumentUrl = None
    name = property(None, None, None,
                    )

    values = {}

  RedoStack = None

  class ResourceType(object):

    HtmlResource = None
    ImageResource = None
    StyleSheetResource = None
    UserResource = None
    name = property(None, None, None,
                    )

    values = {}

  class Stacks(object):

    RedoStack = None
    UndoAndRedoStacks = None
    UndoStack = None
    name = property(None, None, None,
                    )

    values = {}

  StyleSheetResource = None
  UndoAndRedoStacks = None
  UndoStack = None
  UserResource = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addResource():
    pass

  def adjustSize():
    pass

  def allFormats():
    pass

  def availableRedoSteps():
    pass

  def availableUndoSteps():
    pass

  def begin():
    pass

  def blockCount():
    pass

  def blockCountChanged():
    """ Signal """
    pass

  def characterAt():
    pass

  def characterCount():
    pass

  def clear():
    pass

  def clearUndoRedoStacks():
    pass

  def clone():
    pass

  def connect():
    pass

  def contentsChange():
    """ Signal """
    pass

  def contentsChanged():
    """ Signal """
    pass

  def createObject():
    pass

  def cursorPositionChanged():
    """ Signal """
    pass

  def defaultCursorMoveStyle():
    pass

  def defaultFont():
    pass

  def defaultStyleSheet():
    pass

  def defaultTextOption():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def documentLayout():
    pass

  def documentLayoutChanged():
    """ Signal """
    pass

  def documentMargin():
    pass

  def drawContents():
    pass

  def end():
    pass

  def find():
    pass

  def findBlock():
    pass

  def findBlockByLineNumber():
    pass

  def findBlockByNumber():
    pass

  def firstBlock():
    pass

  def frameAt():
    pass

  def idealWidth():
    pass

  def indentWidth():
    pass

  def isEmpty():
    pass

  def isModified():
    pass

  def isRedoAvailable():
    pass

  def isUndoAvailable():
    pass

  def isUndoRedoEnabled():
    pass

  def lastBlock():
    pass

  def lineCount():
    pass

  def loadResource():
    pass

  def markContentsDirty():
    pass

  def maximumBlockCount():
    pass

  def metaInformation():
    pass

  def modificationChanged():
    """ Signal """
    pass

  def object():
    pass

  def objectForFormat():
    pass

  def pageCount():
    pass

  def pageSize():
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

  def resource():
    pass

  def revision():
    pass

  def rootFrame():
    pass

  def setDefaultCursorMoveStyle():
    pass

  def setDefaultFont():
    pass

  def setDefaultStyleSheet():
    pass

  def setDefaultTextOption():
    pass

  def setDocumentLayout():
    pass

  def setDocumentMargin():
    pass

  def setHtml():
    pass

  def setIndentWidth():
    pass

  def setMaximumBlockCount():
    pass

  def setMetaInformation():
    pass

  def setModified():
    pass

  def setPageSize():
    pass

  def setPlainText():
    pass

  def setTextWidth():
    pass

  def setUndoRedoEnabled():
    pass

  def setUseDesignMetrics():
    pass

  def size():
    pass

  staticMetaObject = None

  def textWidth():
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

  def undoCommandAdded():
    """ Signal """
    pass

  def useDesignMetrics():
    pass

class QTextDocumentFragment(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def fromHtml():
    pass

  def fromPlainText():
    pass

  def isEmpty():
    pass

  def toHtml():
    pass

  def toPlainText():
    pass

class QTextFormat(Object):

  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None
  CharFormat = None
  CssFloat = None
  FirstFontProperty = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None
  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineHeight = None
  LineHeightType = None
  ListFormat = None
  ListIndent = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListStyle = None
  NoObject = None
  ObjectIndex = None
  ObjectType = None
  OutlinePen = None
  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None
  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None
  UserFormat = None
  UserObject = None
  UserProperty = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def background():
    pass

  def boolProperty():
    pass

  def brushProperty():
    pass

  def clearBackground():
    pass

  def clearForeground():
    pass

  def clearProperty():
    pass

  def colorProperty():
    pass

  def doubleProperty():
    pass

  def foreground():
    pass

  def hasProperty():
    pass

  def intProperty():
    pass

  def isBlockFormat():
    pass

  def isCharFormat():
    pass

  def isFrameFormat():
    pass

  def isImageFormat():
    pass

  def isListFormat():
    pass

  def isTableCellFormat():
    pass

  def isTableFormat():
    pass

  def isValid():
    pass

  def layoutDirection():
    pass

  def lengthProperty():
    pass

  def lengthVectorProperty():
    pass

  def merge():
    pass

  def objectIndex():
    pass

  def objectType():
    pass

  def penProperty():
    pass

  def properties():
    pass

  def property():
    pass

  def propertyCount():
    pass

  def setBackground():
    pass

  def setForeground():
    pass

  def setLayoutDirection():
    pass

  def setObjectIndex():
    pass

  def setObjectType():
    pass

  def setProperty():
    pass

  def stringProperty():
    pass

  def toBlockFormat():
    pass

  def toCharFormat():
    pass

  def toFrameFormat():
    pass

  def toImageFormat():
    pass

  def toListFormat():
    pass

  def toTableCellFormat():
    pass

  def toTableFormat():
    pass

  def type():
    pass

class QTextFragment(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def charFormat():
    pass

  def charFormatIndex():
    pass

  def contains():
    pass

  def isValid():
    pass

  def length():
    pass

  def position():
    pass

  def text():
    pass

class QTextFrame(QTextObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def begin():
    pass

  def childFrames():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def end():
    pass

  def firstCursorPosition():
    pass

  def firstPosition():
    pass

  def frameFormat():
    pass

  class iterator(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    def atEnd():
      pass

    def currentBlock():
      pass

    def currentFrame():
      pass

    def next():
      """ x.next() -> the next value, or raise StopIteration """
      return None

    def parentFrame():
      pass

  def lastCursorPosition():
    pass

  def lastPosition():
    pass

  def parentFrame():
    pass

  def registerUserData():
    pass

  def setFrameFormat():
    pass

  staticMetaObject = None

class QTextFrameFormat(QTextFormat):

  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None

  class BorderStyle(object):

    BorderStyle_Dashed = None
    BorderStyle_DotDash = None
    BorderStyle_DotDotDash = None
    BorderStyle_Dotted = None
    BorderStyle_Double = None
    BorderStyle_Groove = None
    BorderStyle_Inset = None
    BorderStyle_None = None
    BorderStyle_Outset = None
    BorderStyle_Ridge = None
    BorderStyle_Solid = None
    name = property(None, None, None,
                    )

    values = {}

  BorderStyle_Dashed = None
  BorderStyle_DotDash = None
  BorderStyle_DotDotDash = None
  BorderStyle_Dotted = None
  BorderStyle_Double = None
  BorderStyle_Groove = None
  BorderStyle_Inset = None
  BorderStyle_None = None
  BorderStyle_Outset = None
  BorderStyle_Ridge = None
  BorderStyle_Solid = None
  CharFormat = None
  CssFloat = None
  FirstFontProperty = None
  FloatLeft = None
  FloatRight = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None
  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InFlow = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineHeight = None
  LineHeightType = None
  ListFormat = None
  ListIndent = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListStyle = None
  NoObject = None
  ObjectIndex = None
  ObjectType = None
  OutlinePen = None
  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None

  class Position(object):

    FloatLeft = None
    FloatRight = None
    InFlow = None
    name = property(None, None, None,
                    )

    values = {}

  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None
  UserFormat = None
  UserObject = None
  UserProperty = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def border():
    pass

  def borderBrush():
    pass

  def borderStyle():
    pass

  def bottomMargin():
    pass

  def height():
    pass

  def isValid():
    pass

  def leftMargin():
    pass

  def margin():
    pass

  def padding():
    pass

  def pageBreakPolicy():
    pass

  def position():
    pass

  def rightMargin():
    pass

  def setBorder():
    pass

  def setBorderBrush():
    pass

  def setBorderStyle():
    pass

  def setBottomMargin():
    pass

  def setHeight():
    pass

  def setLeftMargin():
    pass

  def setMargin():
    pass

  def setPadding():
    pass

  def setPageBreakPolicy():
    pass

  def setPosition():
    pass

  def setRightMargin():
    pass

  def setTopMargin():
    pass

  def setWidth():
    pass

  def topMargin():
    pass

  def width():
    pass

class QTextImageFormat(QTextCharFormat):

  AlignBaseline = None
  AlignBottom = None
  AlignMiddle = None
  AlignNormal = None
  AlignSubScript = None
  AlignSuperScript = None
  AlignTop = None
  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None
  CharFormat = None
  CssFloat = None
  DashDotDotLine = None
  DashDotLine = None
  DashUnderline = None
  DotLine = None
  FirstFontProperty = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None
  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineHeight = None
  LineHeightType = None
  ListFormat = None
  ListIndent = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListStyle = None
  NoObject = None
  NoUnderline = None
  ObjectIndex = None
  ObjectType = None
  OutlinePen = None
  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None
  SingleUnderline = None
  SpellCheckUnderline = None
  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None
  UserFormat = None
  UserObject = None
  UserProperty = None
  WaveUnderline = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def height():
    pass

  def isValid():
    pass

  def name():
    pass

  def setHeight():
    pass

  def setName():
    pass

  def setWidth():
    pass

  def width():
    pass

class QTextInlineObject(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def ascent():
    pass

  def descent():
    pass

  def format():
    pass

  def formatIndex():
    pass

  def height():
    pass

  def isValid():
    pass

  def rect():
    pass

  def setAscent():
    pass

  def setDescent():
    pass

  def setWidth():
    pass

  def textDirection():
    pass

  def textPosition():
    pass

  def width():
    pass

class QTextItem(Object):

  Dummy = None
  Overline = None

  class RenderFlag(object):

    Dummy = None
    Overline = None
    RightToLeft = None
    StrikeOut = None
    Underline = None
    name = property(None, None, None,
                    )

    values = {}

  class RenderFlags(object):

    pass

  RightToLeft = None
  StrikeOut = None
  Underline = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def ascent():
    pass

  def descent():
    pass

  def font():
    pass

  def renderFlags():
    pass

  def text():
    pass

  def width():
    pass

class QTextLayout(Object):

  class CursorMode(object):

    SkipCharacters = None
    SkipWords = None
    name = property(None, None, None,
                    )

    values = {}

  class FormatRange(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    format = property(None, None, None,
                      )

    length = property(None, None, None,
                      )

    start = property(None, None, None,
                     )


  SkipCharacters = None
  SkipWords = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def additionalFormats():
    pass

  def beginLayout():
    pass

  def boundingRect():
    pass

  def cacheEnabled():
    pass

  def clearAdditionalFormats():
    pass

  def clearLayout():
    pass

  def createLine():
    pass

  def cursorMoveStyle():
    pass

  def draw():
    pass

  def drawCursor():
    pass

  def endLayout():
    pass

  def font():
    pass

  def isValidCursorPosition():
    pass

  def leftCursorPosition():
    pass

  def lineAt():
    pass

  def lineCount():
    pass

  def lineForTextPosition():
    pass

  def maximumWidth():
    pass

  def minimumWidth():
    pass

  def nextCursorPosition():
    pass

  def position():
    pass

  def preeditAreaPosition():
    pass

  def preeditAreaText():
    pass

  def previousCursorPosition():
    pass

  def rightCursorPosition():
    pass

  def setAdditionalFormats():
    pass

  def setCacheEnabled():
    pass

  def setCursorMoveStyle():
    pass

  def setFlags():
    pass

  def setFont():
    pass

  def setPosition():
    pass

  def setPreeditArea():
    pass

  def setText():
    pass

  def setTextOption():
    pass

  def text():
    pass

  def textOption():
    pass

class QTextLength(Object):

  FixedLength = None
  PercentageLength = None

  class Type(object):

    FixedLength = None
    PercentageLength = None
    VariableLength = None
    name = property(None, None, None,
                    )

    values = {}

  VariableLength = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def rawValue():
    pass

  def type():
    pass

  def value():
    pass

class QTextLine(Object):

  CursorBetweenCharacters = None
  CursorOnCharacter = None

  class CursorPosition(object):

    CursorBetweenCharacters = None
    CursorOnCharacter = None
    name = property(None, None, None,
                    )

    values = {}

  class Edge(object):

    Leading = None
    Trailing = None
    name = property(None, None, None,
                    )

    values = {}

  Leading = None
  Trailing = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def ascent():
    pass

  def cursorToX():
    pass

  def descent():
    pass

  def draw():
    pass

  def height():
    pass

  def horizontalAdvance():
    pass

  def isValid():
    pass

  def leading():
    pass

  def leadingIncluded():
    pass

  def lineNumber():
    pass

  def naturalTextRect():
    pass

  def naturalTextWidth():
    pass

  def position():
    pass

  def rect():
    pass

  def setLeadingIncluded():
    pass

  def setLineWidth():
    pass

  def setNumColumns():
    pass

  def setPosition():
    pass

  def textLength():
    pass

  def textStart():
    pass

  def width():
    pass

  def x():
    pass

  def xToCursor():
    pass

  def y():
    pass

class QTextList(QTextBlockGroup):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def add():
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

  def format():
    pass

  def item():
    pass

  def itemNumber():
    pass

  def itemText():
    pass

  def registerUserData():
    pass

  def remove():
    pass

  def removeItem():
    pass

  def setFormat():
    pass

  staticMetaObject = None

class QTextListFormat(QTextFormat):

  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None
  CharFormat = None
  CssFloat = None
  FirstFontProperty = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None
  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineHeight = None
  LineHeightType = None
  ListCircle = None
  ListDecimal = None
  ListDisc = None
  ListFormat = None
  ListIndent = None
  ListLowerAlpha = None
  ListLowerRoman = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListSquare = None
  ListStyle = None
  ListStyleUndefined = None
  ListUpperAlpha = None
  ListUpperRoman = None
  NoObject = None
  ObjectIndex = None
  ObjectType = None
  OutlinePen = None
  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None
  class Style(object):

    ListCircle = None
    ListDecimal = None
    ListDisc = None
    ListLowerAlpha = None
    ListLowerRoman = None
    ListSquare = None
    ListStyleUndefined = None
    ListUpperAlpha = None
    ListUpperRoman = None
    name = property(None, None, None,
                    )

    values = {}

  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None
  UserFormat = None
  UserObject = None
  UserProperty = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def indent():
    pass

  def isValid():
    pass

  def numberPrefix():
    pass

  def numberSuffix():
    pass

  def setIndent():
    pass

  def setNumberPrefix():
    pass

  def setNumberSuffix():
    pass

  def setStyle():
    pass

  def style():
    pass

class QTextObject(QObject):

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

  def document():
    pass

  def format():
    pass

  def formatIndex():
    pass

  def objectIndex():
    pass

  def registerUserData():
    pass

  def setFormat():
    pass

  staticMetaObject = None

class QTextObjectInterface(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def drawObject():
    pass

  def intrinsicSize():
    pass

class QTextOption(Object):

  AddSpaceForLineAndParagraphSeparators = None
  CenterTab = None
  DelimiterTab = None

  class Flag(object):

    AddSpaceForLineAndParagraphSeparators = None
    IncludeTrailingSpaces = None
    ShowLineAndParagraphSeparators = None
    ShowTabsAndSpaces = None
    SuppressColors = None
    name = property(None, None, None,
                    )

    values = {}

  class Flags(object):

    pass

  IncludeTrailingSpaces = None
  LeftTab = None
  ManualWrap = None
  NoWrap = None
  RightTab = None
  ShowLineAndParagraphSeparators = None
  ShowTabsAndSpaces = None
  SuppressColors = None

  class Tab(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    delimiter = property(None, None, None,
                         )

    position = property(None, None, None,
                        )

    type = property(None, None, None,
                    )


  class TabType(object):

    CenterTab = None
    DelimiterTab = None
    LeftTab = None
    RightTab = None
    name = property(None, None, None,
                    )

    values = {}

  WordWrap = None
  WrapAnywhere = None
  WrapAtWordBoundaryOrAnywhere = None

  class WrapMode(object):

    ManualWrap = None
    NoWrap = None
    WordWrap = None
    WrapAnywhere = None
    WrapAtWordBoundaryOrAnywhere = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def flags():
    pass

  def setAlignment():
    pass

  def setFlags():
    pass

  def setTabArray():
    pass

  def setTabStop():
    pass

  def setTabs():
    pass

  def setTextDirection():
    pass

  def setUseDesignMetrics():
    pass

  def setWrapMode():
    pass

  def tabArray():
    pass

  def tabStop():
    pass

  def tabs():
    pass

  def textDirection():
    pass

  def useDesignMetrics():
    pass

  def wrapMode():
    pass

class QTextTable(QTextFrame):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def appendColumns():
    pass

  def appendRows():
    pass

  def cellAt():
    pass

  def columns():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def format():
    pass

  def insertColumns():
    pass

  def insertRows():
    pass

  def mergeCells():
    pass

  def registerUserData():
    pass

  def removeColumns():
    pass

  def removeRows():
    pass

  def resize():
    pass

  def rowEnd():
    pass

  def rowStart():
    pass

  def rows():
    pass

  def setFormat():
    pass

  def splitCell():
    pass

  staticMetaObject = None

class QTextTableCell(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def begin():
    pass

  def column():
    pass

  def columnSpan():
    pass

  def end():
    pass

  def firstCursorPosition():
    pass

  def firstPosition():
    pass

  def format():
    pass

  def isValid():
    pass

  def lastCursorPosition():
    pass

  def lastPosition():
    pass

  def row():
    pass

  def rowSpan():
    pass

  def setFormat():
    pass

  def tableCellFormatIndex():
    pass

class QTextTableCellFormat(QTextCharFormat):

  AlignBaseline = None
  AlignBottom = None
  AlignMiddle = None
  AlignNormal = None
  AlignSubScript = None
  AlignSuperScript = None
  AlignTop = None
  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None
  CharFormat = None
  CssFloat = None
  DashDotDotLine = None
  DashDotLine = None
  DashUnderline = None
  DotLine = None
  FirstFontProperty = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None
  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineHeight = None
  LineHeightType = None
  ListFormat = None
  ListIndent = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListStyle = None
  NoObject = None
  NoUnderline = None
  ObjectIndex = None
  ObjectType = None
  OutlinePen = None
  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None
  SingleUnderline = None
  SpellCheckUnderline = None
  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None
  UserFormat = None
  UserObject = None
  UserProperty = None
  WaveUnderline = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bottomPadding():
    pass

  def isValid():
    pass

  def leftPadding():
    pass

  def rightPadding():
    pass

  def setBottomPadding():
    pass

  def setLeftPadding():
    pass

  def setPadding():
    pass

  def setRightPadding():
    pass

  def setTopPadding():
    pass

  def topPadding():
    pass

class QTextTableFormat(QTextFrameFormat):

  AnchorHref = None
  AnchorName = None
  BackgroundBrush = None
  BackgroundImageUrl = None
  BlockAlignment = None
  BlockBottomMargin = None
  BlockFormat = None
  BlockIndent = None
  BlockLeftMargin = None
  BlockNonBreakableLines = None
  BlockRightMargin = None
  BlockTopMargin = None
  BlockTrailingHorizontalRulerWidth = None
  BorderStyle_Dashed = None
  BorderStyle_DotDash = None
  BorderStyle_DotDotDash = None
  BorderStyle_Dotted = None
  BorderStyle_Double = None
  BorderStyle_Groove = None
  BorderStyle_Inset = None
  BorderStyle_None = None
  BorderStyle_Outset = None
  BorderStyle_Ridge = None
  BorderStyle_Solid = None
  CharFormat = None
  CssFloat = None
  FirstFontProperty = None
  FloatLeft = None
  FloatRight = None
  FontCapitalization = None
  FontFamily = None
  FontFixedPitch = None
  FontHintingPreference = None
  FontItalic = None
  FontKerning = None
  FontLetterSpacing = None
  FontOverline = None
  FontPixelSize = None
  FontPointSize = None
  FontSizeAdjustment = None
  FontSizeIncrement = None
  FontStrikeOut = None
  FontStyleHint = None
  FontStyleStrategy = None
  FontUnderline = None
  FontWeight = None
  FontWordSpacing = None
  ForegroundBrush = None
  FrameBorder = None
  FrameBorderBrush = None
  FrameBorderStyle = None
  FrameBottomMargin = None
  FrameFormat = None
  FrameHeight = None
  FrameLeftMargin = None
  FrameMargin = None
  FramePadding = None
  FrameRightMargin = None
  FrameTopMargin = None
  FrameWidth = None
  FullWidthSelection = None
  ImageHeight = None
  ImageName = None
  ImageObject = None
  ImageWidth = None
  InFlow = None
  InvalidFormat = None
  IsAnchor = None
  LastFontProperty = None
  LayoutDirection = None
  LineHeight = None
  LineHeightType = None
  ListFormat = None
  ListIndent = None
  ListNumberPrefix = None
  ListNumberSuffix = None
  ListStyle = None
  NoObject = None
  ObjectIndex = None
  ObjectType = None
  OutlinePen = None
  PageBreakPolicy = None
  PageBreak_AlwaysAfter = None
  PageBreak_AlwaysBefore = None
  PageBreak_Auto = None
  TabPositions = None
  TableCellBottomPadding = None
  TableCellColumnSpan = None
  TableCellLeftPadding = None
  TableCellObject = None
  TableCellPadding = None
  TableCellRightPadding = None
  TableCellRowSpan = None
  TableCellSpacing = None
  TableCellTopPadding = None
  TableColumnWidthConstraints = None
  TableColumns = None
  TableFormat = None
  TableHeaderRowCount = None
  TableObject = None
  TextIndent = None
  TextOutline = None
  TextToolTip = None
  TextUnderlineColor = None
  TextUnderlineStyle = None
  TextVerticalAlignment = None
  UserFormat = None
  UserObject = None
  UserProperty = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def alignment():
    pass

  def cellPadding():
    pass

  def cellSpacing():
    pass

  def clearColumnWidthConstraints():
    pass

  def columnWidthConstraints():
    pass

  def columns():
    pass

  def headerRowCount():
    pass

  def isValid():
    pass

  def setAlignment():
    pass

  def setCellPadding():
    pass

  def setCellSpacing():
    pass

  def setColumnWidthConstraints():
    pass

  def setColumns():
    pass

  def setHeaderRowCount():
    pass

class QTouchEvent(QInputEvent):

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

  class DeviceType(object):

    TouchPad = None
    TouchScreen = None
    name = property(None, None, None,
                    )

    values = {}

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
  TouchPad = None

  class TouchPoint(Object):

    def __init__(self, *args):
      """ x.__init__(...) initializes x; see help(type(x)) for signature """
      pass

    def id():
      pass

    def isPrimary():
      pass

    def lastNormalizedPos():
      pass

    def lastPos():
      pass

    def lastScenePos():
      pass

    def lastScreenPos():
      pass

    def normalizedPos():
      pass

    def pos():
      pass

    def pressure():
      pass

    def rect():
      pass

    def scenePos():
      pass

    def sceneRect():
      pass

    def screenPos():
      pass

    def screenRect():
      pass

    def setId():
      pass

    def setLastNormalizedPos():
      pass

    def setLastPos():
      pass

    def setLastScenePos():
      pass

    def setLastScreenPos():
      pass

    def setNormalizedPos():
      pass

    def setPos():
      pass

    def setPressure():
      pass

    def setRect():
      pass

    def setScenePos():
      pass

    def setSceneRect():
      pass

    def setScreenPos():
      pass

    def setScreenRect():
      pass

    def setStartNormalizedPos():
      pass

    def setStartPos():
      pass

    def setStartScenePos():
      pass

    def setStartScreenPos():
      pass

    def startNormalizedPos():
      pass

    def startPos():
      pass

    def startScenePos():
      pass

    def startScreenPos():
      pass

    def state():
      pass

  TouchScreen = None
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

  def deviceType():
    pass

  def registerEventType():
    pass

  def setDeviceType():
    pass

  def setTouchPoints():
    pass

  def setWidget():
    pass

  def touchPoints():
    pass

  def widget():
    pass

class QTransform(Object):

  class TransformationType(object):

    TxNone = None
    TxProject = None
    TxRotate = None
    TxScale = None
    TxShear = None
    TxTranslate = None
    name = property(None, None, None,
                    )

    values = {}

  TxNone = None
  TxProject = None
  TxRotate = None
  TxScale = None
  TxShear = None
  TxTranslate = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def adjoint():
    pass

  def det():
    pass

  def determinant():
    pass

  def dx():
    pass

  def dy():
    pass

  def fromScale():
    pass

  def fromTranslate():
    pass

  def inverted():
    pass

  def isAffine():
    pass

  def isIdentity():
    pass

  def isInvertible():
    pass

  def isRotating():
    pass

  def isScaling():
    pass

  def isTranslating():
    pass

  def m11():
    pass

  def m12():
    pass

  def m13():
    pass

  def m21():
    pass

  def m22():
    pass

  def m23():
    pass

  def m31():
    pass

  def m32():
    pass

  def m33():
    pass

  def map():
    pass

  def mapRect():
    pass

  def mapToPolygon():
    pass

  def quadToQuad():
    pass

  def quadToSquare():
    pass

  def reset():
    pass

  def rotate():
    pass

  def rotateRadians():
    pass

  def scale():
    pass

  def setMatrix():
    pass

  def shear():
    pass

  def squareToQuad():
    pass

  def toAffine():
    pass

  def translate():
    pass

  def transposed():
    pass

  def type():
    pass

class QValidator(QObject):

  Acceptable = None
  Intermediate = None
  Invalid = None
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

  def fixup():
    pass

  def locale():
    pass

  def registerUserData():
    pass

  def setLocale():
    pass

  staticMetaObject = None

  def validate():
    pass

class QVector2D(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def dotProduct():
    pass

  def isNull():
    pass

  def length():
    pass

  def lengthSquared():
    pass

  def normalize():
    pass

  def normalized():
    pass

  def setX():
    pass

  def setY():
    pass

  def toPoint():
    pass

  def toPointF():
    pass

  def toTuple():
    pass

  def toVector3D():
    pass

  def toVector4D():
    pass

  def x():
    pass

  def y():
    pass

class QVector3D(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def crossProduct():
    pass

  def distanceToLine():
    pass

  def distanceToPlane():
    pass

  def dotProduct():
    pass

  def isNull():
    pass

  def length():
    pass

  def lengthSquared():
    pass

  def normal():
    pass

  def normalize():
    pass

  def normalized():
    pass

  def setX():
    pass

  def setY():
    pass

  def setZ():
    pass

  def toPoint():
    pass

  def toPointF():
    pass

  def toTuple():
    pass

  def toVector2D():
    pass

  def toVector4D():
    pass

  def x():
    pass

  def y():
    pass

  def z():
    pass

class QVector4D(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def dotProduct():
    pass

  def isNull():
    pass

  def length():
    pass

  def lengthSquared():
    pass

  def normalize():
    pass

  def normalized():
    pass

  def setW():
    pass

  def setX():
    pass

  def setY():
    pass

  def setZ():
    pass

  def toPoint():
    pass

  def toPointF():
    pass

  def toTuple():
    pass

  def toVector2D():
    pass

  def toVector2DAffine():
    pass

  def toVector3D():
    pass

  def toVector3DAffine():
    pass

  def w():
    pass

  def x():
    pass

  def y():
    pass

  def z():
    pass

class QWhatsThisClickedEvent(QEvent):

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

  def href():
    pass

  def registerEventType():
    pass

class QWheelEvent(QInputEvent):

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

  def globalPos():
    pass

  def globalX():
    pass

  def globalY():
    pass

  def orientation():
    pass

  def pos():
    pass

  def registerEventType():
    pass

  def x():
    pass

  def y():
    pass

class QWindowStateChangeEvent(QEvent):

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

  def isOverride():
    pass

  def oldState():
    pass

  def registerEventType():
    pass

__doc__ = None
__name__ = 'Qt.QtGui'

def qAlpha():
  pass

def qBlue():
  pass

def qGray():
  pass

def qGreen():
  pass

def qIsGray():
  pass

def qRed():
  pass

def qRgb():
  pass

def qRgba():
  pass

