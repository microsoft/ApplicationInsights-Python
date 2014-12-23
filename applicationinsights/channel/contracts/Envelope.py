import collections
import copy
from .Utils import _write_complex_object

class Envelope(object):
    """Data contract class for type Envelope.
    """
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
        """Initializes a new instance of the class.
        """
        self._values = {
            'ver': 1,
            'name': None,
            'time': None,
            'sampleRate': 100.0,
        }
        self._initialize()
        
    @property
    def ver(self):
        """The ver property.
        
        Returns:
            (int). the property value. (defaults to: 1)
        """
        if 'ver' in self._values:
            return self._values['ver']
        return self._defaults['ver']
        
    @ver.setter
    def ver(self, value):
        """The ver property.
        
        Args:
            value (int). the property value.
        """
        if value == self._defaults['ver'] and 'ver' in self._values:
            del self._values['ver']
        else:
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
    def time(self):
        """The time property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        return self._values['time']
        
    @time.setter
    def time(self, value):
        """The time property.
        
        Args:
            value (string). the property value.
        """
        self._values['time'] = value
        
    @property
    def sample_rate(self):
        """The sample_rate property.
        
        Returns:
            (float). the property value. (defaults to: 100.0)
        """
        if 'sampleRate' in self._values:
            return self._values['sampleRate']
        return self._defaults['sampleRate']
        
    @sample_rate.setter
    def sample_rate(self, value):
        """The sample_rate property.
        
        Args:
            value (float). the property value.
        """
        if value == self._defaults['sampleRate'] and 'sampleRate' in self._values:
            del self._values['sampleRate']
        else:
            self._values['sampleRate'] = value
        
    @property
    def seq(self):
        """The seq property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'seq' in self._values:
            return self._values['seq']
        return self._defaults['seq']
        
    @seq.setter
    def seq(self, value):
        """The seq property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['seq'] and 'seq' in self._values:
            del self._values['seq']
        else:
            self._values['seq'] = value
        
    @property
    def ikey(self):
        """The ikey property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'iKey' in self._values:
            return self._values['iKey']
        return self._defaults['iKey']
        
    @ikey.setter
    def ikey(self, value):
        """The ikey property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['iKey'] and 'iKey' in self._values:
            del self._values['iKey']
        else:
            self._values['iKey'] = value
        
    @property
    def flags(self):
        """The flags property.
        
        Returns:
            (int). the property value. (defaults to: None)
        """
        if 'flags' in self._values:
            return self._values['flags']
        return self._defaults['flags']
        
    @flags.setter
    def flags(self, value):
        """The flags property.
        
        Args:
            value (int). the property value.
        """
        if value == self._defaults['flags'] and 'flags' in self._values:
            del self._values['flags']
        else:
            self._values['flags'] = value
        
    @property
    def device_id(self):
        """The device_id property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'deviceId' in self._values:
            return self._values['deviceId']
        return self._defaults['deviceId']
        
    @device_id.setter
    def device_id(self, value):
        """The device_id property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['deviceId'] and 'deviceId' in self._values:
            del self._values['deviceId']
        else:
            self._values['deviceId'] = value
        
    @property
    def os(self):
        """The os property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'os' in self._values:
            return self._values['os']
        return self._defaults['os']
        
    @os.setter
    def os(self, value):
        """The os property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['os'] and 'os' in self._values:
            del self._values['os']
        else:
            self._values['os'] = value
        
    @property
    def os_ver(self):
        """The os_ver property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'osVer' in self._values:
            return self._values['osVer']
        return self._defaults['osVer']
        
    @os_ver.setter
    def os_ver(self, value):
        """The os_ver property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['osVer'] and 'osVer' in self._values:
            del self._values['osVer']
        else:
            self._values['osVer'] = value
        
    @property
    def app_id(self):
        """The app_id property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'appId' in self._values:
            return self._values['appId']
        return self._defaults['appId']
        
    @app_id.setter
    def app_id(self, value):
        """The app_id property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['appId'] and 'appId' in self._values:
            del self._values['appId']
        else:
            self._values['appId'] = value
        
    @property
    def app_ver(self):
        """The app_ver property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'appVer' in self._values:
            return self._values['appVer']
        return self._defaults['appVer']
        
    @app_ver.setter
    def app_ver(self, value):
        """The app_ver property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['appVer'] and 'appVer' in self._values:
            del self._values['appVer']
        else:
            self._values['appVer'] = value
        
    @property
    def user_id(self):
        """The user_id property.
        
        Returns:
            (string). the property value. (defaults to: None)
        """
        if 'userId' in self._values:
            return self._values['userId']
        return self._defaults['userId']
        
    @user_id.setter
    def user_id(self, value):
        """The user_id property.
        
        Args:
            value (string). the property value.
        """
        if value == self._defaults['userId'] and 'userId' in self._values:
            del self._values['userId']
        else:
            self._values['userId'] = value
        
    @property
    def tags(self):
        """The tags property.
        
        Returns:
            (hash). the property value. (defaults to: {})
        """
        if 'tags' in self._values:
            return self._values['tags']
        self._values['tags'] = copy.deepcopy(self._defaults['tags'])
        return self._values['tags']
        
    @tags.setter
    def tags(self, value):
        """The tags property.
        
        Args:
            value (hash). the property value.
        """
        if value == self._defaults['tags'] and 'tags' in self._values:
            del self._values['tags']
        else:
            self._values['tags'] = value
        
    @property
    def data(self):
        """The data property.
        
        Returns:
            (object). the property value. (defaults to: None)
        """
        if 'data' in self._values:
            return self._values['data']
        return self._defaults['data']
        
    @data.setter
    def data(self, value):
        """The data property.
        
        Args:
            value (object). the property value.
        """
        if value == self._defaults['data'] and 'data' in self._values:
            del self._values['data']
        else:
            self._values['data'] = value
        
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

