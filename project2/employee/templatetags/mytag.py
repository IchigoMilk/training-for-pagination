# フィルタやタグを登録するのに使うモジュール
from django import template

register = template.Library()

# @あっと付きはデコレータ
@register.simple_tag
def url_replace(request, field, value):
  # GETパラメータのfield部分をvalueに置き換える
  url_dict = request.GET.copy()
  url_dict[field] = value
  return url_dict.urlencode()
