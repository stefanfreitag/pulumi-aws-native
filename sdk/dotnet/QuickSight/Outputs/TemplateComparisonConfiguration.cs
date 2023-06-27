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
    public sealed class TemplateComparisonConfiguration
    {
        public readonly Outputs.TemplateComparisonFormatConfiguration? ComparisonFormat;
        public readonly Pulumi.AwsNative.QuickSight.TemplateComparisonMethod? ComparisonMethod;

        [OutputConstructor]
        private TemplateComparisonConfiguration(
            Outputs.TemplateComparisonFormatConfiguration? comparisonFormat,

            Pulumi.AwsNative.QuickSight.TemplateComparisonMethod? comparisonMethod)
        {
            ComparisonFormat = comparisonFormat;
            ComparisonMethod = comparisonMethod;
        }
    }
}
