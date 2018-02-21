import scrapy
from casper.items import CasperItem


class CasperSpider(scrapy.Spider):
    name = "wave"
    allowed_urls = ['https://www.casper.com/']
    start_urls = ['https://casper.com/mattresses/reviews?order=desc&rating=']

    def verify(self, content):     
        if content is None:
            return ""
        elif isinstance(content, list):    
            if len(content) > 0:
                content = content[0]     
                return content.encode('ascii','ignore')
            else:       
                return ""
        else:
            return content.encode('ascii','ignore')


    def parse(self, response):    
        
        #grab page
        page    = response.xpath('.//span[@class="page current"]//text()').extract_first().strip()
        page    = self.verify(page)

        #list of reviews
        reviews = response.xpath('//article[@itemprop="review"]')
        
        #review loop
        for singlereview in reviews:

            #scrape info
            name    = singlereview.xpath('.//div[@class="review-name"]/text()').extract_first()
            age     = singlereview.xpath('.//div[@class="review-age"]/text()').extract_first()
            city    = singlereview.xpath('.//div[@class="review-info"]/text()').extract_first()
            state   = singlereview.xpath('.//div[@class="review-info"]/text()').extract_first()
            title   = singlereview.xpath('.//div[@class="review-title body--serif"]/text()').extract_first()
            review  = singlereview.xpath('.//p//text()').extract_first()
            rating  = singlereview.xpath('.//meta/@ratingvalue').extract_first()
            hours   = singlereview.xpath('.//div[@class="review-hours-number"]/text()').extract_first()
            partners= singlereview.xpath('.//div[@class="review-partner-label"]/text()').extract_first()
            date    = singlereview.xpath('.//div[@class="review-date"]/text()').extract_first()
            verified= singlereview.xpath('.//div[@class="review-verified-wrapper js-review-verified-wrapper"]//text()').extract_first()

            # verify
            name        = self.verify(name)     
            age         = self.verify(age)     
            city        = self.verify(city)     
            state       = self.verify(state)     
            title       = self.verify(title)     
            review      = self.verify(review)     
            rating      = self.verify(rating)     
            hours       = self.verify(hours)     
            partners    = self.verify(partners)     
            date        = self.verify(date)     
            verified    = self.verify(verified)     
          

            # yield item
            item = CasperItem()

            item['name']        = name
            item['age']         = age
            item['city']        = city
            item['state']       = state
            item['title']       = title
            item['review']      = review
            item['rating']      = rating
            item['hours']       = hours
            item['partners']    = partners
            item['date']        = date
            item['verified']    = verified
            item['page']        = page

            yield item

        #next page
        next_page = str(response.xpath('//a[@rel="next"]/@href').extract_first())
        next_page = 'https://www.casper.com/' + next_page
        yield scrapy.Request(next_page, callback=self.parse)
