#!/usr/bin/env python


import json
import sys
import os


class JsonToSrt():

    def __init__(self, sysargv):

        if len(sysargv) != 2:
            raise Exception('You need exactly 1 input argument: an input file string. It can be a relative address.')

        self.infile = sysargv[1]
        if os.path.isabs(self.infile):
            pass
        else:
            self.infile = os.path.join(os.path.curdir, self.infile)

        infileNoExt = os.path.splitext(self.infile)[0]
        self.outfile = infileNoExt + '.srt'

    def load(self):
        if os.path.isfile(self.infile):
            with open(self.infile, 'r') as f:
                try:
                    self.data = json.load(f)
                except Exception as e:
                    print('Something went wrong when trying to parse the JSON file. Check if the file is compliant' +\
                    ' at "http://jsonlint.com/".')
                    raise e

    def convert(self):

        fmt = '%d\n%s --> %s\n%s\n\n'
        index = 0

        with open(self.outfile, 'w') as f:
            for subtitle in self.data['subtitles']:
                index += 1
                f.write(fmt % (index, subtitle['from'], subtitle['to'], subtitle['string']))


if __name__ == '__main__':

    converter = JsonToSrt(sys.argv)
    converter.load()
    converter.convert()