// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardLineChartAggregatedFieldWellsArgs : global::Pulumi.ResourceArgs
    {
        [Input("category")]
        private InputList<Inputs.DashboardDimensionFieldArgs>? _category;
        public InputList<Inputs.DashboardDimensionFieldArgs> Category
        {
            get => _category ?? (_category = new InputList<Inputs.DashboardDimensionFieldArgs>());
            set => _category = value;
        }

        [Input("colors")]
        private InputList<Inputs.DashboardDimensionFieldArgs>? _colors;
        public InputList<Inputs.DashboardDimensionFieldArgs> Colors
        {
            get => _colors ?? (_colors = new InputList<Inputs.DashboardDimensionFieldArgs>());
            set => _colors = value;
        }

        [Input("smallMultiples")]
        private InputList<Inputs.DashboardDimensionFieldArgs>? _smallMultiples;
        public InputList<Inputs.DashboardDimensionFieldArgs> SmallMultiples
        {
            get => _smallMultiples ?? (_smallMultiples = new InputList<Inputs.DashboardDimensionFieldArgs>());
            set => _smallMultiples = value;
        }

        [Input("values")]
        private InputList<Inputs.DashboardMeasureFieldArgs>? _values;
        public InputList<Inputs.DashboardMeasureFieldArgs> Values
        {
            get => _values ?? (_values = new InputList<Inputs.DashboardMeasureFieldArgs>());
            set => _values = value;
        }

        public DashboardLineChartAggregatedFieldWellsArgs()
        {
        }
        public static new DashboardLineChartAggregatedFieldWellsArgs Empty => new DashboardLineChartAggregatedFieldWellsArgs();
    }
}
