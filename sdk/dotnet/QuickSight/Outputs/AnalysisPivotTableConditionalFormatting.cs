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
    public sealed class AnalysisPivotTableConditionalFormatting
    {
        public readonly ImmutableArray<Outputs.AnalysisPivotTableConditionalFormattingOption> ConditionalFormattingOptions;

        [OutputConstructor]
        private AnalysisPivotTableConditionalFormatting(ImmutableArray<Outputs.AnalysisPivotTableConditionalFormattingOption> conditionalFormattingOptions)
        {
            ConditionalFormattingOptions = conditionalFormattingOptions;
        }
    }
}
