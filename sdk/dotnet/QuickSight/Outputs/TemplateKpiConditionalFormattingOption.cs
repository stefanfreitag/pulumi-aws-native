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
    public sealed class TemplateKpiConditionalFormattingOption
    {
        public readonly Outputs.TemplateKpiActualValueConditionalFormatting? ActualValue;
        public readonly Outputs.TemplateKpiComparisonValueConditionalFormatting? ComparisonValue;
        public readonly Outputs.TemplateKpiPrimaryValueConditionalFormatting? PrimaryValue;
        public readonly Outputs.TemplateKpiProgressBarConditionalFormatting? ProgressBar;

        [OutputConstructor]
        private TemplateKpiConditionalFormattingOption(
            Outputs.TemplateKpiActualValueConditionalFormatting? actualValue,

            Outputs.TemplateKpiComparisonValueConditionalFormatting? comparisonValue,

            Outputs.TemplateKpiPrimaryValueConditionalFormatting? primaryValue,

            Outputs.TemplateKpiProgressBarConditionalFormatting? progressBar)
        {
            ActualValue = actualValue;
            ComparisonValue = comparisonValue;
            PrimaryValue = primaryValue;
            ProgressBar = progressBar;
        }
    }
}
