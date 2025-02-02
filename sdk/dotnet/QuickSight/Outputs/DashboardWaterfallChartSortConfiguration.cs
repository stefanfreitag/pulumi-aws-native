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
    public sealed class DashboardWaterfallChartSortConfiguration
    {
        public readonly Outputs.DashboardItemsLimitConfiguration? BreakdownItemsLimit;
        public readonly ImmutableArray<Outputs.DashboardFieldSortOptions> CategorySort;

        [OutputConstructor]
        private DashboardWaterfallChartSortConfiguration(
            Outputs.DashboardItemsLimitConfiguration? breakdownItemsLimit,

            ImmutableArray<Outputs.DashboardFieldSortOptions> categorySort)
        {
            BreakdownItemsLimit = breakdownItemsLimit;
            CategorySort = categorySort;
        }
    }
}
