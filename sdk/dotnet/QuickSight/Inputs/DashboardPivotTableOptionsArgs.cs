// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardPivotTableOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("cellStyle")]
        public Input<Inputs.DashboardTableCellStyleArgs>? CellStyle { get; set; }

        [Input("collapsedRowDimensionsVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardVisibility>? CollapsedRowDimensionsVisibility { get; set; }

        [Input("columnHeaderStyle")]
        public Input<Inputs.DashboardTableCellStyleArgs>? ColumnHeaderStyle { get; set; }

        [Input("columnNamesVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardVisibility>? ColumnNamesVisibility { get; set; }

        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("defaultCellWidth")]
        public Input<string>? DefaultCellWidth { get; set; }

        [Input("metricPlacement")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardPivotTableMetricPlacement>? MetricPlacement { get; set; }

        [Input("rowAlternateColorOptions")]
        public Input<Inputs.DashboardRowAlternateColorOptionsArgs>? RowAlternateColorOptions { get; set; }

        [Input("rowFieldNamesStyle")]
        public Input<Inputs.DashboardTableCellStyleArgs>? RowFieldNamesStyle { get; set; }

        [Input("rowHeaderStyle")]
        public Input<Inputs.DashboardTableCellStyleArgs>? RowHeaderStyle { get; set; }

        [Input("rowsLabelOptions")]
        public Input<Inputs.DashboardPivotTableRowsLabelOptionsArgs>? RowsLabelOptions { get; set; }

        [Input("rowsLayout")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardPivotTableRowsLayout>? RowsLayout { get; set; }

        [Input("singleMetricVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardVisibility>? SingleMetricVisibility { get; set; }

        [Input("toggleButtonsVisibility")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardVisibility>? ToggleButtonsVisibility { get; set; }

        public DashboardPivotTableOptionsArgs()
        {
        }
        public static new DashboardPivotTableOptionsArgs Empty => new DashboardPivotTableOptionsArgs();
    }
}
