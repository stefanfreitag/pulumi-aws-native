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
    /// Defines which patches should be included in a patch baseline.
    /// </summary>
    [OutputType]
    public sealed class PatchBaselinePatchFilter
    {
        public readonly Pulumi.AwsNative.Ssm.PatchBaselinePatchFilterKey? Key;
        public readonly ImmutableArray<string> Values;

        [OutputConstructor]
        private PatchBaselinePatchFilter(
            Pulumi.AwsNative.Ssm.PatchBaselinePatchFilterKey? key,

            ImmutableArray<string> values)
        {
            Key = key;
            Values = values;
        }
    }
}
