#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author:xd 
   @file: avatar.py 
   @time: 2018/04/25
"""

import scrapy
import json
import os


class AvatarSpider(scrapy.Spider):

    name = 'avatar'

    def start_requests(self):
        url = 'http://stats.nba.com/'

        yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        file_name = os.path.join(os.path.dirname(__file__),'player_filter.json')
        with open(file_name,'r') as f:
            data = json.load(f)

        base_url = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/{team_id}/2017/260x190/{player_id}.png'

        image_urls = []
        for player in data:
            team_id = str(player['team_id'])
            player_id = str(player['player_id'])
            url = base_url.format(team_id=team_id, player_id=player_id)

            image_urls.append(url)

        yield {'image_urls' : image_urls}


# if __name__ == '__main__':
#     dir_name = os.path.dirname(__file__)
#     print(dir_name)