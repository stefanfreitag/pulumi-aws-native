// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisTotalOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("customLabel")]
        public Input<string>? CustomLabel { get; set; }

        [Input("placement")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisTableTotalsPlacement>? Placement { get; set; }

        [Input("scrollStatus")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisTableTotalsScrollStatus>? ScrollStatus { get; set; }

        [Input("totalAggregationOptions")]
        private InputList<Inputs.AnalysisTotalAggregationOptionArgs>? _totalAggregationOptions;
        public InputList<Inputs.AnalysisTotalAggregationOptionArgs> TotalAggregationOptions
        {
            get => _totalAggregationOptions ?? (_totalAggregationOptions = new InputList<Inputs.AnalysisTotalAggregationOptionArgs>());
            set => _totalAggregationOptions = value;
        }

        [Input("totalCellStyle")]
        public Input<Inputs.AnalysisTableCellStyleArgs>? TotalCellStyle { get; set; }

        [Input("totalsVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? TotalsVisibility { get; set; }

        public AnalysisTotalOptionsArgs()
        {
        }
        public static new AnalysisTotalOptionsArgs Empty => new AnalysisTotalOptionsArgs();
    }
}
