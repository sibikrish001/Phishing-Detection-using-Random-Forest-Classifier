import joblib
from flask import Flask,render_template,request
app=Flask(__name__)
import re
from urllib.parse import urlparse
import socket
import ipaddress
import requests
import os



result=""



def unshorten_url(url):
    try:
        response = requests.head("https://"+url, allow_redirects=True)
        return response.url
    except requests.exceptions.RequestException:
        return None



def has_brackets_or_parentheses(url):
    if '[' in url or ']' in url or '(' in url or ')' in url:
        return 1
    else:
        return 0



def anchor_tag(url):
    # Send a GET request to fetch the HTML content
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

    # Count the number of anchor tags
        return len(soup.find_all("a"))
    except requests.exceptions.RequestException as e:
        return 0


def iframe_count(url):
    # Send a GET request to fetch the HTML content
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        response.raise_for_status()
        iframe_tags = soup.find_all('iframe')
        return len(iframe_tags)
    except requests.exceptions.RequestException as e:
        return 0

def pctExtHyperlinks(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.content
    # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')
    # PctExtHyperlinks
        total_hyperlinks = len(soup.find_all('a'))
        external_hyperlinks = len([link for link in soup.find_all('a') if link.get('href') and 'http' in link.get('href')])
        return (external_hyperlinks / total_hyperlinks) * 100 if total_hyperlinks > 0 else 0
    except requests.exceptions.RequestException as e:
        return 0


def pctExtResourceUrls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        total_resource_urls = len(soup.find_all(['img', 'script', 'link', 'iframe']))
        external_resource_urls = len([resource for resource in soup.find_all(['img', 'script', 'link', 'iframe']) if
                                  resource.get('src') and 'http' in resource.get('src')])
        return (external_resource_urls / total_resource_urls) * 100 if total_resource_urls > 0 else 0
    except requests.exceptions.RequestException as e:
        return 0


def  extFavicon(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        favicon_links = soup.find_all('link', rel='icon')
        return int(any(link.get('href').startswith('http') for link in favicon_links))
    except requests.exceptions.RequestException as e:
        return 0


def insecureForms(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")
        forms = soup.find_all('form')
        return int(any(form.get('action', '').startswith('http://') for form in forms))
    except requests.exceptions.RequestException as e:
        return 0

def ratio_of_numbers_to_letters(url):
    numbers = sum(c.isdigit() for c in url)
    letters = sum(c.isalpha() for c in url)
    return numbers / letters if letters else float('inf')


def get_domain_age(url):
    try:
        whois_info = whois.whois(url)
        creation_date = whois_info.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(creation_date, datetime.datetime):
            today = datetime.datetime.now()
            age = today - creation_date
            return age.days
    except Exception as e:
        print("Error:", e)
    return -1



def count_non_ascii_characters(url):
    count = 0
    for char in url:
        if ord(char) > 127:
            count += 1
    return count


def subdomains_to_domain_length_ratio(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2]  # Extract the domain part
    subdomains = parsed_url.netloc.split('.')[:-2]  # Extract subdomains
    subdomain_count = len(subdomains)
    domain_length = len(domain)

    if domain_length > 0:
        return subdomain_count / domain_length
    else:
        return 0


def has_excessive_subdomains(url):
    threshold=2
    parsed_url = urlparse(url)
    subdomains = parsed_url.hostname.split('.')
    num_subdomains = len(subdomains) - 2  # Subtract TLD and domain

    return 1 if num_subdomains > threshold else 0





def symbolAt(url):
    return  int('@' in url)


def countDot(url):
    return url.count('.')


def urlLength(url):
    return len(url)


def dashInHostname(url):
    return urlparse(url).netloc.count('-')




def noHttps(url):
    return 1 if not url.startswith('https://') else 0


def subDomainLevel(url):
    parts = url.split('.')
    a = len(parts) - 2
    if len(parts) >= 3 and parts[0].lower() == 'www':
        a-= 1
    return a


def pathLevel(url):
    s= url.split('://')[-1]
    s1 = s.split('/')
    a = len([i for i in s1 if i.strip() != ''])
    return a


def pathLength(url):
    return len(urlparse(url).path)


def numUnderscore(url):
    return url.count('_')


def numPercent(url):
    return url.count('%')


def numAmpersand(url):
    return url.count('&')


def numHash(url):
    return url.count('#')


def numNumericCharacter(url):
    s=sum(1 for i in url if i.isdigit())
    return s


def numDash(url):
    return url.count('-')

def is_ipaddress(url):
    return 1 if re.match(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', urlparse(url).netloc) else 0


def tildeSymbol(url):
    return 1 if '~' in url else 0


def randomString(url):
    return 1 if re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', url) else 0


def hn_Length(url):
    return len(urlparse(url).netloc)

def dsInPath(url):
    parts = url.split("://")
    if len(parts) > 1:
        path = parts[1]
        return 1 if "//" in path else 0


def nqComponents(url):
    return len(urlparse(url).query.split('&'))


def fdnMismatch(url):
    parsed_url = urlparse(url)
    frequent_domains = [
        "copyright.com","google.com", "youtube.com", "facebook.com", "wikipedia.org", "twitter.com",
        "amazon.com", "instagram.com", "linkedin.com", "netflix.com", "reddit.com",
        "yahoo.com", "bing.com", "live.com", "microsoft.com", "ebay.com", "office.com",
        "apple.com", "pinterest.com", "whatsapp.com", "blogspot.com", "tumblr.com",
        "adobe.com", "dropbox.com", "stackoverflow.com", "medium.com", "wordpress.com",
        "quora.com", "github.com", "flipkart.com", "snapdeal.com", "paytm.com",
        "hdfcbank.com", "sbi.co.in", "axisbank.com", "icicibank.com", "irctc.co.in",
        "indiatimes.com", "naukri.com", "timesofindia.indiatimes.com", "hindustantimes.com",
        "indianexpress.com", "economictimes.indiatimes.com", "moneycontrol.com", "firstpost.com",
        "rediff.com", "cricbuzz.com", "zeenews.india.com", "ndtv.com", "aajtak.intoday.in",
        "news18.com", "thehindu.com", "jagran.com", "bollywoodhungama.com", "filmibeat.com",
        "bookmyshow.com", "makemytrip.com", "yatra.com", "cleartrip.com", "goibibo.com",
        "airindia.in", "jetairways.com", "spicejet.com", "indigo.in", "vistara.com",
        "etihad.com", "emirates.com", "qatarairways.com", "britishairways.com", "airasia.com",
        "olx.in", "quickr.com", "magicbricks.com", "99acres.com", "housing.com", "commonfloor.com",
        "zomato.com", "swiggy.com", "foodpanda.com", "dominos.co.in", "pizzaonline.dominos.co.in",
        "mcdelivery.co.in", "ubereats.com", "ola.com", "uber.com", "rapido.bike", "shuttl.com",
        "redseer.com", "lenskart.com", "titan.co.in", "tanishq.co.in", "bluestone.com",
        "caratlane.com", "pcjeweller.com", "kalyanjewellers.net", "joyalukkas.com",
        "malabargoldanddiamonds.com", "pngadgil.com", "voylla.com", "ctbuh.org", "skyscrapercenter.com"
    ]
    domain = parsed_url.netloc.split(':')[0]

    if any(domain.endswith(fd) or domain == fd for fd in frequent_domains):
        return 0
    else:
        return 1 #detected



def query_length(url):
    return len(urlparse(url).query)


def domiSubdomains(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split('.')[-2]
    subdomains = parsed_url.netloc.split('.')[:-2]
    return 1 if domain in subdomains else 0


def domiPaths(url):
    return 1 if urlparse(url).netloc.split('.')[0] in urlparse(url).path else 0


def hiHostname(url):
    return 1 if 'https' in urlparse(url).netloc else 0


def numSenWords(url):
    phishing_patterns = [
        r"account|login|signin|verify|password",
        r"bank|paypal|secure|finance|payment",
        r"alert|urgent|confirm|update|verify",
        r"click|link|redirect|url|website",
        r"free|discount|offer|win|prize",
        r"official|legit|secure|authentic",
        r"verify|validation|validate|auth",
        r"ssl|https|secure|encrypted",
        r"\d{4,6}-\d{4,6}-\d{4,6}-\d{4,6}",
        r"phishing|scam|fraud|hack|spoof",
        r"login\.|signin\.|paypal\.|secure\.",
        r"update\-|verify\-|password\-",
        r"(\b[0-9a-fA-F]{40}\b)",
        r"(\b[0-9a-fA-F]{64}\b)",
        r"account[-_]?recovery",
        r"apple[-_]?id|itunes[-_]?login",
        r"amazon[-_]?signin",
        r"google[-_]?account[-_]?recovery",
        r"microsoft[-_]?account[-_]?security",
        r"paypal[-_]?verification[-_]?",
        r"irs[-_]?refund[-_]?status",
        r"irs[-_]?tax[-_]?refund[-_]?",
        r"irs[-_]?gov[-_]?",
        r"online[-_]?banking[-_]?login",
        r"update[-_]?your[-_]?password",
        r"security[-_]?alert[-_]?",
    ]
    count = 0

    for pattern in phishing_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            count += 1

    return count


def output(a):
    if a[0] == 0:
        return "The URL is predicted to be a legitimate URL."
    else:
        return "The URL is predicted to be a Phishing URL."


def work(url):
    my_feature =[[countDot(url),subDomainLevel(url),pathLevel(url),urlLength(url),dashInHostname(url),symbolAt(url),numUnderscore(url),numPercent(url),numAmpersand(url),numHash(url),
  numNumericCharacter(url),noHttps(url),pathLength(url),is_ipaddress(url),tildeSymbol(url),hn_Length(url),dsInPath(url),query_length(url),nqComponents(url),fdnMismatch(url),
  numSenWords(url),numDash(url),domiSubdomains(url),domiPaths(url),hiHostname(url),ratio_of_numbers_to_letters(url),has_brackets_or_parentheses(url),count_non_ascii_characters(url),subdomains_to_domain_length_ratio(url),has_excessive_subdomains(url)
  ]]
    loaded = joblib.load("C:/Users/prave/PycharmProjects/pythonProject5/CAT96.pkl")
    a=loaded.predict(my_feature)
    result=output(a)
    return result


picFolder=os.path.join('static','pics')
app.config['UPLOAD_FOLDER']=picFolder



@app.route('/')
def index():
    img=os.path.join(app.config['UPLOAD_FOLDER'],'img.jpg')
    return render_template('html2.html',u_img=img)

@app.route('/', methods=['POST'])
def process_input():
    url = request.form['user_input']
    result=work(url)
    img = os.path.join(app.config['UPLOAD_FOLDER'], 'img.jpg')
    return render_template('html2.html',u_img=img,Result=result)

if __name__=="__main__":
    app.run(debug=True)


