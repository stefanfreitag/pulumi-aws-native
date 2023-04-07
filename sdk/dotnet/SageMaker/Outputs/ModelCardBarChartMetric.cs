// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    [OutputType]
    public sealed class ModelCardBarChartMetric
    {
        public readonly string Name;
        public readonly string? Notes;
        public readonly Pulumi.AwsNative.SageMaker.ModelCardBarChartMetricType Type;
        public readonly ImmutableArray<double> Value;
        public readonly ImmutableArray<string> XAxisName;
        public readonly string? YAxisName;

        [OutputConstructor]
        private ModelCardBarChartMetric(
            string name,

            string? notes,

            Pulumi.AwsNative.SageMaker.ModelCardBarChartMetricType type,

            ImmutableArray<double> value,

            ImmutableArray<string> xAxisName,

            string? yAxisName)
        {
            Name = name;
            Notes = notes;
            Type = type;
            Value = value;
            XAxisName = xAxisName;
            YAxisName = yAxisName;
        }
    }
}
