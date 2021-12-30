def getMongodataDateRange():
    day_1=datetimeutils.getPastMongoDate(2)
    day_2=datetimeutils.getPastMongoDate(1)
    print(day_1)
    day_dates[startDay]={}
    mObjs=pcoll.find({"$and":[{"$and":[{'registrationDate':{"$gte":day_1}},{'registrationDate':{"$lt":day_2}}]},{"goal":"Spoken"}]})
