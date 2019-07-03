# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QAbstractPrintDialog(QDialog):

  Accepted = None
  AllPages = None
  CurrentPage = None

  class DialogCode(object):

    Accepted = None
    Rejected = None
    name = property(None, None, None,
                    )

    values = {}

  DontUseSheet = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  None = None
  PageRange = None

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
  PrintCollateCopies = None
  PrintCurrentPage = None

  class PrintDialogOption(object):

    DontUseSheet = None
    None = None
    PrintCollateCopies = None
    PrintCurrentPage = None
    PrintPageRange = None
    PrintSelection = None
    PrintShowPageSize = None
    PrintToFile = None
    name = property(None, None, None,
                    )

    values = {}

  class PrintDialogOptions(object):

    pass

  PrintPageRange = None

  class PrintRange(object):

    AllPages = None
    CurrentPage = None
    PageRange = None
    Selection = None
    name = property(None, None, None,
                    )

    values = {}

  PrintSelection = None
  PrintShowPageSize = None
  PrintToFile = None
  Rejected = None

  class RenderFlag(object):

    DrawChildren = None
    DrawWindowBackground = None
    IgnoreMask = None
    name = property(None, None, None,
                    )

    values = {}

  class RenderFlags(object):

    pass

  Selection = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def addEnabledOption():
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

  def enabledOptions():
    pass

  def exec_():
    pass

  def finished():
    """ Signal """
    pass

  def fromPage():
    pass

  def isOptionEnabled():
    pass

  def keyboardGrabber():
    pass

  def maxPage():
    pass

  def minPage():
    pass

  def mouseGrabber():
    pass

  def printRange():
    pass

  def printer():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def setEnabledOptions():
    pass

  def setFromTo():
    pass

  def setMinMax():
    pass

  def setOptionTabs():
    pass

  def setPrintRange():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def toPage():
    pass

class QPageSetupDialog(QAbstractPageSetupDialog):

  Accepted = None
  DontUseSheet = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  None = None
  OwnsPrinter = None

  class PageSetupDialogOption(object):

    DontUseSheet = None
    None = None
    OwnsPrinter = None
    name = property(None, None, None,
                    )

    values = {}

  class PageSetupDialogOptions(object):

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
  Rejected = None
  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
    """ Signal """
    pass

  def addEnabledOption():
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

  def enabledOptions():
    pass

  def exec_():
    pass

  def finished():
    """ Signal """
    pass

  def isOptionEnabled():
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

  def setEnabledOptions():
    pass

  def setOption():
    pass

  def setOptions():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def testOption():
    pass

class QPrintDialog(QAbstractPrintDialog):

  Accepted = None
  AllPages = None
  CurrentPage = None
  DontUseSheet = None
  DrawChildren = None
  DrawWindowBackground = None
  IgnoreMask = None
  None = None
  PageRange = None
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
  PrintCollateCopies = None
  PrintCurrentPage = None
  PrintPageRange = None
  PrintSelection = None
  PrintShowPageSize = None
  PrintToFile = None
  Rejected = None
  Selection = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accepted():
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

  def done():
    pass

  def exec_():
    pass

  def finished():
    """ Signal """
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

  def setOption():
    pass

  def setOptions():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def testOption():
    pass

class QPrintEngine(Object):

  PPK_CollateCopies = None
  PPK_ColorMode = None
  PPK_CopyCount = None
  PPK_Creator = None
  PPK_CustomBase = None
  PPK_CustomPaperSize = None
  PPK_DocumentName = None
  PPK_Duplex = None
  PPK_FontEmbedding = None
  PPK_FullPage = None
  PPK_NumberOfCopies = None
  PPK_Orientation = None
  PPK_OutputFileName = None
  PPK_PageMargins = None
  PPK_PageOrder = None
  PPK_PageRect = None
  PPK_PageSize = None
  PPK_PaperRect = None
  PPK_PaperSize = None
  PPK_PaperSource = None
  PPK_PaperSources = None
  PPK_PrinterName = None
  PPK_PrinterProgram = None
  PPK_Resolution = None
  PPK_SelectionOption = None
  PPK_SupportedResolutions = None
  PPK_SupportsMultipleCopies = None
  PPK_SuppressSystemPrintStatus = None
  PPK_WindowsPageSize = None

  class PrintEnginePropertyKey(object):

    PPK_CollateCopies = None
    PPK_ColorMode = None
    PPK_CopyCount = None
    PPK_Creator = None
    PPK_CustomBase = None
    PPK_CustomPaperSize = None
    PPK_DocumentName = None
    PPK_Duplex = None
    PPK_FontEmbedding = None
    PPK_FullPage = None
    PPK_NumberOfCopies = None
    PPK_Orientation = None
    PPK_OutputFileName = None
    PPK_PageMargins = None
    PPK_PageOrder = None
    PPK_PageRect = None
    PPK_PageSize = None
    PPK_PaperRect = None
    PPK_PaperSize = None
    PPK_PaperSource = None
    PPK_PaperSources = None
    PPK_PrinterName = None
    PPK_PrinterProgram = None
    PPK_Resolution = None
    PPK_SelectionOption = None
    PPK_SupportedResolutions = None
    PPK_SupportsMultipleCopies = None
    PPK_SuppressSystemPrintStatus = None
    PPK_WindowsPageSize = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def abort():
    pass

  def metric():
    pass

  def newPage():
    pass

  def printerState():
    pass

  def property():
    pass

  def setProperty():
    pass

