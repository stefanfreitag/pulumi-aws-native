// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AccessAnalyzer.Outputs
{

    /// <summary>
    /// An Access Analyzer archive rule. Archive rules automatically archive new findings that meet the criteria you define when you create the rule.
    /// </summary>
    [OutputType]
    public sealed class AnalyzerArchiveRule
    {
        public readonly ImmutableArray<Outputs.AnalyzerFilter> Filter;
        /// <summary>
        /// The archive rule name
        /// </summary>
        public readonly string RuleName;

        [OutputConstructor]
        private AnalyzerArchiveRule(
            ImmutableArray<Outputs.AnalyzerFilter> filter,

            string ruleName)
        {
            Filter = filter;
            RuleName = ruleName;
        }
    }
}
