# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QAbstractNetworkCache(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cacheSize():
    pass

  def clear():
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

  def insert():
    pass

  def metaData():
    pass

  def prepare():
    pass

  def registerUserData():
    pass

  def remove():
    pass

  staticMetaObject = None

  def updateMetaData():
    pass

class QAbstractSocket(QIODevice):

  AddressInUseError = None
  Append = None
  BoundState = None
  ClosingState = None
  ConnectedState = None
  ConnectingState = None
  ConnectionRefusedError = None
  DatagramTooLargeError = None
  HostLookupState = None
  HostNotFoundError = None
  IPv4Protocol = None
  IPv6Protocol = None
  KeepAliveOption = None
  ListeningState = None
  LowDelayOption = None
  MulticastLoopbackOption = None
  MulticastTtlOption = None
  NetworkError = None

  class NetworkLayerProtocol(object):

    IPv4Protocol = None
    IPv6Protocol = None
    UnknownNetworkLayerProtocol = None
    name = property(None, None, None,
                    )

    values = {}

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

  ProxyAuthenticationRequiredError = None
  ProxyConnectionClosedError = None
  ProxyConnectionRefusedError = None
  ProxyConnectionTimeoutError = None
  ProxyNotFoundError = None
  ProxyProtocolError = None
  ReadOnly = None
  ReadWrite = None
  RemoteHostClosedError = None
  SocketAccessError = None
  SocketAddressNotAvailableError = None

  class SocketError(object):

    AddressInUseError = None
    ConnectionRefusedError = None
    DatagramTooLargeError = None
    HostNotFoundError = None
    NetworkError = None
    ProxyAuthenticationRequiredError = None
    ProxyConnectionClosedError = None
    ProxyConnectionRefusedError = None
    ProxyConnectionTimeoutError = None
    ProxyNotFoundError = None
    ProxyProtocolError = None
    RemoteHostClosedError = None
    SocketAccessError = None
    SocketAddressNotAvailableError = None
    SocketResourceError = None
    SocketTimeoutError = None
    SslHandshakeFailedError = None
    UnfinishedSocketOperationError = None
    UnknownSocketError = None
    UnsupportedSocketOperationError = None
    name = property(None, None, None,
                    )

    values = {}

  class SocketOption(object):

    KeepAliveOption = None
    LowDelayOption = None
    MulticastLoopbackOption = None
    MulticastTtlOption = None
    name = property(None, None, None,
                    )

    values = {}

  SocketResourceError = None

  class SocketState(object):

    BoundState = None
    ClosingState = None
    ConnectedState = None
    ConnectingState = None
    HostLookupState = None
    ListeningState = None
    UnconnectedState = None
    name = property(None, None, None,
                    )

    values = {}

  SocketTimeoutError = None

  class SocketType(object):

    TcpSocket = None
    UdpSocket = None
    UnknownSocketType = None
    name = property(None, None, None,
                    )

    values = {}

  SslHandshakeFailedError = None
  TcpSocket = None
  Text = None
  Truncate = None
  UdpSocket = None
  Unbuffered = None
  UnconnectedState = None
  UnfinishedSocketOperationError = None
  UnknownNetworkLayerProtocol = None
  UnknownSocketError = None
  UnknownSocketType = None
  UnsupportedSocketOperationError = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def abort():
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

  def connectToHost():
    pass

  def connectToHostImplementation():
    pass

  def connected():
    """ Signal """
    pass

  def connectionClosed():
    """ Signal """
    pass

  def delayedCloseFinished():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def disconnectFromHost():
    pass

  def disconnectFromHostImplementation():
    pass

  def disconnected():
    """ Signal """
    pass

  def error():
    """ Signal """
    pass

  def flush():
    pass

  def hostFound():
    """ Signal """
    pass

  def isSequential():
    pass

  def isValid():
    pass

  def localAddress():
    pass

  def localPort():
    pass

  def peerAddress():
    pass

  def peerName():
    pass

  def peerPort():
    pass

  def proxy():
    pass

  def proxyAuthenticationRequired():
    """ Signal """
    pass

  def readBufferSize():
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readData():
    pass

  def readLineData():
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setLocalAddress():
    pass

  def setLocalPort():
    pass

  def setPeerAddress():
    pass

  def setPeerName():
    pass

  def setPeerPort():
    pass

  def setProxy():
    pass

  def setReadBufferSize():
    pass

  def setSocketDescriptor():
    pass

  def setSocketError():
    pass

  def setSocketOption():
    pass

  def setSocketState():
    pass

  def socketDescriptor():
    pass

  def socketOption():
    pass

  def socketType():
    pass

  def state():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def waitForBytesWritten():
    pass

  def waitForConnected():
    pass

  def waitForDisconnected():
    pass

  def waitForReadyRead():
    pass

  def writeData():
    pass

