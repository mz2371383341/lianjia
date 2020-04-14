# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lianjia.items import LianjiaItem


class FangSpider(CrawlSpider):
    name = 'fang'
    allowed_domains = ['su.lianjia.com']
    start_urls = ['https://su.lianjia.com/ershoufang/']

    # 翻页
    page_link = LinkExtractor(allow=r'/ershoufang/pg\d$')
    # 房间详情信息
    detail_link = LinkExtractor(restrict_xpaths='//ul[@class="sellListContent"]/li/a')

    rules = (
        Rule(page_link, follow=True),
        Rule(detail_link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = LianjiaItem()
        # 照片
        house_photo = response.xpath('//ul[@class="smallpic"]/li/@data-src').extract()
        # 价格
        mon = response.xpath('//div[@class="content"]/div/span').xpath('string(.)').extract()[2:4]
        money = '/'.join(mon)
        # 一平米多少钱
        one_area = \
        response.xpath('//div[@class="content"]/div/div[@class="text"]/div[1]/span').xpath('string(.)').extract()[0]
        # 房间
        rom = response.xpath('//div[@class="houseInfo"]/div[@class="room"]/div').xpath('string(.)').extract()
        room = ','.join(rom)
        # 类型
        tp = response.xpath('//div[@class="houseInfo"]/div[@class="type"]/div').xpath('string(.)').extract()
        typ = ','.join(tp)
        # 面积
        ara = response.xpath('//div[@class="houseInfo"]/div[@class="area"]/div').xpath('string(.)').extract()
        area = ','.join(ara)
        # 介绍
        # 小区名称
        info_position = response.xpath('//div[@class="aroundInfo"]/div[1]').xpath('string(.)').extract()
        # 位置
        region = response.xpath('//div[@class="aroundInfo"]/div[2]').xpath('string(.)').extract()
        info_region = ''.join(region).split()
        # 看房时间
        info_look_time = response.xpath('//div[@class="aroundInfo"]/div[3]').xpath('string(.)').extract()
        # 链家编号
        info_number = response.xpath('//div[@class="aroundInfo"]/div[4]//span/text()').extract()
        # 基本属性
        basic_attributes = response.xpath('//div[@class="base"]/div[@class="content"]/ul/li').xpath(
            'string(.)').extract()
        # 交易属性
        tran_attribute = response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li').xpath(
            'string(.)').extract()
        transaction_attribute = ''.join(tran_attribute).split()

        # 注意
        careful = response.xpath('//div[@class="introContent"]/div[@class="disclaimer"]/text()').extract()

        # 房源特色-->房源标签
        hous_label = response.xpath('//div[@class="box-l"]/div[2]/div/div[1]/div[2]/a/text()').extract()
        housing_label = ''.join(hous_label).split()[0]
        # 房源特色-->周边配套
        peri_matching = response.xpath('//div[@class="box-l"]/div[2]/div/div[2]/div[2]/text()').extract()
        peripheral_matching = ''.join(peri_matching).split()[0]
        # 房源特色-->小区介绍
        com_introduction = response.xpath('//div[@class="box-l"]/div[2]/div/div[3]/div[2]/text()').extract()
        community_introduction = ''.join(com_introduction).split()[0]
        # 房源特色-->装修描述
        dec_description = response.xpath('//div[@class="box-l"]/div[2]/div/div[4]/div[2]/text()').extract()
        decoration_description = ''.join(dec_description).split()[0]
        # 房源特色 --> 核心卖点
        cor_sell_point = response.xpath('//div[@class="box-l"]/div[2]/div/div[5]/div[2]/text()').extract()
        core_selling_point = ''.join(cor_sell_point).split()[0]
        # 注意事项
        matters_needing_attention = \
        response.xpath('//div[@class="box-l"]/div[2]/div/div[@class="disclaimer"]/text()').extract()[0]

        # 联系人照片
        contacts_photo = response.xpath('//div[@class="component-agent-es-pc-6"]/a/img/@src').extract()[0]
        # 联系人名字
        contacts_name = response.xpath('//div[@class="component-agent-es-pc-6"]/div/div/a/text()').extract()[0]
        # 联系人评分
        contacts_sco = response.xpath('//div[@class="component-agent-es-pc-6"]/div/div[2]/span/text()').extract()
        contacts_score = ''.join(contacts_sco)
        # 联系人电话
        contacts_tel = response.xpath('//div[@class="component-agent-es-pc-6"]/div/div[3]/text()').extract()
        contacts_telephone = '转'.join(contacts_tel)
        contacts_company = response.xpath(
            '//div[@class="component-agent-es-pc-6"]/div/div[@class="brokerName"]/div/span/text()').extract()[0]

        item['house_photo'] = house_photo
        item['money'] = money
        item['one_area'] = one_area
        item['room'] = room
        item['area'] = area
        item['typ'] = typ
        item['careful'] = careful
        item['info_position'] = info_position
        item['info_region'] = info_region
        item['info_look_time'] = info_look_time
        item['info_number'] = info_number
        item['basic_attributes'] = basic_attributes
        item['transaction_attribute'] = transaction_attribute
        item['housing_label'] = housing_label
        item['peripheral_matching'] = peripheral_matching
        item['community_introduction'] = community_introduction
        item['decoration_description'] = decoration_description
        item['core_selling_point'] = core_selling_point
        item['matters_needing_attention'] = matters_needing_attention
        item['contacts_photo'] = contacts_photo
        item['contacts_name'] = contacts_name
        item['contacts_score'] = contacts_score
        item['contacts_telephone'] = contacts_telephone
        item['contacts_company'] = contacts_company
        yield item
