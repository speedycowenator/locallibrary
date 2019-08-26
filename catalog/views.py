from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from catalog.forms import SearchForm

from catalog.models import Article

from datetime import date
import datetime

from django.shortcuts import render, get_object_or_404
####################################


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Article = Article.objects.all().count()
    
    # Available books (status = 'a')
    
    # The 'all()' is implied by default.    
    
    context = {
        'num_articles': num_Article,
     
    
}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic



def year_archive(request, year):
   
    context = {'year': year}
    return render(request, 'catalog/year_archive.html', context)


def month_archive(request, year, month):
    a_list = Article.objects.filter(date_publication__month=month, date_publication__year=year)
    month_dictionary = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',   
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December',
        }
    context = {'month': month, 'year': year, 'article_list': a_list, 'month_long' : month_dictionary[month]}
    return render(request, 'catalog/month_archive.html', context)

  

class ArticleListView(generic.ListView):
    model = Article
   

class ArticleDetailView(generic.DetailView):
    model = Article
    

from django.db.models import Q

def search_console(request):
    model = Article
    form = SearchForm
    context = {'form' : form}
    return render(request, 'catalog/search-console.html', context)

class SearchResultsView(ListView):
    model = Article
    template_name = 'catalog/search_results.html'

    def get_queryset(self):
        text_search_1 = self.request.GET.get('text_search_1')
        if text_search_1 == '<all>':
            text_search_1 = ' '

        text_search_2 = self.request.GET.get('text_search_2')
        if text_search_2 == '<all>':
            text_search_2 = ' '
        
        text_search_3 = self.request.GET.get('text_search_3')
        if text_search_3 == '<all>':
            text_search_3 = ' '
        
        title_search_1 = self.request.GET.get('title_search_1')
        if title_search_1 == '<all>':
            title_search_1 = ' ' 
        
        before_date = self.request.GET.get('before_date')
        after_date = self.request.GET.get('after_date')


        article_list = Article.objects.filter(Q(summary__icontains=text_search_1)).filter(Q(summary__icontains=text_search_2)).filter(Q(summary__icontains=text_search_3)).filter(Q(title__icontains=title_search_1)).filter(Q(date_publication__year__lte=before_date)).filter(Q(date_publication__year__gte=after_date))
            
        return article_list


'''
        if  title_search_1 != '' and  text_search_1 != '':
            article_list = Article.objects.filter(Q(summary__icontains=text_search_1)).filter(Q(title__icontains=title_search_1))
            return article_list
        if  title_search_1 != '' and  text_search_1 == '': 
            article_list = Article.objects.filter(Q(title__icontains=title_search_1))
            return article_list
        if  title_search_1 == '' and  text_search_1 != '': 
            article_list = Article.objects.filter(Q(summary__icontains=text_search_1))
            return article_list

 
    '''


'''
def search_bar(request, search):
    model = Article
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list


    form = SearchForm(request.GET)
    search_data = {'after_date' : after_date}
    
    def get_search_data(self):
        return Article.objects.filter(
            date_publication__year >= after_date
        )


    context = {'form' : form, 'article_list': get_search_data(search)}
    return render(request, 'catalog/search_bar.html', context)
        
'''