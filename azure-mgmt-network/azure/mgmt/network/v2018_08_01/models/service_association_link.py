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

from .sub_resource import SubResource


class ServiceAssociationLink(SubResource):
    """ServiceAssociationLink resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param linked_resource_type: Resource type of the linked resource.
    :type linked_resource_type: str
    :param link: Link to the external resource.
    :type link: str
    :ivar provisioning_state: Provisioning state of the ServiceAssociationLink
     resource.
    :vartype provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :ivar etag: A unique read-only string that changes whenever the resource
     is updated.
    :vartype etag: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'etag': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'linked_resource_type': {'key': 'properties.linkedResourceType', 'type': 'str'},
        'link': {'key': 'properties.link', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServiceAssociationLink, self).__init__(**kwargs)
        self.linked_resource_type = kwargs.get('linked_resource_type', None)
        self.link = kwargs.get('link', None)
        self.provisioning_state = None
        self.name = kwargs.get('name', None)
        self.etag = None
