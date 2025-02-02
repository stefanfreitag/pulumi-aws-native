// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisColumnTooltipItemArgs : global::Pulumi.ResourceArgs
    {
        [Input("aggregation")]
        public Input<Inputs.AnalysisAggregationFunctionArgs>? Aggregation { get; set; }

        [Input("column", required: true)]
        public Input<Inputs.AnalysisColumnIdentifierArgs> Column { get; set; } = null!;

        [Input("label")]
        public Input<string>? Label { get; set; }

        [Input("visibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? Visibility { get; set; }

        public AnalysisColumnTooltipItemArgs()
        {
        }
        public static new AnalysisColumnTooltipItemArgs Empty => new AnalysisColumnTooltipItemArgs();
    }
}
