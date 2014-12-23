import json

class TestJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if obj and obj.__class__.__name__ == 'object':
            return {}
        return json.JSONEncoder.default(self, obj)