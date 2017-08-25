import urllib2


class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return
        respone = urllib2.urlopen(url)
        if respone.getcode()!=200:
            return None
        return respone.read()