// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationAutoScaling.Inputs
{

    /// <summary>
    /// Represents a predefined metric for a target tracking scaling policy to use with Application Auto Scaling.
    /// </summary>
    public sealed class ScalingPolicyPredefinedMetricSpecificationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The metric type. The ALBRequestCountPerTarget metric type applies only to Spot Fleets and ECS services.
        /// </summary>
        [Input("predefinedMetricType", required: true)]
        public Input<string> PredefinedMetricType { get; set; } = null!;

        /// <summary>
        /// Identifies the resource associated with the metric type. You can't specify a resource label unless the metric type is ALBRequestCountPerTarget and there is a target group attached to the Spot Fleet or ECS service.
        /// </summary>
        [Input("resourceLabel")]
        public Input<string>? ResourceLabel { get; set; }

        public ScalingPolicyPredefinedMetricSpecificationArgs()
        {
        }
        public static new ScalingPolicyPredefinedMetricSpecificationArgs Empty => new ScalingPolicyPredefinedMetricSpecificationArgs();
    }
}
