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
    public sealed class TemplateCategoricalMeasureField
    {
        public readonly Pulumi.AwsNative.QuickSight.TemplateCategoricalAggregationFunction? AggregationFunction;
        public readonly Outputs.TemplateColumnIdentifier Column;
        public readonly string FieldId;
        public readonly Outputs.TemplateStringFormatConfiguration? FormatConfiguration;

        [OutputConstructor]
        private TemplateCategoricalMeasureField(
            Pulumi.AwsNative.QuickSight.TemplateCategoricalAggregationFunction? aggregationFunction,

            Outputs.TemplateColumnIdentifier column,

            string fieldId,

            Outputs.TemplateStringFormatConfiguration? formatConfiguration)
        {
            AggregationFunction = aggregationFunction;
            Column = column;
            FieldId = fieldId;
            FormatConfiguration = formatConfiguration;
        }
    }
}