class QPrintPreviewDialog(QDialog):

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

  def open():
    pass

  def paintRequested():
    """ Signal """
    pass

  def printer():
    pass

  def registerUserData():
    pass

  def rejected():
    """ Signal """
    pass

  def setTabOrder():
    pass

  def setVisible():
    pass

  staticMetaObject = None

class QPrintPreviewWidget(QWidget):

  AllPagesView = None
  CustomZoom = None
  DrawChildren = None
  DrawWindowBackground = None
  FacingPagesView = None
  FitInView = None
  FitToWidth = None
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
  SinglePageView = None

  class ViewMode(object):

    AllPagesView = None
    FacingPagesView = None
    SinglePageView = None
    name = property(None, None, None,
                    )

    values = {}

  class ZoomMode(object):

    CustomZoom = None
    FitInView = None
    FitToWidth = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def connect():
    pass

  def currentPage():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def fitInView():
    pass

  def fitToWidth():
    pass

  def keyboardGrabber():
    pass

  def mouseGrabber():
    pass

  def numPages():
    pass

  def orientation():
    pass

  def pageCount():
    pass

  def paintRequested():
    """ Signal """
    pass

  def previewChanged():
    """ Signal """
    pass

  def print_():
    pass

  def registerUserData():
    pass

  def setAllPagesViewMode():
    pass

  def setCurrentPage():
    pass

  def setFacingPagesViewMode():
    pass

  def setLandscapeOrientation():
    pass

  def setOrientation():
    pass

  def setPortraitOrientation():
    pass

  def setSinglePageViewMode():
    pass

  def setTabOrder():
    pass

  def setViewMode():
    pass

  def setVisible():
    pass

  def setZoomFactor():
    pass

  def setZoomMode():
    pass

  staticMetaObject = None

  def updatePreview():
    pass

  def viewMode():
    pass

  def zoomFactor():
    pass

  def zoomIn():
    pass

  def zoomMode():
    pass

  def zoomOut():
    pass

