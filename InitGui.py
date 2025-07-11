#***************************************************************************
#*    Copyright (C) 2023 
#*    This library is free software
#***************************************************************************
import inspect
import os
import sys
import FreeCAD
import FreeCADGui

class steepSlopeCvShowCommand:
    def GetResources(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        return { 
          'Pixmap': os.path.join(module_path, "icons", "steepSlopeCv.svg"),
          'MenuText': "steepSlopeCv",
          'ToolTip': "Show/Hide steepSlopeCv"}

    def IsActive(self):
        import steepSlopeCv
        steepSlopeCv
        return True

    def Activated(self):
        try:
          import steepSlopeCv
          steepSlopeCv.main.d.show()
        except Exception as e:
          FreeCAD.Console.PrintError(str(e) + "\n")

    def IsActive(self):
        import steepSlopeCv
        return not FreeCAD.ActiveDocument is None

class steepSlopeCvWB(FreeCADGui.Workbench):
    def __init__(self):
        file_path = inspect.getfile(inspect.currentframe())
        module_path=os.path.dirname(file_path)
        self.__class__.Icon = os.path.join(module_path, "icons", "steepSlopeCv.svg")
        self.__class__.MenuText = "steepSlopeCv"
        self.__class__.ToolTip = "steepSlopeCv by Pascal"

    def Initialize(self):
        self.commandList = ["steepSlopeCv_Show"]
        self.appendToolbar("&steepSlopeCv", self.commandList)
        self.appendMenu("&steepSlopeCv", self.commandList)

    def Activated(self):
        import steepSlopeCv
        steepSlopeCv
        return

    def Deactivated(self):
        return

    def ContextMenu(self, recipient):
        return

    def GetClassName(self): 
        return "Gui::PythonWorkbench"
    
FreeCADGui.addWorkbench(steepSlopeCvWB())
FreeCADGui.addCommand("steepSlopeCv_Show", steepSlopeCvShowCommand())    
