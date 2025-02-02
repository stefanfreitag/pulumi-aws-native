// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AutoScaling.Outputs
{

    [OutputType]
    public sealed class ScalingPolicyMetric
    {
        public readonly ImmutableArray<Outputs.ScalingPolicyMetricDimension> Dimensions;
        public readonly string MetricName;
        public readonly string Namespace;

        [OutputConstructor]
        private ScalingPolicyMetric(
            ImmutableArray<Outputs.ScalingPolicyMetricDimension> dimensions,

            string metricName,

            string @namespace)
        {
            Dimensions = dimensions;
            MetricName = metricName;
            Namespace = @namespace;
        }
    }
}
