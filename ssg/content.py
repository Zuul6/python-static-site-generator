import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = '"^(?:-|\+){3}\s*$"'
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(self, cls, string):
        _ = fm = content = self.__regex.split(string[:2])
        load(fm, Loader = FullLoader)
        return cls(metadata, content)

    def Content(self, metadata, content):
        data = metadata
        self.data = {"content":content}

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"] if "type" in self.data else None
        
    @type.setter
    def type(self, type):
        self.data["type"] = type

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.__iter__()

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key is not "content":
                data[key] = value                
        return str(data)