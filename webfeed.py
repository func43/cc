from datetime import datetime

def rfc822():
    return datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")

def generate_rss():
    feed_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>My Web Feed</title>
    <link>https://www.mywebsite.com</link>
    <description>This is a sample RSS feed for latest updates.</description>
    <language>en-us</language>
    <lastBuildDate>{rfc822()}</lastBuildDate>

    <item>
      <title>New Cloud Computing Course Launched</title>
      <link>https://www.mywebsite.com/cloud-course</link>
      <description>Learn AWS, Google Cloud, and Azure basics.</description>
      <pubDate>{rfc822()}</pubDate>
    </item>

    <item>
      <title>AI Seminar Registration Open</title>
      <link>https://www.mywebsite.com/ai-seminar</link>
      <description>Participate in the upcoming AIML seminar.</description>
      <pubDate>{rfc822()}</pubDate>
    </item>

  </channel>
</rss>
"""

    with open("feed.xml", "w", encoding="utf-8") as file:
        file.write(feed_content)

    print("RSS feed created successfully as feed.xml")

generate_rss()
