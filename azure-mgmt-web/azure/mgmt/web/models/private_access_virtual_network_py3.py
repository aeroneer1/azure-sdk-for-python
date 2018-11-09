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


class PrivateAccessVirtualNetwork(Model):
    """Description of a Virtual Network that is useable for private site access.

    :param name: The name of the Virtual Network.
    :type name: str
    :param key: The key (ID) of the Virtual Network.
    :type key: int
    :param resource_id: The ARM uri of the Virtual Network
    :type resource_id: str
    :param subnets: A List of subnets that access is allowed to on this
     Virtual Network. An empty array (but not null) is interpreted to mean that
     all subnets are allowed within this Virtual Network.
    :type subnets: list[~azure.mgmt.web.models.PrivateAccessSubnet]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'key': {'key': 'key', 'type': 'int'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'subnets': {'key': 'subnets', 'type': '[PrivateAccessSubnet]'},
    }

    def __init__(self, *, name: str=None, key: int=None, resource_id: str=None, subnets=None, **kwargs) -> None:
        super(PrivateAccessVirtualNetwork, self).__init__(**kwargs)
        self.name = name
        self.key = key
        self.resource_id = resource_id
        self.subnets = subnets
