import collections
import copy
from .Utils import _write_complex_object

class MetricData(object):
    """Data contract class for type MetricData."""
    ENVELOPE_TYPE_NAME = 'Microsoft.ApplicationInsights.Metric'
    
    DATA_TYPE_NAME = 'MetricData'
    
    _defaults = collections.OrderedDict([
        ('ver', 2),
        ('metrics', []),
        ('properties', {})
    ])
    
    def __init__(self):
        """Initializes a new instance of the MetricData class."""
        self._values = {
            'ver': 2,
            'metrics': [],
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
    def metrics(self):
        """Gets or sets the metrics property."""
        return self._values['metrics']
        
    @metrics.setter
    def metrics(self, value):
        self._values['metrics'] = value
        
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

