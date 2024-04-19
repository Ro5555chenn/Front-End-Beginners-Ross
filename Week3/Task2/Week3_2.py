# 抓取標題內頁HTML
import urllib.request as req
import bs4
import csv

def findDate(link):
    # 建立一個 Request 物件，附加 Request Header 的資訊
    request=req.Request(link, headers = {
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # 解析原始碼，取得每篇文章標題

    soup = bs4.BeautifulSoup(data,"html.parser") # 用 BeautifulSoup 解析網頁程式碼
    date = soup.find_all("span", class_ = "article-meta-value")
    if len(date) > 3:
        date = date[3].string
    else:
        date = ""
        
    like_count = 0
    dislike_count = 0
    tags = soup.find_all("div", class_="push")
    for tag in tags:
        push_tag = tag.find("span", class_="hl push-tag")
        if push_tag != None:
            tag_text = push_tag.string.strip()
            if '推' == tag_text:
                like_count += 1
            elif '噓' == tag_text:
                dislike_count += 1
    return date, like_count, dislike_count


# 抓取 ptt 樂透版原始碼(HTML)
def getData(url):
    results = []
    # 建立一個 Request 物件，附加 Request Header 的資訊
    for page in range(3):
        request=req.Request(url, headers = {
            "cookie":"over18=1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        # 解析原始碼，取得每篇文章標題
        soup = bs4.BeautifulSoup(data,"html.parser") # 用 BeautifulSoup 解析網頁程式碼
        articles = soup.find_all("div", class_ = "r-ent")

        for article in articles: 
            title = article.find("div", class_="title")  #尋找 class="title" 的 div 標籤
            if title.a != None:
                title = title.a.string
                page_link = article.find("a",string = title)
                link = "https://www.ptt.cc" + page_link["href"]
                publish_date, like_count, dislike_count = findDate(link)
                results.append([title, like_count, dislike_count, publish_date])
            else:
                continue
        next_page = soup.find("a",string="‹ 上頁")
        url = "https://www.ptt.cc" + next_page["href"]

    with open('article.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(results) 

if __name__ == "__main__":
    getData("https://www.ptt.cc/bbs/Lottery/index.html")



