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
    public sealed class DashboardTimeEqualityFilter
    {
        public readonly Outputs.DashboardColumnIdentifier Column;
        public readonly string FilterId;
        public readonly string? ParameterName;
        public readonly Outputs.DashboardRollingDateConfiguration? RollingDate;
        public readonly Pulumi.AwsNative.QuickSight.DashboardTimeGranularity? TimeGranularity;
        public readonly string? Value;

        [OutputConstructor]
        private DashboardTimeEqualityFilter(
            Outputs.DashboardColumnIdentifier column,

            string filterId,

            string? parameterName,

            Outputs.DashboardRollingDateConfiguration? rollingDate,

            Pulumi.AwsNative.QuickSight.DashboardTimeGranularity? timeGranularity,

            string? value)
        {
            Column = column;
            FilterId = filterId;
            ParameterName = parameterName;
            RollingDate = rollingDate;
            TimeGranularity = timeGranularity;
            Value = value;
        }
    }
}
