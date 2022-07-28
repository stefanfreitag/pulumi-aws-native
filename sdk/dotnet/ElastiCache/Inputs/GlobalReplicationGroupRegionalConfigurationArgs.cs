// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache.Inputs
{

    public sealed class GlobalReplicationGroupRegionalConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The replication group id of the Global Datastore member.
        /// </summary>
        [Input("replicationGroupId")]
        public Input<string>? ReplicationGroupId { get; set; }

        /// <summary>
        /// The AWS region of the Global Datastore member.
        /// </summary>
        [Input("replicationGroupRegion")]
        public Input<string>? ReplicationGroupRegion { get; set; }

        [Input("reshardingConfigurations")]
        private InputList<Inputs.GlobalReplicationGroupReshardingConfigurationArgs>? _reshardingConfigurations;

        /// <summary>
        /// A list of PreferredAvailabilityZones objects that specifies the configuration of a node group in the resharded cluster. 
        /// </summary>
        public InputList<Inputs.GlobalReplicationGroupReshardingConfigurationArgs> ReshardingConfigurations
        {
            get => _reshardingConfigurations ?? (_reshardingConfigurations = new InputList<Inputs.GlobalReplicationGroupReshardingConfigurationArgs>());
            set => _reshardingConfigurations = value;
        }

        public GlobalReplicationGroupRegionalConfigurationArgs()
        {
        }
        public static new GlobalReplicationGroupRegionalConfigurationArgs Empty => new GlobalReplicationGroupRegionalConfigurationArgs();
    }
}
