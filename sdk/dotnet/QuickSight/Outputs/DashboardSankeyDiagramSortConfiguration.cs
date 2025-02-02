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
    public sealed class DashboardSankeyDiagramSortConfiguration
    {
        public readonly Outputs.DashboardItemsLimitConfiguration? DestinationItemsLimit;
        public readonly Outputs.DashboardItemsLimitConfiguration? SourceItemsLimit;
        public readonly ImmutableArray<Outputs.DashboardFieldSortOptions> WeightSort;

        [OutputConstructor]
        private DashboardSankeyDiagramSortConfiguration(
            Outputs.DashboardItemsLimitConfiguration? destinationItemsLimit,

            Outputs.DashboardItemsLimitConfiguration? sourceItemsLimit,

            ImmutableArray<Outputs.DashboardFieldSortOptions> weightSort)
        {
            DestinationItemsLimit = destinationItemsLimit;
            SourceItemsLimit = sourceItemsLimit;
            WeightSort = weightSort;
        }
    }
}
