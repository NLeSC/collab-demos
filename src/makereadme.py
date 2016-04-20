#!/usr/bin/env python

import json
import sys
import os
import operator
import requests


class ReadmeMaker:

    def __init__(self):

        self.infile = os.path.join(os.path.curdir, 'readme-data.json')
        self.outfile = 'README.md'
        self.repository = 'https://github.com/NLeSC/collab-demos'
        self.data = None
        self.showTableFooter = False

    def readjson(self):
        if os.path.isfile(self.infile):
            with open(self.infile, 'r') as f:
                try:
                    self.data = json.load(f)
                except Exception as e:
                    print('Something went wrong when trying to parse the JSON file. Check if the file ' +
                          'is JSON-compliant at "http://jsonlint.com/".')
                    raise e

    def writemarkdown(self):

        def linkify(url):

            if len(url) == 0:
                return ':x:'
            else:
                if url[0] == '/':
                    url = self.repository + url

                print('checking "' + url + '"...')

                # verify whether the provided url is valid
                request = requests.get(url, timeout=30.0)
                if request.status_code == 200:
                    # all good, link is valid
                    return '[:white_check_mark:](' + url + ')'
                elif request.status_code == 403:
                    # who knows what the status is, I don't have access!
                    return '[:no_entry_sign:](' + url + ')'
                elif request.status_code == 404:
                    # fail
                    return '[:x:](' + url + ')'
                else:
                    # something else is going on
                    print('Unusual status code (' + str(request.status_code) + ').')
                    self.showTableFooter = True
                    return '[:warning:](' + url + ')(' + str(request.status_code) + ')'



        tableHeader = '| Name | Demo | Document | Screencast | Code | Presentation\n' +\
                      '| --- | --- | --- | --- | --- | --- |\n'
        tabularFormat = '| %d. %s | %s | %s | %s | %s | %s |\n'
        tableFooter = '|  |  |  |  |  |  |\n' + \
                      '| For HTTP codes, see [here](https://www.w3.org/Protocols/rfc26' +\
                      '16/rfc2616-sec10.html) |  |  |  |  |  |\n'

        with open(self.outfile, 'w') as f:
            f.write(self.data['header-paragraphs'])
            f.write(tableHeader)

            # sort list of dictionaries by self.data['data']['name'] value:
            self.data['data'].sort(key=operator.itemgetter('name'))

            count = 0

            for entry in self.data['data']:
                if entry['iscomplete']:
                    count += 1
                    f.write(tabularFormat % (count,
                                             entry['name'],
                                             linkify(entry['urls']['demo']),
                                             linkify(entry['urls']['document']),
                                             linkify(entry['urls']['screencast']),
                                             linkify(entry['urls']['code']),
                                             linkify(entry['urls']['presentation'])))
            if self.showTableFooter:
                f.write(tableFooter)

            print('%d items in the table.' % count)

if __name__ == '__main__':

    readmeMaker = ReadmeMaker()
    readmeMaker.readjson()
    readmeMaker.writemarkdown()
