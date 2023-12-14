import requests, os
import lxml.html
from urllib.parse import urljoin

class HTMLScraper(object):
    def __init__(self, url, outputdir):
        self.url = url
        response = requests.get(url, stream=True)
        response.raw.decode_content = True
        self.tree = lxml.html.parse(response.raw)
        self.outputdir = outputdir
    
    def download_from_url_xpath(self, xpath, text_spec=''):
        download_url = self.tree.xpath(xpath)[0]
        if text_spec in download_url:
            filename = download_url.split('/')[-1]
            if not 'http' in download_url:
                download_url = urljoin(self.url, download_url)
            r = requests.get(download_url)
            filepath = os.path.join(self.outputdir, filename)
            print('-> {}...'.format(filepath))
            with open(filepath, 'wb') as f:
                f.write(r.content)

class SimpleHTMLScraper(HTMLScraper):
    def __init__(self, url, outputdir, xpath_inp=None, ext_inp=None):
        super(SimpleHTMLScraper, self).__init__(url, outputdir)
        oneshot = (xpath_inp is not None) and (ext_inp is not None)
        while True:
            if xpath_inp is None:
                xpath = input('Enter Full XPath to encompassing element (ENTER to exit): ')
            else:
                xpath = xpath_inp
            if not xpath:
                break
            if ext_inp is None:
                text_spec = input('...Special text that filenames should contain (ENTER for none): ')
            else:
                text_spec = ext_inp
            xpath_results = self.tree.xpath(xpath)
            print(self.tree)
            if len(xpath_results) > 0:
                try:
                    for xpath_child in self.get_xpath_children(self.tree.xpath(xpath)[0]):
                        self.download_from_url_xpath(xpath_child, text_spec)
                except TypeError:
                    if oneshot:
                        print('XPath element does not appear to have the child elements you\'re searching for')
                        break
                    else:
                        print('XPath element does not appear to have the child elements you\'re searching for; please try again...')
            else:
                if oneshot:
                    print('XPath turned no results')
                    break
                else:
                    print('XPath turned no results; please try again...')
                    yn = input('Would you like me to print out the entire XPath tree [y/N]: ')
                    if yn.lower() == 'y':
                        print()
                        for e in self.tree.getroot().iter():
                            print(self.tree.getpath(e))
                        print()
            if oneshot:
                break

    def get_xpath_children(self, xpath):
        return []

class SimpleLinkScraper(SimpleHTMLScraper):
    def __init__(self, args):
        super(SimpleLinkScraper, self).__init__(args.page, args.output, args.xpath, args.ext)
    
    def get_xpath_children(self, root):
        xpath_children = list()
        for child in root.iter('a'):
            xpath_children.append('{}/@href'.format(self.tree.getpath(child)))

        return xpath_children

class SimpleImageScraper(SimpleHTMLScraper):
    def __init__(self, args):
        super(SimpleImageScraper, self).__init__(args.page, args.output, args.xpath, args.ext)
    
    def get_xpath_children(self, root):
        xpath_children = list()
        for child in root.iter('img'):
            xpath_children.append('{}/@src'.format(self.tree.getpath(child)))
        
        return xpath_children
