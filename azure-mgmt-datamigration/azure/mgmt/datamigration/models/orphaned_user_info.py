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


class OrphanedUserInfo(Model):
    """Information of orphaned users on the SQL server database.

    :param name: Name of the orphaned user
    :type name: str
    :param database_name: Parent DB of the user
    :type database_name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OrphanedUserInfo, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.database_name = kwargs.get('database_name', None)
