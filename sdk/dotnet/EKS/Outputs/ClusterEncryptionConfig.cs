// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EKS.Outputs
{

    [OutputType]
    public sealed class ClusterEncryptionConfig
    {
        public readonly Outputs.ClusterProvider? Provider;
        public readonly ImmutableArray<string> Resources;

        [OutputConstructor]
        private ClusterEncryptionConfig(
            Outputs.ClusterProvider? provider,

            ImmutableArray<string> resources)
        {
            Provider = provider;
            Resources = resources;
        }
    }
}
