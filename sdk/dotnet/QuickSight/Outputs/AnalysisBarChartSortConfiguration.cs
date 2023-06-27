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
    public sealed class AnalysisBarChartSortConfiguration
    {
        public readonly Outputs.AnalysisItemsLimitConfiguration? CategoryItemsLimit;
        public readonly ImmutableArray<Outputs.AnalysisFieldSortOptions> CategorySort;
        public readonly Outputs.AnalysisItemsLimitConfiguration? ColorItemsLimit;
        public readonly ImmutableArray<Outputs.AnalysisFieldSortOptions> ColorSort;
        public readonly Outputs.AnalysisItemsLimitConfiguration? SmallMultiplesLimitConfiguration;
        public readonly ImmutableArray<Outputs.AnalysisFieldSortOptions> SmallMultiplesSort;

        [OutputConstructor]
        private AnalysisBarChartSortConfiguration(
            Outputs.AnalysisItemsLimitConfiguration? categoryItemsLimit,

            ImmutableArray<Outputs.AnalysisFieldSortOptions> categorySort,

            Outputs.AnalysisItemsLimitConfiguration? colorItemsLimit,

            ImmutableArray<Outputs.AnalysisFieldSortOptions> colorSort,

            Outputs.AnalysisItemsLimitConfiguration? smallMultiplesLimitConfiguration,

            ImmutableArray<Outputs.AnalysisFieldSortOptions> smallMultiplesSort)
        {
            CategoryItemsLimit = categoryItemsLimit;
            CategorySort = categorySort;
            ColorItemsLimit = colorItemsLimit;
            ColorSort = colorSort;
            SmallMultiplesLimitConfiguration = smallMultiplesLimitConfiguration;
            SmallMultiplesSort = smallMultiplesSort;
        }
    }
}
