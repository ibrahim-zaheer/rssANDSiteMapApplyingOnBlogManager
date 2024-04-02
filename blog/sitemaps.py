from django.contrib.sitemaps import Sitemap
from .models import posts

# sitemap class
class blogSitemap(Sitemap):
# change frequency and priority
	changefreq = "daily"
	priority = 1.0

	def items(self):
		return posts.objects.filter(status = 1)

	def lastmod(self, obj):
		return obj.updated_on
