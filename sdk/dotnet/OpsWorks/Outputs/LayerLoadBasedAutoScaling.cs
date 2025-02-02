// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpsWorks.Outputs
{

    [OutputType]
    public sealed class LayerLoadBasedAutoScaling
    {
        public readonly Outputs.LayerAutoScalingThresholds? DownScaling;
        public readonly bool? Enable;
        public readonly Outputs.LayerAutoScalingThresholds? UpScaling;

        [OutputConstructor]
        private LayerLoadBasedAutoScaling(
            Outputs.LayerAutoScalingThresholds? downScaling,

            bool? enable,

            Outputs.LayerAutoScalingThresholds? upScaling)
        {
            DownScaling = downScaling;
            Enable = enable;
            UpScaling = upScaling;
        }
    }
}
