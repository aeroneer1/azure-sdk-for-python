# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FixedScaleSettings(Model):
    """Fixed scale settings for the pool.

    :param resize_timeout: The timeout for allocation of compute nodes to the
     pool. The default value is 15 minutes. Timeout values use ISO 8601 format.
     For example, use PT10M for 10 minutes. The minimum value is 5 minutes. If
     you specify a value less than 5 minutes, the Batch service rejects the
     request with an error; if you are calling the REST API directly, the HTTP
     status code is 400 (Bad Request).
    :type resize_timeout: timedelta
    :param target_dedicated_nodes: The desired number of dedicated compute
     nodes in the pool. At least one of targetDedicatedNodes, targetLowPriority
     nodes must be set.
    :type target_dedicated_nodes: int
    :param target_low_priority_nodes: The desired number of low-priority
     compute nodes in the pool. At least one of targetDedicatedNodes,
     targetLowPriority nodes must be set.
    :type target_low_priority_nodes: int
    :param node_deallocation_option: Determines what to do with a node and its
     running task(s) if the pool size is decreasing. If omitted, the default
     value is Requeue. Possible values include: 'Requeue', 'Terminate',
     'TaskCompletion', 'RetainedData'
    :type node_deallocation_option: str or
     ~azure.mgmt.batch.models.ComputeNodeDeallocationOption
    """

    _attribute_map = {
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'target_dedicated_nodes': {'key': 'targetDedicatedNodes', 'type': 'int'},
        'target_low_priority_nodes': {'key': 'targetLowPriorityNodes', 'type': 'int'},
        'node_deallocation_option': {'key': 'nodeDeallocationOption', 'type': 'ComputeNodeDeallocationOption'},
    }

    def __init__(self, **kwargs):
        super(FixedScaleSettings, self).__init__(**kwargs)
        self.resize_timeout = kwargs.get('resize_timeout', None)
        self.target_dedicated_nodes = kwargs.get('target_dedicated_nodes', None)
        self.target_low_priority_nodes = kwargs.get('target_low_priority_nodes', None)
        self.node_deallocation_option = kwargs.get('node_deallocation_option', None)
