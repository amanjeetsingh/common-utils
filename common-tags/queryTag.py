#!/usr/bin/env python

__copyright__ = '(c) 2016 DataNexus Inc.  All Rights Reserved.'
__license__ = 'APLv2.0'
__author__ = 'ckeller@datanexus.org'
__version__ = '0.1'

def match_tags (line, args):
    
    app_repo = line.split(',')[0]
    app_repo = app_repo[app_repo.find(':')+1:]    
    app_name = app_repo[app_repo.rfind('/')+1:]
    app_tag=line.split(',')[1].lstrip()
    app_tag = app_tag[app_tag.find(':')+1:]
    
    if args.url == app_repo: return (app_tag)
    if args.application == app_name: return (app_tag)
    if args.tag == app_tag: return (app_name)
    return None
    
def read_file (args):
    import sys
    
    """read file into in-memory hash"""
    
    try:
        with open(args.db, 'r') as f:
            while True:
                app_line = f.readline()
                if app_line == '': break
                app_line = app_line.partition('#')[0].rstrip()
                if not app_line == '':
                    result = match_tags(app_line, args)
                    if result is not None: print result
    except IOError:
        print "'%s' not found...exiting" % args.db
        sys.exit(1)
    
def main():
    """Main function"""
    
    import argparse
    parser = argparse.ArgumentParser(description='Install DN Platform')
    parser.add_argument('--url', dest='url', help='return the tag associated with the URL')
    parser.add_argument('--app', dest='application',help='return the tag associated with the repository application name')
    parser.add_argument('--tag', dest='tag',help='return the repository application name associated with the tag')
    parser.add_argument('--db', dest='db', default="tagsDB", help='database file to use')
    
    read_file(parser.parse_args())
    
if __name__ == '__main__': 
    main()
    