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
    /// Resource Type definition for AWS::IAM::User
    /// </summary>
    [AwsNativeResourceType("aws-native:iam:User")]
    public partial class User : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see IAM Identifiers in the IAM User Guide.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A list of group names to which you want to add the user.
        /// </summary>
        [Output("groups")]
        public Output<ImmutableArray<string>> Groups { get; private set; } = null!;

        /// <summary>
        /// Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console.
        /// </summary>
        [Output("loginProfile")]
        public Output<Outputs.UserLoginProfile?> LoginProfile { get; private set; } = null!;

        /// <summary>
        /// A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.
        /// </summary>
        [Output("managedPolicyArns")]
        public Output<ImmutableArray<string>> ManagedPolicyArns { get; private set; } = null!;

        /// <summary>
        /// The path to the user. For more information about paths, see IAM identifiers in the IAM User Guide. The ARN of the policy used to set the permissions boundary for the user.
        /// </summary>
        [Output("path")]
        public Output<string?> Path { get; private set; } = null!;

        /// <summary>
        /// The ARN of the policy that is used to set the permissions boundary for the user.
        /// </summary>
        [Output("permissionsBoundary")]
        public Output<string?> PermissionsBoundary { get; private set; } = null!;

        /// <summary>
        /// Adds or updates an inline policy document that is embedded in the specified IAM role.
        /// </summary>
        [Output("policies")]
        public Output<ImmutableArray<Outputs.UserPolicy>> Policies { get; private set; } = null!;

        /// <summary>
        /// A list of tags that are associated with the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.UserTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The friendly name identifying the user.
        /// </summary>
        [Output("userName")]
        public Output<string?> UserName { get; private set; } = null!;


        /// <summary>
        /// Create a User resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public User(string name, UserArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iam:User", name, args ?? new UserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private User(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iam:User", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "userName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing User resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static User Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new User(name, id, options);
        }
    }

    public sealed class UserArgs : global::Pulumi.ResourceArgs
    {
        [Input("groups")]
        private InputList<string>? _groups;

        /// <summary>
        /// A list of group names to which you want to add the user.
        /// </summary>
        public InputList<string> Groups
        {
            get => _groups ?? (_groups = new InputList<string>());
            set => _groups = value;
        }

        /// <summary>
        /// Creates a password for the specified IAM user. A password allows an IAM user to access AWS services through the AWS Management Console.
        /// </summary>
        [Input("loginProfile")]
        public Input<Inputs.UserLoginProfileArgs>? LoginProfile { get; set; }

        [Input("managedPolicyArns")]
        private InputList<string>? _managedPolicyArns;

        /// <summary>
        /// A list of Amazon Resource Names (ARNs) of the IAM managed policies that you want to attach to the role.
        /// </summary>
        public InputList<string> ManagedPolicyArns
        {
            get => _managedPolicyArns ?? (_managedPolicyArns = new InputList<string>());
            set => _managedPolicyArns = value;
        }

        /// <summary>
        /// The path to the user. For more information about paths, see IAM identifiers in the IAM User Guide. The ARN of the policy used to set the permissions boundary for the user.
        /// </summary>
        [Input("path")]
        public Input<string>? Path { get; set; }

        /// <summary>
        /// The ARN of the policy that is used to set the permissions boundary for the user.
        /// </summary>
        [Input("permissionsBoundary")]
        public Input<string>? PermissionsBoundary { get; set; }

        [Input("policies")]
        private InputList<Inputs.UserPolicyArgs>? _policies;

        /// <summary>
        /// Adds or updates an inline policy document that is embedded in the specified IAM role.
        /// </summary>
        public InputList<Inputs.UserPolicyArgs> Policies
        {
            get => _policies ?? (_policies = new InputList<Inputs.UserPolicyArgs>());
            set => _policies = value;
        }

        [Input("tags")]
        private InputList<Inputs.UserTagArgs>? _tags;

        /// <summary>
        /// A list of tags that are associated with the user. For more information about tagging, see Tagging IAM resources in the IAM User Guide.
        /// </summary>
        public InputList<Inputs.UserTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.UserTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The friendly name identifying the user.
        /// </summary>
        [Input("userName")]
        public Input<string>? UserName { get; set; }

        public UserArgs()
        {
        }
        public static new UserArgs Empty => new UserArgs();
    }
}
