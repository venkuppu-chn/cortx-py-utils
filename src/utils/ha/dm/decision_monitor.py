#!/usr/bin/env python3

"""
 ****************************************************************************
 Filename:          decision_monitor.py
 Description:       Decision Monitor

 Creation Date:     04/15/2020
 Author:            Ajay Paratmandali

 Do NOT modify or remove this copyright and confidentiality notice!
 Copyright (c) 2001 - $Date: 2015/01/14 $ Seagate Technology, LLC.
 The code contained herein is CONFIDENTIAL to Seagate Technology, LLC.
 Portions are also trade secret. Any use, duplication, derivation, distribution
 or disclosure of this code, for any reason, not expressly authorized is
 prohibited. All other rights are expressly reserved by Seagate Technology, LLC.
 ****************************************************************************
"""
from eos.utils.ha.hac import const
from eos.utils.ha.dm.repository.node_status import NodeStatusDB
from eos.utils.ha.dm.dm.node_status import NodeStatusModel

class DecisionMonitor:
    def __init__(self):
        self._local_node = None
        self._node_status = NodeStatusDB()

    def acknowledge_events(self, entity, entity_id, node_id, component,
                           component_id):
        """
        Acknowledge all event for related path.
        """
        pass

    def get_status(self, node_id, path, **kwargs):
        """
        Get status for io and management path.
        Check entity for local node:
            if they are same then then check functional path.
            if they are different then check recovery path.
        Functional status:
        Recovery status:
        """
        data = self._node_status.get(node_id)
        if not data or isinstance(data[0], NodeStatusModel):
            return True
        if path == const.io:
            if data[0].io_failure_count == 0:
                return True
        elif path == const.mgmt:
            if data[0].mgmt_failure_count == 0:
                return True
        return False
