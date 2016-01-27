# Image>Create>Business

ワンポイントIdeaをためていくWebアプリ.

サクラレンタルサーバーにアップロードしてるが動作できずストップ(2016/1/26)

## sakuraレンタルサーバー作業ログ
どうもcgiで動作できない。Internal Server Error。
パーミッションをすべて755にしてるがだめ。testappは起動できている。

## git clone
```
>git clone https://github.com/peace098beat/ImageCreateBuesiness
```

## git pull
リモートリポジトリの差分を更新
```
>git pull origin
```

## エラー対策
```
Internal Server Error

The server encountered an internal error or misconfiguration and was unable to complete your request.
Please contact the server administrator, support@sakura.ad.jp and inform them of the time the error occurred, and anything you might have done that may have caused the error.
More information about this error may be available in the server error log.
```


## パーミッション
```
>chmod 755 ./*
>再帰
>chmod -R 755 ./*
```

![img](./version0.1.0.jpg)
# SQLiteの使い方

# IDの自動インクリメント
    # AUTOINCREMENT削除されても同じIDは使われない
    ID INTEGER PRIMARY KEY AUTOINCREMENT,

# 自動でタイムスタンプを追加する
CREATE TABLE GPS_Logger (
    ID INTEGER PRIMARY KEY,
    t TIMESTAMP CURRENT_TIMESTAMP  <-INSERT時に値を指定しなければTIMESTAMPにはタイムスタンプが自動で指定
    t TIMESTAMP DEFAULT (DATETIME(‘now’,’localtime’)) <-デフォルトTimeZoneをJST
    )

CURRENT_TIME         HH:MM:SS
CURRENT_DATE         YYYY-MM-DD
CURRENT_TIMESTAMP    YYYY-MM-DD HH:MM:SS