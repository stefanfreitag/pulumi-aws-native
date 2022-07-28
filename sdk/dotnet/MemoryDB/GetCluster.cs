// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MemoryDB
{
    public static class GetCluster
    {
        /// <summary>
        /// The AWS::MemoryDB::Cluster resource creates an Amazon MemoryDB Cluster.
        /// </summary>
        public static Task<GetClusterResult> InvokeAsync(GetClusterArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClusterResult>("aws-native:memorydb:getCluster", args ?? new GetClusterArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::MemoryDB::Cluster resource creates an Amazon MemoryDB Cluster.
        /// </summary>
        public static Output<GetClusterResult> Invoke(GetClusterInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetClusterResult>("aws-native:memorydb:getCluster", args ?? new GetClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClusterArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the cluster. This value must be unique as it also serves as the cluster identifier.
        /// </summary>
        [Input("clusterName", required: true)]
        public string ClusterName { get; set; } = null!;

        public GetClusterArgs()
        {
        }
        public static new GetClusterArgs Empty => new GetClusterArgs();
    }

    public sealed class GetClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the cluster. This value must be unique as it also serves as the cluster identifier.
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        public GetClusterInvokeArgs()
        {
        }
        public static new GetClusterInvokeArgs Empty => new GetClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetClusterResult
    {
        /// <summary>
        /// The name of the Access Control List to associate with the cluster.
        /// </summary>
        public readonly string? ACLName;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the cluster.
        /// </summary>
        public readonly string? ARN;
        /// <summary>
        /// A flag that enables automatic minor version upgrade when set to true.
        /// 
        /// You cannot modify the value of AutoMinorVersionUpgrade after the cluster is created. To enable AutoMinorVersionUpgrade on a cluster you must set AutoMinorVersionUpgrade to true when you create a cluster.
        /// </summary>
        public readonly bool? AutoMinorVersionUpgrade;
        /// <summary>
        /// The cluster endpoint.
        /// </summary>
        public readonly Outputs.ClusterEndpoint? ClusterEndpoint;
        /// <summary>
        /// An optional description of the cluster.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The Redis engine version used by the cluster.
        /// </summary>
        public readonly string? EngineVersion;
        /// <summary>
        /// The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. MemoryDB creates the snapshot, and then deletes the cluster immediately afterward.
        /// </summary>
        public readonly string? FinalSnapshotName;
        /// <summary>
        /// Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
        /// </summary>
        public readonly string? MaintenanceWindow;
        /// <summary>
        /// The compute and memory capacity of the nodes in the cluster.
        /// </summary>
        public readonly string? NodeType;
        /// <summary>
        /// The number of replicas to apply to each shard. The limit is 5.
        /// </summary>
        public readonly int? NumReplicasPerShard;
        /// <summary>
        /// The number of shards the cluster will contain.
        /// </summary>
        public readonly int? NumShards;
        /// <summary>
        /// The name of the parameter group associated with the cluster.
        /// </summary>
        public readonly string? ParameterGroupName;
        /// <summary>
        /// The status of the parameter group used by the cluster.
        /// </summary>
        public readonly string? ParameterGroupStatus;
        /// <summary>
        /// One or more Amazon VPC security groups associated with this cluster.
        /// </summary>
        public readonly ImmutableArray<string> SecurityGroupIds;
        /// <summary>
        /// The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
        /// </summary>
        public readonly int? SnapshotRetentionLimit;
        /// <summary>
        /// The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.
        /// </summary>
        public readonly string? SnapshotWindow;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
        /// </summary>
        public readonly string? SnsTopicArn;
        /// <summary>
        /// The status of the Amazon SNS notification topic. Notifications are sent only if the status is enabled.
        /// </summary>
        public readonly string? SnsTopicStatus;
        /// <summary>
        /// The status of the cluster. For example, Available, Updating, Creating.
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// The name of the subnet group to be used for the cluster.
        /// </summary>
        public readonly string? SubnetGroupName;
        /// <summary>
        /// An array of key-value pairs to apply to this cluster.
        /// </summary>
        public readonly ImmutableArray<Outputs.ClusterTag> Tags;

        [OutputConstructor]
        private GetClusterResult(
            string? aCLName,

            string? aRN,

            bool? autoMinorVersionUpgrade,

            Outputs.ClusterEndpoint? clusterEndpoint,

            string? description,

            string? engineVersion,

            string? finalSnapshotName,

            string? maintenanceWindow,

            string? nodeType,

            int? numReplicasPerShard,

            int? numShards,

            string? parameterGroupName,

            string? parameterGroupStatus,

            ImmutableArray<string> securityGroupIds,

            int? snapshotRetentionLimit,

            string? snapshotWindow,

            string? snsTopicArn,

            string? snsTopicStatus,

            string? status,

            string? subnetGroupName,

            ImmutableArray<Outputs.ClusterTag> tags)
        {
            ACLName = aCLName;
            ARN = aRN;
            AutoMinorVersionUpgrade = autoMinorVersionUpgrade;
            ClusterEndpoint = clusterEndpoint;
            Description = description;
            EngineVersion = engineVersion;
            FinalSnapshotName = finalSnapshotName;
            MaintenanceWindow = maintenanceWindow;
            NodeType = nodeType;
            NumReplicasPerShard = numReplicasPerShard;
            NumShards = numShards;
            ParameterGroupName = parameterGroupName;
            ParameterGroupStatus = parameterGroupStatus;
            SecurityGroupIds = securityGroupIds;
            SnapshotRetentionLimit = snapshotRetentionLimit;
            SnapshotWindow = snapshotWindow;
            SnsTopicArn = snsTopicArn;
            SnsTopicStatus = snsTopicStatus;
            Status = status;
            SubnetGroupName = subnetGroupName;
            Tags = tags;
        }
    }
}
