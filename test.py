import time
import pickle
import datetime
import os


class Statement:
    '''Saving python data(dicts,lists) in binary to use in future
    Need to create class object(filename can contains file path like '/usr/example/example.bin') .
    Then create new dump
    One file can contains only one object
    You can only rewrite, or read dump, be carefull
    Method 'read' returns saved objects
    Method 'rewrite' clears the dump file and write new object into it '''

    def __init__(self, filename):
        self.filepath = filename  # Path to binary

    def checkfile(self):
        filename = self.filepath
        if os.path.exists(filename):
            return True
        return False

    def newdump(self):
        if not self.checkfile():
            with open(self.filepath, 'wb') as fl:
                pass
        else:
            print('File already exists, use method rewrite')

    def rewrite(self,data):
        if self.checkfile():
            with open(self.filepath, 'wb') as fl:
                pickle.dump(data, fl)
        else:
            print('File does not exists, use method newdump')

    def read(self):
        if self.checkfile():
            with open(self.filepath, 'rb') as fl:
                data = pickle.load(fl)
            return data
        else:
            print('File does not exists, use method newdump')

state_dict={}
nowdate = datetime.datetime.today().strftime("%d-%m-%Y")
lines = [["4", "5", "6"]]
state=Statement(nowdate)
state.newdump()
state.rewrite(lines)
print(state.read())
lines=[['hui'],['hui']*2]
state_dict['16-10-2020']=lines
state.rewrite(state_dict)
a=state.read().get('16-10-2020')
a.append(['fgvhgfjghj','hgfgfnhgfng'])
state_dict=state.read()
state_dict[nowdate]=a
state.rewrite(state_dict)
print(state.read())
