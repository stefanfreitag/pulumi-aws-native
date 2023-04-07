// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisTopBottomMoversComputationArgs : global::Pulumi.ResourceArgs
    {
        [Input("category", required: true)]
        public Input<Inputs.AnalysisDimensionFieldArgs> Category { get; set; } = null!;

        [Input("computationId", required: true)]
        public Input<string> ComputationId { get; set; } = null!;

        [Input("moverSize")]
        public Input<double>? MoverSize { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("sortOrder")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisTopBottomSortOrder>? SortOrder { get; set; }

        [Input("time", required: true)]
        public Input<Inputs.AnalysisDimensionFieldArgs> Time { get; set; } = null!;

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisTopBottomComputationType> Type { get; set; } = null!;

        [Input("value")]
        public Input<Inputs.AnalysisMeasureFieldArgs>? Value { get; set; }

        public AnalysisTopBottomMoversComputationArgs()
        {
        }
        public static new AnalysisTopBottomMoversComputationArgs Empty => new AnalysisTopBottomMoversComputationArgs();
    }
}
