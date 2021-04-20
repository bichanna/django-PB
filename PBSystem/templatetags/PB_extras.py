
from django import template
from django.shortcuts import resolve_url
from urllib import parse

register = template.Library()

@register.simple_tag
def get_return_link(request):
	"""
		一つ前のページのURLを取得するテンプレートタグ
	"""
	top_page = resolve_url("PBSystem:bank_account_data_list")
	referer = request.environ.get("HTTP_REFERER")

	if referer:


		parse_result = parse.urlparse(referer)
		if request.get_host() == parse_result.netloc:
			return referer
	#なければトップページへ
	return top_page


@register.simple_tag
def url_replace(request, field, value):
	"""
		GETパラメータの一部を書き換える。
	"""
	url_dict = request.GET.copy()
	url_dict[field] = str(value)
	return url_dict.urlencode()