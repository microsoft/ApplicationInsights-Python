import collections
import copy
from .Utils import _write_complex_object
from .DataPointType import DataPointType

class DataPoint(object):
    """Data contract class for type DataPoint."""
    _defaults = collections.OrderedDict([
        ('name', None),
        ('kind', DataPointType.measurement),
        ('value', None),
        ('count', None),
        ('min', None),
        ('max', None),
        ('stdDev', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the DataPoint class."""
        self._values = {
            'name': None,
            'kind': DataPointType.measurement,
            'value': None,
        }
        self._initialize()
        
    @property
    def name(self):
        """Gets or sets the name property."""
        return self._values['name']
        
    @name.setter
    def name(self, value):
        self._values['name'] = value
        
    @property
    def kind(self):
        """Gets or sets the kind property."""
        if 'kind' in self._values:
            return self._values['kind']
        return self._defaults['kind']
        
    @kind.setter
    def kind(self, value):
        if value == self._defaults['kind'] and 'kind' in self._values:
            del self._values['kind']
        else:
            self._values['kind'] = value
        
    @property
    def value(self):
        """Gets or sets the value property."""
        return self._values['value']
        
    @value.setter
    def value(self, value):
        self._values['value'] = value
        
    @property
    def count(self):
        """Gets or sets the count property."""
        if 'count' in self._values:
            return self._values['count']
        return self._defaults['count']
        
    @count.setter
    def count(self, value):
        if value == self._defaults['count'] and 'count' in self._values:
            del self._values['count']
        else:
            self._values['count'] = value
        
    @property
    def min(self):
        """Gets or sets the min property."""
        if 'min' in self._values:
            return self._values['min']
        return self._defaults['min']
        
    @min.setter
    def min(self, value):
        if value == self._defaults['min'] and 'min' in self._values:
            del self._values['min']
        else:
            self._values['min'] = value
        
    @property
    def max(self):
        """Gets or sets the max property."""
        if 'max' in self._values:
            return self._values['max']
        return self._defaults['max']
        
    @max.setter
    def max(self, value):
        if value == self._defaults['max'] and 'max' in self._values:
            del self._values['max']
        else:
            self._values['max'] = value
        
    @property
    def std_dev(self):
        """Gets or sets the std_dev property."""
        if 'stdDev' in self._values:
            return self._values['stdDev']
        return self._defaults['stdDev']
        
    @std_dev.setter
    def std_dev(self, value):
        if value == self._defaults['stdDev'] and 'stdDev' in self._values:
            del self._values['stdDev']
        else:
            self._values['stdDev'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

