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
    public sealed class DashboardDecimalParameterDeclaration
    {
        public readonly Outputs.DashboardDecimalDefaultValues? DefaultValues;
        public readonly ImmutableArray<Outputs.DashboardMappedDataSetParameter> MappedDataSetParameters;
        public readonly string Name;
        public readonly Pulumi.AwsNative.QuickSight.DashboardParameterValueType ParameterValueType;
        public readonly Outputs.DashboardDecimalValueWhenUnsetConfiguration? ValueWhenUnset;

        [OutputConstructor]
        private DashboardDecimalParameterDeclaration(
            Outputs.DashboardDecimalDefaultValues? defaultValues,

            ImmutableArray<Outputs.DashboardMappedDataSetParameter> mappedDataSetParameters,

            string name,

            Pulumi.AwsNative.QuickSight.DashboardParameterValueType parameterValueType,

            Outputs.DashboardDecimalValueWhenUnsetConfiguration? valueWhenUnset)
        {
            DefaultValues = defaultValues;
            MappedDataSetParameters = mappedDataSetParameters;
            Name = name;
            ParameterValueType = parameterValueType;
            ValueWhenUnset = valueWhenUnset;
        }
    }
}
