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


class VolumePatch(Model):
    """Volume patch resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param location: Resource location
    :type location: str
    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param tags: Resource tags
    :type tags: object
    :param name1: FileSystem name. FileSystem name
    :type name1: str
    :param service_level: serviceLevel. The service level of the file system.
     Possible values include: 'Standard', 'Premium', 'Extreme'. Default value:
     "Premium" .
    :type service_level: str or ~azure.mgmt.netapp.models.ServiceLevel
    :param usage_threshold: usageThreshold. Maximum storage quota allowed for
     a file system in bytes. This is a soft quota used for alerting only.
     Minimum size is 100 GiB. Upper limit is 100TiB. Default value:
     107374182400 .
    :type usage_threshold: long
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'usage_threshold': {'maximum': 109951162777600, 'minimum': 107374182400},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': 'object'},
        'name1': {'key': 'properties.name', 'type': 'str'},
        'service_level': {'key': 'properties.serviceLevel', 'type': 'str'},
        'usage_threshold': {'key': 'properties.usageThreshold', 'type': 'long'},
    }

    def __init__(self, **kwargs):
        super(VolumePatch, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.id = None
        self.name = None
        self.type = None
        self.tags = kwargs.get('tags', None)
        self.name1 = kwargs.get('name1', None)
        self.service_level = kwargs.get('service_level', "Premium")
        self.usage_threshold = kwargs.get('usage_threshold', 107374182400)
