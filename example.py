from cpptypes import readlib
import ctypes

lib = ctypes.cdll.LoadLibrary('libQtCore.so.4')
print readlib.read_names(lib)
