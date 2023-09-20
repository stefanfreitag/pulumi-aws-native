// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackageV2.Outputs
{

    /// <summary>
    /// &lt;p&gt;The parameters for the SPEKE key provider.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class OriginEndpointSpekeKeyProvider
    {
        /// <summary>
        /// &lt;p&gt;The DRM solution provider you're using to protect your content during distribution.&lt;/p&gt;
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.MediaPackageV2.OriginEndpointDrmSystem> DrmSystems;
        public readonly Outputs.OriginEndpointEncryptionContractConfiguration EncryptionContractConfiguration;
        /// <summary>
        /// &lt;p&gt;The unique identifier for the content. The service sends this to the key server to identify the current endpoint. How unique you make this depends on how fine-grained you want access controls to be. The service does not permit you to use the same ID for two simultaneous encryption processes. The resource ID is also known as the content ID.&lt;/p&gt;
        ///          &lt;p&gt;The following example shows a resource ID: &lt;code&gt;MovieNight20171126093045&lt;/code&gt;
        ///          &lt;/p&gt;
        /// </summary>
        public readonly string ResourceId;
        /// <summary>
        /// &lt;p&gt;The ARN for the IAM role granted by the key provider that provides access to the key provider API. This role must have a trust policy that allows MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Get this from your DRM solution provider.&lt;/p&gt;
        ///          &lt;p&gt;Valid format: &lt;code&gt;arn:aws:iam::{accountID}:role/{name}&lt;/code&gt;. The following example shows a role ARN: &lt;code&gt;arn:aws:iam::444455556666:role/SpekeAccess&lt;/code&gt;
        ///          &lt;/p&gt;
        /// </summary>
        public readonly string RoleArn;
        /// <summary>
        /// &lt;p&gt;The URL of the API Gateway proxy that you set up to talk to your key server. The API Gateway proxy must reside in the same AWS Region as MediaPackage and must start with https://.&lt;/p&gt;
        ///          &lt;p&gt;The following example shows a URL: &lt;code&gt;https://1wm2dx1f33.execute-api.us-west-2.amazonaws.com/SpekeSample/copyProtection&lt;/code&gt;
        ///          &lt;/p&gt;
        /// </summary>
        public readonly string Url;

        [OutputConstructor]
        private OriginEndpointSpekeKeyProvider(
            ImmutableArray<Pulumi.AwsNative.MediaPackageV2.OriginEndpointDrmSystem> drmSystems,

            Outputs.OriginEndpointEncryptionContractConfiguration encryptionContractConfiguration,

            string resourceId,

            string roleArn,

            string url)
        {
            DrmSystems = drmSystems;
            EncryptionContractConfiguration = encryptionContractConfiguration;
            ResourceId = resourceId;
            RoleArn = roleArn;
            Url = url;
        }
    }
}
