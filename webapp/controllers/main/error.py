from flask import render_template
from . import main

# 全局错误处理
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
# 模块错误处理
# @main.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
# @main.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500