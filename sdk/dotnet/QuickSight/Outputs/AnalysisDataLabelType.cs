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
    public sealed class AnalysisDataLabelType
    {
        public readonly Outputs.AnalysisDataPathLabelType? DataPathLabelType;
        public readonly Outputs.AnalysisFieldLabelType? FieldLabelType;
        public readonly Outputs.AnalysisMaximumLabelType? MaximumLabelType;
        public readonly Outputs.AnalysisMinimumLabelType? MinimumLabelType;
        public readonly Outputs.AnalysisRangeEndsLabelType? RangeEndsLabelType;

        [OutputConstructor]
        private AnalysisDataLabelType(
            Outputs.AnalysisDataPathLabelType? dataPathLabelType,

            Outputs.AnalysisFieldLabelType? fieldLabelType,

            Outputs.AnalysisMaximumLabelType? maximumLabelType,

            Outputs.AnalysisMinimumLabelType? minimumLabelType,

            Outputs.AnalysisRangeEndsLabelType? rangeEndsLabelType)
        {
            DataPathLabelType = dataPathLabelType;
            FieldLabelType = fieldLabelType;
            MaximumLabelType = maximumLabelType;
            MinimumLabelType = minimumLabelType;
            RangeEndsLabelType = rangeEndsLabelType;
        }
    }
}
