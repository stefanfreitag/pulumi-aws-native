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
    public sealed class TemplateFilter
    {
        public readonly Outputs.TemplateCategoryFilter? CategoryFilter;
        public readonly Outputs.TemplateNumericEqualityFilter? NumericEqualityFilter;
        public readonly Outputs.TemplateNumericRangeFilter? NumericRangeFilter;
        public readonly Outputs.TemplateRelativeDatesFilter? RelativeDatesFilter;
        public readonly Outputs.TemplateTimeEqualityFilter? TimeEqualityFilter;
        public readonly Outputs.TemplateTimeRangeFilter? TimeRangeFilter;
        public readonly Outputs.TemplateTopBottomFilter? TopBottomFilter;

        [OutputConstructor]
        private TemplateFilter(
            Outputs.TemplateCategoryFilter? categoryFilter,

            Outputs.TemplateNumericEqualityFilter? numericEqualityFilter,

            Outputs.TemplateNumericRangeFilter? numericRangeFilter,

            Outputs.TemplateRelativeDatesFilter? relativeDatesFilter,

            Outputs.TemplateTimeEqualityFilter? timeEqualityFilter,

            Outputs.TemplateTimeRangeFilter? timeRangeFilter,

            Outputs.TemplateTopBottomFilter? topBottomFilter)
        {
            CategoryFilter = categoryFilter;
            NumericEqualityFilter = numericEqualityFilter;
            NumericRangeFilter = numericRangeFilter;
            RelativeDatesFilter = relativeDatesFilter;
            TimeEqualityFilter = timeEqualityFilter;
            TimeRangeFilter = timeRangeFilter;
            TopBottomFilter = topBottomFilter;
        }
    }
}
