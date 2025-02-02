// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisRadarChartConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("alternateBandColorsVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisVisibility>? AlternateBandColorsVisibility { get; set; }

        [Input("alternateBandEvenColor")]
        public Input<string>? AlternateBandEvenColor { get; set; }

        [Input("alternateBandOddColor")]
        public Input<string>? AlternateBandOddColor { get; set; }

        [Input("axesRangeScale")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisRadarChartAxesRangeScale>? AxesRangeScale { get; set; }

        [Input("baseSeriesSettings")]
        public Input<Inputs.AnalysisRadarChartSeriesSettingsArgs>? BaseSeriesSettings { get; set; }

        [Input("categoryAxis")]
        public Input<Inputs.AnalysisAxisDisplayOptionsArgs>? CategoryAxis { get; set; }

        [Input("categoryLabelOptions")]
        public Input<Inputs.AnalysisChartAxisLabelOptionsArgs>? CategoryLabelOptions { get; set; }

        [Input("colorAxis")]
        public Input<Inputs.AnalysisAxisDisplayOptionsArgs>? ColorAxis { get; set; }

        [Input("colorLabelOptions")]
        public Input<Inputs.AnalysisChartAxisLabelOptionsArgs>? ColorLabelOptions { get; set; }

        [Input("fieldWells")]
        public Input<Inputs.AnalysisRadarChartFieldWellsArgs>? FieldWells { get; set; }

        [Input("legend")]
        public Input<Inputs.AnalysisLegendOptionsArgs>? Legend { get; set; }

        [Input("shape")]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisRadarChartShape>? Shape { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.AnalysisRadarChartSortConfigurationArgs>? SortConfiguration { get; set; }

        [Input("startAngle")]
        public Input<double>? StartAngle { get; set; }

        [Input("visualPalette")]
        public Input<Inputs.AnalysisVisualPaletteArgs>? VisualPalette { get; set; }

        public AnalysisRadarChartConfigurationArgs()
        {
        }
        public static new AnalysisRadarChartConfigurationArgs Empty => new AnalysisRadarChartConfigurationArgs();
    }
}
