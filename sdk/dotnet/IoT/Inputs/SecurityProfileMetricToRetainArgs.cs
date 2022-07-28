// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Inputs
{

    /// <summary>
    /// The metric you want to retain. Dimensions are optional.
    /// </summary>
    public sealed class SecurityProfileMetricToRetainArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// What is measured by the behavior.
        /// </summary>
        [Input("metric", required: true)]
        public Input<string> Metric { get; set; } = null!;

        [Input("metricDimension")]
        public Input<Inputs.SecurityProfileMetricDimensionArgs>? MetricDimension { get; set; }

        public SecurityProfileMetricToRetainArgs()
        {
        }
        public static new SecurityProfileMetricToRetainArgs Empty => new SecurityProfileMetricToRetainArgs();
    }
}
