// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class ContinuousDeploymentPolicySingleWeightConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("sessionStickinessConfig")]
        public Input<Inputs.ContinuousDeploymentPolicySessionStickinessConfigArgs>? SessionStickinessConfig { get; set; }

        [Input("weight", required: true)]
        public Input<double> Weight { get; set; } = null!;

        public ContinuousDeploymentPolicySingleWeightConfigArgs()
        {
        }
        public static new ContinuousDeploymentPolicySingleWeightConfigArgs Empty => new ContinuousDeploymentPolicySingleWeightConfigArgs();
    }
}
