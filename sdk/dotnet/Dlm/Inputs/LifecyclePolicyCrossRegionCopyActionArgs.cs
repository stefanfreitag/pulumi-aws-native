// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Dlm.Inputs
{

    public sealed class LifecyclePolicyCrossRegionCopyActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("encryptionConfiguration", required: true)]
        public Input<Inputs.LifecyclePolicyEncryptionConfigurationArgs> EncryptionConfiguration { get; set; } = null!;

        [Input("retainRule")]
        public Input<Inputs.LifecyclePolicyCrossRegionCopyRetainRuleArgs>? RetainRule { get; set; }

        [Input("target", required: true)]
        public Input<string> Target { get; set; } = null!;

        public LifecyclePolicyCrossRegionCopyActionArgs()
        {
        }
        public static new LifecyclePolicyCrossRegionCopyActionArgs Empty => new LifecyclePolicyCrossRegionCopyActionArgs();
    }
}
