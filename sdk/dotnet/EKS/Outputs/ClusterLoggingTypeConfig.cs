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
    /// Enabled Logging Type
    /// </summary>
    [OutputType]
    public sealed class ClusterLoggingTypeConfig
    {
        /// <summary>
        /// name of the log type
        /// </summary>
        public readonly Pulumi.AwsNative.EKS.ClusterLoggingTypeConfigType? Type;

        [OutputConstructor]
        private ClusterLoggingTypeConfig(Pulumi.AwsNative.EKS.ClusterLoggingTypeConfigType? type)
        {
            Type = type;
        }
    }
}
