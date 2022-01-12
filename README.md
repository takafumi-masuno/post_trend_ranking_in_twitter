# twitter の日本のトレンドランキング bot

## twitter の日本のトレンドを毎時取得して、ランキングをツイートするbotのプログラムです。

実際にはheroku にデプロイして、Heroku Scheduler というアドオンを
<br>
使用して、毎時実行しています。
<br>
<br>
ローカルで使用する場合は
<br>
<br>
twitter Developer
<br>
https://developer.twitter.com/en/portal/dashboard
<br>
<br>
（「Essential」アクセスでは、api でツイートができないので、
<br>
「Elevated」アクセスを申し込まないといけない。）
<br>
<br>
でキーとトークンを発行し、
<br>
<br>
ルートディレクトリに.env ファイルを作成し
<br>
作成した.env ファイルに
<br>
```
CONSUMER_KEY    = '発行したConsumer Key'
CONSUMER_SECRET = '発行したSecret Consumer Key '
ACCESS_TOKEN    = '発行したAccess Token'
ACCESS_SECRET   = '発行したSecret Access Token'
```
記述して保存すれば、使用できます。
