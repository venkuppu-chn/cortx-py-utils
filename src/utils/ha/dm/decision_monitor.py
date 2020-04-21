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

class DecisionMonitor:
    def __init__(self):
        self._local_node = None
        self._functional_path_list = {
            "io": self.is_io_path_functional,
            "mgmt": self.is_mgnt_path_functional
        }
        self._recovered_path_list = {
            "io": self.is_io_path_recovered,
            "mgmt": self.is_mgnt_path_recovered
        }
    
    def is_io_path_functional(self, entity, entity_id):
        """
        Check io path for functionality. 
        If consul have no data return true.
        """
        pass
    
    def is_io_path_recovered(self, entity, entity_id):
        """
        Check io path recovery for given entity.
        If consul have value for key is resolved then return true.
        """
        pass
    
    def is_mgnt_path_functional(self, entity, entity_id):
        """
        Check management path for functionality. 
        If consul have no data return true.
        """
        pass
    
    def is_mgnt_path_recovered(self, entity, entity_id):
        """
        Check management path recovery for given entity.
        If consul have value for key is resolved then return true.
        """
        pass
    
    def delete_events(self, entity, entity_id, node_id, component, component_id):
        """
        Delete all event for related path.
        """
        pass
    
    def get_status(self, entity, entity_id, node_id, path):
        """
        Get status for io and management path.
        Check entity for local node:
            if they are same then then check functional path.
            if they are different then check recovery path.
        Functional status:
        Recovery status:
        """
        if self._local_node == node_id:
            return self._functional_path_list[path]()
        else:
            return self._recovered_path_list[path]()