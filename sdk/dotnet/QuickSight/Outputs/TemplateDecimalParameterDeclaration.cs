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
    public sealed class TemplateDecimalParameterDeclaration
    {
        public readonly Outputs.TemplateDecimalDefaultValues? DefaultValues;
        public readonly ImmutableArray<Outputs.TemplateMappedDataSetParameter> MappedDataSetParameters;
        public readonly string Name;
        public readonly Pulumi.AwsNative.QuickSight.TemplateParameterValueType ParameterValueType;
        public readonly Outputs.TemplateDecimalValueWhenUnsetConfiguration? ValueWhenUnset;

        [OutputConstructor]
        private TemplateDecimalParameterDeclaration(
            Outputs.TemplateDecimalDefaultValues? defaultValues,

            ImmutableArray<Outputs.TemplateMappedDataSetParameter> mappedDataSetParameters,

            string name,

            Pulumi.AwsNative.QuickSight.TemplateParameterValueType parameterValueType,

            Outputs.TemplateDecimalValueWhenUnsetConfiguration? valueWhenUnset)
        {
            DefaultValues = defaultValues;
            MappedDataSetParameters = mappedDataSetParameters;
            Name = name;
            ParameterValueType = parameterValueType;
            ValueWhenUnset = valueWhenUnset;
        }
    }
}
