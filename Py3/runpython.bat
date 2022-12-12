@SET PATH=%PATH%;"C:\Python33";C:\Python33\Scripts;C:\Python33\Tools\Scripts
@SET PYTHONPATH=C:\Python33\Lib

@ASSOC .py=Python.File
@ASSOC .pyc=Python.CompiledFile
@ASSOC .pyo=Python.CompiledFile
@ASSOC .pyw=Python.NoConFile

@FTYPE Python.CompiledFile="C:\Python33\python.exe" "%%1" %%*
@FTYPE Python.File="C:\Python33\python.exe" "%%1" %%*
@FTYPE Python.NoConFile="C:\Python33\pythonw.exe" "%%1" %%*
@SET PATHEXT=.py;%PATHEXT%