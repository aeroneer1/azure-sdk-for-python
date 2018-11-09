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


class CreateDataLakeStoreAccountParameters(Model):
    """CreateDataLakeStoreAccountParameters.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The resource location.
    :type location: str
    :param tags: The resource tags.
    :type tags: dict[str, str]
    :param identity: The Key Vault encryption identity, if any.
    :type identity: ~azure.mgmt.datalake.store.models.EncryptionIdentity
    :param default_group: The default owner group for all new folders and
     files created in the Data Lake Store account.
    :type default_group: str
    :param encryption_config: The Key Vault encryption configuration.
    :type encryption_config:
     ~azure.mgmt.datalake.store.models.EncryptionConfig
    :param encryption_state: The current state of encryption for this Data
     Lake Store account. Possible values include: 'Enabled', 'Disabled'
    :type encryption_state: str or
     ~azure.mgmt.datalake.store.models.EncryptionState
    :param firewall_rules: The list of firewall rules associated with this
     Data Lake Store account.
    :type firewall_rules:
     list[~azure.mgmt.datalake.store.models.CreateFirewallRuleWithAccountParameters]
    :param virtual_network_rules: The list of virtual network rules associated
     with this Data Lake Store account.
    :type virtual_network_rules:
     list[~azure.mgmt.datalake.store.models.CreateVirtualNetworkRuleWithAccountParameters]
    :param firewall_state: The current state of the IP address firewall for
     this Data Lake Store account. Possible values include: 'Enabled',
     'Disabled'
    :type firewall_state: str or
     ~azure.mgmt.datalake.store.models.FirewallState
    :param firewall_allow_azure_ips: The current state of allowing or
     disallowing IPs originating within Azure through the firewall. If the
     firewall is disabled, this is not enforced. Possible values include:
     'Enabled', 'Disabled'
    :type firewall_allow_azure_ips: str or
     ~azure.mgmt.datalake.store.models.FirewallAllowAzureIpsState
    :param trusted_id_providers: The list of trusted identity providers
     associated with this Data Lake Store account.
    :type trusted_id_providers:
     list[~azure.mgmt.datalake.store.models.CreateTrustedIdProviderWithAccountParameters]
    :param trusted_id_provider_state: The current state of the trusted
     identity provider feature for this Data Lake Store account. Possible
     values include: 'Enabled', 'Disabled'
    :type trusted_id_provider_state: str or
     ~azure.mgmt.datalake.store.models.TrustedIdProviderState
    :param new_tier: The commitment tier to use for next month. Possible
     values include: 'Consumption', 'Commitment_1TB', 'Commitment_10TB',
     'Commitment_100TB', 'Commitment_500TB', 'Commitment_1PB', 'Commitment_5PB'
    :type new_tier: str or ~azure.mgmt.datalake.store.models.TierType
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'EncryptionIdentity'},
        'default_group': {'key': 'properties.defaultGroup', 'type': 'str'},
        'encryption_config': {'key': 'properties.encryptionConfig', 'type': 'EncryptionConfig'},
        'encryption_state': {'key': 'properties.encryptionState', 'type': 'EncryptionState'},
        'firewall_rules': {'key': 'properties.firewallRules', 'type': '[CreateFirewallRuleWithAccountParameters]'},
        'virtual_network_rules': {'key': 'properties.virtualNetworkRules', 'type': '[CreateVirtualNetworkRuleWithAccountParameters]'},
        'firewall_state': {'key': 'properties.firewallState', 'type': 'FirewallState'},
        'firewall_allow_azure_ips': {'key': 'properties.firewallAllowAzureIps', 'type': 'FirewallAllowAzureIpsState'},
        'trusted_id_providers': {'key': 'properties.trustedIdProviders', 'type': '[CreateTrustedIdProviderWithAccountParameters]'},
        'trusted_id_provider_state': {'key': 'properties.trustedIdProviderState', 'type': 'TrustedIdProviderState'},
        'new_tier': {'key': 'properties.newTier', 'type': 'TierType'},
    }

    def __init__(self, *, location: str, tags=None, identity=None, default_group: str=None, encryption_config=None, encryption_state=None, firewall_rules=None, virtual_network_rules=None, firewall_state=None, firewall_allow_azure_ips=None, trusted_id_providers=None, trusted_id_provider_state=None, new_tier=None, **kwargs) -> None:
        super(CreateDataLakeStoreAccountParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.identity = identity
        self.default_group = default_group
        self.encryption_config = encryption_config
        self.encryption_state = encryption_state
        self.firewall_rules = firewall_rules
        self.virtual_network_rules = virtual_network_rules
        self.firewall_state = firewall_state
        self.firewall_allow_azure_ips = firewall_allow_azure_ips
        self.trusted_id_providers = trusted_id_providers
        self.trusted_id_provider_state = trusted_id_provider_state
        self.new_tier = new_tier