class QAuthenticator(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def isNull():
    pass

  def option():
    pass

  def options():
    pass

  def password():
    pass

  def realm():
    pass

  def setOption():
    pass

  def setPassword():
    pass

  def setUser():
    pass

  def user():
    pass

class QHostAddress(Object):

  Any = None
  AnyIPv6 = None
  Broadcast = None
  LocalHost = None
  LocalHostIPv6 = None
  Null = None

  class SpecialAddress(object):

    Any = None
    AnyIPv6 = None
    Broadcast = None
    LocalHost = None
    LocalHostIPv6 = None
    Null = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clear():
    pass

  def isInSubnet():
    pass

  def isNull():
    pass

  def parseSubnet():
    pass

  def protocol():
    pass

  def scopeId():
    pass

  def setAddress():
    pass

  def setScopeId():
    pass

  def toIPv4Address():
    pass

  def toIPv6Address():
    pass

  def toString():
    pass

class QHostInfo(Object):

  class HostInfoError(object):

    HostNotFound = None
    NoError = None
    UnknownError = None
    name = property(None, None, None,
                    )

    values = {}

  HostNotFound = None
  NoError = None
  UnknownError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def abortHostLookup():
    pass

  def addresses():
    pass

  def error():
    pass

  def errorString():
    pass

  def fromName():
    pass

  def hostName():
    pass

  def localDomainName():
    pass

  def localHostName():
    pass

  def lookupId():
    pass

  def setAddresses():
    pass

  def setError():
    pass

  def setErrorString():
    pass

  def setHostName():
    pass

  def setLookupId():
    pass

class QLocalServer(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
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

  def fullServerName():
    pass

  def hasPendingConnections():
    pass

  def isListening():
    pass

  def listen():
    pass

  def maxPendingConnections():
    pass

  def newConnection():
    """ Signal """
    pass

  def nextPendingConnection():
    pass

  def registerUserData():
    pass

  def removeServer():
    pass

  def serverError():
    pass

  def serverName():
    pass

  def setMaxPendingConnections():
    pass

  staticMetaObject = None

  def waitForNewConnection():
    pass

class QLocalSocket(QIODevice):

  Append = None
  ClosingState = None
  ConnectedState = None
  ConnectingState = None
  ConnectionError = None
  ConnectionRefusedError = None
  DatagramTooLargeError = None

  class LocalSocketError(object):

    ConnectionError = None
    ConnectionRefusedError = None
    DatagramTooLargeError = None
    PeerClosedError = None
    ServerNotFoundError = None
    SocketAccessError = None
    SocketResourceError = None
    SocketTimeoutError = None
    UnknownSocketError = None
    UnsupportedSocketOperationError = None
    name = property(None, None, None,
                    )

    values = {}

  class LocalSocketState(object):

    ClosingState = None
    ConnectedState = None
    ConnectingState = None
    UnconnectedState = None
    name = property(None, None, None,
                    )

    values = {}

  NotOpen = None
  PeerClosedError = None
  ReadOnly = None
  ReadWrite = None
  ServerNotFoundError = None
  SocketAccessError = None
  SocketResourceError = None
  SocketTimeoutError = None
  Text = None
  Truncate = None
  Unbuffered = None
  UnconnectedState = None
  UnknownSocketError = None
  UnsupportedSocketOperationError = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def abort():
    pass

  def aboutToClose():
    """ Signal """
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

  def connectToServer():
    pass

  def connected():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def disconnectFromServer():
    pass

  def disconnected():
    """ Signal """
    pass

  def error():
    """ Signal """
    pass

  def flush():
    pass

  def fullServerName():
    pass

  def isSequential():
    pass

  def isValid():
    pass

  def readBufferSize():
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

  def serverName():
    pass

  def setReadBufferSize():
    pass

  def state():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def waitForBytesWritten():
    pass

  def waitForConnected():
    pass

  def waitForDisconnected():
    pass

  def waitForReadyRead():
    pass

  def writeData():
    pass

class QNetworkAccessManager(QObject):

  Accessible = None
  CustomOperation = None
  DeleteOperation = None
  GetOperation = None
  HeadOperation = None

  class NetworkAccessibility(object):

    Accessible = None
    NotAccessible = None
    UnknownAccessibility = None
    name = property(None, None, None,
                    )

    values = {}

  NotAccessible = None

  class Operation(object):

    CustomOperation = None
    DeleteOperation = None
    GetOperation = None
    HeadOperation = None
    PostOperation = None
    PutOperation = None
    UnknownOperation = None
    name = property(None, None, None,
                    )

    values = {}

  PostOperation = None
  PutOperation = None
  UnknownAccessibility = None
  UnknownOperation = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def activeConfiguration():
    pass

  def authenticationRequired():
    """ Signal """
    pass

  def cache():
    pass

  def configuration():
    pass

  def connect():
    pass

  def cookieJar():
    pass

  def createRequest():
    pass

  def deleteResource():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def finished():
    """ Signal """
    pass

  def get():
    pass

  def head():
    pass

  def networkAccessible():
    pass

  def networkAccessibleChanged():
    """ Signal """
    pass

  def networkSessionConnected():
    """ Signal """
    pass

  def post():
    pass

  def proxy():
    pass

  def proxyAuthenticationRequired():
    """ Signal """
    pass

  def proxyFactory():
    pass

  def put():
    pass

  def registerUserData():
    pass

  def sendCustomRequest():
    pass

  def setCache():
    pass

  def setConfiguration():
    pass

  def setCookieJar():
    pass

  def setNetworkAccessible():
    pass

  def setProxy():
    pass

  def setProxyFactory():
    pass

  def sslErrors():
    """ Signal """
    pass

  staticMetaObject = None

class QNetworkAddressEntry(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def broadcast():
    pass

  def ip():
    pass

  def netmask():
    pass

  def prefixLength():
    pass

  def setBroadcast():
    pass

  def setIp():
    pass

  def setNetmask():
    pass

  def setPrefixLength():
    pass

class QNetworkCacheMetaData(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def attributes():
    pass

  def expirationDate():
    pass

  def isValid():
    pass

  def lastModified():
    pass

  def rawHeaders():
    pass

  def saveToDisk():
    pass

  def setAttributes():
    pass

  def setExpirationDate():
    pass

  def setLastModified():
    pass

  def setRawHeaders():
    pass

  def setSaveToDisk():
    pass

  def setUrl():
    pass

  def url():
    pass

class QNetworkConfiguration(Object):

  Active = None
  Bearer2G = None
  BearerBluetooth = None
  BearerCDMA2000 = None
  BearerEthernet = None
  BearerHSPA = None

  class BearerType(object):

    Bearer2G = None
    BearerBluetooth = None
    BearerCDMA2000 = None
    BearerEthernet = None
    BearerHSPA = None
    BearerUnknown = None
    BearerWCDMA = None
    BearerWLAN = None
    BearerWiMAX = None
    name = property(None, None, None,
                    )

    values = {}

  BearerUnknown = None
  BearerWCDMA = None
  BearerWLAN = None
  BearerWiMAX = None
  Defined = None
  Discovered = None
  InternetAccessPoint = None
  Invalid = None
  PrivatePurpose = None
  PublicPurpose = None

  class Purpose(object):

    PrivatePurpose = None
    PublicPurpose = None
    ServiceSpecificPurpose = None
    UnknownPurpose = None
    name = property(None, None, None,
                    )

    values = {}

  ServiceNetwork = None
  ServiceSpecificPurpose = None

  class StateFlag(object):

    Active = None
    Defined = None
    Discovered = None
    Undefined = None
    name = property(None, None, None,
                    )

    values = {}

  class StateFlags(object):

    pass

  class Type(object):

    InternetAccessPoint = None
    Invalid = None
    ServiceNetwork = None
    UserChoice = None
    name = property(None, None, None,
                    )

    values = {}

  Undefined = None
  UnknownPurpose = None
  UserChoice = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bearerName():
    pass

  def bearerType():
    pass

  def bearerTypeName():
    pass

  def children():
    pass

  def identifier():
    pass

  def isRoamingAvailable():
    pass

  def isValid():
    pass

  def name():
    pass

  def purpose():
    pass

  def state():
    pass

  def type():
    pass

class QNetworkConfigurationManager(QObject):

  ApplicationLevelRoaming = None
  CanStartAndStopInterfaces = None

  class Capabilities(object):

    pass

  class Capability(object):

    ApplicationLevelRoaming = None
    CanStartAndStopInterfaces = None
    DataStatistics = None
    DirectConnectionRouting = None
    ForcedRoaming = None
    NetworkSessionRequired = None
    SystemSessionSupport = None
    name = property(None, None, None,
                    )

    values = {}

  DataStatistics = None
  DirectConnectionRouting = None
  ForcedRoaming = None
  NetworkSessionRequired = None
  SystemSessionSupport = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def allConfigurations():
    pass

  def capabilities():
    pass

  def configurationAdded():
    """ Signal """
    pass

  def configurationChanged():
    """ Signal """
    pass

  def configurationFromIdentifier():
    pass

  def configurationRemoved():
    """ Signal """
    pass

  def connect():
    pass

  def defaultConfiguration():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def isOnline():
    pass

  def onlineStateChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  staticMetaObject = None

  def updateCompleted():
    """ Signal """
    pass

  def updateConfigurations():
    pass

class QNetworkCookie(Object):

  Full = None
  NameAndValueOnly = None

  class RawForm(object):

    Full = None
    NameAndValueOnly = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def domain():
    pass

  def expirationDate():
    pass

  def isHttpOnly():
    pass

  def isSecure():
    pass

  def isSessionCookie():
    pass

  def name():
    pass

  def parseCookies():
    pass

  def path():
    pass

  def setDomain():
    pass

  def setExpirationDate():
    pass

  def setHttpOnly():
    pass

  def setName():
    pass

  def setPath():
    pass

  def setSecure():
    pass

  def setValue():
    pass

  def toRawForm():
    pass

  def value():
    pass

class QNetworkCookieJar(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def allCookies():
    pass

  def connect():
    pass

  def cookiesForUrl():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def registerUserData():
    pass

  def setAllCookies():
    pass

  def setCookiesFromUrl():
    pass

  staticMetaObject = None

class QNetworkDiskCache(QAbstractNetworkCache):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def cacheDirectory():
    pass

  def cacheSize():
    pass

  def clear():
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

  def expire():
    pass

  def fileMetaData():
    pass

  def insert():
    pass

  def maximumCacheSize():
    pass

  def metaData():
    pass

  def prepare():
    pass

  def registerUserData():
    pass

  def remove():
    pass

  def setCacheDirectory():
    pass

  def setMaximumCacheSize():
    pass

  staticMetaObject = None

  def updateMetaData():
    pass

class QNetworkInterface(Object):

  CanBroadcast = None
  CanMulticast = None

  class InterfaceFlag(object):

    CanBroadcast = None
    CanMulticast = None
    IsLoopBack = None
    IsPointToPoint = None
    IsRunning = None
    IsUp = None
    name = property(None, None, None,
                    )

    values = {}

  class InterfaceFlags(object):

    pass

  IsLoopBack = None
  IsPointToPoint = None
  IsRunning = None
  IsUp = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addressEntries():
    pass

  def allAddresses():
    pass

  def allInterfaces():
    pass

  def flags():
    pass

  def hardwareAddress():
    pass

  def humanReadableName():
    pass

  def index():
    pass

  def interfaceFromIndex():
    pass

  def interfaceFromName():
    pass

  def isValid():
    pass

  def name():
    pass

class QNetworkProxy(Object):

  CachingCapability = None

  class Capabilities(object):

    pass

  class Capability(object):

    CachingCapability = None
    HostNameLookupCapability = None
    ListeningCapability = None
    TunnelingCapability = None
    UdpTunnelingCapability = None
    name = property(None, None, None,
                    )

    values = {}

  DefaultProxy = None
  FtpCachingProxy = None
  HostNameLookupCapability = None
  HttpCachingProxy = None
  HttpProxy = None
  ListeningCapability = None
  NoProxy = None

  class ProxyType(object):

    DefaultProxy = None
    FtpCachingProxy = None
    HttpCachingProxy = None
    HttpProxy = None
    NoProxy = None
    Socks5Proxy = None
    name = property(None, None, None,
                    )

    values = {}

  Socks5Proxy = None
  TunnelingCapability = None
  UdpTunnelingCapability = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def applicationProxy():
    pass

  def capabilities():
    pass

  def hostName():
    pass

  def isCachingProxy():
    pass

  def isTransparentProxy():
    pass

  def password():
    pass

  def port():
    pass

  def setApplicationProxy():
    pass

  def setCapabilities():
    pass

  def setHostName():
    pass

  def setPassword():
    pass

  def setPort():
    pass

  def setType():
    pass

  def setUser():
    pass

  def type():
    pass

  def user():
    pass

class QNetworkProxyFactory(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def proxyForQuery():
    pass

  def queryProxy():
    pass

  def setApplicationProxyFactory():
    pass

  def setUseSystemConfiguration():
    pass

  def systemProxyForQuery():
    pass

class QNetworkProxyQuery(Object):

  class QueryType(object):

    TcpServer = None
    TcpSocket = None
    UdpSocket = None
    UrlRequest = None
    name = property(None, None, None,
                    )

    values = {}

  TcpServer = None
  TcpSocket = None
  UdpSocket = None
  UrlRequest = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def localPort():
    pass

  def networkConfiguration():
    pass

  def peerHostName():
    pass

  def peerPort():
    pass

  def protocolTag():
    pass

  def queryType():
    pass

  def setLocalPort():
    pass

  def setNetworkConfiguration():
    pass

  def setPeerHostName():
    pass

  def setPeerPort():
    pass

  def setProtocolTag():
    pass

  def setQueryType():
    pass

  def setUrl():
    pass

  def url():
    pass

class QNetworkReply(QIODevice):

  Append = None
  AuthenticationRequiredError = None
  ConnectionRefusedError = None
  ContentAccessDenied = None
  ContentNotFoundError = None
  ContentOperationNotPermittedError = None
  ContentReSendError = None
  HostNotFoundError = None

  class NetworkError(object):

    AuthenticationRequiredError = None
    ConnectionRefusedError = None
    ContentAccessDenied = None
    ContentNotFoundError = None
    ContentOperationNotPermittedError = None
    ContentReSendError = None
    HostNotFoundError = None
    NoError = None
    OperationCanceledError = None
    ProtocolFailure = None
    ProtocolInvalidOperationError = None
    ProtocolUnknownError = None
    ProxyAuthenticationRequiredError = None
    ProxyConnectionClosedError = None
    ProxyConnectionRefusedError = None
    ProxyNotFoundError = None
    ProxyTimeoutError = None
    RemoteHostClosedError = None
    SslHandshakeFailedError = None
    TemporaryNetworkFailureError = None
    TimeoutError = None
    UnknownContentError = None
    UnknownNetworkError = None
    UnknownProxyError = None
    name = property(None, None, None,
                    )

    values = {}

  NoError = None
  NotOpen = None
  OperationCanceledError = None
  ProtocolFailure = None
  ProtocolInvalidOperationError = None
  ProtocolUnknownError = None
  ProxyAuthenticationRequiredError = None
  ProxyConnectionClosedError = None
  ProxyConnectionRefusedError = None
  ProxyNotFoundError = None
  ProxyTimeoutError = None
  ReadOnly = None
  ReadWrite = None
  RemoteHostClosedError = None
  SslHandshakeFailedError = None
  TemporaryNetworkFailureError = None
  Text = None
  TimeoutError = None
  Truncate = None
  Unbuffered = None
  UnknownContentError = None
  UnknownNetworkError = None
  UnknownProxyError = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def abort():
    pass

  def aboutToClose():
    """ Signal """
    pass

  def attribute():
    pass

  def bytesWritten():
    """ Signal """
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

  def downloadProgress():
    """ Signal """
    pass

  def error():
    """ Signal """
    pass

  def finished():
    """ Signal """
    pass

  def hasRawHeader():
    pass

  def header():
    pass

  def ignoreSslErrors():
    pass

  def isFinished():
    pass

  def isRunning():
    pass

  def isSequential():
    pass

  def manager():
    pass

  def metaDataChanged():
    """ Signal """
    pass

  def operation():
    pass

  def rawHeader():
    pass

  def rawHeaderList():
    pass

  def rawHeaderPairs():
    pass

  def readBufferSize():
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def request():
    pass

  def setAttribute():
    pass

  def setError():
    pass

  def setFinished():
    pass

  def setHeader():
    pass

  def setOperation():
    pass

  def setRawHeader():
    pass

  def setReadBufferSize():
    pass

  def setRequest():
    pass

  def setSslConfiguration():
    pass

  def setUrl():
    pass

  def sslConfiguration():
    pass

  def sslErrors():
    """ Signal """
    pass

  staticMetaObject = None

  def uploadProgress():
    """ Signal """
    pass

  def url():
    pass

  def writeData():
    pass

class QNetworkRequest(Object):

  AlwaysCache = None
  AlwaysNetwork = None

  class Attribute(object):

    AuthenticationReuseAttribute = None
    CacheLoadControlAttribute = None
    CacheSaveControlAttribute = None
    ConnectionEncryptedAttribute = None
    CookieLoadControlAttribute = None
    CookieSaveControlAttribute = None
    CustomVerbAttribute = None
    DoNotBufferUploadDataAttribute = None
    DownloadBufferAttribute = None
    HttpPipeliningAllowedAttribute = None
    HttpPipeliningWasUsedAttribute = None
    HttpReasonPhraseAttribute = None
    HttpStatusCodeAttribute = None
    MaximumDownloadBufferSizeAttribute = None
    RedirectionTargetAttribute = None
    SourceIsFromCacheAttribute = None
    SynchronousRequestAttribute = None
    User = None
    UserMax = None
    name = property(None, None, None,
                    )

    values = {}

  AuthenticationReuseAttribute = None
  Automatic = None

  class CacheLoadControl(object):

    AlwaysCache = None
    AlwaysNetwork = None
    PreferCache = None
    PreferNetwork = None
    name = property(None, None, None,
                    )

    values = {}

  CacheLoadControlAttribute = None
  CacheSaveControlAttribute = None
  ConnectionEncryptedAttribute = None
  ContentDispositionHeader = None
  ContentLengthHeader = None
  ContentTypeHeader = None
  CookieHeader = None
  CookieLoadControlAttribute = None
  CookieSaveControlAttribute = None
  CustomVerbAttribute = None
  DoNotBufferUploadDataAttribute = None
  DownloadBufferAttribute = None
  HighPriority = None
  HttpPipeliningAllowedAttribute = None
  HttpPipeliningWasUsedAttribute = None
  HttpReasonPhraseAttribute = None
  HttpStatusCodeAttribute = None

  class KnownHeaders(object):

    ContentDispositionHeader = None
    ContentLengthHeader = None
    ContentTypeHeader = None
    CookieHeader = None
    LastModifiedHeader = None
    LocationHeader = None
    SetCookieHeader = None
    name = property(None, None, None,
                    )

    values = {}

  LastModifiedHeader = None

  class LoadControl(object):

    Automatic = None
    Manual = None
    name = property(None, None, None,
                    )

    values = {}

  LocationHeader = None
  LowPriority = None
  Manual = None
  MaximumDownloadBufferSizeAttribute = None
  NormalPriority = None
  PreferCache = None
  PreferNetwork = None

  class Priority(object):

    HighPriority = None
    LowPriority = None
    NormalPriority = None
    name = property(None, None, None,
                    )

    values = {}

  RedirectionTargetAttribute = None
  SetCookieHeader = None
  SourceIsFromCacheAttribute = None
  SynchronousRequestAttribute = None
  User = None
  UserMax = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def attribute():
    pass

  def hasRawHeader():
    pass

  def header():
    pass

  def originatingObject():
    pass

  def priority():
    pass

  def rawHeader():
    pass

  def rawHeaderList():
    pass

  def setAttribute():
    pass

  def setHeader():
    pass

  def setOriginatingObject():
    pass

  def setPriority():
    pass

  def setRawHeader():
    pass

  def setSslConfiguration():
    pass

  def setUrl():
    pass

  def sslConfiguration():
    pass

  def url():
    pass

class QNetworkSession(QObject):

  Closing = None
  Connected = None
  Connecting = None
  Disconnected = None
  Invalid = None
  InvalidConfigurationError = None
  NotAvailable = None
  OperationNotSupportedError = None
  Roaming = None
  RoamingError = None
  SessionAbortedError = None

  class SessionError(object):

    InvalidConfigurationError = None
    OperationNotSupportedError = None
    RoamingError = None
    SessionAbortedError = None
    UnknownSessionError = None
    name = property(None, None, None,
                    )

    values = {}

  class State(object):

    Closing = None
    Connected = None
    Connecting = None
    Disconnected = None
    Invalid = None
    NotAvailable = None
    Roaming = None
    name = property(None, None, None,
                    )

    values = {}

  UnknownSessionError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def accept():
    pass

  def activeTime():
    pass

  def bytesReceived():
    pass

  def bytesWritten():
    pass

  def close():
    pass

  def closed():
    """ Signal """
    pass

  def configuration():
    pass

  def connect():
    pass

  def connectNotify():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def disconnectNotify():
    pass

  def error():
    """ Signal """
    pass

  def errorString():
    pass

  def ignore():
    pass

  def interface():
    pass

  def isOpen():
    pass

  def migrate():
    pass

  def newConfigurationActivated():
    """ Signal """
    pass

  def open():
    pass

  def opened():
    """ Signal """
    pass

  def preferredConfigurationChanged():
    """ Signal """
    pass

  def registerUserData():
    pass

  def reject():
    pass

  def sessionProperty():
    pass

  def setSessionProperty():
    pass

  def state():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def stop():
    pass

  def waitForOpened():
    pass

class QSsl(Object):

  class AlternateNameEntryType(object):

    DnsEntry = None
    EmailEntry = None
    name = property(None, None, None,
                    )

    values = {}

  AnyProtocol = None
  Der = None
  DnsEntry = None
  Dsa = None
  EmailEntry = None

  class EncodingFormat(object):

    Der = None
    Pem = None
    name = property(None, None, None,
                    )

    values = {}

  class KeyAlgorithm(object):

    Dsa = None
    Rsa = None
    name = property(None, None, None,
                    )

    values = {}

  class KeyType(object):

    PrivateKey = None
    PublicKey = None
    name = property(None, None, None,
                    )

    values = {}

  Pem = None
  PrivateKey = None
  PublicKey = None
  Rsa = None
  SecureProtocols = None

  class SslProtocol(object):

    AnyProtocol = None
    SecureProtocols = None
    SslV2 = None
    SslV3 = None
    TlsV1 = None
    TlsV1SslV3 = None
    UnknownProtocol = None
    name = property(None, None, None,
                    )

    values = {}

  SslV2 = None
  SslV3 = None
  TlsV1 = None
  TlsV1SslV3 = None
  UnknownProtocol = None

class QTcpServer(QObject):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addPendingConnection():
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

  def hasPendingConnections():
    pass

  def incomingConnection():
    pass

  def isListening():
    pass

  def listen():
    pass

  def maxPendingConnections():
    pass

  def newConnection():
    """ Signal """
    pass

  def nextPendingConnection():
    pass

  def proxy():
    pass

  def registerUserData():
    pass

  def serverAddress():
    pass

  def serverError():
    pass

  def serverPort():
    pass

  def setMaxPendingConnections():
    pass

  def setProxy():
    pass

  def setSocketDescriptor():
    pass

  def socketDescriptor():
    pass

  staticMetaObject = None

  def waitForNewConnection():
    pass

class QTcpSocket(QAbstractSocket):

  AddressInUseError = None
  Append = None
  BoundState = None
  ClosingState = None
  ConnectedState = None
  ConnectingState = None
  ConnectionRefusedError = None
  DatagramTooLargeError = None
  HostLookupState = None
  HostNotFoundError = None
  IPv4Protocol = None
  IPv6Protocol = None
  KeepAliveOption = None
  ListeningState = None
  LowDelayOption = None
  MulticastLoopbackOption = None
  MulticastTtlOption = None
  NetworkError = None
  NotOpen = None
  ProxyAuthenticationRequiredError = None
  ProxyConnectionClosedError = None
  ProxyConnectionRefusedError = None
  ProxyConnectionTimeoutError = None
  ProxyNotFoundError = None
  ProxyProtocolError = None
  ReadOnly = None
  ReadWrite = None
  RemoteHostClosedError = None
  SocketAccessError = None
  SocketAddressNotAvailableError = None
  SocketResourceError = None
  SocketTimeoutError = None
  SslHandshakeFailedError = None
  TcpSocket = None
  Text = None
  Truncate = None
  UdpSocket = None
  Unbuffered = None
  UnconnectedState = None
  UnfinishedSocketOperationError = None
  UnknownNetworkLayerProtocol = None
  UnknownSocketError = None
  UnknownSocketType = None
  UnsupportedSocketOperationError = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToClose():
    """ Signal """
    pass

  def bytesWritten():
    """ Signal """
    pass

  def connect():
    pass

  def connected():
    """ Signal """
    pass

  def connectionClosed():
    """ Signal """
    pass

  def delayedCloseFinished():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def disconnected():
    """ Signal """
    pass

  def error():
    """ Signal """
    pass

  def hostFound():
    """ Signal """
    pass

  def proxyAuthenticationRequired():
    """ Signal """
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

class QUdpSocket(QAbstractSocket):

  AddressInUseError = None
  Append = None

  class BindFlag(object):

    DefaultForPlatform = None
    DontShareAddress = None
    ReuseAddressHint = None
    ShareAddress = None
    name = property(None, None, None,
                    )

    values = {}

  class BindMode(object):

    pass

  BoundState = None
  ClosingState = None
  ConnectedState = None
  ConnectingState = None
  ConnectionRefusedError = None
  DatagramTooLargeError = None
  DefaultForPlatform = None
  DontShareAddress = None
  HostLookupState = None
  HostNotFoundError = None
  IPv4Protocol = None
  IPv6Protocol = None
  KeepAliveOption = None
  ListeningState = None
  LowDelayOption = None
  MulticastLoopbackOption = None
  MulticastTtlOption = None
  NetworkError = None
  NotOpen = None
  ProxyAuthenticationRequiredError = None
  ProxyConnectionClosedError = None
  ProxyConnectionRefusedError = None
  ProxyConnectionTimeoutError = None
  ProxyNotFoundError = None
  ProxyProtocolError = None
  ReadOnly = None
  ReadWrite = None
  RemoteHostClosedError = None
  ReuseAddressHint = None
  ShareAddress = None
  SocketAccessError = None
  SocketAddressNotAvailableError = None
  SocketResourceError = None
  SocketTimeoutError = None
  SslHandshakeFailedError = None
  TcpSocket = None
  Text = None
  Truncate = None
  UdpSocket = None
  Unbuffered = None
  UnconnectedState = None
  UnfinishedSocketOperationError = None
  UnknownNetworkLayerProtocol = None
  UnknownSocketError = None
  UnknownSocketType = None
  UnsupportedSocketOperationError = None
  WriteOnly = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def aboutToClose():
    """ Signal """
    pass

  def bind():
    pass

  def bytesWritten():
    """ Signal """
    pass

  def connect():
    pass

  def connected():
    """ Signal """
    pass

  def connectionClosed():
    """ Signal """
    pass

  def delayedCloseFinished():
    """ Signal """
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def disconnected():
    """ Signal """
    pass

  def error():
    """ Signal """
    pass

  def hasPendingDatagrams():
    pass

  def hostFound():
    """ Signal """
    pass

  def joinMulticastGroup():
    pass

  def leaveMulticastGroup():
    pass

  def multicastInterface():
    pass

  def pendingDatagramSize():
    pass

  def proxyAuthenticationRequired():
    """ Signal """
    pass

  def readChannelFinished():
    """ Signal """
    pass

  def readDatagram():
    pass

  def readyRead():
    """ Signal """
    pass

  def registerUserData():
    pass

  def setMulticastInterface():
    pass

  def stateChanged():
    """ Signal """
    pass

  staticMetaObject = None

  def writeDatagram():
    pass

__doc__ = None
__name__ = 'Qt.QtNetwork'

