import collections
import copy
from .Utils import _write_complex_object

class StackFrame(object):
    """Data contract class for type StackFrame."""
    _defaults = collections.OrderedDict([
        ('level', None),
        ('method', None),
        ('assembly', None),
        ('fileName', None),
        ('line', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the StackFrame class."""
        self._values = {
            'level': None,
            'method': None,
        }
        self._initialize()
        
    @property
    def level(self):
        """Gets or sets the level property."""
        return self._values['level']
        
    @level.setter
    def level(self, value):
        self._values['level'] = value
        
    @property
    def method(self):
        """Gets or sets the method property."""
        return self._values['method']
        
    @method.setter
    def method(self, value):
        self._values['method'] = value
        
    @property
    def assembly(self):
        """Gets or sets the assembly property."""
        if 'assembly' in self._values:
            return self._values['assembly']
        return self._defaults['assembly']
        
    @assembly.setter
    def assembly(self, value):
        if value == self._defaults['assembly'] and 'assembly' in self._values:
            del self._values['assembly']
        else:
            self._values['assembly'] = value
        
    @property
    def file_name(self):
        """Gets or sets the file_name property."""
        if 'fileName' in self._values:
            return self._values['fileName']
        return self._defaults['fileName']
        
    @file_name.setter
    def file_name(self, value):
        if value == self._defaults['fileName'] and 'fileName' in self._values:
            del self._values['fileName']
        else:
            self._values['fileName'] = value
        
    @property
    def line(self):
        """Gets or sets the line property."""
        if 'line' in self._values:
            return self._values['line']
        return self._defaults['line']
        
    @line.setter
    def line(self, value):
        if value == self._defaults['line'] and 'line' in self._values:
            del self._values['line']
        else:
            self._values['line'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

