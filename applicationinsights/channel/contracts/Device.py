import collections
import copy
from .Utils import _write_complex_object

class Device(object):
    """Data contract class for type Device."""
    _defaults = collections.OrderedDict([
        ('ai.device.id', None),
        ('ai.device.ip', None),
        ('ai.device.language', None),
        ('ai.device.locale', None),
        ('ai.device.model', None),
        ('ai.device.network', None),
        ('ai.device.oemName', None),
        ('ai.device.os', None),
        ('ai.device.osVersion', None),
        ('ai.device.roleInstance', None),
        ('ai.device.roleName', None),
        ('ai.device.screenResolution', None),
        ('ai.device.type', None),
        ('ai.device.vmName', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the Device class."""
        self._values = {
        }
        self._initialize()
        
    @property
    def id(self):
        """Gets or sets the id property."""
        if 'ai.device.id' in self._values:
            return self._values['ai.device.id']
        return self._defaults['ai.device.id']
        
    @id.setter
    def id(self, value):
        if value == self._defaults['ai.device.id'] and 'ai.device.id' in self._values:
            del self._values['ai.device.id']
        else:
            self._values['ai.device.id'] = value
        
    @property
    def ip(self):
        """Gets or sets the ip property."""
        if 'ai.device.ip' in self._values:
            return self._values['ai.device.ip']
        return self._defaults['ai.device.ip']
        
    @ip.setter
    def ip(self, value):
        if value == self._defaults['ai.device.ip'] and 'ai.device.ip' in self._values:
            del self._values['ai.device.ip']
        else:
            self._values['ai.device.ip'] = value
        
    @property
    def language(self):
        """Gets or sets the language property."""
        if 'ai.device.language' in self._values:
            return self._values['ai.device.language']
        return self._defaults['ai.device.language']
        
    @language.setter
    def language(self, value):
        if value == self._defaults['ai.device.language'] and 'ai.device.language' in self._values:
            del self._values['ai.device.language']
        else:
            self._values['ai.device.language'] = value
        
    @property
    def locale(self):
        """Gets or sets the locale property."""
        if 'ai.device.locale' in self._values:
            return self._values['ai.device.locale']
        return self._defaults['ai.device.locale']
        
    @locale.setter
    def locale(self, value):
        if value == self._defaults['ai.device.locale'] and 'ai.device.locale' in self._values:
            del self._values['ai.device.locale']
        else:
            self._values['ai.device.locale'] = value
        
    @property
    def model(self):
        """Gets or sets the model property."""
        if 'ai.device.model' in self._values:
            return self._values['ai.device.model']
        return self._defaults['ai.device.model']
        
    @model.setter
    def model(self, value):
        if value == self._defaults['ai.device.model'] and 'ai.device.model' in self._values:
            del self._values['ai.device.model']
        else:
            self._values['ai.device.model'] = value
        
    @property
    def network(self):
        """Gets or sets the network property."""
        if 'ai.device.network' in self._values:
            return self._values['ai.device.network']
        return self._defaults['ai.device.network']
        
    @network.setter
    def network(self, value):
        if value == self._defaults['ai.device.network'] and 'ai.device.network' in self._values:
            del self._values['ai.device.network']
        else:
            self._values['ai.device.network'] = value
        
    @property
    def oem_name(self):
        """Gets or sets the oem_name property."""
        if 'ai.device.oemName' in self._values:
            return self._values['ai.device.oemName']
        return self._defaults['ai.device.oemName']
        
    @oem_name.setter
    def oem_name(self, value):
        if value == self._defaults['ai.device.oemName'] and 'ai.device.oemName' in self._values:
            del self._values['ai.device.oemName']
        else:
            self._values['ai.device.oemName'] = value
        
    @property
    def os(self):
        """Gets or sets the os property."""
        if 'ai.device.os' in self._values:
            return self._values['ai.device.os']
        return self._defaults['ai.device.os']
        
    @os.setter
    def os(self, value):
        if value == self._defaults['ai.device.os'] and 'ai.device.os' in self._values:
            del self._values['ai.device.os']
        else:
            self._values['ai.device.os'] = value
        
    @property
    def os_version(self):
        """Gets or sets the os_version property."""
        if 'ai.device.osVersion' in self._values:
            return self._values['ai.device.osVersion']
        return self._defaults['ai.device.osVersion']
        
    @os_version.setter
    def os_version(self, value):
        if value == self._defaults['ai.device.osVersion'] and 'ai.device.osVersion' in self._values:
            del self._values['ai.device.osVersion']
        else:
            self._values['ai.device.osVersion'] = value
        
    @property
    def role_instance(self):
        """Gets or sets the role_instance property."""
        if 'ai.device.roleInstance' in self._values:
            return self._values['ai.device.roleInstance']
        return self._defaults['ai.device.roleInstance']
        
    @role_instance.setter
    def role_instance(self, value):
        if value == self._defaults['ai.device.roleInstance'] and 'ai.device.roleInstance' in self._values:
            del self._values['ai.device.roleInstance']
        else:
            self._values['ai.device.roleInstance'] = value
        
    @property
    def role_name(self):
        """Gets or sets the role_name property."""
        if 'ai.device.roleName' in self._values:
            return self._values['ai.device.roleName']
        return self._defaults['ai.device.roleName']
        
    @role_name.setter
    def role_name(self, value):
        if value == self._defaults['ai.device.roleName'] and 'ai.device.roleName' in self._values:
            del self._values['ai.device.roleName']
        else:
            self._values['ai.device.roleName'] = value
        
    @property
    def screen_resolution(self):
        """Gets or sets the screen_resolution property."""
        if 'ai.device.screenResolution' in self._values:
            return self._values['ai.device.screenResolution']
        return self._defaults['ai.device.screenResolution']
        
    @screen_resolution.setter
    def screen_resolution(self, value):
        if value == self._defaults['ai.device.screenResolution'] and 'ai.device.screenResolution' in self._values:
            del self._values['ai.device.screenResolution']
        else:
            self._values['ai.device.screenResolution'] = value
        
    @property
    def type(self):
        """Gets or sets the type property."""
        if 'ai.device.type' in self._values:
            return self._values['ai.device.type']
        return self._defaults['ai.device.type']
        
    @type.setter
    def type(self, value):
        if value == self._defaults['ai.device.type'] and 'ai.device.type' in self._values:
            del self._values['ai.device.type']
        else:
            self._values['ai.device.type'] = value
        
    @property
    def vm_name(self):
        """Gets or sets the vm_name property."""
        if 'ai.device.vmName' in self._values:
            return self._values['ai.device.vmName']
        return self._defaults['ai.device.vmName']
        
    @vm_name.setter
    def vm_name(self, value):
        if value == self._defaults['ai.device.vmName'] and 'ai.device.vmName' in self._values:
            del self._values['ai.device.vmName']
        else:
            self._values['ai.device.vmName'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

