// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.XRay.Outputs
{

    [OutputType]
    public sealed class SamplingRuleSamplingRuleRecord
    {
        /// <summary>
        /// When the rule was created, in Unix time seconds.
        /// </summary>
        public readonly string? CreatedAt;
        /// <summary>
        /// When the rule was modified, in Unix time seconds.
        /// </summary>
        public readonly string? ModifiedAt;
        public readonly Outputs.SamplingRuleSamplingRule? SamplingRule;

        [OutputConstructor]
        private SamplingRuleSamplingRuleRecord(
            string? createdAt,

            string? modifiedAt,

            Outputs.SamplingRuleSamplingRule? samplingRule)
        {
            CreatedAt = createdAt;
            ModifiedAt = modifiedAt;
            SamplingRule = samplingRule;
        }
    }
}
