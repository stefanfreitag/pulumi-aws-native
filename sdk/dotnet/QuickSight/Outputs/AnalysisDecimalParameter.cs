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
    public sealed class AnalysisDecimalParameter
    {
        public readonly string Name;
        public readonly ImmutableArray<double> Values;

        [OutputConstructor]
        private AnalysisDecimalParameter(
            string name,

            ImmutableArray<double> values)
        {
            Name = name;
            Values = values;
        }
    }
}
