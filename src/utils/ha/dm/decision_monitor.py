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
import asyncio
from eos.utils.ha.hac import const
from eos.utils.schema.payload import Json
from eos.utils.ha.dm.repository.node_status import NodeStatusDB
from eos.utils.ha.dm.models.node_status import NodeStatusModel
from eos.utils.ha.dm.models.decisiondb import DecisionDB

class DecisionMonitor:
    def __init__(self):
        self._mapping = Json(const.DECISION_MAPPING_FILE).load()
        self._local_node = self._mapping.get('local')
        self._node_status = NodeStatusDB()
        self._decisiondb = DecisionDB()
        self._loop = asyncio.get_event_loop()

    def check_path_functional(self, node_id, path):
        """
        Checks whether the path is Functional or Not
        :param node_id: Node_id for which Path count needs to be tested :type:Str
        :param path: Path io/mgmt for mgmt path to be checked.
        :return: True if Count is 0/Data not Found else False
        """
        data = self._node_status.get(node_id)
        if not data or isinstance(data[0], NodeStatusModel):
            return False
        if path == const.IO_PATH:
            if data[0].io_failure_count != 0:
                return True
        elif path == const.MGMT_PATH:
            if data[0].mgmt_failure_count != 0:
                return True
        return False

    def check_path_recovered(self, node_id):
        """
        Check if the Both the Paths are Recovered.
        :param node_id: Node ID for Path.
        :return:
        """
        data = self._node_status.get(node_id)
        if not data or isinstance(data[0], NodeStatusModel):
            return False
        if data[0].io_failure_count == 0 and data[0].mgmt_failure_count == 0:
            self.acknowledge_events(node_id)
            return True
        return False

    def acknowledge_events(self, node_id, **kwargs):
        """
        Acknowledge all event for related path.
        """
        keys = self._mapping.get(node_id)
        for each_key in keys:
            args = tuple(each_key.split("/"))
            self._loop.run_until_complete(self._decisiondb.delete_event(*args))

    def get_status(self, node_id, path, **kwargs):
        """
        Get status for io and management path.
        Check entity for local node:
            if they are same then then check functional path.
            if they are different then check recovery path.
        Functional status:
        Recovery status:
        """
        if self._local_node == node_id:
            return self.check_path_functional(node_id, path)
        else:
            return not self.check_path_recovered(node_id)
