from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class authMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def process_response(self, request, response):
        if not request.user.is_authenticated and request.path != '/login/':
            return HttpResponseRedirect('/login/')
        return response


class LoginRequiredMiddleware(MiddlewareMixin):
    def process_response(self, request, response):

        if request.user.is_anonymous:  # 未ログインの処理

            if (request.path == '/') or ('/logout' in request.path) or ('/login' in request.path):  # ログインしなくても閲覧可能なページ
                return response

        else:  # 上記ページ以外に未ログインユーザーがアクセスして来たらトップページにリダイレクト
            return redirect('/')

        return response
