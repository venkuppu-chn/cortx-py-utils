#!/usr/bin/env python3

BUILD_PATH = "/tmp"
PROV_CONF_INDEX = "PROV_CONF_INDEX"
HAC_LOG = "/tmp/hac.log"
HA_MODES = ["active_passive", "active_active", "master_slave"]
HA_GROUP = ["common", "management", "io"]
IO_PATH = 'io'
MGMT_PATH = 'mgmt'
DECISION_MAPPING_FILE = '/opt/seagate/cortx/ha/schema/decision_maker_mapping.json'