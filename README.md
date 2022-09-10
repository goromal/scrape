# Scrape

Bare-bones Python script for web scraping based off of URLs and XPaths.

## Usage

```bash
usage: scrape [-h] [-o DIRNAME] {simple-link-scraper,simple-image-scraper} page

Scrape content off the internet, quickly.

positional arguments:
  {simple-link-scraper,simple-image-scraper}
                        The type of content to be scraped.
  page                  Webpage url.

optional arguments:
  -h, --help            show this help message and exit
  -o DIRNAME, --output DIRNAME
                        Output directory.
```