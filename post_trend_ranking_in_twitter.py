from config import twitter_api

# トレンドトピックのある場所とwoeidを取得
# available_trend_list = twitter_api().available_trends()

#トレンドを取得する地域のwoeid
woeid = {
    '日本':   23424856
}

# トレンド取得
trend_list = twitter_api().get_place_trends(woeid['日本'])
# ツイート内容を入れる空文字列を用意
tweet_text = ''

# タイムラインで降順になるように、50位からループを回す
for i in reversed(trend_list[0]['trends']):
    # ハッシュが含まれているか、含まれていなかったら#をつける
    if  '#' in i['name']:
        tweet_text = str(trend_list[0]['trends'].index(i)+1) + '位 ' + i['name'] + '\n' + tweet_text
    else:
        tweet_text = str(trend_list[0]['trends'].index(i)+1) + '位 #' + i['name'] + '\n' + tweet_text
    # 10位ごとにツイートする
    if trend_list[0]['trends'].index(i) % 10 == 0:
        twitter_api().update_status(tweet_text)
        # ツイートしたので、空文字列に戻す
        tweet_text = ''