# 開放台灣民間租屋資料

長期收集各租屋網站、品牌公寓的可公開資訊，清洗後整理成格式統一的資料，供後續有需要的人使用。

- 專案資訊請見 [hackpad](https://g0v.hackpad.tw/Ih7Jp4pUD5y)。


# 程式使用方式與注意事項：

## 爬蟲

### 環境需求
1. Python3 + pip

### 使用方式
```
# 安裝相關套件
virtualenv -p python3 .
pip install -r requirements.txt

cd backend
# 設定資料庫與使用環境
cp settings.sample.py settings.py
vim settins.py

# 設定 Scrapy
cp crawler/settints.sample.py crawler/settings.py
vim crawler/settings.py

# 設定資料庫
python tools/setup_db.py

# 開始爬資料
./go.sh
```

### 注意事項

1. 請友善對待租屋網站，下載頻率不要超過一般人類的使用習慣，可使用 Scrapy 內附的
   [DOWNLOAD_DELAY](https://doc.scrapy.org/en/latest/topics/settings.html#std:setting-DOWNLOAD_DELAY) 或 
   [AUTO_THROTTLING](https://doc.scrapy.org/en/latest/topics/autothrottle.html) 調整爬蟲速度。
2. 爬蟲以收集各網站可散佈的共同資料欄位為主，不會儲存所有網頁上的欄位。
3. 其他事項請參見[授權頁面](LICENSE)。


