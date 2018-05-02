#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: hupu_player.py 
   @time: 2018/05/02
"""

import scrapy
import re
from ..items import HupuPlayerItem

class PlayerSpider(scrapy.Spider):

    name = 'hupu_player'

    # def start_requests(self):
    #     base_url = 'https://nba.hupu.com/stats/players/pts/%s'
    #     for page in range(1,7):
    #         url = base_url % page
    #         yield scrapy.Request(url=url,callback=self.parse)

    start_urls = ['https://nba.hupu.com/teams']


    def parse(self, response):
        for team_url in response.css('div.team a::attr(href)').extract():
            if team_url:
                yield scrapy.Request(team_url,callback=self.parse_team)


    def parse_team(self,response):
        for player_url in response.css('div.x_list a::attr(href)').extract():
            if player_url:
                yield scrapy.Request(url=player_url,callback=self.parse_player)

    def parse_player(self,response):
        name = response.css('title::text').extract_first().split('|')[1]
        player_id = re.findall('.*?(\d+).html',response.url)[0]
        raw_salary = response.css('div.font p::text').extract()[-2]
        salary = re.findall('.*?(\d+).*',raw_salary)[0]

        player = HupuPlayerItem()
        player['name'] = name.strip()
        player['player_id'] = player_id
        player['salary'] = salary
        player['url'] = response.url

        yield player