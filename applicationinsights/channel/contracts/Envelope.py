import collections
import copy
from .Utils import _write_complex_object

class Envelope(object):
    """Data contract class for type Envelope."""
    _defaults = collections.OrderedDict([
        ('ver', 1),
        ('name', None),
        ('time', None),
        ('sampleRate', 100.0),
        ('seq', None),
        ('iKey', None),
        ('flags', None),
        ('deviceId', None),
        ('os', None),
        ('osVer', None),
        ('appId', None),
        ('appVer', None),
        ('userId', None),
        ('tags', {}),
        ('data', None)
    ])
    
    def __init__(self):
        """Initializes a new instance of the Envelope class."""
        self._values = {
            'ver': 1,
            'name': None,
            'time': None,
            'sampleRate': 100.0,
        }
        self._initialize()
        
    @property
    def ver(self):
        """Gets or sets the ver property."""
        if 'ver' in self._values:
            return self._values['ver']
        return self._defaults['ver']
        
    @ver.setter
    def ver(self, value):
        if value == self._defaults['ver'] and 'ver' in self._values:
            del self._values['ver']
        else:
            self._values['ver'] = value
        
    @property
    def name(self):
        """Gets or sets the name property."""
        return self._values['name']
        
    @name.setter
    def name(self, value):
        self._values['name'] = value
        
    @property
    def time(self):
        """Gets or sets the time property."""
        return self._values['time']
        
    @time.setter
    def time(self, value):
        self._values['time'] = value
        
    @property
    def sample_rate(self):
        """Gets or sets the sample_rate property."""
        if 'sampleRate' in self._values:
            return self._values['sampleRate']
        return self._defaults['sampleRate']
        
    @sample_rate.setter
    def sample_rate(self, value):
        if value == self._defaults['sampleRate'] and 'sampleRate' in self._values:
            del self._values['sampleRate']
        else:
            self._values['sampleRate'] = value
        
    @property
    def seq(self):
        """Gets or sets the seq property."""
        if 'seq' in self._values:
            return self._values['seq']
        return self._defaults['seq']
        
    @seq.setter
    def seq(self, value):
        if value == self._defaults['seq'] and 'seq' in self._values:
            del self._values['seq']
        else:
            self._values['seq'] = value
        
    @property
    def ikey(self):
        """Gets or sets the ikey property."""
        if 'iKey' in self._values:
            return self._values['iKey']
        return self._defaults['iKey']
        
    @ikey.setter
    def ikey(self, value):
        if value == self._defaults['iKey'] and 'iKey' in self._values:
            del self._values['iKey']
        else:
            self._values['iKey'] = value
        
    @property
    def flags(self):
        """Gets or sets the flags property."""
        if 'flags' in self._values:
            return self._values['flags']
        return self._defaults['flags']
        
    @flags.setter
    def flags(self, value):
        if value == self._defaults['flags'] and 'flags' in self._values:
            del self._values['flags']
        else:
            self._values['flags'] = value
        
    @property
    def device_id(self):
        """Gets or sets the device_id property."""
        if 'deviceId' in self._values:
            return self._values['deviceId']
        return self._defaults['deviceId']
        
    @device_id.setter
    def device_id(self, value):
        if value == self._defaults['deviceId'] and 'deviceId' in self._values:
            del self._values['deviceId']
        else:
            self._values['deviceId'] = value
        
    @property
    def os(self):
        """Gets or sets the os property."""
        if 'os' in self._values:
            return self._values['os']
        return self._defaults['os']
        
    @os.setter
    def os(self, value):
        if value == self._defaults['os'] and 'os' in self._values:
            del self._values['os']
        else:
            self._values['os'] = value
        
    @property
    def os_ver(self):
        """Gets or sets the os_ver property."""
        if 'osVer' in self._values:
            return self._values['osVer']
        return self._defaults['osVer']
        
    @os_ver.setter
    def os_ver(self, value):
        if value == self._defaults['osVer'] and 'osVer' in self._values:
            del self._values['osVer']
        else:
            self._values['osVer'] = value
        
    @property
    def app_id(self):
        """Gets or sets the app_id property."""
        if 'appId' in self._values:
            return self._values['appId']
        return self._defaults['appId']
        
    @app_id.setter
    def app_id(self, value):
        if value == self._defaults['appId'] and 'appId' in self._values:
            del self._values['appId']
        else:
            self._values['appId'] = value
        
    @property
    def app_ver(self):
        """Gets or sets the app_ver property."""
        if 'appVer' in self._values:
            return self._values['appVer']
        return self._defaults['appVer']
        
    @app_ver.setter
    def app_ver(self, value):
        if value == self._defaults['appVer'] and 'appVer' in self._values:
            del self._values['appVer']
        else:
            self._values['appVer'] = value
        
    @property
    def user_id(self):
        """Gets or sets the user_id property."""
        if 'userId' in self._values:
            return self._values['userId']
        return self._defaults['userId']
        
    @user_id.setter
    def user_id(self, value):
        if value == self._defaults['userId'] and 'userId' in self._values:
            del self._values['userId']
        else:
            self._values['userId'] = value
        
    @property
    def tags(self):
        """Gets or sets the tags property."""
        if 'tags' in self._values:
            return self._values['tags']
        self._values['tags'] = copy.deepcopy(self._defaults['tags'])
        return self._values['tags']
        
    @tags.setter
    def tags(self, value):
        if value == self._defaults['tags'] and 'tags' in self._values:
            del self._values['tags']
        else:
            self._values['tags'] = value
        
    @property
    def data(self):
        """Gets or sets the data property."""
        if 'data' in self._values:
            return self._values['data']
        return self._defaults['data']
        
    @data.setter
    def data(self, value):
        if value == self._defaults['data'] and 'data' in self._values:
            del self._values['data']
        else:
            self._values['data'] = value
        
    def _initialize(self):
        """Initializes the current instance of the object (can be overridden)."""
        pass
    
    def write(self):
        """Writes the contents of this object and returns the content as a dict object."""
        return _write_complex_object(self._defaults, self._values)

