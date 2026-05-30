import feedparser
import time

FEEDS = {
    "ar": [
        "https://www.aljazeera.net/xml/rss/all.xml",
        "https://feeds.bbci.co.uk/arabic/rss.xml",
    ],
    "en": [
        "https://feeds.bbci.co.uk/news/rss.xml",
        "https://feeds.reuters.com/reuters/topNews",
    ],
}


def get_headlines():
    headlines = []
    for lang, urls in FEEDS.items():
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                headlines.append(
                    {
                        "title": entry.title,
                        "language": lang,
                        "source": (
                            feed.feed.title if hasattr(feed.feed, "title") else url
                        ),
                        "url": entry.link,
                    }
                )
    return headlines


if __name__ == "__main__":
    headlines = get_headlines()
    for h in headlines:
        print(h)
