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


class OrchestratorProfile(Model):
    """Contains information about orchestrator.

    :param orchestrator_type: Orchestrator type.
    :type orchestrator_type: str
    :param orchestrator_version: Orchestrator version (major, minor, patch).
    :type orchestrator_version: str
    """

    _validation = {
        'orchestrator_type': {'required': True},
        'orchestrator_version': {'required': True},
    }

    _attribute_map = {
        'orchestrator_type': {'key': 'orchestratorType', 'type': 'str'},
        'orchestrator_version': {'key': 'orchestratorVersion', 'type': 'str'},
    }

    def __init__(self, orchestrator_type, orchestrator_version):
        super(OrchestratorProfile, self).__init__()
        self.orchestrator_type = orchestrator_type
        self.orchestrator_version = orchestrator_version