class QPrinter(QPaintDevice):

  A0 = None
  A1 = None
  A2 = None
  A3 = None
  A4 = None
  A5 = None
  A6 = None
  A7 = None
  A8 = None
  A9 = None
  Aborted = None
  Active = None
  AllPages = None
  Auto = None
  B0 = None
  B1 = None
  B10 = None
  B2 = None
  B3 = None
  B4 = None
  B5 = None
  B6 = None
  B7 = None
  B8 = None
  B9 = None
  C5E = None
  Cassette = None
  Cicero = None
  Color = None

  class ColorMode(object):

    Color = None
    GrayScale = None
    name = property(None, None, None,
                    )

    values = {}

  Comm10E = None
  CurrentPage = None
  Custom = None
  DLE = None
  DevicePixel = None
  Didot = None
  DuplexAuto = None
  DuplexLongSide = None

  class DuplexMode(object):

    DuplexAuto = None
    DuplexLongSide = None
    DuplexNone = None
    DuplexShortSide = None
    name = property(None, None, None,
                    )

    values = {}

  DuplexNone = None
  DuplexShortSide = None
  Envelope = None
  EnvelopeManual = None
  Error = None
  Executive = None
  FirstPageFirst = None
  Folio = None
  FormSource = None
  GrayScale = None
  HighResolution = None
  Idle = None
  Inch = None
  Landscape = None
  LargeCapacity = None
  LargeFormat = None
  LastPageFirst = None
  Ledger = None
  Legal = None
  Letter = None
  Lower = None
  Manual = None
  MaxPageSource = None
  Middle = None
  Millimeter = None
  NPageSize = None
  NPaperSize = None
  NativeFormat = None
  OnlyOne = None

  class Orientation(object):

    Landscape = None
    Portrait = None
    name = property(None, None, None,
                    )

    values = {}

  class OutputFormat(object):

    NativeFormat = None
    PdfFormat = None
    PostScriptFormat = None
    name = property(None, None, None,
                    )

    values = {}

  class PageOrder(object):

    FirstPageFirst = None
    LastPageFirst = None
    name = property(None, None, None,
                    )

    values = {}

  PageRange = None

  class PageSize(object):

    A0 = None
    A1 = None
    A2 = None
    A3 = None
    A4 = None
    A5 = None
    A6 = None
    A7 = None
    A8 = None
    A9 = None
    B0 = None
    B1 = None
    B10 = None
    B2 = None
    B3 = None
    B4 = None
    B5 = None
    B6 = None
    B7 = None
    B8 = None
    B9 = None
    C5E = None
    Comm10E = None
    Custom = None
    DLE = None
    Executive = None
    Folio = None
    Ledger = None
    Legal = None
    Letter = None
    NPageSize = None
    NPaperSize = None
    Tabloid = None
    name = property(None, None, None,
                    )

    values = {}

  class PaperSource(object):

    Auto = None
    Cassette = None
    Envelope = None
    EnvelopeManual = None
    FormSource = None
    LargeCapacity = None
    LargeFormat = None
    Lower = None
    Manual = None
    MaxPageSource = None
    Middle = None
    OnlyOne = None
    SmallFormat = None
    Tractor = None
    name = property(None, None, None,
                    )

    values = {}

  PdfFormat = None
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
  Pica = None
  Point = None
  Portrait = None
  PostScriptFormat = None

  class PrintRange(object):

    AllPages = None
    CurrentPage = None
    PageRange = None
    Selection = None
    name = property(None, None, None,
                    )

    values = {}

  class PrinterMode(object):

    HighResolution = None
    PrinterResolution = None
    ScreenResolution = None
    name = property(None, None, None,
                    )

    values = {}

  PrinterResolution = None

  class PrinterState(object):

    Aborted = None
    Active = None
    Error = None
    Idle = None
    name = property(None, None, None,
                    )

    values = {}

  ScreenResolution = None
  Selection = None
  SmallFormat = None
  Tabloid = None
  Tractor = None

  class Unit(object):

    Cicero = None
    DevicePixel = None
    Didot = None
    Inch = None
    Millimeter = None
    Pica = None
    Point = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def abort():
    pass

  def actualNumCopies():
    pass

  def collateCopies():
    pass

  def colorMode():
    pass

  def copyCount():
    pass

  def creator():
    pass

  def devType():
    pass

  def docName():
    pass

  def doubleSidedPrinting():
    pass

  def duplex():
    pass

  def fontEmbeddingEnabled():
    pass

  def fromPage():
    pass

  def fullPage():
    pass

  def getPageMargins():
    pass

  def isValid():
    pass

  def metric():
    pass

  def newPage():
    pass

  def numCopies():
    pass

  def orientation():
    pass

  def outputFileName():
    pass

  def outputFormat():
    pass

  def pageOrder():
    pass

  def pageRect():
    pass

  def pageSize():
    pass

  def paintEngine():
    pass

  def paperRect():
    pass

  def paperSize():
    pass

  def paperSource():
    pass

  def printEngine():
    pass

  def printProgram():
    pass

  def printRange():
    pass

  def printerName():
    pass

  def printerState():
    pass

  def resolution():
    pass

  def setCollateCopies():
    pass

  def setColorMode():
    pass

  def setCopyCount():
    pass

  def setCreator():
    pass

  def setDocName():
    pass

  def setDoubleSidedPrinting():
    pass

  def setDuplex():
    pass

  def setEngines():
    pass

  def setFontEmbeddingEnabled():
    pass

  def setFromTo():
    pass

  def setFullPage():
    pass

  def setNumCopies():
    pass

  def setOrientation():
    pass

  def setOutputFileName():
    pass

  def setOutputFormat():
    pass

  def setPageMargins():
    pass

  def setPageOrder():
    pass

  def setPageSize():
    pass

  def setPaperSize():
    pass

  def setPaperSource():
    pass

  def setPrintProgram():
    pass

  def setPrintRange():
    pass

  def setPrinterName():
    pass

  def setResolution():
    pass

  def setWinPageSize():
    pass

  def supportedPaperSources():
    pass

  def supportedResolutions():
    pass

  def supportsMultipleCopies():
    pass

  def toPage():
    pass

  def winPageSize():
    pass

class QPrinterInfo(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def availablePrinters():
    pass

  def defaultPrinter():
    pass

  def isDefault():
    pass

  def isNull():
    pass

  def printerName():
    pass

  def supportedPaperSizes():
    pass

__doc__ = None
__name__ = 'Qt.QtPrintSupport'

