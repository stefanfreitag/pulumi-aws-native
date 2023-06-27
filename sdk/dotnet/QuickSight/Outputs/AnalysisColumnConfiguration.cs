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
    public sealed class AnalysisColumnConfiguration
    {
        public readonly Outputs.AnalysisColumnIdentifier Column;
        public readonly Outputs.AnalysisFormatConfiguration? FormatConfiguration;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisColumnRole? Role;

        [OutputConstructor]
        private AnalysisColumnConfiguration(
            Outputs.AnalysisColumnIdentifier column,

            Outputs.AnalysisFormatConfiguration? formatConfiguration,

            Pulumi.AwsNative.QuickSight.AnalysisColumnRole? role)
        {
            Column = column;
            FormatConfiguration = formatConfiguration;
            Role = role;
        }
    }
}
