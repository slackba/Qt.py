# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QGL(Object):

  AccumBuffer = None
  AlphaChannel = None
  ColorIndex = None
  DeprecatedFunctions = None
  DepthBuffer = None
  DirectRendering = None
  DoubleBuffer = None

  class FormatOption(object):

    AccumBuffer = None
    AlphaChannel = None
    ColorIndex = None
    DeprecatedFunctions = None
    DepthBuffer = None
    DirectRendering = None
    DoubleBuffer = None
    HasOverlay = None
    IndirectRendering = None
    NoAccumBuffer = None
    NoAlphaChannel = None
    NoDeprecatedFunctions = None
    NoDepthBuffer = None
    NoOverlay = None
    NoSampleBuffers = None
    NoStencilBuffer = None
    NoStereoBuffers = None
    Rgba = None
    SampleBuffers = None
    SingleBuffer = None
    StencilBuffer = None
    StereoBuffers = None
    name = property(None, None, None,
                    )

    values = {}

  class FormatOptions(object):

    pass

  HasOverlay = None
  IndirectRendering = None
  NoAccumBuffer = None
  NoAlphaChannel = None
  NoDeprecatedFunctions = None
  NoDepthBuffer = None
  NoOverlay = None
  NoSampleBuffers = None
  NoStencilBuffer = None
  NoStereoBuffers = None
  Rgba = None
  SampleBuffers = None
  SingleBuffer = None
  StencilBuffer = None
  StereoBuffers = None

  def setPreferredPaintEngine():
    pass

class QGLContext(Object):

  class BindOption(object):

    CanFlipNativePixmapBindOption = None
    DefaultBindOption = None
    InternalBindOption = None
    InvertedYBindOption = None
    LinearFilteringBindOption = None
    MemoryManagedBindOption = None
    MipmapBindOption = None
    NoBindOption = None
    PremultipliedAlphaBindOption = None
    name = property(None, None, None,
                    )

    values = {}

  class BindOptions(object):

    pass

  CanFlipNativePixmapBindOption = None
  DefaultBindOption = None
  InternalBindOption = None
  InvertedYBindOption = None
  LinearFilteringBindOption = None
  MemoryManagedBindOption = None
  MipmapBindOption = None
  NoBindOption = None
  PremultipliedAlphaBindOption = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def areSharing():
    pass

  def bindTexture():
    pass

  def chooseContext():
    pass

  def colorIndex():
    pass

  def create():
    pass

  def currentContext():
    pass

  def deleteTexture():
    pass

  def device():
    pass

  def deviceIsPixmap():
    pass

  def doneCurrent():
    pass

  def drawTexture():
    pass

  def format():
    pass

  def getProcAddress():
    pass

  def initialized():
    pass

  def isSharing():
    pass

  def isValid():
    pass

  def makeCurrent():
    pass

  def overlayTransparentColor():
    pass

  def requestedFormat():
    pass

  def reset():
    pass

  def setDevice():
    pass

  def setFormat():
    pass

  def setInitialized():
    pass

  def setTextureCacheLimit():
    pass

  def setValid():
    pass

  def setWindowCreated():
    pass

  def swapBuffers():
    pass

  def textureCacheLimit():
    pass

  def windowCreated():
    pass

