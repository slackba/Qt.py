# coding: utf-8
# AUTO-GENERATED FILE -- DO NOT EDIT


class QTest(Object):

  AI_Description = None
  AI_Errors = None
  AI_Failures = None
  AI_File = None
  AI_Iterations = None
  AI_Line = None
  AI_Metric = None
  AI_Name = None
  AI_PropertyValue = None
  AI_QTestVersion = None
  AI_QtVersion = None
  AI_Result = None
  AI_Tag = None
  AI_Tests = None
  AI_Type = None
  AI_Undefined = None
  AI_Value = None
  Abort = None

  class AttributeIndex(object):

    AI_Description = None
    AI_Errors = None
    AI_Failures = None
    AI_File = None
    AI_Iterations = None
    AI_Line = None
    AI_Metric = None
    AI_Name = None
    AI_PropertyValue = None
    AI_QTestVersion = None
    AI_QtVersion = None
    AI_Result = None
    AI_Tag = None
    AI_Tests = None
    AI_Type = None
    AI_Undefined = None
    AI_Value = None
    name = property(None, None, None,
                    )

    values = {}

  BitsPerSecond = None
  BytesPerSecond = None
  CPUTicks = None
  Click = None
  Continue = None
  Events = None
  FramesPerSecond = None
  InstructionReads = None

  class KeyAction(object):

    Click = None
    Press = None
    Release = None
    name = property(None, None, None,
                    )

    values = {}

  LET_Benchmark = None
  LET_Error = None
  LET_Failure = None
  LET_Properties = None
  LET_Property = None
  LET_SystemError = None
  LET_TestCase = None
  LET_TestSuite = None
  LET_Undefined = None

  class LogElementType(object):

    LET_Benchmark = None
    LET_Error = None
    LET_Failure = None
    LET_Properties = None
    LET_Property = None
    LET_SystemError = None
    LET_TestCase = None
    LET_TestSuite = None
    LET_Undefined = None
    name = property(None, None, None,
                    )

    values = {}

  class MouseAction(object):

    MouseClick = None
    MouseDClick = None
    MouseMove = None
    MousePress = None
    MouseRelease = None
    name = property(None, None, None,
                    )

    values = {}

  MouseClick = None
  MouseDClick = None
  MouseMove = None
  MousePress = None
  MouseRelease = None
  Press = None

  class QBenchmarkMetric(object):

    BitsPerSecond = None
    BytesPerSecond = None
    CPUTicks = None
    Events = None
    FramesPerSecond = None
    InstructionReads = None
    WalltimeMilliseconds = None
    name = property(None, None, None,
                    )

    values = {}

  class QTouchEventSequence(Object):

    def commit():
      pass

    def move():
      pass

    def press():
      pass

    def release():
      pass

    def stationary():
      pass

  Release = None
  SkipAll = None

  class SkipMode(object):

    SkipAll = None
    SkipSingle = None
    name = property(None, None, None,
                    )

    values = {}

  SkipSingle = None

  class TestFailMode(object):

    Abort = None
    Continue = None
    name = property(None, None, None,
                    )

    values = {}

  WalltimeMilliseconds = None

  def addColumnInternal():
    pass

  def asciiToKey():
    pass

  def compare_ptr_helper():
    pass

  def compare_string_helper():
    pass

  def currentDataTag():
    pass

  def currentTestFailed():
    pass

  def currentTestFunction():
    pass

  def ignoreMessage():
    pass

  def keyClick():
    pass

  def keyClicks():
    pass

  def keyEvent():
    pass

  def keyPress():
    pass

  def keyRelease():
    pass

  def keyToAscii():
    pass

  def mouseClick():
    pass

  def mouseDClick():
    pass

  def mouseEvent():
    pass

  def mouseMove():
    pass

  def mousePress():
    pass

  def mouseRelease():
    pass

  def qElementData():
    pass

  def qExpectFail():
    pass

  def qGlobalData():
    pass

  def qSkip():
    pass

  def qWaitForWindowShown():
    pass

  def sendKeyEvent():
    pass

  def setBenchmarkResult():
    pass

  def simulateEvent():
    pass

  def testObject():
    pass

  def touchEvent():
    pass

__doc__ = None
__name__ = 'Qt.QtTest'

