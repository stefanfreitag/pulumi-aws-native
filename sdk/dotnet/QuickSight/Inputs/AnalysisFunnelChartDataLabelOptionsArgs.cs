// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisFunnelChartDataLabelOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("categoryLabelVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? CategoryLabelVisibility { get; set; }

        [Input("labelColor")]
        public Input<string>? LabelColor { get; set; }

        [Input("labelFontConfiguration")]
        public Input<Inputs.AnalysisFontConfigurationArgs>? LabelFontConfiguration { get; set; }

        [Input("measureDataLabelStyle")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisFunnelChartMeasureDataLabelStyle>? MeasureDataLabelStyle { get; set; }

        [Input("measureLabelVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? MeasureLabelVisibility { get; set; }

        [Input("position")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisDataLabelPosition>? Position { get; set; }

        [Input("visibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? Visibility { get; set; }

        public AnalysisFunnelChartDataLabelOptionsArgs()
        {
        }
        public static new AnalysisFunnelChartDataLabelOptionsArgs Empty => new AnalysisFunnelChartDataLabelOptionsArgs();
    }
}
