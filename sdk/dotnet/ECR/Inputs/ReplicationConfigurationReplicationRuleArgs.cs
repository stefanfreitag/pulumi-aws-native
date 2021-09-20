// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ECR.Inputs
{

    /// <summary>
    /// An array of objects representing the details of a replication destination.
    /// </summary>
    public sealed class ReplicationConfigurationReplicationRuleArgs : Pulumi.ResourceArgs
    {
        [Input("destinations", required: true)]
        private InputList<Inputs.ReplicationConfigurationReplicationDestinationArgs>? _destinations;

        /// <summary>
        /// An array of objects representing the details of a replication destination.
        /// </summary>
        public InputList<Inputs.ReplicationConfigurationReplicationDestinationArgs> Destinations
        {
            get => _destinations ?? (_destinations = new InputList<Inputs.ReplicationConfigurationReplicationDestinationArgs>());
            set => _destinations = value;
        }

        public ReplicationConfigurationReplicationRuleArgs()
        {
        }
    }
}
