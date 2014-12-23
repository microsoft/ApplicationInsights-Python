import collections
import copy
from .Utils import _write_complex_object

class Operation(object):
    """Data contract class for type Operation.
    """
    _defaults = collections.OrderedDict([
        ('ai.operation.id', None),
        ('ai.operation.name', None),
        ('ai.operation.parentId', None),
        ('ai.operation.rootId', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the class.
        """
        self._values = {
        }
        self._initialize()
        
    @property
    def id(self):
        """The id property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'ai.operation.id' in self._values:
            return self._values['ai.operation.id']
        return self._defaults['ai.operation.id']
        
    @id.setter
    def id(self, value):
        """The id property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['ai.operation.id'] and 'ai.operation.id' in self._values:
            del self._values['ai.operation.id']
        else:
            self._values['ai.operation.id'] = value
        
    @property
    def name(self):
        """The name property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'ai.operation.name' in self._values:
            return self._values['ai.operation.name']
        return self._defaults['ai.operation.name']
        
    @name.setter
    def name(self, value):
        """The name property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['ai.operation.name'] and 'ai.operation.name' in self._values:
            del self._values['ai.operation.name']
        else:
            self._values['ai.operation.name'] = value
        
    @property
    def parent_id(self):
        """The parent_id property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'ai.operation.parentId' in self._values:
            return self._values['ai.operation.parentId']
        return self._defaults['ai.operation.parentId']
        
    @parent_id.setter
    def parent_id(self, value):
        """The parent_id property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['ai.operation.parentId'] and 'ai.operation.parentId' in self._values:
            del self._values['ai.operation.parentId']
        else:
            self._values['ai.operation.parentId'] = value
        
    @property
    def root_id(self):
        """The root_id property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'ai.operation.rootId' in self._values:
            return self._values['ai.operation.rootId']
        return self._defaults['ai.operation.rootId']
        
    @root_id.setter
    def root_id(self, value):
        """The root_id property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['ai.operation.rootId'] and 'ai.operation.rootId' in self._values:
            del self._values['ai.operation.rootId']
        else:
            self._values['ai.operation.rootId'] = value
        
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

