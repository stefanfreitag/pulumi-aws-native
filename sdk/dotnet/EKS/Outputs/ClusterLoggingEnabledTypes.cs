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
    /// The cluster control plane logging configuration for your cluster. 
    /// </summary>
    [OutputType]
    public sealed class ClusterLoggingEnabledTypes
    {
        public readonly ImmutableArray<Outputs.ClusterLoggingTypeConfig> EnabledTypes;

        [OutputConstructor]
        private ClusterLoggingEnabledTypes(ImmutableArray<Outputs.ClusterLoggingTypeConfig> enabledTypes)
        {
            EnabledTypes = enabledTypes;
        }
    }
}
