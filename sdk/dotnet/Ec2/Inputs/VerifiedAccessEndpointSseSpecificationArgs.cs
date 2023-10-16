// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    /// <summary>
    /// The configuration options for customer provided KMS encryption.
    /// </summary>
    public sealed class VerifiedAccessEndpointSseSpecificationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to encrypt the policy with the provided key or disable encryption
        /// </summary>
        [Input("customerManagedKeyEnabled")]
        public Input<bool>? CustomerManagedKeyEnabled { get; set; }

        /// <summary>
        /// KMS Key Arn used to encrypt the group policy
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        public VerifiedAccessEndpointSseSpecificationArgs()
        {
        }
        public static new VerifiedAccessEndpointSseSpecificationArgs Empty => new VerifiedAccessEndpointSseSpecificationArgs();
    }
}
