# -*- coding: utf-8 -*-

from django import template
from school.viewMark import MAX_COL
register = template.Library()


@register.simple_tag
def convertMarkToCharacter(x):
    if x==1:
        return "aaaa"
    else:
        return """ bbbb"""

@register.filter
def convertHlToVietnamese(x):
    if x=='G':
        return u'Giỏi'
    elif x=='K':
        return u'Khá'
    elif x=='TB':
        return u'TB'
    elif x=='Y':
        return u'Yếu'
    elif x=='Kem':
        return u'Kém'
    else:
        return u''    
@register.filter
def convertMarkToCharacter(x):
    if x==9:
        return u'Giỏi'
    elif x==7:
        return u'Khá'
    elif x==6:
        return u'TB'
    elif x==4:
        return u'Yếu'
    elif x==1:
        return u'Kém'
    else:
        return  u''   
@register.filter
def convertHKToVietnamese(x):
    if x=='T':
        return u'Tốt' 
    elif x=='K':
        return u'Khá'
    elif x=='TB':
        return u'TB'
    elif x=='Y':
        return u'Yếu'
    else:
        return u''    
@register.filter
def convertDHToVietnamese(x):
    if x=='G':
        return u'HSG' 
    elif x=='TT':
        return u'HSTT'
    else:
        return u''

@register.filter
def filterNote(content,userId):
    contentList = content.split("/")
    for c in contentList:
        cs = c.split("##")
        if (cs[0]==str(userId)):
            return cs[1]
    return ""

@register.filter
def getMark(markStr,x):
    return "chao"
@register.filter
def toNumber(x,y):
    return int(x)*MAX_COL + int(y)