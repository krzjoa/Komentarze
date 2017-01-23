#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Krzysztof Joachimiak 2016
# Komentarze: korpus komentarzy z portalu Wirtualna Polska

from os.path import join
from os import listdir

class Komentarze(object):


    def __init__(self, path='.'):
        '''

        Class for easy handling comments from the Komentarze corpus

        Parameters
        ----------
        path: str, default '.'
            Path to Komentarze root directory

        Attributes
        ----------
        set_names: dict
            Map of subset names

        '''
        self.root_path = path
        self.set_names = {'gk':'Groźby karalne',
                          'obr': 'Obraźliwe',
                          'zl': 'Złośliwe',
                          'kr':'Krytyka',
                          'ok': 'Ostra krytyka',
                          'poz': 'Pozostałe' }


        self.data = {name:[] for name in self.set_names.keys()}

    def load(self):
        for name in self.set_names.values():
            self.data[name] = load_multiple_json(join(self.root_path, name))
        return self

    def get_dataframe(self):
        from pandas import DataFrame
        _prepared_list = []
        for key in self.data:
            for item in self.data[key]:
                item['klasa'] = key
                _prepared_list.append(item)
        return DataFrame(_prepared_list)



def load_multiple_json(path):
    import json
    files = []
    for name in listdir(path):
        with open(join(path, name), 'r') as f:
            files.append(json.load(f))
    return files

