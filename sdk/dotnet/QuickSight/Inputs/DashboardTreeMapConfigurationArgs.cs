// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardTreeMapConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("colorLabelOptions")]
        public Input<Inputs.DashboardChartAxisLabelOptionsArgs>? ColorLabelOptions { get; set; }

        [Input("colorScale")]
        public Input<Inputs.DashboardColorScaleArgs>? ColorScale { get; set; }

        [Input("dataLabels")]
        public Input<Inputs.DashboardDataLabelOptionsArgs>? DataLabels { get; set; }

        [Input("fieldWells")]
        public Input<Inputs.DashboardTreeMapFieldWellsArgs>? FieldWells { get; set; }

        [Input("groupLabelOptions")]
        public Input<Inputs.DashboardChartAxisLabelOptionsArgs>? GroupLabelOptions { get; set; }

        [Input("legend")]
        public Input<Inputs.DashboardLegendOptionsArgs>? Legend { get; set; }

        [Input("sizeLabelOptions")]
        public Input<Inputs.DashboardChartAxisLabelOptionsArgs>? SizeLabelOptions { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.DashboardTreeMapSortConfigurationArgs>? SortConfiguration { get; set; }

        [Input("tooltip")]
        public Input<Inputs.DashboardTooltipOptionsArgs>? Tooltip { get; set; }

        public DashboardTreeMapConfigurationArgs()
        {
        }
        public static new DashboardTreeMapConfigurationArgs Empty => new DashboardTreeMapConfigurationArgs();
    }
}
