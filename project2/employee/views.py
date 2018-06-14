from django.views import generic
from .forms import SearchForm
from .models import Employee

# TemplateViewは適当な仮のテンプレに使いやすい
class IndexView(generic.ListView):
  model = Employee
  # 勝手に読み込まれる
  # template_name = 'employee/employee_list.html'

  paginate_by = 2

  def get_context_data(self):
    # オーバーライドしなければテンプレートに渡す辞書の作成
    context = super().get_context_data() # 元の処理
    context['form'] = SearchForm(self.request.GET)
    return context

  def get_queryset(self):
    # オーバーライドしなければテンプレートに渡すemployee_listの作成
    form = SearchForm(self.request.GET)
    form.is_valid() # これをしないとcleaned_dataができない

    # 全社員を取得
    queryset = super().get_queryset() # 元の処理

    # 部署の選択があれば絞り込み
    department = form.cleaned_data['department']
    if department: # 部署が選択できていれば…
      queryset = queryset.filter(department=department)

    # サークルの選択があれば絞り込み
    club = form.cleaned_data['club'] # モデルのインスタンスが格納される
    if club:
      queryset = queryset.filter(club=club)

    return queryset
