#!/usr/bin/env python3

# Imports
import ast
import sys
import json
import argparse
import textwrap
from datetime import datetime
from fastavro import reader
from rec_avro import from_rec_avro_destructive

# Generate parser
def gen_parser():
    parser = argparse.ArgumentParser(
        prog='',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''
        ==================================
        LIF runner
        ==================================
        '''))
    parser.add_argument('-l', metavar='file.lif', type=argparse.FileType('r'), help='Name of *.lif file')
    return parser

# Generate schema from LIF
def gen_schema(name):
    with open(name, 'rb') as f_in:
        lif_json = gen_json(name)
        lif_schema = get_schema(name)
        new_schema = {
            'type' : lif_schema['type'],
            'name' : name.split('.')[0],
            'fields' : gen_fields(lif_json[0])
        }
        write_schema(new_schema)
        return new_schema

# Generate JSON
def gen_json(name):
    with open(name, 'rb') as f_in:
        return [from_rec_avro_destructive(rec) for rec in reader(f_in)]

# Get schema from LIF
def get_schema(name):
    with open(name, 'rb') as fo:
        r = reader(fo)
        return json.loads(r.metadata['avro.schema'])

# Generate fields for LIF schema
def gen_fields(data):
    acc = []
    if isinstance(data, list):
        for key, value in data[0].items():
            fields = {
                'type' : typing_helper(value),
                'name' : key
            }
            acc.append(fields)
        return acc
    elif isinstance(data, dict):
        for key, value in data.items():
            fields = {
                'type' : typing(value),
                'name' : key,
                'items' : {
                    'type' : typing(value[0]),
                    'name' : key + '_item',
                    'fields' : gen_fields(value)
                }
            }
            acc.append(fields)
        return acc
    else:
        print('Not Implemented Yet!')
        exit(1)

# Write schema
def write_schema(data):
    jsonf = open('schema.json', 'w')
    jsonf.write(json.dumps(data))
    jsonf.close()

# Typing AVRO
def typing(x):
    if x == None:
        return 'null'
    elif isinstance(x, dict):
        if '$record' in x:
            return x['$record']
        return 'record'
    elif isinstance(x, list):
        return 'array'
    elif isinstance(x, bool):
        return 'boolean'
    elif isinstance(x, int):
        return 'integer'
    elif isinstance(x, float):
        return 'float'
    elif isinstance(x, datetime):
        return 'date'
    else:
        assert isinstance(x, bytes) or isinstance(x, str)
        return 'string'

# Helper for typing
'''
 For ISO 8601 is used pattern '%Y-%m-%dT%H:%M:%S%z'
 But in current test.if file is used '01/12' format for date what is equal to pattern '%m/%d'
'''
def typing_helper(data):
    try:
        return typing(ast.literal_eval(data))
    except:
        try:
            return typing(datetime.strptime(data, '%Y-%m-%dT%H:%M:%S%z'))
        except:
            return 'string'

# Main
def main():
    args = gen_parser().parse_args()
    if args.l == None:
        print("Error. For info how use lif runner, run: $ ./lifer.py -h")
        return

    if args.l.name:
        gen_schema(args.l.name)

if __name__ == "__main__":
  sys.exit(main())
