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
    /// An object representing the replication configuration for a registry.
    /// </summary>
    public sealed class ReplicationConfigurationReplicationConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("rules", required: true)]
        private InputList<Inputs.ReplicationConfigurationReplicationRuleArgs>? _rules;

        /// <summary>
        /// An array of objects representing the replication rules for a replication configuration. A replication configuration may contain only one replication rule but the rule may contain one or more replication destinations.
        /// </summary>
        public InputList<Inputs.ReplicationConfigurationReplicationRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.ReplicationConfigurationReplicationRuleArgs>());
            set => _rules = value;
        }

        public ReplicationConfigurationReplicationConfigurationArgs()
        {
        }
    }
}
