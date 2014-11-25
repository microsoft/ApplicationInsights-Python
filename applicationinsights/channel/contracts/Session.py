import collections
import copy
from .Utils import _write_complex_object

class Session(object):
    """Data contract class for type Session."""
    _defaults = collections.OrderedDict([
        ('ai.session.id', None),
        ('ai.session.isFirst', None),
        ('ai.session.isNew', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the Session class."""
        self._values = {
        }
        self._initialize()
        
    @property
    def id(self):
        """Gets or sets the id property."""
        if 'ai.session.id' in self._values:
            return self._values['ai.session.id']
        return self._defaults['ai.session.id']
        
    @id.setter
    def id(self, value):
        if value == self._defaults['ai.session.id'] and 'ai.session.id' in self._values:
            del self._values['ai.session.id']
        else:
            self._values['ai.session.id'] = value
        
    @property
    def is_first(self):
        """Gets or sets the is_first property."""
        if 'ai.session.isFirst' in self._values:
            return self._values['ai.session.isFirst']
        return self._defaults['ai.session.isFirst']
        
    @is_first.setter
    def is_first(self, value):
        if value == self._defaults['ai.session.isFirst'] and 'ai.session.isFirst' in self._values:
            del self._values['ai.session.isFirst']
        else:
            self._values['ai.session.isFirst'] = value
        
    @property
    def is_new(self):
        """Gets or sets the is_new property."""
        if 'ai.session.isNew' in self._values:
            return self._values['ai.session.isNew']
        return self._defaults['ai.session.isNew']
        
    @is_new.setter
    def is_new(self, value):
        if value == self._defaults['ai.session.isNew'] and 'ai.session.isNew' in self._values:
            del self._values['ai.session.isNew']
        else:
            self._values['ai.session.isNew'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

