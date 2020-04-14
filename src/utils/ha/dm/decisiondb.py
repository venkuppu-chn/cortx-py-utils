#!/usr/bin/env python3

"""
 ****************************************************************************
 Filename:          decisiondb.py
 Description:       Dicision for consul

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

class DecisionDB:
    def __init__(self):
        pass

    def create(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass

    def get_list(self):
        pass

class ConsulDecisionDB(DecisionDB):
    """
    The class encapsulates decision management activities.
    This is intended to be used during decision management
    """
    def __init__(self, storage: DataBaseProvider) -> None:
        self.storage = storage

    async def create(self, decision: Decision) -> Decision:
        """
        Stores a new Decision
        :param decision: Decision model instance
        """
        return await self.storage(Decision).store(decision)

    async def get(self, decision_id) -> Decision:
        """
        Fetches a single decision.
        :param decision_id: decision identifier
        :returns: decision object in case of success. None otherwise.
        """
        all_decision = await self.get_list()
        for decision in all_decision:
            if decision["decision_id"].lower() == decision_id.lower():
                return decision
        return None

    async def delete(self, decision_id: str) -> None:
        await self.storage(Decision).delete(Compare(Decision.decision_id, '=', decision_id))

    async def get_list(self, offset: int = None, limit: int = None,
                       sort: SortBy = None) -> List[User]:
        """
        Fetches the list of Decision.
        :param offset: Number of items to skip.
        :param limit: Maximum number of items to return.
        :param sort: What field to sort on.
        :returns: A list of Decision models
        """
        query = Query()

        if offset:
            query = query.offset(offset)

        if limit:
            query = query.limit(limit)

        if sort:
            query = query.order_by(getattr(Decision, sort.field), sort.order)
        return await self.storage(Decision).get(query)

    async def count(self):
        return await self.storage(Decision).count(None)

    async def save(self, decision: Decision):
        """
        Stores an already existing Decision.
        :param Decision:
        """
        await self.storage(Decision).store(decision)

