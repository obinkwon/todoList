# 날짜 util
from datetime import datetime, timedelta


# 날짜 문자열로 가져오기
def str_date(format, day=0): # 날짜 포맷, 오늘로부터 이전 날짜 (-)
    # 현재 날짜 가져오기 (default)
    today = datetime.now()

    if day > 0:
        today = today - timedelta(days=day)
    return today.strftime(format)
