import os, argparse
from scrape.utils import ColorPrint
from scrape.scrapers import SimpleLinkScraper, SimpleImageScraper

def cli():
    scrapers = {'simple-link-scraper':  SimpleLinkScraper, 
                'simple-image-scraper': SimpleImageScraper}

    argparser = argparse.ArgumentParser(description='Scrape content off the internet, quickly.')
    argparser.add_argument('scraper', choices=scrapers.keys(), help='The type of content to be scraped.')
    argparser.add_argument('page', type=str, help='Webpage url.')
    argparser.add_argument('-o', '--output', metavar='DIRNAME',  dest='output', type=str, default='',  action='store', help='Output directory.')
    args = argparser.parse_args()

    if not args.output == '':
        if not os.path.exists(args.output):
            ColorPrint.Warn('Creating output directory: {}'.format(args.output))
            os.makedirs(args.output)

    print()
    _ = scrapers[args.scraper](args)
    print()
    ColorPrint.Green('Finished!')
