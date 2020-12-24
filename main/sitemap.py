from django.contrib.sitemaps import Sitemap
from blog.models import Blog

class MyBlogSiteMap(Sitemap):

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return Blog.objects.all()

    def location(self,item):
        return "/blog/" +str(item)