# django-pagination
Django helps you manage paginated data – that is, data that’s split across several pages, with “Previous/Next” links.
All methods of pagination use the Paginator class. It actually splits a QuerySet into Page objects Given list of objects and the number of items you’d like to have on each page to Paginator class,  it gives you methods for accessing the items for each page. 

Basic Example:
>>>from django.core.paginator import Paginator
>>>from .models import Post
>>>posts = Post.objects.all()         
>>>paginator = Paginator(posts, 2)
>>>paginator.count          # gives total number of  objects
6
>>> paginator.num_pages    # gives total number of  pages
3
>>> paginator.page_range    # gives total number of  pages as iterator
range(1, 4)
>>> page1 = paginator.page(1)
>>> page1
<Page 1 of 3>
>>> page1.object_list
[‘title1’, 'title2’]
>>> page3.has_next()
False
>>> page3.has_previous()
True
>>> page3.has_other_pages()
True
>>> page3.next_page_number()
Traceback (most recent call last):
...
EmptyPage: That page contains no results
>>> page2.previous_page_number()
1
>>> page2.start_index() # The 1-based index of the first item on this page
4
>>> page2.end_index() # The 1-based index of the last item on this page
6
>>> p.page(0)
Traceback (most recent call last):
...
EmptyPage: That page number is less than 1

