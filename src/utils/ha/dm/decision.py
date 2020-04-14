#!/usr/bin/env python3

"""
 ****************************************************************************
 Filename:          decision.py
 Description:       Dicision Maker

 Creation Date:     11/21/2019
 Author:            Ajay Paratmandali

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 ****************************************************************************
"""

import sys
import time
import asyncio
import re
from typing import Dict, List, Optional, Iterable

from eos.utils.queries import SortBy, SortOrder, QueryLimits, DateTimeRange
from eos.utils.ha.dm.models.decision import Decision
from eos.utils.data.db.db_provider import (DataBaseProvider, GeneralConfig)
from eos.utils.data.access.filters import Compare, And, Or
from eos.utils.data.access import Query, SortOrder

class DecisionMaker:
    def __init__(self, db):
        self.decision_db = ConsulDecisionDB(db)
        self.rule_engine = RulesEngine()

    async def send_alert(self, alert):
        """
        Interface to set alert for decision.
        """
        payload = await self.rule_engine.process_request(alert)
        Decision = Decision.instantiate_decision(payload)
        return await self.decision_db.create(Decision)

class RulesEngine:
    def __init__(self):
        pass

    async def process_request(self, alert):
        pass

