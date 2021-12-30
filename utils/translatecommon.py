# -*- coding: utf-8 -*-
import sys
sys.path.append("../Config")
import config
import requests
import json
import html.parser
def translateText(text):
    if text=="":
        return ""
    r = requests.get(
        "https://translation.googleapis.com/language/translate/v2",
        params={
            "key": config.getGoogleTranslationKey(),
            "q": text,
            "target": "hi",
            "alt": "json",
            "source": "en"
        }
    )
    oajson=r.content.decode()
    oa=json.loads(oajson)
    if 'data' in oa and 'translations' in oa['data'] and len(oa['data']['translations'])>0:
        return oa["data"]["translations"][0]['translatedText']
    return ""


def translateTextH2E(text):
    if text=="":
        return ""
    r = requests.get(
        "https://translation.googleapis.com/language/translate/v2",
        params={
            "key": config.getTranslationKey(),
            "q": text,
            "target": "en",
            "alt": "json",
            "source": "hi"
        }
    )
    #print(r.content)
    oajson=r.content.decode()
    oa=json.loads(oajson)
    if 'data' in oa and 'translations' in oa['data'] and len(oa['data']['translations'])>0:
        tt= oa["data"]["translations"][0]['translatedText']
        #print(tt)
        tt=html.parser.unescape(tt)
        return tt
    return ""

def translateTextCachedH2E(mconn,text):
    mdb=mconn.translation_cache
    mcoll=mdb.hi_2_en
    mobjs=mcoll.find({'hi_text':text})
    for mobj in mobjs:
        return mobj['en_text']
    en_text=translateTextH2E(text)
    mcoll.insert_one({'en_text':en_text,'hi_text':text})
    return en_text
