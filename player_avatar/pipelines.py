# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.images import ImagesPipeline
from os.path import join,basename
from urllib.parse import urlparse

class PlayerAvatarPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        dir_path = 'download_avatar'
        file_name = basename(path)
        return join(dir_path,file_name)
