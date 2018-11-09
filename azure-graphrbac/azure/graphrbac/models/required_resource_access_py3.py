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


class RequiredResourceAccess(Model):
    """Specifies the set of OAuth 2.0 permission scopes and app roles under the
    specified resource that an application requires access to. The specified
    OAuth 2.0 permission scopes may be requested by client applications
    (through the requiredResourceAccess collection) when calling a resource
    application. The requiredResourceAccess property of the Application entity
    is a collection of ReqiredResourceAccess.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param resource_access: Required. The list of OAuth2.0 permission scopes
     and app roles that the application requires from the specified resource.
    :type resource_access: list[~azure.graphrbac.models.ResourceAccess]
    :param resource_app_id: The unique identifier for the resource that the
     application requires access to. This should be equal to the appId declared
     on the target resource application.
    :type resource_app_id: str
    """

    _validation = {
        'resource_access': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'resource_access': {'key': 'resourceAccess', 'type': '[ResourceAccess]'},
        'resource_app_id': {'key': 'resourceAppId', 'type': 'str'},
    }

    def __init__(self, *, resource_access, additional_properties=None, resource_app_id: str=None, **kwargs) -> None:
        super(RequiredResourceAccess, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.resource_access = resource_access
        self.resource_app_id = resource_app_id
