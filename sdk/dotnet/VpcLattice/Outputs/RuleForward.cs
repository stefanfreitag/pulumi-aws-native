// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice.Outputs
{

    [OutputType]
    public sealed class RuleForward
    {
        public readonly ImmutableArray<Outputs.RuleWeightedTargetGroup> TargetGroups;

        [OutputConstructor]
        private RuleForward(ImmutableArray<Outputs.RuleWeightedTargetGroup> targetGroups)
        {
            TargetGroups = targetGroups;
        }
    }
}
