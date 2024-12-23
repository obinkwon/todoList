# 날짜 util
from datetime import datetime, timedelta


def str_date(format, day=0):
    """
    날짜 문자열로 가져오기

    :param format: 날짜 포맷
    :param day: 오늘로부터 이전 날짜 (-) (default : 0)
    """
    # 현재 날짜 가져오기 (default)
    today = datetime.now()

    if day > 0:
        today = today - timedelta(days=day)
    return today.strftime(format)


def format_date(format, date=str_date("%Y%m%d")):
    """
    날짜 포맷 변경

    :param format: 날짜 포맷
    :param date: 날짜_문자열 (default: 오늘)
    """
    currdate = datetime.strptime(date, "%Y%m%d")
    return currdate.strftime(format)
