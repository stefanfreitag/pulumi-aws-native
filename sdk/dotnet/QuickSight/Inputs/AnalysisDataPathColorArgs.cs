// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisDataPathColorArgs : global::Pulumi.ResourceArgs
    {
        [Input("color", required: true)]
        public Input<string> Color { get; set; } = null!;

        [Input("element", required: true)]
        public Input<Inputs.AnalysisDataPathValueArgs> Element { get; set; } = null!;

        [Input("timeGranularity")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisTimeGranularity>? TimeGranularity { get; set; }

        public AnalysisDataPathColorArgs()
        {
        }
        public static new AnalysisDataPathColorArgs Empty => new AnalysisDataPathColorArgs();
    }
}
