import scrapy
import re


class SpiderArtworks(scrapy.Spider):
    name = 'artworks'
    art_urls = []
    page_number = 1
    link_list = []
    start_urls = [
        'http://pstrial-2019-12-16.toscrape.com/browse/insunsh',
        'http://pstrial-2019-12-16.toscrape.com/browse/summertime'
    ]
    custom_settings = {
        'FEED_URI': 'artwork.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
        }

    def parse_art(self, response, **kwargs):
        url = kwargs['url']
        category = kwargs['category'][1:].split('/')
        artist = response.xpath('//h2[contains(@class, "artist")]/text()').get()
        title = response.xpath('//h1/text()').get()
        size = response.xpath('//td[contains(text(), "Dimensions")]/following::td[1]/text()').get()
        cm_size = self.size_formatter(size)
        description = response.xpath('//div[@class="description"]/p/text()').get()
        image = response.xpath('//img/@src').get()
        img_url = 'http://pstrial-2019-12-16.toscrape.com{}'.format(image)
        if cm_size:
            splited_cm = cm_size.split('x')
            try:
                width = splited_cm[0]
            except:
                width = ""
            try:
                hight = splited_cm[1]
            except:
                hight = ""
        else:
            width = ""
            hight = ""
        yield {
            'url': response.request.url,
            'image': img_url,
            'artist': artist,
            'title': title,
            'width': width,
            'hight': hight,
            'description': description,
            'category': category
        }

    def size_formatter(self, size):
        #This one was kinda tricky
        pattern = re.compile(r"(?:\s|\()([\.\d]+)\s*(x|cm)")
        if size:
            m = pattern.findall(size)
            b = [i for sub in m for i in sub]
            return ' '.join(b)

    def parse_art_links(self, response, **kwargs):
        art_links = kwargs.get('art_links')
        url = kwargs.get('url')
        if art_links:
            art_links.extend(response.xpath('//div[@id="body"]/div[not(@id="popular")]/a[not (contains(@style, "hidden"))]/@href').getall())
        else:
            art_links = response.xpath('//div[@id="body"]/div[not(@id="popular")]/a[not (contains(@style, "hidden"))]/@href').getall()
        if len(response.xpath('//div[@id="body"]/div[not(@id="popular")]/a[not (contains(@style, "hidden"))]/@href').getall()) >= 1:
            next_page_number = kwargs.get('next_page_number', 1)
            next_link = 'http://pstrial-2019-12-16.toscrape.com{}'.format(url) + '?page={}'.format(next_page_number)
            yield response.follow(next_link, callback=self.parse_art_links, cb_kwargs={'art_links': art_links, 'next_page_number': next_page_number + 1, 'url':url})
        else:
            for art_link in art_links:
                category = url[7:]
                yield response.follow(art_link, callback=self.parse_art, cb_kwargs={'url':art_link, 'category':category})

    def parse(self, response, **kwargs):
        links = kwargs.get('link')
        if not links:
            links = response.xpath('//div[@id="subcats"]//h3/../..//li/a/@href').getall()
            links.extend(response.xpath('//div[@id="subcats"]//div/ul[not(li)]/../a/@href').getall())
        else:
            links = response.xpath('//div[@id="subcats"]//div/ul[not(li)]/../a/@href').getall()
        
        for link in links:
            if not response.xpath('//div[@id="subcats"]//div/ul[not(li)]/../a/@href').getall():
                yield response.follow(link, callback=self.parse)
            else:
                yield response.follow(link, callback=self.parse_art_links, cb_kwargs={'url': link})
