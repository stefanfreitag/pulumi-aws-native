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
    public sealed class AnalysisTextAreaControlDisplayOptions
    {
        public readonly Outputs.AnalysisSheetControlInfoIconLabelOptions? InfoIconLabelOptions;
        public readonly Outputs.AnalysisTextControlPlaceholderOptions? PlaceholderOptions;
        public readonly Outputs.AnalysisLabelOptions? TitleOptions;

        [OutputConstructor]
        private AnalysisTextAreaControlDisplayOptions(
            Outputs.AnalysisSheetControlInfoIconLabelOptions? infoIconLabelOptions,

            Outputs.AnalysisTextControlPlaceholderOptions? placeholderOptions,

            Outputs.AnalysisLabelOptions? titleOptions)
        {
            InfoIconLabelOptions = infoIconLabelOptions;
            PlaceholderOptions = placeholderOptions;
            TitleOptions = titleOptions;
        }
    }
}
