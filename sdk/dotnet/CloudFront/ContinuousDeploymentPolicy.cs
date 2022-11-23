// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront
{
    /// <summary>
    /// Resource Type definition for AWS::CloudFront::ContinuousDeploymentPolicy
    /// </summary>
    [AwsNativeResourceType("aws-native:cloudfront:ContinuousDeploymentPolicy")]
    public partial class ContinuousDeploymentPolicy : global::Pulumi.CustomResource
    {
        [Output("continuousDeploymentPolicyConfig")]
        public Output<Outputs.ContinuousDeploymentPolicyConfig> ContinuousDeploymentPolicyConfig { get; private set; } = null!;

        [Output("lastModifiedTime")]
        public Output<string> LastModifiedTime { get; private set; } = null!;


        /// <summary>
        /// Create a ContinuousDeploymentPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ContinuousDeploymentPolicy(string name, ContinuousDeploymentPolicyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cloudfront:ContinuousDeploymentPolicy", name, args ?? new ContinuousDeploymentPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ContinuousDeploymentPolicy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cloudfront:ContinuousDeploymentPolicy", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ContinuousDeploymentPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ContinuousDeploymentPolicy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ContinuousDeploymentPolicy(name, id, options);
        }
    }

    public sealed class ContinuousDeploymentPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("continuousDeploymentPolicyConfig", required: true)]
        public Input<Inputs.ContinuousDeploymentPolicyConfigArgs> ContinuousDeploymentPolicyConfig { get; set; } = null!;

        public ContinuousDeploymentPolicyArgs()
        {
        }
        public static new ContinuousDeploymentPolicyArgs Empty => new ContinuousDeploymentPolicyArgs();
    }
}
