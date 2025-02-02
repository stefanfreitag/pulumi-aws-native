// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class DashboardNumericRangeFilter
    {
        public readonly Outputs.DashboardAggregationFunction? AggregationFunction;
        public readonly Outputs.DashboardColumnIdentifier Column;
        public readonly string FilterId;
        public readonly bool? IncludeMaximum;
        public readonly bool? IncludeMinimum;
        public readonly Pulumi.AwsNative.QuickSight.DashboardFilterNullOption NullOption;
        public readonly Outputs.DashboardNumericRangeFilterValue? RangeMaximum;
        public readonly Outputs.DashboardNumericRangeFilterValue? RangeMinimum;
        public readonly Pulumi.AwsNative.QuickSight.DashboardNumericFilterSelectAllOptions? SelectAllOptions;

        [OutputConstructor]
        private DashboardNumericRangeFilter(
            Outputs.DashboardAggregationFunction? aggregationFunction,

            Outputs.DashboardColumnIdentifier column,

            string filterId,

            bool? includeMaximum,

            bool? includeMinimum,

            Pulumi.AwsNative.QuickSight.DashboardFilterNullOption nullOption,

            Outputs.DashboardNumericRangeFilterValue? rangeMaximum,

            Outputs.DashboardNumericRangeFilterValue? rangeMinimum,

            Pulumi.AwsNative.QuickSight.DashboardNumericFilterSelectAllOptions? selectAllOptions)
        {
            AggregationFunction = aggregationFunction;
            Column = column;
            FilterId = filterId;
            IncludeMaximum = includeMaximum;
            IncludeMinimum = includeMinimum;
            NullOption = nullOption;
            RangeMaximum = rangeMaximum;
            RangeMinimum = rangeMinimum;
            SelectAllOptions = selectAllOptions;
        }
    }
}
