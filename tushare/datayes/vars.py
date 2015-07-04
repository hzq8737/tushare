#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Created on 2015年7月4日
@author: JimmyLiu
@QQ:52799046
"""
import sys
PY3 = (sys.version_info[0] >= 3)

_MASTER_HEAD = '/api/master/'
TRADE_DATE = _MASTER_HEAD + 'getTradeCal.csv?exchangeCD=%s&beginDate=%s&endDate=%s&field=%s'
SEC_ID = _MASTER_HEAD + 'getSecID.csv?ticker=%s&partyID=%s&cnSpell=%s&assetClass=%s&field=%s'
EQU_INFO = _MASTER_HEAD + 'getEquInfo.csv?ticker=%s&pagesize=%s&pagenum=%s&field=%s'
REGION = _MASTER_HEAD + 'getSecTypeRegion.csv?field=%s'
REGION_REL = _MASTER_HEAD + 'getSecTypeRegionRel.csv?ticker=%s&typeID=%s&secID=%s&field=%s'
SEC_TYPE = _MASTER_HEAD + 'getSecType.csv?field=%s'
SEC_TYPE_REL = _MASTER_HEAD + 'getSecTypeRel.csv?ticker=%s&typeID=%s&secID=%s&field=%s'
