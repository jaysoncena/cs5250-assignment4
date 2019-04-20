import sys

from collections import deque, MutableSequence

class ProcessList(MutableSequence):
    def __init__(self, data=None):
        super(ProcessList, self).__init__()
        if data is None:
            self._list = list()
        else:
            self._list = list(data)
        
    def __repr__(self):
        ret = ["<{2}> {0} {1}".format(type(x), x, self.__class__.__name__) for x in self._list]
        return "\n".join(ret)
    def __len__(self):
        return len(self._list)
    def __getitem__(self, ii):
        return self._list[ii]
    def __delitem__(self, ii):
        del self._list[ii]
    def __setitem__(self, ii, val):
        self._list[ii] = val
    def __str__(self):
        return self.__repr__()
    def insert(self, val):
        self.append(val)
    def append(self, val):
        self._list.append(val)