import collections
import copy
from .Utils import _write_complex_object

class User(object):
    """Data contract class for type User."""
    _defaults = collections.OrderedDict([
        ('ai.user.accountAcquisitionDate', None),
        ('ai.user.accountId', None),
        ('ai.user.userAgent', None),
        ('ai.user.id', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the User class."""
        self._values = {
        }
        self._initialize()
        
    @property
    def account_acquisition_date(self):
        """Gets or sets the account_acquisition_date property."""
        if 'ai.user.accountAcquisitionDate' in self._values:
            return self._values['ai.user.accountAcquisitionDate']
        return self._defaults['ai.user.accountAcquisitionDate']
        
    @account_acquisition_date.setter
    def account_acquisition_date(self, value):
        if value == self._defaults['ai.user.accountAcquisitionDate'] and 'ai.user.accountAcquisitionDate' in self._values:
            del self._values['ai.user.accountAcquisitionDate']
        else:
            self._values['ai.user.accountAcquisitionDate'] = value
        
    @property
    def account_id(self):
        """Gets or sets the account_id property."""
        if 'ai.user.accountId' in self._values:
            return self._values['ai.user.accountId']
        return self._defaults['ai.user.accountId']
        
    @account_id.setter
    def account_id(self, value):
        if value == self._defaults['ai.user.accountId'] and 'ai.user.accountId' in self._values:
            del self._values['ai.user.accountId']
        else:
            self._values['ai.user.accountId'] = value
        
    @property
    def user_agent(self):
        """Gets or sets the user_agent property."""
        if 'ai.user.userAgent' in self._values:
            return self._values['ai.user.userAgent']
        return self._defaults['ai.user.userAgent']
        
    @user_agent.setter
    def user_agent(self, value):
        if value == self._defaults['ai.user.userAgent'] and 'ai.user.userAgent' in self._values:
            del self._values['ai.user.userAgent']
        else:
            self._values['ai.user.userAgent'] = value
        
    @property
    def id(self):
        """Gets or sets the id property."""
        if 'ai.user.id' in self._values:
            return self._values['ai.user.id']
        return self._defaults['ai.user.id']
        
    @id.setter
    def id(self, value):
        if value == self._defaults['ai.user.id'] and 'ai.user.id' in self._values:
            del self._values['ai.user.id']
        else:
            self._values['ai.user.id'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

