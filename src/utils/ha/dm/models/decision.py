#!/usr/bin/env python3

"""
 ****************************************************************************
 Filename:          decision.py
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
import json
import bcrypt
from schematics.models import Model
from schematics.types import IntType, StringType, DateType, ListType, DateTimeType
from datetime import datetime, timedelta, timezone
from typing import Optional, Iterable
from enum import Enum

from eos.utils.data.access import BaseModel
from eos.utils.queries import SortBy, QueryLimits, DateTimeRange

class Decision(BaseModel):
    _id = "decision_id"

    decision_id = StringType()
    alert_type = StringType()
    severity = ListType(StringType)
    action = StringType()

    @staticmethod
    def instantiate_decision(**dicision_payload):
        decision = Decision()
        Decision.decision_id = dicision_payload.decision_id
        Decision.alert_type = dicision_payload.alert_type
        Decision.severity = dicision_payload.severity
        Decision.action = dicision_payload.action
        return Decision
