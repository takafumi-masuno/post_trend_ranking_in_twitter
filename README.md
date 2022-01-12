# post_trend_ranking_in_twitter

twitter の日本のトレンドランキング bot

twitter の日本のトレンドを毎時取得して、
ランキングをツイートする bot です。

heroku にデプロイして、Heroku Scheduler というアドオンを
使用して、毎時実行しています。

ローカルで使用する場合は
twitter Developer
https://developer.twitter.com/en/portal/dashboard

（「Essential」アクセスでは、api でツイートができないので、
「Elevated」アクセスを申し込まないといけない。）

でキーとトークンを発行し、
ルートディレクトリ.env ファイルを作成し
.env ファイルに

```
CONSUMER_KEY    = '発行したConsumer Key'
CONSUMER_SECRET = '発行したSecret Consumer Key '
ACCESS_TOKEN    = '発行したAccess Token'
ACCESS_SECRET   = '発行したSecret Access Token'
```

記述して保存すれば、使用できます。
