// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Outputs
{

    [OutputType]
    public sealed class NetworkInsightsAnalysisAnalysisAclRule
    {
        public readonly string? Cidr;
        public readonly bool? Egress;
        public readonly Outputs.NetworkInsightsAnalysisPortRange? PortRange;
        public readonly string? Protocol;
        public readonly string? RuleAction;
        public readonly int? RuleNumber;

        [OutputConstructor]
        private NetworkInsightsAnalysisAnalysisAclRule(
            string? cidr,

            bool? egress,

            Outputs.NetworkInsightsAnalysisPortRange? portRange,

            string? protocol,

            string? ruleAction,

            int? ruleNumber)
        {
            Cidr = cidr;
            Egress = egress;
            PortRange = portRange;
            Protocol = protocol;
            RuleAction = ruleAction;
            RuleNumber = ruleNumber;
        }
    }
}
