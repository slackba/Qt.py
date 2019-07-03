# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QAbstractVideoBuffer(Object):

  CoreImageHandle = None
  GLTextureHandle = None

  class HandleType(object):

    CoreImageHandle = None
    GLTextureHandle = None
    NoHandle = None
    QPixmapHandle = None
    UserHandle = None
    XvShmImageHandle = None
    name = property(None, None, None,
                    )

    values = {}

  class MapMode(object):

    NotMapped = None
    ReadOnly = None
    ReadWrite = None
    WriteOnly = None
    name = property(None, None, None,
                    )

    values = {}

  NoHandle = None
  NotMapped = None
  QPixmapHandle = None
  ReadOnly = None
  ReadWrite = None
  UserHandle = None
  WriteOnly = None
  XvShmImageHandle = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def handle():
    pass

  def handleType():
    pass

  def mapMode():
    pass

  def unmap():
    pass

class QAbstractVideoSurface(QObject):

  class Error(object):

    IncorrectFormatError = None
    NoError = None
    ResourceError = None
    StoppedError = None
    UnsupportedFormatError = None
    name = property(None, None, None,
                    )

    values = {}

  IncorrectFormatError = None
  NoError = None
  ResourceError = None
  StoppedError = None
  UnsupportedFormatError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activeChanged():
    """ Signal """
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def error():
    pass

  def isActive():
    pass

  def isFormatSupported():
    pass

  def nearestFormat():
    pass

  def present():
    pass

  def registerUserData():
    pass

  def setError():
    pass

  def start():
    pass

  staticMetaObject = None

  def stop():
    pass

  def supportedFormatsChanged():
    """ Signal """
    pass

  def supportedPixelFormats():
    pass

  def surfaceFormat():
    pass

  def surfaceFormatChanged():
    """ Signal """
    pass

class QAudio(Object):

  ActiveState = None
  AudioInput = None
  AudioOutput = None

  class Error(object):

    FatalError = None
    IOError = None
    NoError = None
    OpenError = None
    UnderrunError = None
    name = property(None, None, None,
                    )

    values = {}

  FatalError = None
  IOError = None
  IdleState = None

  class Mode(object):

    AudioInput = None
    AudioOutput = None
    name = property(None, None, None,
                    )

    values = {}

  NoError = None
  OpenError = None

  class State(object):

    ActiveState = None
    IdleState = None
    StoppedState = None
    SuspendedState = None
    name = property(None, None, None,
                    )

    values = {}

  StoppedState = None
  SuspendedState = None
  UnderrunError = None

