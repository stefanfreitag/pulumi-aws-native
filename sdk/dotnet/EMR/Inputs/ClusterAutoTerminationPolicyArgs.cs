// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR.Inputs
{

    public sealed class ClusterAutoTerminationPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("idleTimeout")]
        public Input<int>? IdleTimeout { get; set; }

        public ClusterAutoTerminationPolicyArgs()
        {
        }
        public static new ClusterAutoTerminationPolicyArgs Empty => new ClusterAutoTerminationPolicyArgs();
    }
}
