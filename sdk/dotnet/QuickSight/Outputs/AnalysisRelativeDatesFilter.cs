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
    public sealed class AnalysisRelativeDatesFilter
    {
        public readonly Outputs.AnalysisAnchorDateConfiguration AnchorDateConfiguration;
        public readonly Outputs.AnalysisColumnIdentifier Column;
        public readonly Outputs.AnalysisExcludePeriodConfiguration? ExcludePeriodConfiguration;
        public readonly string FilterId;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisTimeGranularity? MinimumGranularity;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisFilterNullOption NullOption;
        public readonly string? ParameterName;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisRelativeDateType RelativeDateType;
        public readonly double? RelativeDateValue;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisTimeGranularity TimeGranularity;

        [OutputConstructor]
        private AnalysisRelativeDatesFilter(
            Outputs.AnalysisAnchorDateConfiguration anchorDateConfiguration,

            Outputs.AnalysisColumnIdentifier column,

            Outputs.AnalysisExcludePeriodConfiguration? excludePeriodConfiguration,

            string filterId,

            Pulumi.AwsNative.QuickSight.AnalysisTimeGranularity? minimumGranularity,

            Pulumi.AwsNative.QuickSight.AnalysisFilterNullOption nullOption,

            string? parameterName,

            Pulumi.AwsNative.QuickSight.AnalysisRelativeDateType relativeDateType,

            double? relativeDateValue,

            Pulumi.AwsNative.QuickSight.AnalysisTimeGranularity timeGranularity)
        {
            AnchorDateConfiguration = anchorDateConfiguration;
            Column = column;
            ExcludePeriodConfiguration = excludePeriodConfiguration;
            FilterId = filterId;
            MinimumGranularity = minimumGranularity;
            NullOption = nullOption;
            ParameterName = parameterName;
            RelativeDateType = relativeDateType;
            RelativeDateValue = relativeDateValue;
            TimeGranularity = timeGranularity;
        }
    }
}
