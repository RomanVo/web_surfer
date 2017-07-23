from .. import simplelogger
import datetime
from scrapy.selector import Selector
from scrapy.spiders import BaseSpider
from .. import items
import sqlite3 as lite

logger = simplelogger.SimpleLogger()


def get_utc_timestamp():
    """
    get timestamp in UTC format
    :return: timestamp
    """
    date_obj = datetime.datetime.utcnow()
    return str(date_obj.strftime('%Y-%m-%dT%H:%M:%S'))


def insert_to_db(item):
    """
    Insert values to sqlite db
    @param item: item values
    """
    logger.log_info('Connecting to db')
    con = lite.connect('data.db')

    with con:
        cur = con.cursor()
        logger.log_info('Writing to db')
        query = "INSERT INTO main.oil VALUES('{date}','{price}')".format(date=get_utc_timestamp(), price=item)
        logger.log_info(query)
        cur.execute(query)
    con.commit()
    con.close()


class NetSurfSpider(BaseSpider):
    name = "oil"
    allowed_domains = ["http://finance.yahoo.com/"]
    start_urls = ["http://finance.yahoo.com/"]

    def parse(self, response):
        hxs = Selector(response)
        titles = hxs.xpath('//*[@id="yfs_l84_clm16.nym"]/text()').extract()
        for title in titles:
            item = items.NetSurfItem()
            item["oil"] = title
            logger.log_info('Scrapped item: {item}'.format(item=item["oil"]))
            # insert to db
            insert_to_db(title)
            yield item
        logger.log_info('======================================================')