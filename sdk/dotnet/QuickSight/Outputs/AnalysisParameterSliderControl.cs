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
    public sealed class AnalysisParameterSliderControl
    {
        public readonly Outputs.AnalysisSliderControlDisplayOptions? DisplayOptions;
        public readonly double MaximumValue;
        public readonly double MinimumValue;
        public readonly string ParameterControlId;
        public readonly string SourceParameterName;
        public readonly double StepSize;
        public readonly string Title;

        [OutputConstructor]
        private AnalysisParameterSliderControl(
            Outputs.AnalysisSliderControlDisplayOptions? displayOptions,

            double maximumValue,

            double minimumValue,

            string parameterControlId,

            string sourceParameterName,

            double stepSize,

            string title)
        {
            DisplayOptions = displayOptions;
            MaximumValue = maximumValue;
            MinimumValue = minimumValue;
            ParameterControlId = parameterControlId;
            SourceParameterName = sourceParameterName;
            StepSize = stepSize;
            Title = title;
        }
    }
}
