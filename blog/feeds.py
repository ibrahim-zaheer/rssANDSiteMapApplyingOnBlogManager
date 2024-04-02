from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import posts
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

class blogFeed(Feed):
	title = "Ibrahim Zaheer"
	link = "/posts/"
	description = "RSS feed made for Blogging System"

	def items(self):
		return posts.objects.filter(status = 1)

	def item_title(self, item):
		return item.title
	
	def item_description(self, item):
		return item.metades

	def item_link(self, item):
	    return reverse('post_detail', args =[item.slug])

class atomFeed(Feed):
	feed_type = Atom1Feed
