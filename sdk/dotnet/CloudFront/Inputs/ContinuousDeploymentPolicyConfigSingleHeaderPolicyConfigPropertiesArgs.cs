// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class ContinuousDeploymentPolicyConfigSingleHeaderPolicyConfigPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("header", required: true)]
        public Input<string> Header { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ContinuousDeploymentPolicyConfigSingleHeaderPolicyConfigPropertiesArgs()
        {
        }
        public static new ContinuousDeploymentPolicyConfigSingleHeaderPolicyConfigPropertiesArgs Empty => new ContinuousDeploymentPolicyConfigSingleHeaderPolicyConfigPropertiesArgs();
    }
}
