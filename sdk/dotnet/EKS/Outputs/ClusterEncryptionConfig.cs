// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EKS.Outputs
{

    /// <summary>
    /// The encryption configuration for the cluster
    /// </summary>
    [OutputType]
    public sealed class ClusterEncryptionConfig
    {
        /// <summary>
        /// The encryption provider for the cluster.
        /// </summary>
        public readonly Outputs.ClusterEncryptionConfigProviderProperties? Provider;
        /// <summary>
        /// Specifies the resources to be encrypted. The only supported value is "secrets".
        /// </summary>
        public readonly ImmutableArray<string> Resources;

        [OutputConstructor]
        private ClusterEncryptionConfig(
            Outputs.ClusterEncryptionConfigProviderProperties? provider,

            ImmutableArray<string> resources)
        {
            Provider = provider;
            Resources = resources;
        }
    }
}
