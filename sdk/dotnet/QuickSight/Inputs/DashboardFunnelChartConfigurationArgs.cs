// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardFunnelChartConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("categoryLabelOptions")]
        public Input<Inputs.DashboardChartAxisLabelOptionsArgs>? CategoryLabelOptions { get; set; }

        [Input("dataLabelOptions")]
        public Input<Inputs.DashboardFunnelChartDataLabelOptionsArgs>? DataLabelOptions { get; set; }

        [Input("fieldWells")]
        public Input<Inputs.DashboardFunnelChartFieldWellsArgs>? FieldWells { get; set; }

        [Input("sortConfiguration")]
        public Input<Inputs.DashboardFunnelChartSortConfigurationArgs>? SortConfiguration { get; set; }

        [Input("tooltip")]
        public Input<Inputs.DashboardTooltipOptionsArgs>? Tooltip { get; set; }

        [Input("valueLabelOptions")]
        public Input<Inputs.DashboardChartAxisLabelOptionsArgs>? ValueLabelOptions { get; set; }

        [Input("visualPalette")]
        public Input<Inputs.DashboardVisualPaletteArgs>? VisualPalette { get; set; }

        public DashboardFunnelChartConfigurationArgs()
        {
        }
        public static new DashboardFunnelChartConfigurationArgs Empty => new DashboardFunnelChartConfigurationArgs();
    }
}
