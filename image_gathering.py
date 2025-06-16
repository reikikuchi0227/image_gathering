import os
import hashlib
from PIL import Image
from icrawler.builtin import GoogleImageCrawler
    

keywords = ['イーブイ','イーブイ ぬいぐるみ', 'イーブイ アニメ', 'イーブイ アニメ']

for keyword in keywords:
    crawler = GoogleImageCrawler(storage={"root_dir":r"C:\Users\harap\OneDrive - Kanazawa University\デスクトップ\pokemon\pokemon_dataset\img\133_Eevee"})
    crawler.crawl(keyword = keyword, max_num=50)