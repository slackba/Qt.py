# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QAbstractMessageHandler(QObject):

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

  def handleMessage():
    pass

  def message():
    pass

  def registerUserData():
    pass

  staticMetaObject = None

class QAbstractUriResolver(QObject):

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

  def registerUserData():
    pass

  def resolve():
    pass

  staticMetaObject = None

class QAbstractXmlNodeModel(Object):

  FirstChild = None
  InheritNamespaces = None
  NextSibling = None

  class NodeCopySetting(object):

    InheritNamespaces = None
    PreserveNamespaces = None
    name = property(None, None, None,
                    )

    values = {}

  Parent = None
  PreserveNamespaces = None
  PreviousSibling = None

  class SimpleAxis(object):

    FirstChild = None
    NextSibling = None
    Parent = None
    PreviousSibling = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def attributes():
    pass

  def baseUri():
    pass

  def compareOrder():
    pass

  def createIndex():
    pass

  def documentUri():
    pass

  def elementById():
    pass

  def isDeepEqual():
    pass

  def kind():
    pass

  def name():
    pass

  def namespaceBindings():
    pass

  def namespaceForPrefix():
    pass

  def nextFromSimpleAxis():
    pass

  def nodesByIdref():
    pass

  def root():
    pass

  def sendNamespaces():
    pass

  def sourceLocation():
    pass

  def stringValue():
    pass

  def typedValue():
    pass

class QAbstractXmlReceiver(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def atomicValue():
    pass

  def attribute():
    pass

  def characters():
    pass

  def comment():
    pass

  def endDocument():
    pass

  def endElement():
    pass

  def endOfSequence():
    pass

  def namespaceBinding():
    pass

  def processingInstruction():
    pass

  def startDocument():
    pass

  def startElement():
    pass

  def startOfSequence():
    pass

  def whitespaceOnly():
    pass

class QSourceLocation(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def column():
    pass

  def isNull():
    pass

  def line():
    pass

  def setColumn():
    pass

  def setLine():
    pass

  def setUri():
    pass

  def uri():
    pass

class QXmlFormatter(QXmlSerializer):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def atomicValue():
    pass

  def attribute():
    pass

  def characters():
    pass

  def comment():
    pass

  def endDocument():
    pass

  def endElement():
    pass

  def endOfSequence():
    pass

  def indentationDepth():
    pass

  def processingInstruction():
    pass

  def setIndentationDepth():
    pass

  def startDocument():
    pass

  def startElement():
    pass

  def startOfSequence():
    pass

class QXmlItem(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def isAtomicValue():
    pass

  def isNode():
    pass

  def isNull():
    pass

  def toAtomicValue():
    pass

  def toNodeModelIndex():
    pass

class QXmlName(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def fromClarkName():
    pass

  def isNCName():
    pass

  def isNull():
    pass

  def localName():
    pass

  def namespaceUri():
    pass

  def prefix():
    pass

  def toClarkName():
    pass

class QXmlNamePool(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

class QXmlNodeModelIndex(Object):

  Attribute = None
  Comment = None
  Document = None

  class DocumentOrder(object):

    Follows = None
    Is = None
    Precedes = None
    name = property(None, None, None,
                    )

    values = {}

  Element = None
  Follows = None
  Is = None
  Namespace = None

  class NodeKind(object):

    Attribute = None
    Comment = None
    Document = None
    Element = None
    Namespace = None
    ProcessingInstruction = None
    Text = None
    name = property(None, None, None,
                    )

    values = {}

  Precedes = None
  ProcessingInstruction = None
  Text = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def additionalData():
    pass

  def data():
    pass

  def internalPointer():
    pass

  def isNull():
    pass

  def model():
    pass

class QXmlQuery(Object):

  class QueryLanguage(object):

    XPath20 = None
    XQuery10 = None
    XSLT20 = None
    XmlSchema11IdentityConstraintField = None
    XmlSchema11IdentityConstraintSelector = None
    name = property(None, None, None,
                    )

    values = {}

  XPath20 = None
  XQuery10 = None
  XSLT20 = None
  XmlSchema11IdentityConstraintField = None
  XmlSchema11IdentityConstraintSelector = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def bindVariable():
    pass

  def evaluateTo():
    pass

  def initialTemplateName():
    pass

  def isValid():
    pass

  def messageHandler():
    pass

  def namePool():
    pass

  def queryLanguage():
    pass

  def setFocus():
    pass

  def setInitialTemplateName():
    pass

  def setMessageHandler():
    pass

  def setQuery():
    pass

  def setUriResolver():
    pass

  def uriResolver():
    pass

class QXmlResultItems(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def current():
    pass

  def hasError():
    pass

  def next():
    pass

class QXmlSchema(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def documentUri():
    pass

  def isValid():
    pass

  def load():
    pass

  def messageHandler():
    pass

  def namePool():
    pass

  def setMessageHandler():
    pass

  def setUriResolver():
    pass

  def uriResolver():
    pass

class QXmlSchemaValidator(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def messageHandler():
    pass

  def namePool():
    pass

  def schema():
    pass

  def setMessageHandler():
    pass

  def setSchema():
    pass

  def setUriResolver():
    pass

  def uriResolver():
    pass

  def validate():
    pass

class QXmlSerializer(QAbstractXmlReceiver):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def atomicValue():
    pass

  def attribute():
    pass

  def characters():
    pass

  def codec():
    pass

  def comment():
    pass

  def endDocument():
    pass

  def endElement():
    pass

  def endOfSequence():
    pass

  def namespaceBinding():
    pass

  def outputDevice():
    pass

  def processingInstruction():
    pass

  def setCodec():
    pass

  def startDocument():
    pass

  def startElement():
    pass

  def startOfSequence():
    pass

__doc__ = None
__name__ = 'Qt.QtXmlPatterns'

