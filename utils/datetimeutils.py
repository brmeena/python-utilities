from datetime import datetime
from datetime import timedelta
def getTodayDate(format):
    nowTime=datetime.today()
    todayDate=nowTime.strftime(format)
    return todayDate

def getTomorrowDate(format):
    nowTime=datetime.today()
    tomorrowTime=nowTime+timedelta(days=1)
    tomorrowDate=tomorrowTime.strftime(format)
    return tomorrowDate

def getPastDate(format,days):
    nowTime = datetime.today()
    ydTime = nowTime - timedelta(days=days)
    ydDate = ydTime.strftime(format)
    return ydDate

def getFutureDate(format,days):
    nowTime = datetime.today()
    ydTime = nowTime + timedelta(days=days)
    ydDate = ydTime.strftime(format)
    return ydDate

def getPastMongoDate(days):
    nowTime = datetime.today()
    ydTime = nowTime - timedelta(days=days)
    ydTime=datetime.combine(ydTime, datetime.min.time())
    return ydTime



def getYesterdayDate(format):
    nowTime = datetime.today()
    ydTime = nowTime - timedelta(days=1)
    ydDate = ydTime.strftime(format)
    return ydDate

def getAgeFromDate(dateStr):
    currentTime = datetime.now()
    dobTimeObj = datetime.strptime(dateStr, "%d/%m/%Y")
    time_diff = (currentTime - dobTimeObj).total_seconds()
    td_yrs = time_diff / (60 * 60 * 24 * 365)
    return td_yrs


