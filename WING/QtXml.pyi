# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QDomAttr(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None

  class EncodingPolicy(object):

    EncodingFromDocument = None
    EncodingFromTextStream = None
    name = property(None, None, None,
                    )

    values = {}

  EntityNode = None
  EntityReferenceNode = None

  class NodeType(object):

    AttributeNode = None
    BaseNode = None
    CDATASectionNode = None
    CharacterDataNode = None
    CommentNode = None
    DocumentFragmentNode = None
    DocumentNode = None
    DocumentTypeNode = None
    ElementNode = None
    EntityNode = None
    EntityReferenceNode = None
    NotationNode = None
    ProcessingInstructionNode = None
    TextNode = None
    name = property(None, None, None,
                    )

    values = {}

  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def name():
    pass

  def nodeType():
    pass

  def ownerElement():
    pass

  def setValue():
    pass

  def specified():
    pass

  def value():
    pass

class QDomCDATASection(QDomText):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def nodeType():
    pass

class QDomCharacterData(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def appendData():
    pass

  def data():
    pass

  def deleteData():
    pass

  def insertData():
    pass

  def length():
    pass

  def nodeType():
    pass

  def replaceData():
    pass

  def setData():
    pass

  def substringData():
    pass

class QDomComment(QDomCharacterData):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def nodeType():
    pass

class QDomDocument(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def createAttribute():
    pass

  def createAttributeNS():
    pass

  def createCDATASection():
    pass

  def createComment():
    pass

  def createDocumentFragment():
    pass

  def createElement():
    pass

  def createElementNS():
    pass

  def createEntityReference():
    pass

  def createProcessingInstruction():
    pass

  def createTextNode():
    pass

  def doctype():
    pass

  def documentElement():
    pass

  def elementById():
    pass

  def elementsByTagName():
    pass

  def elementsByTagNameNS():
    pass

  def implementation():
    pass

  def importNode():
    pass

  def nodeType():
    pass

  def setContent():
    pass

  def toByteArray():
    pass

  def toString():
    pass

class QDomDocumentFragment(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def nodeType():
    pass

class QDomDocumentType(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def entities():
    pass

  def internalSubset():
    pass

  def name():
    pass

  def nodeType():
    pass

  def notations():
    pass

  def publicId():
    pass

  def systemId():
    pass

class QDomElement(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def attribute():
    pass

  def attributeNS():
    pass

  def attributeNode():
    pass

  def attributeNodeNS():
    pass

  def attributes():
    pass

  def elementsByTagName():
    pass

  def elementsByTagNameNS():
    pass

  def hasAttribute():
    pass

  def hasAttributeNS():
    pass

  def nodeType():
    pass

  def removeAttribute():
    pass

  def removeAttributeNS():
    pass

  def removeAttributeNode():
    pass

  def setAttribute():
    pass

  def setAttributeNS():
    pass

  def setAttributeNode():
    pass

  def setAttributeNodeNS():
    pass

  def setTagName():
    pass

  def tagName():
    pass

  def text():
    pass

class QDomEntity(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def nodeType():
    pass

  def notationName():
    pass

  def publicId():
    pass

  def systemId():
    pass

class QDomEntityReference(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def nodeType():
    pass

class QDomImplementation(Object):

  AcceptInvalidChars = None
  DropInvalidChars = None

  class InvalidDataPolicy(object):

    AcceptInvalidChars = None
    DropInvalidChars = None
    ReturnNullNode = None
    name = property(None, None, None,
                    )

    values = {}

  ReturnNullNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def createDocument():
    pass

  def createDocumentType():
    pass

  def hasFeature():
    pass

  def invalidDataPolicy():
    pass

  def isNull():
    pass

  def setInvalidDataPolicy():
    pass

class QDomNamedNodeMap(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def contains():
    pass

  def count():
    pass

  def isEmpty():
    pass

  def item():
    pass

  def length():
    pass

  def namedItem():
    pass

  def namedItemNS():
    pass

  def removeNamedItem():
    pass

  def removeNamedItemNS():
    pass

  def setNamedItem():
    pass

  def setNamedItemNS():
    pass

  def size():
    pass

class QDomNode(Object):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def appendChild():
    pass

  def attributes():
    pass

  def childNodes():
    pass

  def clear():
    pass

  def cloneNode():
    pass

  def columnNumber():
    pass

  def firstChild():
    pass

  def firstChildElement():
    pass

  def hasAttributes():
    pass

  def hasChildNodes():
    pass

  def insertAfter():
    pass

  def insertBefore():
    pass

  def isAttr():
    pass

  def isCDATASection():
    pass

  def isCharacterData():
    pass

  def isComment():
    pass

  def isDocument():
    pass

  def isDocumentFragment():
    pass

  def isDocumentType():
    pass

  def isElement():
    pass

  def isEntity():
    pass

  def isEntityReference():
    pass

  def isNotation():
    pass

  def isNull():
    pass

  def isProcessingInstruction():
    pass

  def isSupported():
    pass

  def isText():
    pass

  def lastChild():
    pass

  def lastChildElement():
    pass

  def lineNumber():
    pass

  def localName():
    pass

  def namedItem():
    pass

  def namespaceURI():
    pass

  def nextSibling():
    pass

  def nextSiblingElement():
    pass

  def nodeName():
    pass

  def nodeType():
    pass

  def nodeValue():
    pass

  def normalize():
    pass

  def ownerDocument():
    pass

  def parentNode():
    pass

  def prefix():
    pass

  def previousSibling():
    pass

  def previousSiblingElement():
    pass

  def removeChild():
    pass

  def replaceChild():
    pass

  def save():
    pass

  def setNodeValue():
    pass

  def setPrefix():
    pass

  def toAttr():
    pass

  def toCDATASection():
    pass

  def toCharacterData():
    pass

  def toComment():
    pass

  def toDocument():
    pass

  def toDocumentFragment():
    pass

  def toDocumentType():
    pass

  def toElement():
    pass

  def toEntity():
    pass

  def toEntityReference():
    pass

  def toNotation():
    pass

  def toProcessingInstruction():
    pass

  def toText():
    pass

class QDomNodeList(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def at():
    pass

  def count():
    pass

  def isEmpty():
    pass

  def item():
    pass

  def length():
    pass

  def size():
    pass

class QDomNotation(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def nodeType():
    pass

  def publicId():
    pass

  def systemId():
    pass

class QDomProcessingInstruction(QDomNode):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def nodeType():
    pass

  def setData():
    pass

  def target():
    pass

class QDomText(QDomCharacterData):

  AttributeNode = None
  BaseNode = None
  CDATASectionNode = None
  CharacterDataNode = None
  CommentNode = None
  DocumentFragmentNode = None
  DocumentNode = None
  DocumentTypeNode = None
  ElementNode = None
  EncodingFromDocument = None
  EncodingFromTextStream = None
  EntityNode = None
  EntityReferenceNode = None
  NotationNode = None
  ProcessingInstructionNode = None
  TextNode = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def nodeType():
    pass

  def splitText():
    pass

class QXmlAttributes(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def clear():
    pass

  def count():
    pass

  def index():
    pass

  def length():
    pass

  def localName():
    pass

  def qName():
    pass

  def type():
    pass

  def uri():
    pass

  def value():
    pass

class QXmlContentHandler(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def characters():
    pass

  def endDocument():
    pass

  def endElement():
    pass

  def endPrefixMapping():
    pass

  def errorString():
    pass

  def ignorableWhitespace():
    pass

  def processingInstruction():
    pass

  def setDocumentLocator():
    pass

  def skippedEntity():
    pass

  def startDocument():
    pass

  def startElement():
    pass

  def startPrefixMapping():
    pass

class QXmlDTDHandler(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def errorString():
    pass

  def notationDecl():
    pass

  def unparsedEntityDecl():
    pass

class QXmlDeclHandler(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def attributeDecl():
    pass

  def errorString():
    pass

  def externalEntityDecl():
    pass

  def internalEntityDecl():
    pass

class QXmlDefaultHandler(QXmlContentHandler):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def attributeDecl():
    pass

  def characters():
    pass

  def comment():
    pass

  def endCDATA():
    pass

  def endDTD():
    pass

  def endDocument():
    pass

  def endElement():
    pass

  def endEntity():
    pass

  def endPrefixMapping():
    pass

  def error():
    pass

  def errorString():
    pass

  def externalEntityDecl():
    pass

  def fatalError():
    pass

  def ignorableWhitespace():
    pass

  def internalEntityDecl():
    pass

  def notationDecl():
    pass

  def processingInstruction():
    pass

  def resolveEntity():
    pass

  def setDocumentLocator():
    pass

  def skippedEntity():
    pass

  def startCDATA():
    pass

  def startDTD():
    pass

  def startDocument():
    pass

  def startElement():
    pass

  def startEntity():
    pass

  def startPrefixMapping():
    pass

  def unparsedEntityDecl():
    pass

  def warning():
    pass

class QXmlEntityResolver(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def errorString():
    pass

  def resolveEntity():
    pass

class QXmlErrorHandler(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def error():
    pass

  def errorString():
    pass

  def fatalError():
    pass

  def warning():
    pass

class QXmlInputSource(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def data():
    pass

  def fetchData():
    pass

  def fromRawData():
    pass

  def next():
    pass

  def reset():
    pass

  def setData():
    pass

class QXmlLexicalHandler(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def comment():
    pass

  def endCDATA():
    pass

  def endDTD():
    pass

  def endEntity():
    pass

  def errorString():
    pass

  def startCDATA():
    pass

  def startDTD():
    pass

  def startEntity():
    pass

class QXmlLocator(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def columnNumber():
    pass

  def lineNumber():
    pass

class QXmlNamespaceSupport(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def popContext():
    pass

  def prefix():
    pass

  def prefixes():
    pass

  def processName():
    pass

  def pushContext():
    pass

  def reset():
    pass

  def setPrefix():
    pass

  def splitName():
    pass

  def uri():
    pass

class QXmlParseException(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def columnNumber():
    pass

  def lineNumber():
    pass

  def message():
    pass

  def publicId():
    pass

  def systemId():
    pass

class QXmlReader(Object):

  def DTDHandler():
    pass

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def contentHandler():
    pass

  def declHandler():
    pass

  def entityResolver():
    pass

  def errorHandler():
    pass

  def feature():
    pass

  def hasFeature():
    pass

  def hasProperty():
    pass

  def lexicalHandler():
    pass

  def parse():
    pass

  def property():
    pass

  def setContentHandler():
    pass

  def setDTDHandler():
    pass

  def setDeclHandler():
    pass

  def setEntityResolver():
    pass

  def setErrorHandler():
    pass

  def setFeature():
    pass

  def setLexicalHandler():
    pass

  def setProperty():
    pass

class QXmlSimpleReader(QXmlReader):

  def DTDHandler():
    pass

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def contentHandler():
    pass

  def declHandler():
    pass

  def entityResolver():
    pass

  def errorHandler():
    pass

  def feature():
    pass

  def hasFeature():
    pass

  def hasProperty():
    pass

  def lexicalHandler():
    pass

  def parse():
    pass

  def parseContinue():
    pass

  def property():
    pass

  def setContentHandler():
    pass

  def setDTDHandler():
    pass

  def setDeclHandler():
    pass

  def setEntityResolver():
    pass

  def setErrorHandler():
    pass

  def setFeature():
    pass

  def setLexicalHandler():
    pass

  def setProperty():
    pass

__doc__ = None
__name__ = 'Qt.QtXml'

