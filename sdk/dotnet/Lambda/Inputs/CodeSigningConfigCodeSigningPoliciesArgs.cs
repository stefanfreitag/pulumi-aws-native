// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda.Inputs
{

    /// <summary>
    /// Policies to control how to act if a signature is invalid
    /// </summary>
    public sealed class CodeSigningConfigCodeSigningPoliciesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates how Lambda operations involve updating the code artifact will operate. Default to Warn if not provided
        /// </summary>
        [Input("untrustedArtifactOnDeployment", required: true)]
        public Input<Pulumi.AwsNative.Lambda.CodeSigningConfigCodeSigningPoliciesUntrustedArtifactOnDeployment> UntrustedArtifactOnDeployment { get; set; } = null!;

        public CodeSigningConfigCodeSigningPoliciesArgs()
        {
        }
        public static new CodeSigningConfigCodeSigningPoliciesArgs Empty => new CodeSigningConfigCodeSigningPoliciesArgs();
    }
}
