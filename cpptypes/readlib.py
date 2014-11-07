import ctypes
import subprocess


def read_names(lib):
    path = subprocess.check_output('ldconfig -p | grep %s' % lib._name, shell=True)
    path = path.split('\n')[0]
    path = path.split(' => ')[1]
    
    names = []
    for line in subprocess.check_output('nm -D %s' % path, shell=True).split('\n'):
        vals = line.split(' ')
        if len(vals) != 3:
            continue
        addr, typ, name = vals
        if typ == 'T':
            names.append(name)
            
    return names
    