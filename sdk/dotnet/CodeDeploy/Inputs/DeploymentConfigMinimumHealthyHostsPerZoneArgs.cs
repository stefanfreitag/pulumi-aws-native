// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeDeploy.Inputs
{

    public sealed class DeploymentConfigMinimumHealthyHostsPerZoneArgs : global::Pulumi.ResourceArgs
    {
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("value", required: true)]
        public Input<int> Value { get; set; } = null!;

        public DeploymentConfigMinimumHealthyHostsPerZoneArgs()
        {
        }
        public static new DeploymentConfigMinimumHealthyHostsPerZoneArgs Empty => new DeploymentConfigMinimumHealthyHostsPerZoneArgs();
    }
}
