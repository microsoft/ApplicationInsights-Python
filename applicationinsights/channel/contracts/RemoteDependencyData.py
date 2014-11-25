import collections
import copy
from .Utils import _write_complex_object
from .DataPointType import DataPointType
from .DependencyKind import DependencyKind
from .DependencySourceType import DependencySourceType

class RemoteDependencyData(object):
    """Data contract class for type RemoteDependencyData."""
    ENVELOPE_TYPE_NAME = 'Microsoft.ApplicationInsights.RemoteDependency'
    
    DATA_TYPE_NAME = 'RemoteDependencyData'
    
    _defaults = collections.OrderedDict([
        ('ver', 2),
        ('name', None),
        ('kind', DataPointType.measurement),
        ('value', None),
        ('count', None),
        ('min', None),
        ('max', None),
        ('stdDev', None),
        ('dependencyKind', DependencyKind.undefined),
        ('success', True),
        ('async', None),
        ('dependencySource', DependencySourceType.undefined),
        ('properties', {})
    ])
    
    def __init__(self):
        """Initializes a new instance of the RemoteDependencyData class."""
        self._values = {
            'ver': 2,
            'name': None,
            'kind': DataPointType.measurement,
            'value': None,
            'dependencyKind': DependencyKind.undefined,
            'success': True,
            'dependencySource': DependencySourceType.undefined,
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
        
    @property
    def dependency_kind(self):
        """Gets or sets the dependency_kind property."""
        return self._values['dependencyKind']
        
    @dependency_kind.setter
    def dependency_kind(self, value):
        self._values['dependencyKind'] = value
        
    @property
    def success(self):
        """Gets or sets the success property."""
        if 'success' in self._values:
            return self._values['success']
        return self._defaults['success']
        
    @success.setter
    def success(self, value):
        if value == self._defaults['success'] and 'success' in self._values:
            del self._values['success']
        else:
            self._values['success'] = value
        
    @property
    def async(self):
        """Gets or sets the async property."""
        if 'async' in self._values:
            return self._values['async']
        return self._defaults['async']
        
    @async.setter
    def async(self, value):
        if value == self._defaults['async'] and 'async' in self._values:
            del self._values['async']
        else:
            self._values['async'] = value
        
    @property
    def dependency_source(self):
        """Gets or sets the dependency_source property."""
        if 'dependencySource' in self._values:
            return self._values['dependencySource']
        return self._defaults['dependencySource']
        
    @dependency_source.setter
    def dependency_source(self, value):
        if value == self._defaults['dependencySource'] and 'dependencySource' in self._values:
            del self._values['dependencySource']
        else:
            self._values['dependencySource'] = value
        
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