class QAudioDeviceInfo(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def availableDevices():
    pass

  def defaultInputDevice():
    pass

  def defaultOutputDevice():
    pass

  def deviceName():
    pass

  def isFormatSupported():
    pass

  def isNull():
    pass

  def nearestFormat():
    pass

  def preferredFormat():
    pass

  def supportedByteOrders():
    pass

  def supportedChannelCounts():
    pass

  def supportedChannels():
    pass

  def supportedCodecs():
    pass

  def supportedFrequencies():
    pass

  def supportedSampleRates():
    pass

  def supportedSampleSizes():
    pass

  def supportedSampleTypes():
    pass

class QAudioFormat(Object):

  BigEndian = None

  class Endian(object):

    BigEndian = None
    LittleEndian = None
    name = property(None, None, None,
                    )

    values = {}

  Float = None
  LittleEndian = None

  class SampleType(object):

    Float = None
    SignedInt = None
    UnSignedInt = None
    Unknown = None
    name = property(None, None, None,
                    )

    values = {}

  SignedInt = None
  UnSignedInt = None
  Unknown = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def byteOrder():
    pass

  def channelCount():
    pass

  def channels():
    pass

  def codec():
    pass

  def frequency():
    pass

  def isValid():
    pass

  def sampleRate():
    pass

  def sampleSize():
    pass

  def sampleType():
    pass

  def setByteOrder():
    pass

  def setChannelCount():
    pass

  def setChannels():
    pass

  def setCodec():
    pass

  def setFrequency():
    pass

  def setSampleRate():
    pass

  def setSampleSize():
    pass

  def setSampleType():
    pass

class QAudioInput(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bufferSize():
    pass

  def bytesReady():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def elapsedUSecs():
    pass

  def error():
    pass

  def format():
    pass

  def notify():
    """ Signal """
    pass

  def notifyInterval():
    pass

  def periodSize():
    pass

  def processedUSecs():
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def resume():
    pass

  def setBufferSize():
    pass

  def setNotifyInterval():
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

  def suspend():
    pass

class QAudioOutput(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bufferSize():
    pass

  def bytesFree():
    pass

  def connect():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def elapsedUSecs():
    pass

  def error():
    pass

  def format():
    pass

  def notify():
    """ Signal """
    pass

  def notifyInterval():
    pass

  def periodSize():
    pass

  def processedUSecs():
    pass

  def registerUserData():
    pass

  def reset():
    pass

  def resume():
    pass

  def setBufferSize():
    pass

  def setNotifyInterval():
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

  def suspend():
    pass

class QVideoFrame(Object):

  BottomField = None

  class FieldType(object):

    BottomField = None
    InterlacedFrame = None
    ProgressiveFrame = None
    TopField = None
    name = property(None, None, None,
                    )

    values = {}

  Format_ARGB32 = None
  Format_ARGB32_Premultiplied = None
  Format_ARGB8565_Premultiplied = None
  Format_AYUV444 = None
  Format_AYUV444_Premultiplied = None
  Format_BGR24 = None
  Format_BGR32 = None
  Format_BGR555 = None
  Format_BGR565 = None
  Format_BGRA32 = None
  Format_BGRA32_Premultiplied = None
  Format_BGRA5658_Premultiplied = None
  Format_IMC1 = None
  Format_IMC2 = None
  Format_IMC3 = None
  Format_IMC4 = None
  Format_Invalid = None
  Format_NV12 = None
  Format_NV21 = None
  Format_RGB24 = None
  Format_RGB32 = None
  Format_RGB555 = None
  Format_RGB565 = None
  Format_UYVY = None
  Format_User = None
  Format_Y16 = None
  Format_Y8 = None
  Format_YUV420P = None
  Format_YUV444 = None
  Format_YUYV = None
  Format_YV12 = None
  InterlacedFrame = None

  class PixelFormat(object):

    Format_ARGB32 = None
    Format_ARGB32_Premultiplied = None
    Format_ARGB8565_Premultiplied = None
    Format_AYUV444 = None
    Format_AYUV444_Premultiplied = None
    Format_BGR24 = None
    Format_BGR32 = None
    Format_BGR555 = None
    Format_BGR565 = None
    Format_BGRA32 = None
    Format_BGRA32_Premultiplied = None
    Format_BGRA5658_Premultiplied = None
    Format_IMC1 = None
    Format_IMC2 = None
    Format_IMC3 = None
    Format_IMC4 = None
    Format_Invalid = None
    Format_NV12 = None
    Format_NV21 = None
    Format_RGB24 = None
    Format_RGB32 = None
    Format_RGB555 = None
    Format_RGB565 = None
    Format_UYVY = None
    Format_User = None
    Format_Y16 = None
    Format_Y8 = None
    Format_YUV420P = None
    Format_YUV444 = None
    Format_YUYV = None
    Format_YV12 = None
    name = property(None, None, None,
                    )

    values = {}

  ProgressiveFrame = None
  TopField = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bits():
    pass

  def bytesPerLine():
    pass

  def endTime():
    pass

  def fieldType():
    pass

  def handle():
    pass

  def handleType():
    pass

  def height():
    pass

  def imageFormatFromPixelFormat():
    pass

  def isMapped():
    pass

  def isReadable():
    pass

  def isValid():
    pass

  def isWritable():
    pass

  def map():
    pass

  def mapMode():
    pass

  def mappedBytes():
    pass

  def pixelFormat():
    pass

  def pixelFormatFromImageFormat():
    pass

  def setEndTime():
    pass

  def setFieldType():
    pass

  def setStartTime():
    pass

  def size():
    pass

  def startTime():
    pass

  def unmap():
    pass

  def width():
    pass

class QVideoSurfaceFormat(Object):

  BottomToTop = None

  class Direction(object):

    BottomToTop = None
    TopToBottom = None
    name = property(None, None, None,
                    )

    values = {}

  TopToBottom = None

  class YCbCrColorSpace(object):

    YCbCr_BT601 = None
    YCbCr_BT709 = None
    YCbCr_CustomMatrix = None
    YCbCr_JPEG = None
    YCbCr_Undefined = None
    YCbCr_xvYCC601 = None
    YCbCr_xvYCC709 = None
    name = property(None, None, None,
                    )

    values = {}

  YCbCr_BT601 = None
  YCbCr_BT709 = None
  YCbCr_CustomMatrix = None
  YCbCr_JPEG = None
  YCbCr_Undefined = None
  YCbCr_xvYCC601 = None
  YCbCr_xvYCC709 = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def frameHeight():
    pass

  def frameRate():
    pass

  def frameSize():
    pass

  def frameWidth():
    pass

  def handleType():
    pass

  def isValid():
    pass

  def pixelAspectRatio():
    pass

  def pixelFormat():
    pass

  def property():
    pass

  def propertyNames():
    pass

  def scanLineDirection():
    pass

  def setFrameRate():
    pass

  def setFrameSize():
    pass

  def setPixelAspectRatio():
    pass

  def setProperty():
    pass

  def setScanLineDirection():
    pass

  def setViewport():
    pass

  def setYCbCrColorSpace():
    pass

  def sizeHint():
    pass

  def viewport():
    pass

  def yCbCrColorSpace():
    pass

__doc__ = None
__name__ = 'Qt.QtMultimedia'

