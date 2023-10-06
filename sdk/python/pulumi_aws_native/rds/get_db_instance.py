# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'GetDbInstanceResult',
    'AwaitableGetDbInstanceResult',
    'get_db_instance',
    'get_db_instance_output',
]

@pulumi.output_type
class GetDbInstanceResult:
    def __init__(__self__, allocated_storage=None, associated_roles=None, auto_minor_version_upgrade=None, availability_zone=None, backup_retention_period=None, ca_certificate_identifier=None, certificate_details=None, copy_tags_to_snapshot=None, db_cluster_snapshot_identifier=None, db_instance_arn=None, db_instance_class=None, db_parameter_group_name=None, db_security_groups=None, db_system_id=None, dbi_resource_id=None, deletion_protection=None, domain=None, domain_auth_secret_arn=None, domain_dns_ips=None, domain_fqdn=None, domain_iam_role_name=None, domain_ou=None, enable_cloudwatch_logs_exports=None, enable_iam_database_authentication=None, enable_performance_insights=None, endpoint=None, engine=None, engine_version=None, iops=None, license_model=None, manage_master_user_password=None, master_user_secret=None, max_allocated_storage=None, monitoring_interval=None, monitoring_role_arn=None, multi_az=None, network_type=None, option_group_name=None, performance_insights_kms_key_id=None, performance_insights_retention_period=None, preferred_backup_window=None, preferred_maintenance_window=None, processor_features=None, promotion_tier=None, publicly_accessible=None, replica_mode=None, source_db_cluster_identifier=None, storage_throughput=None, storage_type=None, tags=None, tde_credential_arn=None, vpc_security_groups=None):
        if allocated_storage and not isinstance(allocated_storage, str):
            raise TypeError("Expected argument 'allocated_storage' to be a str")
        pulumi.set(__self__, "allocated_storage", allocated_storage)
        if associated_roles and not isinstance(associated_roles, list):
            raise TypeError("Expected argument 'associated_roles' to be a list")
        pulumi.set(__self__, "associated_roles", associated_roles)
        if auto_minor_version_upgrade and not isinstance(auto_minor_version_upgrade, bool):
            raise TypeError("Expected argument 'auto_minor_version_upgrade' to be a bool")
        pulumi.set(__self__, "auto_minor_version_upgrade", auto_minor_version_upgrade)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if backup_retention_period and not isinstance(backup_retention_period, int):
            raise TypeError("Expected argument 'backup_retention_period' to be a int")
        pulumi.set(__self__, "backup_retention_period", backup_retention_period)
        if ca_certificate_identifier and not isinstance(ca_certificate_identifier, str):
            raise TypeError("Expected argument 'ca_certificate_identifier' to be a str")
        pulumi.set(__self__, "ca_certificate_identifier", ca_certificate_identifier)
        if certificate_details and not isinstance(certificate_details, dict):
            raise TypeError("Expected argument 'certificate_details' to be a dict")
        pulumi.set(__self__, "certificate_details", certificate_details)
        if copy_tags_to_snapshot and not isinstance(copy_tags_to_snapshot, bool):
            raise TypeError("Expected argument 'copy_tags_to_snapshot' to be a bool")
        pulumi.set(__self__, "copy_tags_to_snapshot", copy_tags_to_snapshot)
        if db_cluster_snapshot_identifier and not isinstance(db_cluster_snapshot_identifier, str):
            raise TypeError("Expected argument 'db_cluster_snapshot_identifier' to be a str")
        pulumi.set(__self__, "db_cluster_snapshot_identifier", db_cluster_snapshot_identifier)
        if db_instance_arn and not isinstance(db_instance_arn, str):
            raise TypeError("Expected argument 'db_instance_arn' to be a str")
        pulumi.set(__self__, "db_instance_arn", db_instance_arn)
        if db_instance_class and not isinstance(db_instance_class, str):
            raise TypeError("Expected argument 'db_instance_class' to be a str")
        pulumi.set(__self__, "db_instance_class", db_instance_class)
        if db_parameter_group_name and not isinstance(db_parameter_group_name, str):
            raise TypeError("Expected argument 'db_parameter_group_name' to be a str")
        pulumi.set(__self__, "db_parameter_group_name", db_parameter_group_name)
        if db_security_groups and not isinstance(db_security_groups, list):
            raise TypeError("Expected argument 'db_security_groups' to be a list")
        pulumi.set(__self__, "db_security_groups", db_security_groups)
        if db_system_id and not isinstance(db_system_id, str):
            raise TypeError("Expected argument 'db_system_id' to be a str")
        pulumi.set(__self__, "db_system_id", db_system_id)
        if dbi_resource_id and not isinstance(dbi_resource_id, str):
            raise TypeError("Expected argument 'dbi_resource_id' to be a str")
        pulumi.set(__self__, "dbi_resource_id", dbi_resource_id)
        if deletion_protection and not isinstance(deletion_protection, bool):
            raise TypeError("Expected argument 'deletion_protection' to be a bool")
        pulumi.set(__self__, "deletion_protection", deletion_protection)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if domain_auth_secret_arn and not isinstance(domain_auth_secret_arn, str):
            raise TypeError("Expected argument 'domain_auth_secret_arn' to be a str")
        pulumi.set(__self__, "domain_auth_secret_arn", domain_auth_secret_arn)
        if domain_dns_ips and not isinstance(domain_dns_ips, list):
            raise TypeError("Expected argument 'domain_dns_ips' to be a list")
        pulumi.set(__self__, "domain_dns_ips", domain_dns_ips)
        if domain_fqdn and not isinstance(domain_fqdn, str):
            raise TypeError("Expected argument 'domain_fqdn' to be a str")
        pulumi.set(__self__, "domain_fqdn", domain_fqdn)
        if domain_iam_role_name and not isinstance(domain_iam_role_name, str):
            raise TypeError("Expected argument 'domain_iam_role_name' to be a str")
        pulumi.set(__self__, "domain_iam_role_name", domain_iam_role_name)
        if domain_ou and not isinstance(domain_ou, str):
            raise TypeError("Expected argument 'domain_ou' to be a str")
        pulumi.set(__self__, "domain_ou", domain_ou)
        if enable_cloudwatch_logs_exports and not isinstance(enable_cloudwatch_logs_exports, list):
            raise TypeError("Expected argument 'enable_cloudwatch_logs_exports' to be a list")
        pulumi.set(__self__, "enable_cloudwatch_logs_exports", enable_cloudwatch_logs_exports)
        if enable_iam_database_authentication and not isinstance(enable_iam_database_authentication, bool):
            raise TypeError("Expected argument 'enable_iam_database_authentication' to be a bool")
        pulumi.set(__self__, "enable_iam_database_authentication", enable_iam_database_authentication)
        if enable_performance_insights and not isinstance(enable_performance_insights, bool):
            raise TypeError("Expected argument 'enable_performance_insights' to be a bool")
        pulumi.set(__self__, "enable_performance_insights", enable_performance_insights)
        if endpoint and not isinstance(endpoint, dict):
            raise TypeError("Expected argument 'endpoint' to be a dict")
        pulumi.set(__self__, "endpoint", endpoint)
        if engine and not isinstance(engine, str):
            raise TypeError("Expected argument 'engine' to be a str")
        pulumi.set(__self__, "engine", engine)
        if engine_version and not isinstance(engine_version, str):
            raise TypeError("Expected argument 'engine_version' to be a str")
        pulumi.set(__self__, "engine_version", engine_version)
        if iops and not isinstance(iops, int):
            raise TypeError("Expected argument 'iops' to be a int")
        pulumi.set(__self__, "iops", iops)
        if license_model and not isinstance(license_model, str):
            raise TypeError("Expected argument 'license_model' to be a str")
        pulumi.set(__self__, "license_model", license_model)
        if manage_master_user_password and not isinstance(manage_master_user_password, bool):
            raise TypeError("Expected argument 'manage_master_user_password' to be a bool")
        pulumi.set(__self__, "manage_master_user_password", manage_master_user_password)
        if master_user_secret and not isinstance(master_user_secret, dict):
            raise TypeError("Expected argument 'master_user_secret' to be a dict")
        pulumi.set(__self__, "master_user_secret", master_user_secret)
        if max_allocated_storage and not isinstance(max_allocated_storage, int):
            raise TypeError("Expected argument 'max_allocated_storage' to be a int")
        pulumi.set(__self__, "max_allocated_storage", max_allocated_storage)
        if monitoring_interval and not isinstance(monitoring_interval, int):
            raise TypeError("Expected argument 'monitoring_interval' to be a int")
        pulumi.set(__self__, "monitoring_interval", monitoring_interval)
        if monitoring_role_arn and not isinstance(monitoring_role_arn, str):
            raise TypeError("Expected argument 'monitoring_role_arn' to be a str")
        pulumi.set(__self__, "monitoring_role_arn", monitoring_role_arn)
        if multi_az and not isinstance(multi_az, bool):
            raise TypeError("Expected argument 'multi_az' to be a bool")
        pulumi.set(__self__, "multi_az", multi_az)
        if network_type and not isinstance(network_type, str):
            raise TypeError("Expected argument 'network_type' to be a str")
        pulumi.set(__self__, "network_type", network_type)
        if option_group_name and not isinstance(option_group_name, str):
            raise TypeError("Expected argument 'option_group_name' to be a str")
        pulumi.set(__self__, "option_group_name", option_group_name)
        if performance_insights_kms_key_id and not isinstance(performance_insights_kms_key_id, str):
            raise TypeError("Expected argument 'performance_insights_kms_key_id' to be a str")
        pulumi.set(__self__, "performance_insights_kms_key_id", performance_insights_kms_key_id)
        if performance_insights_retention_period and not isinstance(performance_insights_retention_period, int):
            raise TypeError("Expected argument 'performance_insights_retention_period' to be a int")
        pulumi.set(__self__, "performance_insights_retention_period", performance_insights_retention_period)
        if preferred_backup_window and not isinstance(preferred_backup_window, str):
            raise TypeError("Expected argument 'preferred_backup_window' to be a str")
        pulumi.set(__self__, "preferred_backup_window", preferred_backup_window)
        if preferred_maintenance_window and not isinstance(preferred_maintenance_window, str):
            raise TypeError("Expected argument 'preferred_maintenance_window' to be a str")
        pulumi.set(__self__, "preferred_maintenance_window", preferred_maintenance_window)
        if processor_features and not isinstance(processor_features, list):
            raise TypeError("Expected argument 'processor_features' to be a list")
        pulumi.set(__self__, "processor_features", processor_features)
        if promotion_tier and not isinstance(promotion_tier, int):
            raise TypeError("Expected argument 'promotion_tier' to be a int")
        pulumi.set(__self__, "promotion_tier", promotion_tier)
        if publicly_accessible and not isinstance(publicly_accessible, bool):
            raise TypeError("Expected argument 'publicly_accessible' to be a bool")
        pulumi.set(__self__, "publicly_accessible", publicly_accessible)
        if replica_mode and not isinstance(replica_mode, str):
            raise TypeError("Expected argument 'replica_mode' to be a str")
        pulumi.set(__self__, "replica_mode", replica_mode)
        if source_db_cluster_identifier and not isinstance(source_db_cluster_identifier, str):
            raise TypeError("Expected argument 'source_db_cluster_identifier' to be a str")
        pulumi.set(__self__, "source_db_cluster_identifier", source_db_cluster_identifier)
        if storage_throughput and not isinstance(storage_throughput, int):
            raise TypeError("Expected argument 'storage_throughput' to be a int")
        pulumi.set(__self__, "storage_throughput", storage_throughput)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tde_credential_arn and not isinstance(tde_credential_arn, str):
            raise TypeError("Expected argument 'tde_credential_arn' to be a str")
        pulumi.set(__self__, "tde_credential_arn", tde_credential_arn)
        if vpc_security_groups and not isinstance(vpc_security_groups, list):
            raise TypeError("Expected argument 'vpc_security_groups' to be a list")
        pulumi.set(__self__, "vpc_security_groups", vpc_security_groups)

    @property
    @pulumi.getter(name="allocatedStorage")
    def allocated_storage(self) -> Optional[str]:
        """
        The amount of storage (in gigabytes) to be initially allocated for the database instance.
        """
        return pulumi.get(self, "allocated_storage")

    @property
    @pulumi.getter(name="associatedRoles")
    def associated_roles(self) -> Optional[Sequence['outputs.DbInstanceDbInstanceRole']]:
        """
        The AWS Identity and Access Management (IAM) roles associated with the DB instance.
        """
        return pulumi.get(self, "associated_roles")

    @property
    @pulumi.getter(name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> Optional[bool]:
        """
        A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
        """
        return pulumi.get(self, "auto_minor_version_upgrade")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="backupRetentionPeriod")
    def backup_retention_period(self) -> Optional[int]:
        """
        The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
        """
        return pulumi.get(self, "backup_retention_period")

    @property
    @pulumi.getter(name="caCertificateIdentifier")
    def ca_certificate_identifier(self) -> Optional[str]:
        """
        The identifier of the CA certificate for this DB instance.
        """
        return pulumi.get(self, "ca_certificate_identifier")

    @property
    @pulumi.getter(name="certificateDetails")
    def certificate_details(self) -> Optional['outputs.DbInstanceCertificateDetails']:
        """
        Returns the details of the DB instance's server certificate.
        """
        return pulumi.get(self, "certificate_details")

    @property
    @pulumi.getter(name="copyTagsToSnapshot")
    def copy_tags_to_snapshot(self) -> Optional[bool]:
        """
        A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
        """
        return pulumi.get(self, "copy_tags_to_snapshot")

    @property
    @pulumi.getter(name="dbClusterSnapshotIdentifier")
    def db_cluster_snapshot_identifier(self) -> Optional[str]:
        """
        The identifier for the RDS for MySQL Multi-AZ DB cluster snapshot to restore from. For more information on Multi-AZ DB clusters, see Multi-AZ deployments with two readable standby DB instances in the Amazon RDS User Guide .

        Constraints:
         * Must match the identifier of an existing Multi-AZ DB cluster snapshot.
         * Can't be specified when DBSnapshotIdentifier is specified.
         * Must be specified when DBSnapshotIdentifier isn't specified.
         * If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the DBClusterSnapshotIdentifier must be the ARN of the shared snapshot.
         * Can't be the identifier of an Aurora DB cluster snapshot.
         * Can't be the identifier of an RDS for PostgreSQL Multi-AZ DB cluster snapshot.
        """
        return pulumi.get(self, "db_cluster_snapshot_identifier")

    @property
    @pulumi.getter(name="dbInstanceArn")
    def db_instance_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) for the DB instance.
        """
        return pulumi.get(self, "db_instance_arn")

    @property
    @pulumi.getter(name="dbInstanceClass")
    def db_instance_class(self) -> Optional[str]:
        """
        The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.
        """
        return pulumi.get(self, "db_instance_class")

    @property
    @pulumi.getter(name="dbParameterGroupName")
    def db_parameter_group_name(self) -> Optional[str]:
        """
        The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.
        """
        return pulumi.get(self, "db_parameter_group_name")

    @property
    @pulumi.getter(name="dbSecurityGroups")
    def db_security_groups(self) -> Optional[Sequence[str]]:
        """
        A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
        """
        return pulumi.get(self, "db_security_groups")

    @property
    @pulumi.getter(name="dbSystemId")
    def db_system_id(self) -> Optional[str]:
        """
        The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is valid for RDS Custom only.
        """
        return pulumi.get(self, "db_system_id")

    @property
    @pulumi.getter(name="dbiResourceId")
    def dbi_resource_id(self) -> Optional[str]:
        """
        The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
        """
        return pulumi.get(self, "dbi_resource_id")

    @property
    @pulumi.getter(name="deletionProtection")
    def deletion_protection(self) -> Optional[bool]:
        """
        A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        """
        return pulumi.get(self, "deletion_protection")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        """
        The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="domainAuthSecretArn")
    def domain_auth_secret_arn(self) -> Optional[str]:
        """
        The ARN for the Secrets Manager secret with the credentials for the user joining the domain.
        """
        return pulumi.get(self, "domain_auth_secret_arn")

    @property
    @pulumi.getter(name="domainDnsIps")
    def domain_dns_ips(self) -> Optional[Sequence[str]]:
        """
        The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.
        """
        return pulumi.get(self, "domain_dns_ips")

    @property
    @pulumi.getter(name="domainFqdn")
    def domain_fqdn(self) -> Optional[str]:
        """
        The fully qualified domain name (FQDN) of an Active Directory domain.
        """
        return pulumi.get(self, "domain_fqdn")

    @property
    @pulumi.getter(name="domainIamRoleName")
    def domain_iam_role_name(self) -> Optional[str]:
        """
        Specify the name of the IAM role to be used when making API calls to the Directory Service.
        """
        return pulumi.get(self, "domain_iam_role_name")

    @property
    @pulumi.getter(name="domainOu")
    def domain_ou(self) -> Optional[str]:
        """
        The Active Directory organizational unit for your DB instance to join.
        """
        return pulumi.get(self, "domain_ou")

    @property
    @pulumi.getter(name="enableCloudwatchLogsExports")
    def enable_cloudwatch_logs_exports(self) -> Optional[Sequence[str]]:
        """
        The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.
        """
        return pulumi.get(self, "enable_cloudwatch_logs_exports")

    @property
    @pulumi.getter(name="enableIamDatabaseAuthentication")
    def enable_iam_database_authentication(self) -> Optional[bool]:
        """
        A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
        """
        return pulumi.get(self, "enable_iam_database_authentication")

    @property
    @pulumi.getter(name="enablePerformanceInsights")
    def enable_performance_insights(self) -> Optional[bool]:
        """
        A value that indicates whether to enable Performance Insights for the DB instance.
        """
        return pulumi.get(self, "enable_performance_insights")

    @property
    @pulumi.getter
    def endpoint(self) -> Optional['outputs.DbInstanceEndpoint']:
        """
        Specifies the connection endpoint.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def engine(self) -> Optional[str]:
        """
        The name of the database engine that you want to use for this DB instance.
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[str]:
        """
        The version number of the database engine to use.
        """
        return pulumi.get(self, "engine_version")

    @property
    @pulumi.getter
    def iops(self) -> Optional[int]:
        """
        The number of I/O operations per second (IOPS) that the database provisions.
        """
        return pulumi.get(self, "iops")

    @property
    @pulumi.getter(name="licenseModel")
    def license_model(self) -> Optional[str]:
        """
        License model information for this DB instance.
        """
        return pulumi.get(self, "license_model")

    @property
    @pulumi.getter(name="manageMasterUserPassword")
    def manage_master_user_password(self) -> Optional[bool]:
        """
        A value that indicates whether to manage the master user password with AWS Secrets Manager.
        """
        return pulumi.get(self, "manage_master_user_password")

    @property
    @pulumi.getter(name="masterUserSecret")
    def master_user_secret(self) -> Optional['outputs.DbInstanceMasterUserSecret']:
        """
        Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
        """
        return pulumi.get(self, "master_user_secret")

    @property
    @pulumi.getter(name="maxAllocatedStorage")
    def max_allocated_storage(self) -> Optional[int]:
        """
        The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
        """
        return pulumi.get(self, "max_allocated_storage")

    @property
    @pulumi.getter(name="monitoringInterval")
    def monitoring_interval(self) -> Optional[int]:
        """
        The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        """
        return pulumi.get(self, "monitoring_interval")

    @property
    @pulumi.getter(name="monitoringRoleArn")
    def monitoring_role_arn(self) -> Optional[str]:
        """
        The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.
        """
        return pulumi.get(self, "monitoring_role_arn")

    @property
    @pulumi.getter(name="multiAz")
    def multi_az(self) -> Optional[bool]:
        """
        Specifies whether the database instance is a multiple Availability Zone deployment.
        """
        return pulumi.get(self, "multi_az")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> Optional[str]:
        """
        The network type of the DB cluster.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="optionGroupName")
    def option_group_name(self) -> Optional[str]:
        """
        Indicates that the DB instance should be associated with the specified option group.
        """
        return pulumi.get(self, "option_group_name")

    @property
    @pulumi.getter(name="performanceInsightsKmsKeyId")
    def performance_insights_kms_key_id(self) -> Optional[str]:
        """
        The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
        """
        return pulumi.get(self, "performance_insights_kms_key_id")

    @property
    @pulumi.getter(name="performanceInsightsRetentionPeriod")
    def performance_insights_retention_period(self) -> Optional[int]:
        """
        The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).
        """
        return pulumi.get(self, "performance_insights_retention_period")

    @property
    @pulumi.getter(name="preferredBackupWindow")
    def preferred_backup_window(self) -> Optional[str]:
        """
        The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
        """
        return pulumi.get(self, "preferred_backup_window")

    @property
    @pulumi.getter(name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> Optional[str]:
        """
        he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        """
        return pulumi.get(self, "preferred_maintenance_window")

    @property
    @pulumi.getter(name="processorFeatures")
    def processor_features(self) -> Optional[Sequence['outputs.DbInstanceProcessorFeature']]:
        """
        The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
        """
        return pulumi.get(self, "processor_features")

    @property
    @pulumi.getter(name="promotionTier")
    def promotion_tier(self) -> Optional[int]:
        """
        A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.
        """
        return pulumi.get(self, "promotion_tier")

    @property
    @pulumi.getter(name="publiclyAccessible")
    def publicly_accessible(self) -> Optional[bool]:
        """
        Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
        """
        return pulumi.get(self, "publicly_accessible")

    @property
    @pulumi.getter(name="replicaMode")
    def replica_mode(self) -> Optional[str]:
        """
        The open mode of an Oracle read replica. The default is open-read-only.
        """
        return pulumi.get(self, "replica_mode")

    @property
    @pulumi.getter(name="sourceDbClusterIdentifier")
    def source_db_cluster_identifier(self) -> Optional[str]:
        """
        The identifier of the Multi-AZ DB cluster that will act as the source for the read replica. Each DB cluster can have up to 15 read replicas.
        """
        return pulumi.get(self, "source_db_cluster_identifier")

    @property
    @pulumi.getter(name="storageThroughput")
    def storage_throughput(self) -> Optional[int]:
        """
        Specifies the storage throughput for the DB instance.
        """
        return pulumi.get(self, "storage_throughput")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[str]:
        """
        Specifies the storage type to be associated with the DB instance.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.DbInstanceTag']]:
        """
        Tags to assign to the DB instance.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tdeCredentialArn")
    def tde_credential_arn(self) -> Optional[str]:
        """
        The ARN from the key store with which to associate the instance for TDE encryption.
        """
        return pulumi.get(self, "tde_credential_arn")

    @property
    @pulumi.getter(name="vpcSecurityGroups")
    def vpc_security_groups(self) -> Optional[Sequence[str]]:
        """
        A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.
        """
        return pulumi.get(self, "vpc_security_groups")


class AwaitableGetDbInstanceResult(GetDbInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDbInstanceResult(
            allocated_storage=self.allocated_storage,
            associated_roles=self.associated_roles,
            auto_minor_version_upgrade=self.auto_minor_version_upgrade,
            availability_zone=self.availability_zone,
            backup_retention_period=self.backup_retention_period,
            ca_certificate_identifier=self.ca_certificate_identifier,
            certificate_details=self.certificate_details,
            copy_tags_to_snapshot=self.copy_tags_to_snapshot,
            db_cluster_snapshot_identifier=self.db_cluster_snapshot_identifier,
            db_instance_arn=self.db_instance_arn,
            db_instance_class=self.db_instance_class,
            db_parameter_group_name=self.db_parameter_group_name,
            db_security_groups=self.db_security_groups,
            db_system_id=self.db_system_id,
            dbi_resource_id=self.dbi_resource_id,
            deletion_protection=self.deletion_protection,
            domain=self.domain,
            domain_auth_secret_arn=self.domain_auth_secret_arn,
            domain_dns_ips=self.domain_dns_ips,
            domain_fqdn=self.domain_fqdn,
            domain_iam_role_name=self.domain_iam_role_name,
            domain_ou=self.domain_ou,
            enable_cloudwatch_logs_exports=self.enable_cloudwatch_logs_exports,
            enable_iam_database_authentication=self.enable_iam_database_authentication,
            enable_performance_insights=self.enable_performance_insights,
            endpoint=self.endpoint,
            engine=self.engine,
            engine_version=self.engine_version,
            iops=self.iops,
            license_model=self.license_model,
            manage_master_user_password=self.manage_master_user_password,
            master_user_secret=self.master_user_secret,
            max_allocated_storage=self.max_allocated_storage,
            monitoring_interval=self.monitoring_interval,
            monitoring_role_arn=self.monitoring_role_arn,
            multi_az=self.multi_az,
            network_type=self.network_type,
            option_group_name=self.option_group_name,
            performance_insights_kms_key_id=self.performance_insights_kms_key_id,
            performance_insights_retention_period=self.performance_insights_retention_period,
            preferred_backup_window=self.preferred_backup_window,
            preferred_maintenance_window=self.preferred_maintenance_window,
            processor_features=self.processor_features,
            promotion_tier=self.promotion_tier,
            publicly_accessible=self.publicly_accessible,
            replica_mode=self.replica_mode,
            source_db_cluster_identifier=self.source_db_cluster_identifier,
            storage_throughput=self.storage_throughput,
            storage_type=self.storage_type,
            tags=self.tags,
            tde_credential_arn=self.tde_credential_arn,
            vpc_security_groups=self.vpc_security_groups)


def get_db_instance(db_instance_identifier: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDbInstanceResult:
    """
    The AWS::RDS::DBInstance resource creates an Amazon RDS DB instance.


    :param str db_instance_identifier: A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
    """
    __args__ = dict()
    __args__['dbInstanceIdentifier'] = db_instance_identifier
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:rds:getDbInstance', __args__, opts=opts, typ=GetDbInstanceResult).value

    return AwaitableGetDbInstanceResult(
        allocated_storage=pulumi.get(__ret__, 'allocated_storage'),
        associated_roles=pulumi.get(__ret__, 'associated_roles'),
        auto_minor_version_upgrade=pulumi.get(__ret__, 'auto_minor_version_upgrade'),
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        backup_retention_period=pulumi.get(__ret__, 'backup_retention_period'),
        ca_certificate_identifier=pulumi.get(__ret__, 'ca_certificate_identifier'),
        certificate_details=pulumi.get(__ret__, 'certificate_details'),
        copy_tags_to_snapshot=pulumi.get(__ret__, 'copy_tags_to_snapshot'),
        db_cluster_snapshot_identifier=pulumi.get(__ret__, 'db_cluster_snapshot_identifier'),
        db_instance_arn=pulumi.get(__ret__, 'db_instance_arn'),
        db_instance_class=pulumi.get(__ret__, 'db_instance_class'),
        db_parameter_group_name=pulumi.get(__ret__, 'db_parameter_group_name'),
        db_security_groups=pulumi.get(__ret__, 'db_security_groups'),
        db_system_id=pulumi.get(__ret__, 'db_system_id'),
        dbi_resource_id=pulumi.get(__ret__, 'dbi_resource_id'),
        deletion_protection=pulumi.get(__ret__, 'deletion_protection'),
        domain=pulumi.get(__ret__, 'domain'),
        domain_auth_secret_arn=pulumi.get(__ret__, 'domain_auth_secret_arn'),
        domain_dns_ips=pulumi.get(__ret__, 'domain_dns_ips'),
        domain_fqdn=pulumi.get(__ret__, 'domain_fqdn'),
        domain_iam_role_name=pulumi.get(__ret__, 'domain_iam_role_name'),
        domain_ou=pulumi.get(__ret__, 'domain_ou'),
        enable_cloudwatch_logs_exports=pulumi.get(__ret__, 'enable_cloudwatch_logs_exports'),
        enable_iam_database_authentication=pulumi.get(__ret__, 'enable_iam_database_authentication'),
        enable_performance_insights=pulumi.get(__ret__, 'enable_performance_insights'),
        endpoint=pulumi.get(__ret__, 'endpoint'),
        engine=pulumi.get(__ret__, 'engine'),
        engine_version=pulumi.get(__ret__, 'engine_version'),
        iops=pulumi.get(__ret__, 'iops'),
        license_model=pulumi.get(__ret__, 'license_model'),
        manage_master_user_password=pulumi.get(__ret__, 'manage_master_user_password'),
        master_user_secret=pulumi.get(__ret__, 'master_user_secret'),
        max_allocated_storage=pulumi.get(__ret__, 'max_allocated_storage'),
        monitoring_interval=pulumi.get(__ret__, 'monitoring_interval'),
        monitoring_role_arn=pulumi.get(__ret__, 'monitoring_role_arn'),
        multi_az=pulumi.get(__ret__, 'multi_az'),
        network_type=pulumi.get(__ret__, 'network_type'),
        option_group_name=pulumi.get(__ret__, 'option_group_name'),
        performance_insights_kms_key_id=pulumi.get(__ret__, 'performance_insights_kms_key_id'),
        performance_insights_retention_period=pulumi.get(__ret__, 'performance_insights_retention_period'),
        preferred_backup_window=pulumi.get(__ret__, 'preferred_backup_window'),
        preferred_maintenance_window=pulumi.get(__ret__, 'preferred_maintenance_window'),
        processor_features=pulumi.get(__ret__, 'processor_features'),
        promotion_tier=pulumi.get(__ret__, 'promotion_tier'),
        publicly_accessible=pulumi.get(__ret__, 'publicly_accessible'),
        replica_mode=pulumi.get(__ret__, 'replica_mode'),
        source_db_cluster_identifier=pulumi.get(__ret__, 'source_db_cluster_identifier'),
        storage_throughput=pulumi.get(__ret__, 'storage_throughput'),
        storage_type=pulumi.get(__ret__, 'storage_type'),
        tags=pulumi.get(__ret__, 'tags'),
        tde_credential_arn=pulumi.get(__ret__, 'tde_credential_arn'),
        vpc_security_groups=pulumi.get(__ret__, 'vpc_security_groups'))


@_utilities.lift_output_func(get_db_instance)
def get_db_instance_output(db_instance_identifier: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDbInstanceResult]:
    """
    The AWS::RDS::DBInstance resource creates an Amazon RDS DB instance.


    :param str db_instance_identifier: A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
    """
    ...
