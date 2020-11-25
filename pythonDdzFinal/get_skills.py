#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""This module gets a skills from the json file and prints it out"""

from __future__ import print_function
import json
import argparse
import re

def parser_call():
    """Diefines arguments for parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", "-i", dest="infile", action="store", \
                        type=str, help="set the input file", metavar="FILE")
    parser.add_argument("--outfile", "-o", metavar="FILE", action="store", \
                        dest="outfile", default='sys.stdout', \
                        help="set the ouput file(if not set using console output)")
    return parser

def form_map(map_items):
    """Get list - map items. Form the map of unique skills and it's count"""
    map_skills = {}
    map_shortwords = {}
    set_sort = set()
    pattern = re.compile(r'(\w+)', re.IGNORECASE)
    #pattern = re.compile(r'(.+)', re.IGNORECASE)
    for map_elem in map_items:
        skills_list = map_elem['key_skills']
        if skills_list != []:
            for skills_elem in skills_list:
                map_skills = sort_by_patern(skills_elem, map_skills, map_shortwords,
                                            set_sort, pattern)
    return map_skills


def sort_by_patern(skills_elem, map_skills, map_shortwords, set_sort, pattern):
    """sort the skills element by pattern of regexp"""
    is_unique = True
    result = pattern.findall(str(skills_elem['name']))
    for word in result:
        if word.lower() in set_sort:
            is_unique = False
            map_skills[map_shortwords.get(word.lower())] = \
                map_skills.get(map_shortwords.get(word.lower())) + 1
            break
        set_sort.add(word.lower())
        if is_unique:
            map_skills[str(skills_elem['name'])] = 1
            for word_res in result:
                map_shortwords[word_res.lower()] = str(skills_elem['name'])
    return map_skills

def print_map(map_skills, outfile):
    """Get map of a skills, args outfile. Outputs generated set in filestream/stdout"""
    sorted_map_skills = sorted(map_skills.items(), key=lambda kv: kv[1])
    if outfile == 'sys.stdout':
        for set_elem in sorted_map_skills:
            print(set_elem)
    else:
        with open(outfile, 'w', encoding='utf8') as skills_file:
            skills_file.write('Skills for this vacancy:\n')
            for set_elem in sorted_map_skills:
                skills_file.write(str(set_elem) + '\n')

def main():
    """Main func of the module"""
    parser = parser_call()
    args = parser.parse_args()
    print('Arguments\n' + str(args))
    try:
        file_out = open(args.infile, 'r', encoding='utf8', errors='ignore')
    except FileNotFoundError:
        print('Ошибка! Такого файла не существует.')
    else:
        items = json.load(file_out)
        map_items = items.get('Vacancies')
        map_skills = form_map(map_items)
        print_map(map_skills, args.outfile)

if __name__ == "__main__":
    main()
