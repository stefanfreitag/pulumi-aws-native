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
    public sealed class AnalysisWordCloudAggregatedFieldWells
    {
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> GroupBy;
        public readonly ImmutableArray<Outputs.AnalysisMeasureField> Size;

        [OutputConstructor]
        private AnalysisWordCloudAggregatedFieldWells(
            ImmutableArray<Outputs.AnalysisDimensionField> groupBy,

            ImmutableArray<Outputs.AnalysisMeasureField> size)
        {
            GroupBy = groupBy;
            Size = size;
        }
    }
}
