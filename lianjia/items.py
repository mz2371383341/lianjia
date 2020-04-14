# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # 照片
    house_photo = scrapy.Field()
    # 价钱
    money = scrapy.Field()
    # 面积
    one_area = scrapy.Field()
    room = scrapy.Field()
    typ = scrapy.Field()
    area = scrapy.Field()
    # 介绍
    info_position = scrapy.Field()
    info_region = scrapy.Field()
    info_look_time = scrapy.Field()
    info_number = scrapy.Field()
    careful = scrapy.Field()
    # # 详细介绍
    basic_attributes = scrapy.Field()
    # 交易属性
    transaction_attribute = scrapy.Field()
    # 房源特色 --> 房源标签
    housing_label = scrapy.Field()
    # 房源特色 --> 周边配套
    peripheral_matching = scrapy.Field()
    # 房源特色 --> 小区介绍
    community_introduction = scrapy.Field()
    # 房源特色 --> 装修描述
    decoration_description = scrapy.Field()
    # 房源特色 --> 核心卖点
    core_selling_point = scrapy.Field()
    # 注意事项
    matters_needing_attention = scrapy.Field()
    # 联系人
    contacts_photo = scrapy.Field()
    # 联系人名字
    contacts_name = scrapy.Field()
    # 联系人所属评分
    contacts_score = scrapy.Field()
    # 联系人电话
    contacts_telephone = scrapy.Field()
    # 联系人公司
    contacts_company = scrapy.Field()



