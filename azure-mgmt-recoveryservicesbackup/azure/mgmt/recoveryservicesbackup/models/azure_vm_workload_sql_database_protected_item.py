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

from .protected_item import ProtectedItem


class AzureVmWorkloadSQLDatabaseProtectedItem(ProtectedItem):
    """Azure VM workload-specific protected item representing SQL Database.

    All required parameters must be populated in order to send to Azure.

    :param backup_management_type: Type of backup managemenent for the backed
     up item. Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql', 'AzureStorage', 'AzureWorkload',
     'DefaultBackup'
    :type backup_management_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.BackupManagementType
    :param workload_type: Type of workload this item represents. Possible
     values include: 'Invalid', 'VM', 'FileFolder', 'AzureSqlDb', 'SQLDB',
     'Exchange', 'Sharepoint', 'VMwareVM', 'SystemState', 'Client',
     'GenericDataSource', 'SQLDataBase', 'AzureFileShare', 'SAPHanaDatabase'
    :type workload_type: str or
     ~azure.mgmt.recoveryservicesbackup.models.DataSourceType
    :param container_name: Unique name of container
    :type container_name: str
    :param source_resource_id: ARM ID of the resource to be backed up.
    :type source_resource_id: str
    :param policy_id: ID of the backup policy with which this item is backed
     up.
    :type policy_id: str
    :param last_recovery_point: Timestamp when the last (latest) backup copy
     was created for this backup item.
    :type last_recovery_point: datetime
    :param backup_set_name: Name of the backup set the backup item belongs to
    :type backup_set_name: str
    :param create_mode: Create mode to indicate recovery of existing soft
     deleted data source or creation of new data source. Possible values
     include: 'Invalid', 'Default', 'Recover'
    :type create_mode: str or
     ~azure.mgmt.recoveryservicesbackup.models.CreateMode
    :param protected_item_type: Required. Constant filled by server.
    :type protected_item_type: str
    :param friendly_name: Friendly name of the DB represented by this backup
     item.
    :type friendly_name: str
    :param server_name: Host/Cluster Name for instance or AG
    :type server_name: str
    :param parent_name: Parent name of the DB such as Instance or Availability
     Group.
    :type parent_name: str
    :param parent_type: Parent type of DB, SQLAG or StandAlone
    :type parent_type: str
    :param protection_status: Backup status of this backup item.
    :type protection_status: str
    :param protection_state: Backup state of this backup item. Possible values
     include: 'Invalid', 'IRPending', 'Protected', 'ProtectionError',
     'ProtectionStopped', 'ProtectionPaused'
    :type protection_state: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectionState
    :param last_backup_status: Last backup operation status. Possible values:
     Healthy, Unhealthy. Possible values include: 'Invalid', 'Healthy',
     'Unhealthy', 'IRPending'
    :type last_backup_status: str or
     ~azure.mgmt.recoveryservicesbackup.models.LastBackupStatus
    :param last_backup_time: Timestamp of the last backup operation on this
     backup item.
    :type last_backup_time: datetime
    :param last_backup_error_detail: Error details in last backup
    :type last_backup_error_detail:
     ~azure.mgmt.recoveryservicesbackup.models.ErrorDetail
    :param protected_item_data_source_id: Data ID of the protected item.
    :type protected_item_data_source_id: str
    :param protected_item_health_status: Health status of the backup item,
     evaluated based on last heartbeat received. Possible values include:
     'Invalid', 'Healthy', 'Unhealthy', 'NotReachable', 'IRPending'
    :type protected_item_health_status: str or
     ~azure.mgmt.recoveryservicesbackup.models.ProtectedItemHealthStatus
    :param extended_info: Additional information for this backup item.
    :type extended_info:
     ~azure.mgmt.recoveryservicesbackup.models.AzureVmWorkloadProtectedItemExtendedInfo
    """

    _validation = {
        'protected_item_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'workload_type': {'key': 'workloadType', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'source_resource_id': {'key': 'sourceResourceId', 'type': 'str'},
        'policy_id': {'key': 'policyId', 'type': 'str'},
        'last_recovery_point': {'key': 'lastRecoveryPoint', 'type': 'iso-8601'},
        'backup_set_name': {'key': 'backupSetName', 'type': 'str'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
        'protected_item_type': {'key': 'protectedItemType', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
        'server_name': {'key': 'serverName', 'type': 'str'},
        'parent_name': {'key': 'parentName', 'type': 'str'},
        'parent_type': {'key': 'parentType', 'type': 'str'},
        'protection_status': {'key': 'protectionStatus', 'type': 'str'},
        'protection_state': {'key': 'protectionState', 'type': 'str'},
        'last_backup_status': {'key': 'lastBackupStatus', 'type': 'str'},
        'last_backup_time': {'key': 'lastBackupTime', 'type': 'iso-8601'},
        'last_backup_error_detail': {'key': 'lastBackupErrorDetail', 'type': 'ErrorDetail'},
        'protected_item_data_source_id': {'key': 'protectedItemDataSourceId', 'type': 'str'},
        'protected_item_health_status': {'key': 'protectedItemHealthStatus', 'type': 'str'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AzureVmWorkloadProtectedItemExtendedInfo'},
    }

    def __init__(self, **kwargs):
        super(AzureVmWorkloadSQLDatabaseProtectedItem, self).__init__(**kwargs)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.server_name = kwargs.get('server_name', None)
        self.parent_name = kwargs.get('parent_name', None)
        self.parent_type = kwargs.get('parent_type', None)
        self.protection_status = kwargs.get('protection_status', None)
        self.protection_state = kwargs.get('protection_state', None)
        self.last_backup_status = kwargs.get('last_backup_status', None)
        self.last_backup_time = kwargs.get('last_backup_time', None)
        self.last_backup_error_detail = kwargs.get('last_backup_error_detail', None)
        self.protected_item_data_source_id = kwargs.get('protected_item_data_source_id', None)
        self.protected_item_health_status = kwargs.get('protected_item_health_status', None)
        self.extended_info = kwargs.get('extended_info', None)
        self.protected_item_type = 'AzureVmWorkloadSQLDatabase'
