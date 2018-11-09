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


class AgentProperties(Model):
    """The properties that determine the run agent configuration.

    :param cpu: The CPU configuration in terms of number of cores required for
     the run.
    :type cpu: int
    """

    _attribute_map = {
        'cpu': {'key': 'cpu', 'type': 'int'},
    }

    def __init__(self, *, cpu: int=None, **kwargs) -> None:
        super(AgentProperties, self).__init__(**kwargs)
        self.cpu = cpu
