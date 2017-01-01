#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  host = filename[ filename.index('_') + 1 : ]
  regex_puzzle = "GET (\S+/puzzle/\S+) "
  f = open(filename,"r")
  html_text = f.read()
  img_urls = {}
  log_lines = re.findall(regex_puzzle, html_text)
  for log_line in log_lines:
      url = "http://"+host+log_line
      print url
      img_urls[url] = True
  return sorted(img_urls.keys(), key=sort_url)


def sort_url(url):
  match = re.search('(\w+)-(\w+)\.\w+', url)
  return match.group(2)


def download_images(img_urls, dest_dir):
  if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

  dest_index_html = file(os.path.join(dest_dir, 'index.html'), 'w')
  dest_index_html.write('<html><body>\n')

  i = 0
  for img_url in img_urls:
    img_file_name = 'img%d' % i
    print 'Retrieving...', img_url
    urllib.urlretrieve(img_url, os.path.join(dest_dir, img_file_name))
    dest_index_html.write('<img src="%s">' % (img_file_name,))
    i += 1

  dest_index_html.write('\n</body></html>\n')
  dest_index_html.close()
  
  
def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
