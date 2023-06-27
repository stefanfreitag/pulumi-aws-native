// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Grafana.Inputs
{

    /// <summary>
    /// The configuration settings for an Amazon VPC that contains data sources for your Grafana workspace to connect to.
    /// </summary>
    public sealed class WorkspaceVpcConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("securityGroupIds", required: true)]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// The list of Amazon EC2 security group IDs attached to the Amazon VPC for your Grafana workspace to connect.
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// The list of Amazon EC2 subnet IDs created in the Amazon VPC for your Grafana workspace to connect.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        public WorkspaceVpcConfigurationArgs()
        {
        }
        public static new WorkspaceVpcConfigurationArgs Empty => new WorkspaceVpcConfigurationArgs();
    }
}
