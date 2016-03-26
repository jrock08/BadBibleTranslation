import urllib2
from HTMLParser import HTMLParser

class VerseParser(HTMLParser):
  v = False
  verse = ''
  book = ''
  def handle_starttag(self, tag, attrs):
    if tag == 'b':
      self.v = False    
  def handle_endtag(self, tag):
    if tag == 'b':
      self.v = True
  def handle_data(self, data):
    if self.v:
      self.verse = data.decode('utf-8')
    if not self.v:
      self.book = data.decode('utf-8')

def get_verse():
  response = urllib2.urlopen('http://labs.bible.org/api/?passage=random')
  html = response.read()
  parser = VerseParser()
  parser.feed(html)

  v = parser.verse
  if v.startswith('"') and v.endswith('"'):
    v = v[1:-1]

  return (v, parser.book)

