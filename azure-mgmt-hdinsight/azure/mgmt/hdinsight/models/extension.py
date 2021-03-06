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


class Extension(Model):
    """Cluster monitoring extensions.

    :param workspace_id: The workspace ID for the cluster monitoring
     extension.
    :type workspace_id: str
    :param primary_key: The certificate for the cluster monitoring extensions.
    :type primary_key: str
    """

    _attribute_map = {
        'workspace_id': {'key': 'workspaceId', 'type': 'str'},
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Extension, self).__init__(**kwargs)
        self.workspace_id = kwargs.get('workspace_id', None)
        self.primary_key = kwargs.get('primary_key', None)
