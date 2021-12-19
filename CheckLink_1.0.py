import praw
import re
import vt

client = vt.Client("Virus Total API ID")

reddit = praw.Reddit(
    client_id="reddit client ID",
    client_secret="reddit secret",
    user_agent="<console:CheckLink:1.0>",
    password="reddit password",
    username="reddit username",
)  

def sort(result):

    harmless = result["harmless"]

    malicious = result["malicious"]

    suspicious = result["suspicious"]

    undetected = result["undetected"]

    if malicious > 0:
        reply = "CLICKING ON THE LINK ABOVE IS EXTREMELY DANGEROUS! THE WEBSITE ABOVE HAS THE RATING *MALICIOUS*!"

    elif suspicious > 0:
        reply = "CLICKING ON THE LINK ABOVE IS RISKY! THE WEBSITE ABOVE HAS THE RATING *SUSPICIOUS*!"

    else:
        reply = "The link above appears to be fine but I am just a silly bot. I could be wrong. As always proceed with caution. Surf Safely ;)"

    return reply
    

def virus_scan(domain):
    url_id = vt.url_id(domain)
    url = client.get_object("/urls/{}", url_id)
    result = url.last_analysis_stats
    return result


def find_link(string):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)
    raw_link_list = [x[0] for x in url]
    link = raw_link_list[0]
    domain = link.split('/')[2]
    return domain

    

def calls(parent):
    link = find_link(parent)
    print(link)
    result = virus_scan(link)
    print(result)
    reply = sort(result)
    return reply

def main():
    while True:
        for mention in reddit.inbox.unread(limit=None):
            try:
                parent = mention.parent().body
                print(parent)
                reply = calls(parent)
                mention.reply(reply)
                mention.mark_read()
            except:
                pass

main()

        
        
        