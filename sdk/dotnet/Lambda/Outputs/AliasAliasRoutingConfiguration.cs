// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda.Outputs
{

    [OutputType]
    public sealed class AliasAliasRoutingConfiguration
    {
        public readonly ImmutableArray<Outputs.AliasVersionWeight> AdditionalVersionWeights;

        [OutputConstructor]
        private AliasAliasRoutingConfiguration(ImmutableArray<Outputs.AliasVersionWeight> additionalVersionWeights)
        {
            AdditionalVersionWeights = additionalVersionWeights;
        }
    }
}
