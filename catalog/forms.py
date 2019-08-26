import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



class SearchForm(forms.Form):
    title_search_1 = forms.CharField(label='Title', max_length=100, required=False, initial='<all>') 
    text_search_1 = forms.CharField(label='Text', max_length=100, required=False, initial='<all>')
    text_search_2 = forms.CharField(label='Text', max_length=100, required=False, initial='<all>')
    text_search_3 = forms.CharField(label='Text', max_length=100, required=False, initial='<all>')

    #date restrictions
    year_choices = [('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015')]#, ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ]

    year_choices = tuple(year_choices)

    before_date = forms.ChoiceField(label='Before', choices = year_choices, initial='2015')
    after_date = forms.ChoiceField(label='After', choices = year_choices, initial='1997')


####


