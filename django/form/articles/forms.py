from django import forms
from .models import Article

class ArticleForm(forms.Form):
    title=forms.CharField(label='제목')
    content=forms.CharField(label='내용',widget=forms.Textarea(attrs={
        'rows':5,
        'cols':50,
        'placeholder':'내용을 입력하세요.',
    }))
    
class ArticleModelForm(forms.ModelForm):
    title=forms.CharField(label='제목')
    
    class Meta: #이건 무조건 Meta!!클래스의 정보가 담겨있는 클래스
        model=Article
        fields=['title','content']
        
        