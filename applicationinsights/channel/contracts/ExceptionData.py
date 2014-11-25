import collections
import copy
from .Utils import _write_complex_object

class ExceptionData(object):
    """Data contract class for type ExceptionData."""
    ENVELOPE_TYPE_NAME = 'Microsoft.ApplicationInsights.Exception'
    
    DATA_TYPE_NAME = 'ExceptionData'
    
    _defaults = collections.OrderedDict([
        ('ver', 2),
        ('handledAt', None),
        ('exceptions', []),
        ('severityLevel', None),
        ('properties', {}),
        ('measurements', {})
    ])
    
    def __init__(self):
        """Initializes a new instance of the ExceptionData class."""
        self._values = {
            'ver': 2,
            'handledAt': None,
            'exceptions': [],
        }
        self._initialize()
        
    @property
    def ver(self):
        """Gets or sets the ver property."""
        return self._values['ver']
        
    @ver.setter
    def ver(self, value):
        self._values['ver'] = value
        
    @property
    def handled_at(self):
        """Gets or sets the handled_at property."""
        return self._values['handledAt']
        
    @handled_at.setter
    def handled_at(self, value):
        self._values['handledAt'] = value
        
    @property
    def exceptions(self):
        """Gets or sets the exceptions property."""
        return self._values['exceptions']
        
    @exceptions.setter
    def exceptions(self, value):
        self._values['exceptions'] = value
        
    @property
    def severity_level(self):
        """Gets or sets the severity_level property."""
        if 'severityLevel' in self._values:
            return self._values['severityLevel']
        return self._defaults['severityLevel']
        
    @severity_level.setter
    def severity_level(self, value):
        if value == self._defaults['severityLevel'] and 'severityLevel' in self._values:
            del self._values['severityLevel']
        else:
            self._values['severityLevel'] = value
        
    @property
    def properties(self):
        """Gets or sets the properties property."""
        if 'properties' in self._values:
            return self._values['properties']
        self._values['properties'] = copy.deepcopy(self._defaults['properties'])
        return self._values['properties']
        
    @properties.setter
    def properties(self, value):
        if value == self._defaults['properties'] and 'properties' in self._values:
            del self._values['properties']
        else:
            self._values['properties'] = value
        
    @property
    def measurements(self):
        """Gets or sets the measurements property."""
        if 'measurements' in self._values:
            return self._values['measurements']
        self._values['measurements'] = copy.deepcopy(self._defaults['measurements'])
        return self._values['measurements']
        
    @measurements.setter
    def measurements(self, value):
        if value == self._defaults['measurements'] and 'measurements' in self._values:
            del self._values['measurements']
        else:
            self._values['measurements'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

