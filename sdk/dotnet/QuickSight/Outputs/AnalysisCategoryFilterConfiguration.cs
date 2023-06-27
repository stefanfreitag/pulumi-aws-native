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
    public sealed class AnalysisCategoryFilterConfiguration
    {
        public readonly Outputs.AnalysisCustomFilterConfiguration? CustomFilterConfiguration;
        public readonly Outputs.AnalysisCustomFilterListConfiguration? CustomFilterListConfiguration;
        public readonly Outputs.AnalysisFilterListConfiguration? FilterListConfiguration;

        [OutputConstructor]
        private AnalysisCategoryFilterConfiguration(
            Outputs.AnalysisCustomFilterConfiguration? customFilterConfiguration,

            Outputs.AnalysisCustomFilterListConfiguration? customFilterListConfiguration,

            Outputs.AnalysisFilterListConfiguration? filterListConfiguration)
        {
            CustomFilterConfiguration = customFilterConfiguration;
            CustomFilterListConfiguration = customFilterListConfiguration;
            FilterListConfiguration = filterListConfiguration;
        }
    }
}
