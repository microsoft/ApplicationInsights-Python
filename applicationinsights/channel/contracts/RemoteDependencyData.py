import collections
import copy
from .Utils import _write_complex_object
from .DataPointType import DataPointType
from .DependencyKind import DependencyKind
from .DependencySourceType import DependencySourceType

class RemoteDependencyData(object):
    """Data contract class for type RemoteDependencyData.
    """
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
        """Initializes a new instance of the class.
        """
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
        """The ver property.
        
        Returns:
            (int). the property value. (defaults to: 2)
        """
        return self._values['ver']
        
    @ver.setter
    def ver(self, value):
        """The ver property.
        
        Args:
            value (int). the property value.
        """
        self._values['ver'] = value
        
    @property
    def name(self):
        """The name property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        return self._values['name']
        
    @name.setter
    def name(self, value):
        """The name property.
        
        Args:
            value (string). the property value.
        """
        self._values['name'] = value
        
    @property
    def kind(self):
        """The kind property.
        
        Returns:
            (:class:`DataPointType.measurement`). the property value. (defaults to: DataPointType.measurement)
        """
        if 'kind' in self._values:
            return self._values['kind']
        return self._defaults['kind']
        
    @kind.setter
    def kind(self, value):
        """The kind property.
        
        Args:
            value (:class:`DataPointType.measurement`). the property value.
        """
        if value == self._defaults['kind'] and 'kind' in self._values:
            del self._values['kind']
        else:
            self._values['kind'] = value
        
    @property
    def value(self):
        """The value property.
        
        Returns:
            (float). the property value. (defaults to: None)
        """
        return self._values['value']
        
    @value.setter
    def value(self, value):
        """The value property.
        
        Args:
            value (float). the property value.
        """
        self._values['value'] = value
        
    @property
    def count(self):
        """The count property.
        
        Returns:
            (int). the property value. (defaults to: None)
        """
        if 'count' in self._values:
            return self._values['count']
        return self._defaults['count']
        
    @count.setter
    def count(self, value):
        """The count property.
        
        Args:
            value (int). the property value.
        """
        if value == self._defaults['count'] and 'count' in self._values:
            del self._values['count']
        else:
            self._values['count'] = value
        
    @property
    def min(self):
        """The min property.
        
        Returns:
            (float). the property value. (defaults to: None)
        """
        if 'min' in self._values:
            return self._values['min']
        return self._defaults['min']
        
    @min.setter
    def min(self, value):
        """The min property.
        
        Args:
            value (float). the property value.
        """
        if value == self._defaults['min'] and 'min' in self._values:
            del self._values['min']
        else:
            self._values['min'] = value
        
    @property
    def max(self):
        """The max property.
        
        Returns:
            (float). the property value. (defaults to: None)
        """
        if 'max' in self._values:
            return self._values['max']
        return self._defaults['max']
        
    @max.setter
    def max(self, value):
        """The max property.
        
        Args:
            value (float). the property value.
        """
        if value == self._defaults['max'] and 'max' in self._values:
            del self._values['max']
        else:
            self._values['max'] = value
        
    @property
    def std_dev(self):
        """The std_dev property.
        
        Returns:
            (float). the property value. (defaults to: None)
        """
        if 'stdDev' in self._values:
            return self._values['stdDev']
        return self._defaults['stdDev']
        
    @std_dev.setter
    def std_dev(self, value):
        """The std_dev property.
        
        Args:
            value (float). the property value.
        """
        if value == self._defaults['stdDev'] and 'stdDev' in self._values:
            del self._values['stdDev']
        else:
            self._values['stdDev'] = value
        
    @property
    def dependency_kind(self):
        """The dependency_kind property.
        
        Returns:
            (:class:`DependencyKind.undefined`). the property value. (defaults to: DependencyKind.undefined)
        """
        return self._values['dependencyKind']
        
    @dependency_kind.setter
    def dependency_kind(self, value):
        """The dependency_kind property.
        
        Args:
            value (:class:`DependencyKind.undefined`). the property value.
        """
        self._values['dependencyKind'] = value
        
    @property
    def success(self):
        """The success property.
        
        Returns:
            (bool). the property value. (defaults to: True)
        """
        if 'success' in self._values:
            return self._values['success']
        return self._defaults['success']
        
    @success.setter
    def success(self, value):
        """The success property.
        
        Args:
            value (bool). the property value.
        """
        if value == self._defaults['success'] and 'success' in self._values:
            del self._values['success']
        else:
            self._values['success'] = value
        
    @property
    def async(self):
        """The async property.
        
        Returns:
            (bool). the property value. (defaults to: None)
        """
        if 'async' in self._values:
            return self._values['async']
        return self._defaults['async']
        
    @async.setter
    def async(self, value):
        """The async property.
        
        Args:
            value (bool). the property value.
        """
        if value == self._defaults['async'] and 'async' in self._values:
            del self._values['async']
        else:
            self._values['async'] = value
        
    @property
    def dependency_source(self):
        """The dependency_source property.
        
        Returns:
            (:class:`DependencySourceType.undefined`). the property value. (defaults to: DependencySourceType.undefined)
        """
        if 'dependencySource' in self._values:
            return self._values['dependencySource']
        return self._defaults['dependencySource']
        
    @dependency_source.setter
    def dependency_source(self, value):
        """The dependency_source property.
        
        Args:
            value (:class:`DependencySourceType.undefined`). the property value.
        """
        if value == self._defaults['dependencySource'] and 'dependencySource' in self._values:
            del self._values['dependencySource']
        else:
            self._values['dependencySource'] = value
        
    @property
    def properties(self):
        """The properties property.
        
        Returns:
            (hash). the property value. (defaults to: {})
        """
        if 'properties' in self._values:
            return self._values['properties']
        self._values['properties'] = copy.deepcopy(self._defaults['properties'])
        return self._values['properties']
        
    @properties.setter
    def properties(self, value):
        """The properties property.
        
        Args:
            value (hash). the property value.
        """
        if value == self._defaults['properties'] and 'properties' in self._values:
            del self._values['properties']
        else:
            self._values['properties'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object.
        """
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object.
        
        Returns:
            (dict). the object that represents the same data as the current instance.
        """
        return _write_complex_object(self._defaults, self._values)

