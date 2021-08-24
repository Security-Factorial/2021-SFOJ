from django import forms
from sfoj_system.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board  # 사용할 모델
        fields = ['Title','Content']  # BoardForm에서 사용할 Board 모델의 속성

        labels = {
            'Title' : '제목',
            'Content' : '내용',
        }