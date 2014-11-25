import collections
import copy
from .Utils import _write_complex_object

class Data(object):
    """Data contract class for type Data."""
    _defaults = collections.OrderedDict([
        ('baseType', None),
        ('baseData', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the Data class."""
        self._values = {
            'baseData': None
        }
        self._initialize()
        
    @property
    def base_type(self):
        """Gets or sets the base_type property."""
        if 'baseType' in self._values:
            return self._values['baseType']
        return self._defaults['baseType']
        
    @base_type.setter
    def base_type(self, value):
        if value == self._defaults['baseType'] and 'baseType' in self._values:
            del self._values['baseType']
        else:
            self._values['baseType'] = value
        
    @property
    def base_data(self):
        """Gets or sets the base_data property."""
        return self._values['baseData']
        
    @base_data.setter
    def base_data(self, value):
        self._values['baseData'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

