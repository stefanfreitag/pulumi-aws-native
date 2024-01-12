// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ssm.Outputs
{

    /// <summary>
    /// The patch filter group that defines the criteria for the rule.
    /// </summary>
    [OutputType]
    public sealed class PatchBaselinePatchFilterGroup
    {
        public readonly ImmutableArray<Outputs.PatchBaselinePatchFilter> PatchFilters;

        [OutputConstructor]
        private PatchBaselinePatchFilterGroup(ImmutableArray<Outputs.PatchBaselinePatchFilter> patchFilters)
        {
            PatchFilters = patchFilters;
        }
    }
}
