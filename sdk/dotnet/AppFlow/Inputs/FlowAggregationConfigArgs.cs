// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class FlowAggregationConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("aggregationType")]
        public Input<Pulumi.AwsNative.AppFlow.FlowAggregationType>? AggregationType { get; set; }

        public FlowAggregationConfigArgs()
        {
        }
        public static new FlowAggregationConfigArgs Empty => new FlowAggregationConfigArgs();
    }
}
