// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecr.Inputs
{

    /// <summary>
    /// An array of objects representing the details of a replication destination.
    /// </summary>
    public sealed class ReplicationConfigurationReplicationDestinationArgs : global::Pulumi.ResourceArgs
    {
        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        [Input("registryId", required: true)]
        public Input<string> RegistryId { get; set; } = null!;

        public ReplicationConfigurationReplicationDestinationArgs()
        {
        }
        public static new ReplicationConfigurationReplicationDestinationArgs Empty => new ReplicationConfigurationReplicationDestinationArgs();
    }
}
