# -*- coding: utf-8 -*-
"""
flaskr.py
アイディアの種

使い方
python flaskr.py

Tips
app.run(debug=True) Trueにしてると、自動更新とエラー表示(たぶん)


(2016/01/26) ver0.1 たたき台
"""
__version__ = 0.1
__app_name__ = 'Image Create Business'

# TODO: DB１要素Delete機能の追加

# all the imports
import os
import datetime
import sqlite3
from contextlib import closing
# all the imports
from flask import Flask, request, session, g, redirect
from flask import url_for, abort, render_template, flash
from flask_bootstrap import *

# アプリ生成
app = Flask(__name__)
Bootstrap(app)

# 各種設定情報を記述
DATABASE = 'flaskr.db'
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
DB_INIT = True
DEBUG = True
CSS_DEBUG = False
PAGE_TITLE = u'Image Create Business'

# app.config.from_object()
# from_object() では、与えられたオブジェクトの内で 大文字の変数をすべて取得します。大変便利ですね。
# 上記大文字の変数をすべてConfigに格納している。(便利)
# 今回は flask.py ファイル自体を 渡していますが、コンフィグを別ファイルに書いた場合には、適宜書き換えてください。
# TODO:Configを別ファイルに移動
app.config.from_object(__name__)

# app.config.from_envvar
# 環境変数から設定を引き継ぐことも出来ます from_envvar()
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# DB周り
# DB接続
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


# DBの初期化
def init_db():
    print 'init_db()'
    print '__name__'
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


#########################################################################
#
# 　デコレータ
#
# flaskは、DB処理の前後で別処理をするには以下のようなデコレータを利用することで可能になります。
# before_request() もしくわ after_request()
#########################################################################
# リクエストがきたらまずDBへ接続する。
@app.before_request
def before_request():
    print '__before_request()__'
    g.db = connect_db()


# リクエストに対する後処理
@app.teardown_request
def teardown_request(exception):
    print __name__
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


#########################################################################
#
# View
#
#########################################################################

def fetch_query(g, base=None, keys=None, table=None):
    """
    SQLクエリを生成する関数
    :param keys: リスト
    :param table: テーブル
    """
    if base==None:
        base = 'SELECT %s FROM %s order by id desc'
    column = ','.join(keys)
    query = base % (column, table)
    cur = g.db.execute(query)
    # Fetchはリストでカエルので，辞書に生計
    entries = [dict(zip(keys, row)) for row in cur.fetchall()]
    return entries

@app.route('/')
def top_page():
    """topページのVIEW"""
    flash(u'/top.htmlがひらかれました')

    # DBからエントリの取得
    # cur = g.db.execute('SELECT id, title, url, timestamp FROM tbl_images order by id desc')
    keys = ['id', 'title', 'url', 'timestamp']
    # base = 'SELECT %s FROM %s order by id desc'
    base = 'SELECT %s FROM %s order by id'
    table = 'tbl_images'
    entries = fetch_query(g=g, base=base, keys=keys, table=table)
    print entries

    # 取得したエントリを使ってhtmlをレンダリング
    return render_template('index.html', entries=entries)

# テストページ
@app.route('/test', methods=['GET'])
def test_flask():
    return 'Hello, World!', 200

# エントリー追加
@app.route('/add', methods=['POST'])
def add_entry():
    # if not session.get('logged_in'):
    #     abort(401)

    # SQLでクエリを保存
    print request
    g.db.execute(
        'insert into tbl_images ( title, url ) values (?,?)', [request.form['title'], request.form['url']])
    g.db.commit()

    flash(u'新しいエントリーが追加されました')

    # redirectとrender_templateの違い。おそらくPOSTのデータがクリアされている
    return redirect(url_for('top_page'))


#
# ログインとログアウト
# 以下のファンクションは、ユーザーのログインとログアウト時に使います。
# ログインには、ユーザーネームとパスワードを利用して行ない、session内に logged_in のキーで設定がセットされます。
# もし、ログイン済みの場合は、Keyは True がセットされている ので、ユーザは show_entries ページにリダイレクトされます。
# 追加メッセージで、ユーザに ログインが成功した事が通知され、もしエラーが発生した場合は、ユーザに再度入力を求める

# ログイン
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # POSTのみ利用可能
    if request.method == 'POST':
        # ユーザネームの照合(照合先は先に設定した設定変数)
        if request.form['username'] != app.config['USERNAME']:
            error = u'ユーザ名が間違っています'
        # パスワードの照合(照合先は先に設定した設定変数)
        elif request.form['password'] != app.config['PASSWORD']:
            error = u'パスワードが間違っています'
        # 照合成功!
        else:
            # ログインセッションをTrueにする。これが鍵になる。
            session['logged_in'] = True
            flash(u'ログインしました')
            # ログインできたら
            return redirect(url_for('top_page'))
    # ログイン失敗時に再度login.htmlへリダイレクトされる
    return render_template('login.html', error=error)


#
# ログアウト処理は、sessionからkeyを削除します。
# また、以下のような方法でもログアウト処理を行えます。
# pop() を 使用することでsession内からkeyを削除することが出来ます。
# 未ログイン状態でも 以下のメソッドは使用可能なので、ログイン状態チェックすることなく利用する事が 可能です。
#
# ログアウト
@app.route('/logout')
def logout():
    # pop() を 使用することでsession内からkeyを削除することが出来ます。
    session.pop('logged_in', None)
    flash(u'ログアウトしました')
    return redirect(url_for('top_page'))


if __name__ == '__main__':
    print __name__
    if DB_INIT:
        init_db()
    app.run(debug=DEBUG)
