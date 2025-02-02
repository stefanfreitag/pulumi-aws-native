// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardNumericalAggregationFunctionArgs : global::Pulumi.ResourceArgs
    {
        [Input("percentileAggregation")]
        public Input<Inputs.DashboardPercentileAggregationArgs>? PercentileAggregation { get; set; }

        [Input("simpleNumericalAggregation")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardSimpleNumericalAggregationFunction>? SimpleNumericalAggregation { get; set; }

        public DashboardNumericalAggregationFunctionArgs()
        {
        }
        public static new DashboardNumericalAggregationFunctionArgs Empty => new DashboardNumericalAggregationFunctionArgs();
    }
}
