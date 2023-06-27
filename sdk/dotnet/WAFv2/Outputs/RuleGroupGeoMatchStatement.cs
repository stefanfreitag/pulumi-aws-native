// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Outputs
{

    [OutputType]
    public sealed class RuleGroupGeoMatchStatement
    {
        public readonly ImmutableArray<string> CountryCodes;
        public readonly Outputs.RuleGroupForwardedIPConfiguration? ForwardedIPConfig;

        [OutputConstructor]
        private RuleGroupGeoMatchStatement(
            ImmutableArray<string> countryCodes,

            Outputs.RuleGroupForwardedIPConfiguration? forwardedIPConfig)
        {
            CountryCodes = countryCodes;
            ForwardedIPConfig = forwardedIPConfig;
        }
    }
}
