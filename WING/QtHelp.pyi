# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QHelpContentItem(Object):

  def child():
    pass

  def childCount():
    pass

  def childPosition():
    pass

  def parent():
    pass

  def row():
    pass

  def title():
    pass

  def url():
    pass

class QHelpContentModel(QAbstractItemModel):

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

  def contentItemAt():
    pass

  def contentsCreated():
    """ Signal """
    pass

  def contentsCreationStarted():
    """ Signal """
    pass

  def createContents():
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

  def headerDataChanged():
    """ Signal """
    pass

  def index():
    pass

  def isCreatingContents():
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

  staticMetaObject = None

class QHelpContentWidget(QTreeView):

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

  class RenderFlag(object):

    DrawChildren = None
    DrawWindowBackground = None
    IgnoreMask = None
    name = property(None, None, None,
                    )

    values = {}

  class RenderFlags(object):

    pass

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

  def activated():
    """ Signal """
    pass

  def clicked():
    """ Signal """
    pass

  def collapsed():
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

  def entered():
    """ Signal """
    pass

  def expanded():
    """ Signal """
    pass

  def indexOf():
    pass

  def keyboardGrabber():
    pass

  def linkActivated():
    """ Signal """
    pass

  def mouseGrabber():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def viewportEntered():
    """ Signal """
    pass

class QHelpEngine(QHelpEngineCore):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def contentModel():
    pass

  def contentWidget():
    pass

  def currentFilterChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def indexModel():
    pass

  def indexWidget():
    pass

  def metaData():
    pass

  def namespaceName():
    pass

  def registerUserData():
    pass

  def searchEngine():
    pass

  def setupFinished():
    """ Signal """
    pass

  def setupStarted():
    """ Signal """
    pass

  staticMetaObject = None

  def warning():
    """ Signal """
    pass

class QHelpEngineCore(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addCustomFilter():
    pass

  def autoSaveFilter():
    pass

  def collectionFile():
    pass

  def connect():
    pass

  def copyCollectionFile():
    pass

  def currentFilter():
    pass

  def currentFilterChanged():
    """ Signal """
    pass

  def customFilters():
    pass

  def customValue():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def documentationFileName():
    pass

  def error():
    pass

  def fileData():
    pass

  def files():
    pass

  def filterAttributeSets():
    pass

  def filterAttributes():
    pass

  def findFile():
    pass

  def linksForIdentifier():
    pass

  def metaData():
    pass

  def namespaceName():
    pass

  def registerDocumentation():
    pass

  def registerUserData():
    pass

  def registeredDocumentations():
    pass

  def removeCustomFilter():
    pass

  def removeCustomValue():
    pass

  def setAutoSaveFilter():
    pass

  def setCollectionFile():
    pass

  def setCurrentFilter():
    pass

  def setCustomValue():
    pass

  def setupData():
    pass

  def setupFinished():
    """ Signal """
    pass

  def setupStarted():
    """ Signal """
    pass

  staticMetaObject = None

  def unregisterDocumentation():
    pass

  def warning():
    """ Signal """
    pass

class QHelpIndexModel(QStringListModel):

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

  def dataChanged():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def filter():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def indexCreated():
    """ Signal """
    pass

  def indexCreationStarted():
    """ Signal """
    pass

  def isCreatingIndex():
    pass

  def layoutAboutToBeChanged():
    """ Signal """
    pass

  def layoutChanged():
    """ Signal """
    pass

  def linksForKeyword():
    pass

  def modelAboutToBeReset():
    """ Signal """
    pass

  def modelReset():
    """ Signal """
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

class QHelpIndexWidget(QListView):

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

  def activateCurrentItem():
    pass

  def activated():
    """ Signal """
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

  def entered():
    """ Signal """
    pass

  def filterIndices():
    pass

  def indexesMoved():
    """ Signal """
    pass

  def keyboardGrabber():
    pass

  def linkActivated():
    """ Signal """
    pass

  def linksActivated():
    """ Signal """
    pass

  def mouseGrabber():
    pass

  def pressed():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def viewportEntered():
    """ Signal """
    pass

class QHelpSearchEngine(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cancelIndexing():
    pass

  def cancelSearching():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def hitCount():
    pass

  def hits():
    pass

  def hitsCount():
    pass

  def indexingFinished():
    """ Signal """
    pass

  def indexingStarted():
    """ Signal """
    pass

  def query():
    pass

  def queryWidget():
    pass

  def registerUserData():
    pass

  def reindexDocumentation():
    pass

  def resultWidget():
    pass

  def search():
    pass

  def searchingFinished():
    """ Signal """
    pass

  def searchingStarted():
    """ Signal """
    pass

  staticMetaObject = None

class QHelpSearchQuery(Object):

  ALL = None
  ATLEAST = None
  DEFAULT = None
  FUZZY = None

  class FieldName(object):

    ALL = None
    ATLEAST = None
    DEFAULT = None
    FUZZY = None
    PHRASE = None
    WITHOUT = None
    name = property(None, None, None,
                    )

    values = {}

  PHRASE = None
  WITHOUT = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  fieldName = property(None, None, None,
                       )

  wordList = property(None, None, None,
                      )


class QHelpSearchQueryWidget(QWidget):

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

  def changeEvent():
    pass

  def collapseExtendedSearch():
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

  def expandExtendedSearch():
    pass

  def focusInEvent():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def query():
    pass

  def registerUserData():
    pass

  def search():
    """ Signal """
    pass

  def setQuery():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

class QHelpSearchResultWidget(QWidget):

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

  def keyboardGrabber():
    pass

  def linkAt():
    pass

  def mouseGrabber():
    pass

  def registerUserData():
    pass

  def requestShowLink():
    """ Signal """
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

__doc__ = None
__name__ = 'Qt.QtHelp'

