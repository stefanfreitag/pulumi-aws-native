// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache
{
    public static class GetReplicationGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::ElastiCache::ReplicationGroup
        /// </summary>
        public static Task<GetReplicationGroupResult> InvokeAsync(GetReplicationGroupArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetReplicationGroupResult>("aws-native:elasticache:getReplicationGroup", args ?? new GetReplicationGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ElastiCache::ReplicationGroup
        /// </summary>
        public static Output<GetReplicationGroupResult> Invoke(GetReplicationGroupInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetReplicationGroupResult>("aws-native:elasticache:getReplicationGroup", args ?? new GetReplicationGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetReplicationGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("replicationGroupId", required: true)]
        public string ReplicationGroupId { get; set; } = null!;

        public GetReplicationGroupArgs()
        {
        }
        public static new GetReplicationGroupArgs Empty => new GetReplicationGroupArgs();
    }

    public sealed class GetReplicationGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("replicationGroupId", required: true)]
        public Input<string> ReplicationGroupId { get; set; } = null!;

        public GetReplicationGroupInvokeArgs()
        {
        }
        public static new GetReplicationGroupInvokeArgs Empty => new GetReplicationGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetReplicationGroupResult
    {
        public readonly string? AuthToken;
        public readonly bool? AutoMinorVersionUpgrade;
        public readonly bool? AutomaticFailoverEnabled;
        public readonly string? CacheNodeType;
        public readonly string? CacheParameterGroupName;
        public readonly ImmutableArray<string> CacheSecurityGroupNames;
        public readonly string? ConfigurationEndPointAddress;
        public readonly string? ConfigurationEndPointPort;
        public readonly string? EngineVersion;
        public readonly ImmutableArray<Outputs.ReplicationGroupLogDeliveryConfigurationRequest> LogDeliveryConfigurations;
        public readonly bool? MultiAZEnabled;
        public readonly ImmutableArray<Outputs.ReplicationGroupNodeGroupConfiguration> NodeGroupConfiguration;
        public readonly string? NotificationTopicArn;
        public readonly int? NumCacheClusters;
        public readonly int? NumNodeGroups;
        public readonly string? PreferredMaintenanceWindow;
        public readonly string? PrimaryClusterId;
        public readonly string? PrimaryEndPointAddress;
        public readonly string? PrimaryEndPointPort;
        public readonly string? ReadEndPointAddresses;
        public readonly ImmutableArray<string> ReadEndPointAddressesList;
        public readonly string? ReadEndPointPorts;
        public readonly ImmutableArray<string> ReadEndPointPortsList;
        public readonly string? ReaderEndPointAddress;
        public readonly string? ReaderEndPointPort;
        public readonly string? ReplicationGroupDescription;
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly int? SnapshotRetentionLimit;
        public readonly string? SnapshotWindow;
        public readonly string? SnapshottingClusterId;
        public readonly ImmutableArray<Outputs.ReplicationGroupTag> Tags;
        public readonly ImmutableArray<string> UserGroupIds;

        [OutputConstructor]
        private GetReplicationGroupResult(
            string? authToken,

            bool? autoMinorVersionUpgrade,

            bool? automaticFailoverEnabled,

            string? cacheNodeType,

            string? cacheParameterGroupName,

            ImmutableArray<string> cacheSecurityGroupNames,

            string? configurationEndPointAddress,

            string? configurationEndPointPort,

            string? engineVersion,

            ImmutableArray<Outputs.ReplicationGroupLogDeliveryConfigurationRequest> logDeliveryConfigurations,

            bool? multiAZEnabled,

            ImmutableArray<Outputs.ReplicationGroupNodeGroupConfiguration> nodeGroupConfiguration,

            string? notificationTopicArn,

            int? numCacheClusters,

            int? numNodeGroups,

            string? preferredMaintenanceWindow,

            string? primaryClusterId,

            string? primaryEndPointAddress,

            string? primaryEndPointPort,

            string? readEndPointAddresses,

            ImmutableArray<string> readEndPointAddressesList,

            string? readEndPointPorts,

            ImmutableArray<string> readEndPointPortsList,

            string? readerEndPointAddress,

            string? readerEndPointPort,

            string? replicationGroupDescription,

            ImmutableArray<string> securityGroupIds,

            int? snapshotRetentionLimit,

            string? snapshotWindow,

            string? snapshottingClusterId,

            ImmutableArray<Outputs.ReplicationGroupTag> tags,

            ImmutableArray<string> userGroupIds)
        {
            AuthToken = authToken;
            AutoMinorVersionUpgrade = autoMinorVersionUpgrade;
            AutomaticFailoverEnabled = automaticFailoverEnabled;
            CacheNodeType = cacheNodeType;
            CacheParameterGroupName = cacheParameterGroupName;
            CacheSecurityGroupNames = cacheSecurityGroupNames;
            ConfigurationEndPointAddress = configurationEndPointAddress;
            ConfigurationEndPointPort = configurationEndPointPort;
            EngineVersion = engineVersion;
            LogDeliveryConfigurations = logDeliveryConfigurations;
            MultiAZEnabled = multiAZEnabled;
            NodeGroupConfiguration = nodeGroupConfiguration;
            NotificationTopicArn = notificationTopicArn;
            NumCacheClusters = numCacheClusters;
            NumNodeGroups = numNodeGroups;
            PreferredMaintenanceWindow = preferredMaintenanceWindow;
            PrimaryClusterId = primaryClusterId;
            PrimaryEndPointAddress = primaryEndPointAddress;
            PrimaryEndPointPort = primaryEndPointPort;
            ReadEndPointAddresses = readEndPointAddresses;
            ReadEndPointAddressesList = readEndPointAddressesList;
            ReadEndPointPorts = readEndPointPorts;
            ReadEndPointPortsList = readEndPointPortsList;
            ReaderEndPointAddress = readerEndPointAddress;
            ReaderEndPointPort = readerEndPointPort;
            ReplicationGroupDescription = replicationGroupDescription;
            SecurityGroupIds = securityGroupIds;
            SnapshotRetentionLimit = snapshotRetentionLimit;
            SnapshotWindow = snapshotWindow;
            SnapshottingClusterId = snapshottingClusterId;
            Tags = tags;
            UserGroupIds = userGroupIds;
        }
    }
}
