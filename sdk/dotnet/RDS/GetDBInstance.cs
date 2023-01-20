// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS
{
    public static class GetDBInstance
    {
        /// <summary>
        /// The AWS::RDS::DBInstance resource creates an Amazon RDS DB instance.
        /// </summary>
        public static Task<GetDBInstanceResult> InvokeAsync(GetDBInstanceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDBInstanceResult>("aws-native:rds:getDBInstance", args ?? new GetDBInstanceArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::RDS::DBInstance resource creates an Amazon RDS DB instance.
        /// </summary>
        public static Output<GetDBInstanceResult> Invoke(GetDBInstanceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDBInstanceResult>("aws-native:rds:getDBInstance", args ?? new GetDBInstanceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDBInstanceArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
        /// </summary>
        [Input("dBInstanceIdentifier", required: true)]
        public string DBInstanceIdentifier { get; set; } = null!;

        public GetDBInstanceArgs()
        {
        }
        public static new GetDBInstanceArgs Empty => new GetDBInstanceArgs();
    }

    public sealed class GetDBInstanceInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
        /// </summary>
        [Input("dBInstanceIdentifier", required: true)]
        public Input<string> DBInstanceIdentifier { get; set; } = null!;

        public GetDBInstanceInvokeArgs()
        {
        }
        public static new GetDBInstanceInvokeArgs Empty => new GetDBInstanceInvokeArgs();
    }


    [OutputType]
    public sealed class GetDBInstanceResult
    {
        /// <summary>
        /// The amount of storage (in gigabytes) to be initially allocated for the database instance.
        /// </summary>
        public readonly string? AllocatedStorage;
        /// <summary>
        /// A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
        /// </summary>
        public readonly bool? AllowMajorVersionUpgrade;
        /// <summary>
        /// The AWS Identity and Access Management (IAM) roles associated with the DB instance.
        /// </summary>
        public readonly ImmutableArray<Outputs.DBInstanceRole> AssociatedRoles;
        /// <summary>
        /// A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
        /// </summary>
        public readonly bool? AutoMinorVersionUpgrade;
        /// <summary>
        /// The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.
        /// </summary>
        public readonly string? AvailabilityZone;
        /// <summary>
        /// The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
        /// </summary>
        public readonly int? BackupRetentionPeriod;
        /// <summary>
        /// The identifier of the CA certificate for this DB instance.
        /// </summary>
        public readonly string? CACertificateIdentifier;
        /// <summary>
        /// Returns the details of the DB instance's server certificate.
        /// </summary>
        public readonly Outputs.DBInstanceCertificateDetails? CertificateDetails;
        /// <summary>
        /// A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
        /// </summary>
        public readonly bool? CopyTagsToSnapshot;
        /// <summary>
        /// The identifier for the RDS for MySQL Multi-AZ DB cluster snapshot to restore from. For more information on Multi-AZ DB clusters, see Multi-AZ deployments with two readable standby DB instances in the Amazon RDS User Guide .
        /// 
        /// Constraints:
        ///  * Must match the identifier of an existing Multi-AZ DB cluster snapshot.
        ///  * Can't be specified when DBSnapshotIdentifier is specified.
        ///  * Must be specified when DBSnapshotIdentifier isn't specified.
        ///  * If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the DBClusterSnapshotIdentifier must be the ARN of the shared snapshot.
        ///  * Can't be the identifier of an Aurora DB cluster snapshot.
        ///  * Can't be the identifier of an RDS for PostgreSQL Multi-AZ DB cluster snapshot.
        /// </summary>
        public readonly string? DBClusterSnapshotIdentifier;
        /// <summary>
        /// The Amazon Resource Name (ARN) for the DB instance.
        /// </summary>
        public readonly string? DBInstanceArn;
        /// <summary>
        /// The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.
        /// </summary>
        public readonly string? DBInstanceClass;
        /// <summary>
        /// The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.
        /// </summary>
        public readonly string? DBParameterGroupName;
        /// <summary>
        /// A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
        /// </summary>
        public readonly ImmutableArray<string> DBSecurityGroups;
        /// <summary>
        /// The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is valid for RDS Custom only.
        /// </summary>
        public readonly string? DBSystemId;
        /// <summary>
        /// The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
        /// </summary>
        public readonly string? DbiResourceId;
        /// <summary>
        /// A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.
        /// </summary>
        public readonly bool? DeleteAutomatedBackups;
        /// <summary>
        /// A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        /// </summary>
        public readonly bool? DeletionProtection;
        /// <summary>
        /// The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
        /// </summary>
        public readonly string? Domain;
        /// <summary>
        /// Specify the name of the IAM role to be used when making API calls to the Directory Service.
        /// </summary>
        public readonly string? DomainIAMRoleName;
        /// <summary>
        /// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.
        /// </summary>
        public readonly ImmutableArray<string> EnableCloudwatchLogsExports;
        /// <summary>
        /// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
        /// </summary>
        public readonly bool? EnableIAMDatabaseAuthentication;
        /// <summary>
        /// A value that indicates whether to enable Performance Insights for the DB instance.
        /// </summary>
        public readonly bool? EnablePerformanceInsights;
        /// <summary>
        /// Specifies the connection endpoint.
        /// </summary>
        public readonly Outputs.DBInstanceEndpoint? Endpoint;
        /// <summary>
        /// The name of the database engine that you want to use for this DB instance.
        /// </summary>
        public readonly string? Engine;
        /// <summary>
        /// The version number of the database engine to use.
        /// </summary>
        public readonly string? EngineVersion;
        /// <summary>
        /// The number of I/O operations per second (IOPS) that the database provisions.
        /// </summary>
        public readonly int? Iops;
        /// <summary>
        /// License model information for this DB instance.
        /// </summary>
        public readonly string? LicenseModel;
        /// <summary>
        /// A value that indicates whether to manage the master user password with AWS Secrets Manager.
        /// </summary>
        public readonly bool? ManageMasterUserPassword;
        /// <summary>
        /// Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
        /// </summary>
        public readonly Outputs.DBInstanceMasterUserSecret? MasterUserSecret;
        /// <summary>
        /// The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
        /// </summary>
        public readonly int? MaxAllocatedStorage;
        /// <summary>
        /// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        /// </summary>
        public readonly int? MonitoringInterval;
        /// <summary>
        /// The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.
        /// </summary>
        public readonly string? MonitoringRoleArn;
        /// <summary>
        /// Specifies whether the database instance is a multiple Availability Zone deployment.
        /// </summary>
        public readonly bool? MultiAZ;
        /// <summary>
        /// The network type of the DB cluster.
        /// </summary>
        public readonly string? NetworkType;
        /// <summary>
        /// Indicates that the DB instance should be associated with the specified option group.
        /// </summary>
        public readonly string? OptionGroupName;
        /// <summary>
        /// The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
        /// </summary>
        public readonly string? PerformanceInsightsKMSKeyId;
        /// <summary>
        /// The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).
        /// </summary>
        public readonly int? PerformanceInsightsRetentionPeriod;
        /// <summary>
        /// The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
        /// </summary>
        public readonly string? PreferredBackupWindow;
        /// <summary>
        /// he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
        /// </summary>
        public readonly string? PreferredMaintenanceWindow;
        /// <summary>
        /// The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
        /// </summary>
        public readonly ImmutableArray<Outputs.DBInstanceProcessorFeature> ProcessorFeatures;
        /// <summary>
        /// A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.
        /// </summary>
        public readonly int? PromotionTier;
        /// <summary>
        /// Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
        /// </summary>
        public readonly bool? PubliclyAccessible;
        /// <summary>
        /// The open mode of an Oracle read replica. The default is open-read-only.
        /// </summary>
        public readonly string? ReplicaMode;
        /// <summary>
        /// Specifies the storage throughput for the DB instance.
        /// </summary>
        public readonly int? StorageThroughput;
        /// <summary>
        /// Specifies the storage type to be associated with the DB instance.
        /// </summary>
        public readonly string? StorageType;
        /// <summary>
        /// Tags to assign to the DB instance.
        /// </summary>
        public readonly ImmutableArray<Outputs.DBInstanceTag> Tags;
        /// <summary>
        /// The ARN from the key store with which to associate the instance for TDE encryption.
        /// </summary>
        public readonly string? TdeCredentialArn;
        /// <summary>
        /// A value that indicates whether the DB instance class of the DB instance uses its default processor features.
        /// </summary>
        public readonly bool? UseDefaultProcessorFeatures;
        /// <summary>
        /// A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.
        /// </summary>
        public readonly ImmutableArray<string> VPCSecurityGroups;

        [OutputConstructor]
        private GetDBInstanceResult(
            string? allocatedStorage,

            bool? allowMajorVersionUpgrade,

            ImmutableArray<Outputs.DBInstanceRole> associatedRoles,

            bool? autoMinorVersionUpgrade,

            string? availabilityZone,

            int? backupRetentionPeriod,

            string? cACertificateIdentifier,

            Outputs.DBInstanceCertificateDetails? certificateDetails,

            bool? copyTagsToSnapshot,

            string? dBClusterSnapshotIdentifier,

            string? dBInstanceArn,

            string? dBInstanceClass,

            string? dBParameterGroupName,

            ImmutableArray<string> dBSecurityGroups,

            string? dBSystemId,

            string? dbiResourceId,

            bool? deleteAutomatedBackups,

            bool? deletionProtection,

            string? domain,

            string? domainIAMRoleName,

            ImmutableArray<string> enableCloudwatchLogsExports,

            bool? enableIAMDatabaseAuthentication,

            bool? enablePerformanceInsights,

            Outputs.DBInstanceEndpoint? endpoint,

            string? engine,

            string? engineVersion,

            int? iops,

            string? licenseModel,

            bool? manageMasterUserPassword,

            Outputs.DBInstanceMasterUserSecret? masterUserSecret,

            int? maxAllocatedStorage,

            int? monitoringInterval,

            string? monitoringRoleArn,

            bool? multiAZ,

            string? networkType,

            string? optionGroupName,

            string? performanceInsightsKMSKeyId,

            int? performanceInsightsRetentionPeriod,

            string? preferredBackupWindow,

            string? preferredMaintenanceWindow,

            ImmutableArray<Outputs.DBInstanceProcessorFeature> processorFeatures,

            int? promotionTier,

            bool? publiclyAccessible,

            string? replicaMode,

            int? storageThroughput,

            string? storageType,

            ImmutableArray<Outputs.DBInstanceTag> tags,

            string? tdeCredentialArn,

            bool? useDefaultProcessorFeatures,

            ImmutableArray<string> vPCSecurityGroups)
        {
            AllocatedStorage = allocatedStorage;
            AllowMajorVersionUpgrade = allowMajorVersionUpgrade;
            AssociatedRoles = associatedRoles;
            AutoMinorVersionUpgrade = autoMinorVersionUpgrade;
            AvailabilityZone = availabilityZone;
            BackupRetentionPeriod = backupRetentionPeriod;
            CACertificateIdentifier = cACertificateIdentifier;
            CertificateDetails = certificateDetails;
            CopyTagsToSnapshot = copyTagsToSnapshot;
            DBClusterSnapshotIdentifier = dBClusterSnapshotIdentifier;
            DBInstanceArn = dBInstanceArn;
            DBInstanceClass = dBInstanceClass;
            DBParameterGroupName = dBParameterGroupName;
            DBSecurityGroups = dBSecurityGroups;
            DBSystemId = dBSystemId;
            DbiResourceId = dbiResourceId;
            DeleteAutomatedBackups = deleteAutomatedBackups;
            DeletionProtection = deletionProtection;
            Domain = domain;
            DomainIAMRoleName = domainIAMRoleName;
            EnableCloudwatchLogsExports = enableCloudwatchLogsExports;
            EnableIAMDatabaseAuthentication = enableIAMDatabaseAuthentication;
            EnablePerformanceInsights = enablePerformanceInsights;
            Endpoint = endpoint;
            Engine = engine;
            EngineVersion = engineVersion;
            Iops = iops;
            LicenseModel = licenseModel;
            ManageMasterUserPassword = manageMasterUserPassword;
            MasterUserSecret = masterUserSecret;
            MaxAllocatedStorage = maxAllocatedStorage;
            MonitoringInterval = monitoringInterval;
            MonitoringRoleArn = monitoringRoleArn;
            MultiAZ = multiAZ;
            NetworkType = networkType;
            OptionGroupName = optionGroupName;
            PerformanceInsightsKMSKeyId = performanceInsightsKMSKeyId;
            PerformanceInsightsRetentionPeriod = performanceInsightsRetentionPeriod;
            PreferredBackupWindow = preferredBackupWindow;
            PreferredMaintenanceWindow = preferredMaintenanceWindow;
            ProcessorFeatures = processorFeatures;
            PromotionTier = promotionTier;
            PubliclyAccessible = publiclyAccessible;
            ReplicaMode = replicaMode;
            StorageThroughput = storageThroughput;
            StorageType = storageType;
            Tags = tags;
            TdeCredentialArn = tdeCredentialArn;
            UseDefaultProcessorFeatures = useDefaultProcessorFeatures;
            VPCSecurityGroups = vPCSecurityGroups;
        }
    }
}