class QGLFormat(Object):

  CompatibilityProfile = None
  CoreProfile = None
  NoProfile = None

  class OpenGLContextProfile(object):

    CompatibilityProfile = None
    CoreProfile = None
    NoProfile = None
    name = property(None, None, None,
                    )

    values = {}

  class OpenGLVersionFlag(object):

    OpenGL_ES_CommonLite_Version_1_0 = None
    OpenGL_ES_CommonLite_Version_1_1 = None
    OpenGL_ES_Common_Version_1_0 = None
    OpenGL_ES_Common_Version_1_1 = None
    OpenGL_ES_Version_2_0 = None
    OpenGL_Version_1_1 = None
    OpenGL_Version_1_2 = None
    OpenGL_Version_1_3 = None
    OpenGL_Version_1_4 = None
    OpenGL_Version_1_5 = None
    OpenGL_Version_2_0 = None
    OpenGL_Version_2_1 = None
    OpenGL_Version_3_0 = None
    OpenGL_Version_3_1 = None
    OpenGL_Version_3_2 = None
    OpenGL_Version_3_3 = None
    OpenGL_Version_4_0 = None
    OpenGL_Version_None = None
    name = property(None, None, None,
                    )

    values = {}

  class OpenGLVersionFlags(object):

    pass

  OpenGL_ES_CommonLite_Version_1_0 = None
  OpenGL_ES_CommonLite_Version_1_1 = None
  OpenGL_ES_Common_Version_1_0 = None
  OpenGL_ES_Common_Version_1_1 = None
  OpenGL_ES_Version_2_0 = None
  OpenGL_Version_1_1 = None
  OpenGL_Version_1_2 = None
  OpenGL_Version_1_3 = None
  OpenGL_Version_1_4 = None
  OpenGL_Version_1_5 = None
  OpenGL_Version_2_0 = None
  OpenGL_Version_2_1 = None
  OpenGL_Version_3_0 = None
  OpenGL_Version_3_1 = None
  OpenGL_Version_3_2 = None
  OpenGL_Version_3_3 = None
  OpenGL_Version_4_0 = None
  OpenGL_Version_None = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accum():
    pass

  def accumBufferSize():
    pass

  def alpha():
    pass

  def alphaBufferSize():
    pass

  def blueBufferSize():
    pass

  def defaultFormat():
    pass

  def defaultOverlayFormat():
    pass

  def depth():
    pass

  def depthBufferSize():
    pass

  def directRendering():
    pass

  def doubleBuffer():
    pass

  def greenBufferSize():
    pass

  def hasOpenGL():
    pass

  def hasOpenGLOverlays():
    pass

  def hasOverlay():
    pass

  def majorVersion():
    pass

  def minorVersion():
    pass

  def openGLVersionFlags():
    pass

  def plane():
    pass

  def profile():
    pass

  def redBufferSize():
    pass

  def rgba():
    pass

  def sampleBuffers():
    pass

  def samples():
    pass

  def setAccum():
    pass

  def setAccumBufferSize():
    pass

  def setAlpha():
    pass

  def setAlphaBufferSize():
    pass

  def setBlueBufferSize():
    pass

  def setDefaultFormat():
    pass

  def setDefaultOverlayFormat():
    pass

  def setDepth():
    pass

  def setDepthBufferSize():
    pass

  def setDirectRendering():
    pass

  def setDoubleBuffer():
    pass

  def setGreenBufferSize():
    pass

  def setOption():
    pass

  def setOverlay():
    pass

  def setPlane():
    pass

  def setProfile():
    pass

  def setRedBufferSize():
    pass

  def setRgba():
    pass

  def setSampleBuffers():
    pass

  def setSamples():
    pass

  def setStencil():
    pass

  def setStencilBufferSize():
    pass

  def setStereo():
    pass

  def setSwapInterval():
    pass

  def setVersion():
    pass

  def stencil():
    pass

  def stencilBufferSize():
    pass

  def stereo():
    pass

  def swapInterval():
    pass

  def testOption():
    pass

class QGLWidget(QWidget):

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

  def autoBufferSwap():
    pass

  def bindTexture():
    pass

  def colormap():
    pass

  def connect():
    pass

  def context():
    pass

  def convertToGLFormat():
    pass

  def customContextMenuRequested():
    """ Signal """
    pass

  def deleteTexture():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def doneCurrent():
    pass

  def doubleBuffer():
    pass

  def drawTexture():
    pass

  def event():
    pass

  def format():
    pass

  def glDraw():
    pass

  def glInit():
    pass

  def grabFrameBuffer():
    pass

  def initializeGL():
    pass

  def initializeOverlayGL():
    pass

  def isSharing():
    pass

  def isValid():
    pass

  def keyboardGrabber():
    pass

  def makeCurrent():
    pass

  def makeOverlayCurrent():
    pass

  def mouseGrabber():
    pass

  def overlayContext():
    pass

  def paintEngine():
    pass

  def paintEvent():
    pass

  def paintGL():
    pass

  def paintOverlayGL():
    pass

  def qglClearColor():
    pass

  def qglColor():
    pass

  def registerUserData():
    pass

  def renderPixmap():
    pass

  def renderText():
    pass

  def resizeEvent():
    pass

  def resizeGL():
    pass

  def resizeOverlayGL():
    pass

  def setAutoBufferSwap():
    pass

  def setColormap():
    pass

  def setMouseTracking():
    pass

  def setTabOrder():
    pass

  staticMetaObject = None

  def swapBuffers():
    pass

  def updateGL():
    pass

  def updateOverlayGL():
    pass

__doc__ = None
__name__ = 'Qt.QtOpenGL'

