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
    public sealed class TemplateTopBottomRankedComputation
    {
        public readonly Outputs.TemplateDimensionField Category;
        public readonly string ComputationId;
        public readonly string? Name;
        public readonly double? ResultSize;
        public readonly Pulumi.AwsNative.QuickSight.TemplateTopBottomComputationType Type;
        public readonly Outputs.TemplateMeasureField? Value;

        [OutputConstructor]
        private TemplateTopBottomRankedComputation(
            Outputs.TemplateDimensionField category,

            string computationId,

            string? name,

            double? resultSize,

            Pulumi.AwsNative.QuickSight.TemplateTopBottomComputationType type,

            Outputs.TemplateMeasureField? value)
        {
            Category = category;
            ComputationId = computationId;
            Name = name;
            ResultSize = resultSize;
            Type = type;
            Value = value;
        }
    }
}
