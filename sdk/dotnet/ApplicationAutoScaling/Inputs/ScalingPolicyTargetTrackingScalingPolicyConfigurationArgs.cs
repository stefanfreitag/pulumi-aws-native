// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationAutoScaling.Inputs
{

    public sealed class ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("customizedMetricSpecification")]
        public Input<Inputs.ScalingPolicyCustomizedMetricSpecificationArgs>? CustomizedMetricSpecification { get; set; }

        [Input("disableScaleIn")]
        public Input<bool>? DisableScaleIn { get; set; }

        [Input("predefinedMetricSpecification")]
        public Input<Inputs.ScalingPolicyPredefinedMetricSpecificationArgs>? PredefinedMetricSpecification { get; set; }

        [Input("scaleInCooldown")]
        public Input<int>? ScaleInCooldown { get; set; }

        [Input("scaleOutCooldown")]
        public Input<int>? ScaleOutCooldown { get; set; }

        [Input("targetValue", required: true)]
        public Input<double> TargetValue { get; set; } = null!;

        public ScalingPolicyTargetTrackingScalingPolicyConfigurationArgs()
        {
        }
    }
}
