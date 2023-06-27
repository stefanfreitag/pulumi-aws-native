// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardHeatMapAggregatedFieldWellsArgs : global::Pulumi.ResourceArgs
    {
        [Input("columns")]
        private InputList<Inputs.DashboardDimensionFieldArgs>? _columns;
        public InputList<Inputs.DashboardDimensionFieldArgs> Columns
        {
            get => _columns ?? (_columns = new InputList<Inputs.DashboardDimensionFieldArgs>());
            set => _columns = value;
        }

        [Input("rows")]
        private InputList<Inputs.DashboardDimensionFieldArgs>? _rows;
        public InputList<Inputs.DashboardDimensionFieldArgs> Rows
        {
            get => _rows ?? (_rows = new InputList<Inputs.DashboardDimensionFieldArgs>());
            set => _rows = value;
        }

        [Input("values")]
        private InputList<Inputs.DashboardMeasureFieldArgs>? _values;
        public InputList<Inputs.DashboardMeasureFieldArgs> Values
        {
            get => _values ?? (_values = new InputList<Inputs.DashboardMeasureFieldArgs>());
            set => _values = value;
        }

        public DashboardHeatMapAggregatedFieldWellsArgs()
        {
        }
        public static new DashboardHeatMapAggregatedFieldWellsArgs Empty => new DashboardHeatMapAggregatedFieldWellsArgs();
    }
}
