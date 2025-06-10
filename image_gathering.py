from icrawler.builtin import GoogleImageCrawler

crawler = GoogleImageCrawler(storage={"root_dir":r"C:\Users\harap\OneDrive - Kanazawa University\デスクトップ\pokemon\pokemon_dataset\img\133_Eevee"})

crawler.crawl(keyword="イーブイ", max_num=20)