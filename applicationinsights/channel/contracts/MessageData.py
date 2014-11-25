import collections
import copy
from .Utils import _write_complex_object

class MessageData(object):
    """Data contract class for type MessageData."""
    ENVELOPE_TYPE_NAME = 'Microsoft.ApplicationInsights.Message'
    
    DATA_TYPE_NAME = 'MessageData'
    
    _defaults = collections.OrderedDict([
        ('ver', 2),
        ('message', None),
        ('severityLevel', None),
        ('properties', {})
    ])
    
    def __init__(self):
        """Initializes a new instance of the MessageData class."""
        self._values = {
            'ver': 2,
            'message': None,
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
    def message(self):
        """Gets or sets the message property."""
        return self._values['message']
        
    @message.setter
    def message(self, value):
        self._values['message'] = value
        
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
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

