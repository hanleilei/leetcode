#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from lxml.html import fromstring
from functools import reduce
from collections import ChainMap
import pprint
import codecs

pp = pprint.PrettyPrinter(indent=4)


class Extract_table(object):
    def __init__(self,html_name):
        self.html_name = html_name

    def retrieve_tables(self):
        h = open(self.html_name, 'r', encoding = 'GBK').read()
        # return fromstring(h).xpath('//table[@class="tableStyle"]/tbody')
        for i in fromstring(h).xpath('//table[@style="border-collapse: collapse;border:none"]/tbody/tr/td/div'):
        # for i in fromstring(h).xpath('//HTML/BODY/table/tbody/tr/td'):
            for j in i:
                print(j.text_content().strip())

    @staticmethod
    def retrieve_rows(tabb):
        table = tabb.xpath('./tr')

        data = list()
        for tab in table:
            data.append([b.text_content().strip() for b in tab.xpath('./td[@class="tdStyle"]')])

        lk = reduce(lambda x, y: x+y,data[::2])
        lv = reduce(lambda x, y: x+y,data[1::2])
        return dict(zip(lk,lv))
        # print(data)

    def dump_json(self,data):
        filename = os.path.splitext(self.html_name)[0]+'.json'
        with open(filename, 'w',encoding = 'GBK') as f:
            json.dump(data, f,ensure_ascii = False, indent = 4)

if __name__ == '__main__':
    files = os.listdir(os.getcwd())
    file = 'credits.html'
    h = Extract_table(file)
    # tables = h.retrieve_tables()
    h.retrieve_tables()
    #
    # data = {}
    # for table in tables:
    #     data = ChainMap(data,h.retrieve_rows(table))
    # h.dump_json(dict(data))




