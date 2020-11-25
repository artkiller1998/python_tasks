#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module gets a skills from the json file and prints it out
"""

import json
import argparse
import re
from __future__ import print_function

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", "-i", dest="infile", action="store", \
                        type=str, help="set the input file", metavar="FILE")
    parser.add_argument("--outfile", "-o", metavar="FILE", action="store", \
                        dest="outfile", default='sys.stdout', \
                        help="set the ouput file(if not set using console output)")
    return parser

def formSet(map):
    setSkills = set()
    setSort = set()
    #pattern = re.compile('(.+)',re.IGNORECASE)
    pattern = re.compile(r'(\w+)', re.IGNORECASE)
    for mapElem in map:
        skillsList = mapElem['key_skills']
        if skillsList != []:
            for skillsElem in skillsList:
                isUnique = True
                result = pattern.findall(str(skillsElem['name']))
                for word in result:
                    if word.lower() in setSort:
                        isUnique = False
                        break
                    setSort.add(word.lower())
                if isUnique: setSkills.add(skillsElem['name'])
    return setSkills

def printSet(setSkills, args):
    if (args.outfile) == 'sys.stdout':
        for setElem in sorted(setSkills):
            print(setElem)
    else:
        with open(args.outfile, 'w', encoding='utf8') as skillsFile:
            skillsFile.write('Skills for this vacancy:\n')
            for setElem in sorted(setSkills):
                skillsFile.write(setElem + '\n')

def main():
    parser = parseArgs()
    args = parser.parse_args()
    print('Arguments\n' + str(args))
    try:
        jh = open(args.infile, 'r', encoding='utf8', errors='ignore')
    except FileNotFoundError:
        print('Ошибка! Такого файла не существует.')
    else:
        items = json.load(jh)
        map = items.get('Vacancies')
        setSkills = formSet(map)
        printSet(setSkills, args)

if __name__ == "__main__":
    main()
