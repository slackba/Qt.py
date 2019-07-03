# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QSql(Object):

  AfterLastRow = None
  AllTables = None
  BeforeFirstRow = None
  Binary = None
  HighPrecision = None
  In = None
  InOut = None

  class Location(object):

    AfterLastRow = None
    BeforeFirstRow = None
    name = property(None, None, None,
                    )

    values = {}

  LowPrecisionDouble = None
  LowPrecisionInt32 = None
  LowPrecisionInt64 = None

  class NumericalPrecisionPolicy(object):

    HighPrecision = None
    LowPrecisionDouble = None
    LowPrecisionInt32 = None
    LowPrecisionInt64 = None
    name = property(None, None, None,
                    )

    values = {}

  Out = None

  class ParamType(object):

    pass

  class ParamTypeFlag(object):

    Binary = None
    In = None
    InOut = None
    Out = None
    name = property(None, None, None,
                    )

    values = {}

  SystemTables = None

  class TableType(object):

    AllTables = None
    SystemTables = None
    Tables = None
    Views = None
    name = property(None, None, None,
                    )

    values = {}

  Tables = None
  Views = None

class QSqlDatabase(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addDatabase():
    pass

  def cloneDatabase():
    pass

  def close():
    pass

  def commit():
    pass

  def connectOptions():
    pass

  def connectionName():
    pass

  def connectionNames():
    pass

  def contains():
    pass

  def database():
    pass

  def databaseName():
    pass

  defaultConnection = 'qt_sql_default_connection'

  def driver():
    pass

  def driverName():
    pass

  def drivers():
    pass

  def exec_():
    pass

  def hostName():
    pass

  def isDriverAvailable():
    pass

  def isOpen():
    pass

  def isOpenError():
    pass

  def isValid():
    pass

  def lastError():
    pass

  def numericalPrecisionPolicy():
    pass

  def open():
    pass

  def password():
    pass

  def port():
    pass

  def primaryIndex():
    pass

  def record():
    pass

  def registerSqlDriver():
    pass

  def removeDatabase():
    pass

  def rollback():
    pass

  def setConnectOptions():
    pass

  def setDatabaseName():
    pass

  def setHostName():
    pass

  def setNumericalPrecisionPolicy():
    pass

  def setPassword():
    pass

  def setPort():
    pass

  def setUserName():
    pass

  def tables():
    pass

  def transaction():
    pass

  def userName():
    pass

class QSqlDriver(QObject):

  BLOB = None
  BatchOperations = None
  DeleteStatement = None

  class DriverFeature(object):

    BLOB = None
    BatchOperations = None
    EventNotifications = None
    FinishQuery = None
    LastInsertId = None
    LowPrecisionNumbers = None
    MultipleResultSets = None
    NamedPlaceholders = None
    PositionalPlaceholders = None
    PreparedQueries = None
    QuerySize = None
    SimpleLocking = None
    Transactions = None
    Unicode = None
    name = property(None, None, None,
                    )

    values = {}

  EventNotifications = None
  FieldName = None
  FinishQuery = None

  class IdentifierType(object):

    FieldName = None
    TableName = None
    name = property(None, None, None,
                    )

    values = {}

  InsertStatement = None
  LastInsertId = None
  LowPrecisionNumbers = None
  MultipleResultSets = None
  NamedPlaceholders = None
  PositionalPlaceholders = None
  PreparedQueries = None
  QuerySize = None
  SelectStatement = None
  SimpleLocking = None

  class StatementType(object):

    DeleteStatement = None
    InsertStatement = None
    SelectStatement = None
    UpdateStatement = None
    WhereStatement = None
    name = property(None, None, None,
                    )

    values = {}

  TableName = None
  Transactions = None
  Unicode = None
  UpdateStatement = None
  WhereStatement = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def beginTransaction():
    pass

  def close():
    pass

  def commitTransaction():
    pass

  def connect():
    pass

  def createResult():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def escapeIdentifier():
    pass

  def formatValue():
    pass

  def hasFeature():
    pass

  def isIdentifierEscaped():
    pass

  def isIdentifierEscapedImplementation():
    pass

  def isOpen():
    pass

  def isOpenError():
    pass

  def lastError():
    pass

  def notification():
    """ Signal """
    pass

  def numericalPrecisionPolicy():
    pass

  def open():
    pass

  def primaryIndex():
    pass

  def record():
    pass

  def registerUserData():
    pass

  def rollbackTransaction():
    pass

  def setLastError():
    pass

  def setNumericalPrecisionPolicy():
    pass

  def setOpen():
    pass

  def setOpenError():
    pass

  def sqlStatement():
    pass

  staticMetaObject = None

  def stripDelimiters():
    pass

  def stripDelimitersImplementation():
    pass

  def subscribeToNotification():
    pass

  def subscribeToNotificationImplementation():
    pass

  def subscribedToNotifications():
    pass

  def subscribedToNotificationsImplementation():
    pass

  def tables():
    pass

  def unsubscribeFromNotification():
    pass

  def unsubscribeFromNotificationImplementation():
    pass

class QSqlDriverCreatorBase(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def createObject():
    pass

class QSqlError(Object):

  ConnectionError = None

  class ErrorType(object):

    ConnectionError = None
    NoError = None
    StatementError = None
    TransactionError = None
    UnknownError = None
    name = property(None, None, None,
                    )

    values = {}

  NoError = None
  StatementError = None
  TransactionError = None
  UnknownError = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def databaseText():
    pass

  def driverText():
    pass

  def isValid():
    pass

  def number():
    pass

  def setDatabaseText():
    pass

  def setDriverText():
    pass

  def setNumber():
    pass

  def setType():
    pass

  def text():
    pass

  def type():
    pass

class QSqlField(Object):

  Optional = None
  Required = None

  class RequiredStatus(object):

    Optional = None
    Required = None
    Unknown = None
    name = property(None, None, None,
                    )

    values = {}

  Unknown = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def clear():
    pass

  def defaultValue():
    pass

  def isAutoValue():
    pass

  def isGenerated():
    pass

  def isNull():
    pass

  def isReadOnly():
    pass

  def isValid():
    pass

  def length():
    pass

  def name():
    pass

  def precision():
    pass

  def requiredStatus():
    pass

  def setAutoValue():
    pass

  def setDefaultValue():
    pass

  def setGenerated():
    pass

  def setLength():
    pass

  def setName():
    pass

  def setPrecision():
    pass

  def setReadOnly():
    pass

  def setRequired():
    pass

  def setRequiredStatus():
    pass

  def setSqlType():
    pass

  def setType():
    pass

  def setValue():
    pass

  def type():
    pass

  def typeID():
    pass

  def value():
    pass

class QSqlIndex(QSqlRecord):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def cursorName():
    pass

  def isDescending():
    pass

  def name():
    pass

  def setCursorName():
    pass

  def setDescending():
    pass

  def setName():
    pass

class QSqlQuery(Object):

  class BatchExecutionMode(object):

    ValuesAsColumns = None
    ValuesAsRows = None
    name = property(None, None, None,
                    )

    values = {}

  ValuesAsColumns = None
  ValuesAsRows = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addBindValue():
    pass

  def at():
    pass

  def bindValue():
    pass

  def boundValue():
    pass

  def boundValues():
    pass

  def clear():
    pass

  def driver():
    pass

  def execBatch():
    pass

  def exec_():
    pass

  def executedQuery():
    pass

  def finish():
    pass

  def first():
    pass

  def isActive():
    pass

  def isForwardOnly():
    pass

  def isNull():
    pass

  def isSelect():
    pass

  def isValid():
    pass

  def last():
    pass

  def lastError():
    pass

  def lastInsertId():
    pass

  def lastQuery():
    pass

  def next():
    pass

  def nextResult():
    pass

  def numRowsAffected():
    pass

  def numericalPrecisionPolicy():
    pass

  def prepare():
    pass

  def previous():
    pass

  def record():
    pass

  def result():
    pass

  def seek():
    pass

  def setForwardOnly():
    pass

  def setNumericalPrecisionPolicy():
    pass

  def size():
    pass

  def value():
    pass

class QSqlQueryModel(QAbstractTableModel):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def canFetchMore():
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

  def fetchMore():
    pass

  def headerData():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def indexInQuery():
    pass

  def insertColumns():
    pass

  def lastError():
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

  def query():
    pass

  def queryChange():
    pass

  def record():
    pass

  def registerUserData():
    pass

  def removeColumns():
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

  def setHeaderData():
    pass

  def setLastError():
    pass

  def setQuery():
    pass

  staticMetaObject = None

class QSqlRecord(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def append():
    pass

  def clear():
    pass

  def clearValues():
    pass

  def contains():
    pass

  def count():
    pass

  def field():
    pass

  def fieldName():
    pass

  def indexOf():
    pass

  def insert():
    pass

  def isEmpty():
    pass

  def isGenerated():
    pass

  def isNull():
    pass

  def remove():
    pass

  def replace():
    pass

  def setGenerated():
    pass

  def setNull():
    pass

  def setValue():
    pass

  def value():
    pass

class QSqlRelation(Object):

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def displayColumn():
    pass

  def indexColumn():
    pass

  def isValid():
    pass

  def tableName():
    pass

class QSqlRelationalDelegate(QItemDelegate):

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

  def registerUserData():
    pass

  def setEditorData():
    pass

  def setModelData():
    pass

  def sizeHintChanged():
    """ Signal """
    pass

  staticMetaObject = None

class QSqlRelationalTableModel(QSqlTableModel):

  class EditStrategy(object):

    OnFieldChange = None
    OnManualSubmit = None
    OnRowChange = None
    name = property(None, None, None,
                    )

    values = {}

  OnFieldChange = None
  OnManualSubmit = None
  OnRowChange = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def beforeDelete():
    """ Signal """
    pass

  def beforeInsert():
    """ Signal """
    pass

  def beforeUpdate():
    """ Signal """
    pass

  def clear():
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

  def headerDataChanged():
    """ Signal """
    pass

  def insertRowIntoTable():
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

  def orderByClause():
    pass

  def primeInsert():
    """ Signal """
    pass

  def registerUserData():
    pass

  def relation():
    pass

  def relationModel():
    pass

  def removeColumns():
    pass

  def revertRow():
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

  def select():
    pass

  def selectStatement():
    pass

  def setData():
    pass

  def setRelation():
    pass

  def setTable():
    pass

  staticMetaObject = None

  def updateRowInTable():
    pass

class QSqlResult(Object):

  BatchOperation = None

  class BindingSyntax(object):

    NamedBinding = None
    PositionalBinding = None
    name = property(None, None, None,
                    )

    values = {}

  DetachFromResultSet = None
  NamedBinding = None
  NextResult = None
  PositionalBinding = None
  SetNumericalPrecision = None

  class VirtualHookOperation(object):

    BatchOperation = None
    DetachFromResultSet = None
    NextResult = None
    SetNumericalPrecision = None
    name = property(None, None, None,
                    )

    values = {}

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def addBindValue():
    pass

  def at():
    pass

  def bindValue():
    pass

  def bindValueType():
    pass

  def bindingSyntax():
    pass

  def boundValue():
    pass

  def boundValueCount():
    pass

  def boundValueName():
    pass

  def boundValues():
    pass

  def clear():
    pass

  def data():
    pass

  def detachFromResultSet():
    pass

  def driver():
    pass

  def execBatch():
    pass

  def exec_():
    pass

  def executedQuery():
    pass

  def fetch():
    pass

  def fetchFirst():
    pass

  def fetchLast():
    pass

  def fetchNext():
    pass

  def fetchPrevious():
    pass

  def handle():
    pass

  def hasOutValues():
    pass

  def isActive():
    pass

  def isForwardOnly():
    pass

  def isNull():
    pass

  def isSelect():
    pass

  def isValid():
    pass

  def lastError():
    pass

  def lastInsertId():
    pass

  def lastQuery():
    pass

  def nextResult():
    pass

  def numRowsAffected():
    pass

  def numericalPrecisionPolicy():
    pass

  def prepare():
    pass

  def record():
    pass

  def reset():
    pass

  def savePrepare():
    pass

  def setActive():
    pass

  def setAt():
    pass

  def setForwardOnly():
    pass

  def setLastError():
    pass

  def setNumericalPrecisionPolicy():
    pass

  def setQuery():
    pass

  def setSelect():
    pass

  def size():
    pass

class QSqlTableModel(QSqlQueryModel):

  OnFieldChange = None
  OnManualSubmit = None
  OnRowChange = None

  def __init__(self, *args):
    """ x.__init__(...) initializes x; see help(type(x)) for signature """
    pass

  def beforeDelete():
    """ Signal """
    pass

  def beforeInsert():
    """ Signal """
    pass

  def beforeUpdate():
    """ Signal """
    pass

  def clear():
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

  def database():
    pass

  def deleteRowFromTable():
    pass

  def destroyed():
    """ Signal """
    pass

  def disconnect():
    pass

  def editStrategy():
    pass

  def fieldIndex():
    pass

  def filter():
    pass

  def flags():
    pass

  def headerData():
    pass

  def headerDataChanged():
    """ Signal """
    pass

  def indexInQuery():
    pass

  def insertRecord():
    pass

  def insertRowIntoTable():
    pass

  def insertRows():
    pass

  def isDirty():
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

  def orderByClause():
    pass

  def primaryKey():
    pass

  def primeInsert():
    """ Signal """
    pass

  def registerUserData():
    pass

  def removeColumns():
    pass

  def removeRows():
    pass

  def revert():
    pass

  def revertAll():
    pass

  def revertRow():
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

  def select():
    pass

  def selectStatement():
    pass

  def setData():
    pass

  def setEditStrategy():
    pass

  def setFilter():
    pass

  def setPrimaryKey():
    pass

  def setQuery():
    pass

  def setRecord():
    pass

  def setSort():
    pass

  def setTable():
    pass

  def sort():
    pass

  staticMetaObject = None

  def submit():
    pass

  def submitAll():
    pass

  def tableName():
    pass

  def updateRowInTable():
    pass

__doc__ = None
__name__ = 'Qt.QtSql'

