import collections
import copy
from .Utils import _write_complex_object

class PageViewData(object):
    """Data contract class for type PageViewData."""
    ENVELOPE_TYPE_NAME = 'Microsoft.ApplicationInsights.PageView'
    
    DATA_TYPE_NAME = 'PageViewData'
    
    _defaults = collections.OrderedDict([
        ('ver', 2),
        ('url', None),
        ('name', None),
        ('duration', None),
        ('properties', {}),
        ('measurements', {})
    ])
    
    def __init__(self):
        """Initializes a new instance of the PageViewData class."""
        self._values = {
            'ver': 2,
            'name': None,
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
    def url(self):
        """Gets or sets the url property."""
        if 'url' in self._values:
            return self._values['url']
        return self._defaults['url']
        
    @url.setter
    def url(self, value):
        if value == self._defaults['url'] and 'url' in self._values:
            del self._values['url']
        else:
            self._values['url'] = value
        
    @property
    def name(self):
        """Gets or sets the name property."""
        return self._values['name']
        
    @name.setter
    def name(self, value):
        self._values['name'] = value
        
    @property
    def duration(self):
        """Gets or sets the duration property."""
        if 'duration' in self._values:
            return self._values['duration']
        return self._defaults['duration']
        
    @duration.setter
    def duration(self, value):
        if value == self._defaults['duration'] and 'duration' in self._values:
            del self._values['duration']
        else:
            self._values['duration'] = value
        
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

