// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Iam
{
    /// <summary>
    /// Schema for IAM User Policy
    /// </summary>
    [AwsNativeResourceType("aws-native:iam:UserPolicy")]
    public partial class UserPolicy : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The policy document.
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::UserPolicy` for more information about the expected schema for this property.
        /// </summary>
        [Output("policyDocument")]
        public Output<object?> PolicyDocument { get; private set; } = null!;

        /// <summary>
        /// The name of the policy document.
        /// </summary>
        [Output("policyName")]
        public Output<string> PolicyName { get; private set; } = null!;

        /// <summary>
        /// The name of the user to associate the policy with.
        /// </summary>
        [Output("userName")]
        public Output<string> UserName { get; private set; } = null!;


        /// <summary>
        /// Create a UserPolicy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public UserPolicy(string name, UserPolicyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iam:UserPolicy", name, args ?? new UserPolicyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private UserPolicy(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iam:UserPolicy", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "policyName",
                    "userName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing UserPolicy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static UserPolicy Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new UserPolicy(name, id, options);
        }
    }

    public sealed class UserPolicyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The policy document.
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::IAM::UserPolicy` for more information about the expected schema for this property.
        /// </summary>
        [Input("policyDocument")]
        public Input<object>? PolicyDocument { get; set; }

        /// <summary>
        /// The name of the policy document.
        /// </summary>
        [Input("policyName", required: true)]
        public Input<string> PolicyName { get; set; } = null!;

        /// <summary>
        /// The name of the user to associate the policy with.
        /// </summary>
        [Input("userName", required: true)]
        public Input<string> UserName { get; set; } = null!;

        public UserPolicyArgs()
        {
        }
        public static new UserPolicyArgs Empty => new UserPolicyArgs();
    }
}
