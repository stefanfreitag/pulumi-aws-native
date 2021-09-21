// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito
{
    /// <summary>
    /// Resource Type definition for AWS::Cognito::UserPoolUser
    /// </summary>
    [Obsolete(@"UserPoolUser is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:cognito:UserPoolUser")]
    public partial class UserPoolUser : Pulumi.CustomResource
    {
        [Output("clientMetadata")]
        public Output<object?> ClientMetadata { get; private set; } = null!;

        [Output("desiredDeliveryMediums")]
        public Output<ImmutableArray<string>> DesiredDeliveryMediums { get; private set; } = null!;

        [Output("forceAliasCreation")]
        public Output<bool?> ForceAliasCreation { get; private set; } = null!;

        [Output("messageAction")]
        public Output<string?> MessageAction { get; private set; } = null!;

        [Output("userAttributes")]
        public Output<ImmutableArray<Outputs.UserPoolUserAttributeType>> UserAttributes { get; private set; } = null!;

        [Output("userPoolId")]
        public Output<string> UserPoolId { get; private set; } = null!;

        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;

        [Output("validationData")]
        public Output<ImmutableArray<Outputs.UserPoolUserAttributeType>> ValidationData { get; private set; } = null!;


        /// <summary>
        /// Create a UserPoolUser resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public UserPoolUser(string name, UserPoolUserArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cognito:UserPoolUser", name, args ?? new UserPoolUserArgs(), MakeResourceOptions(options, ""))
        {
        }

        private UserPoolUser(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cognito:UserPoolUser", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing UserPoolUser resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static UserPoolUser Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new UserPoolUser(name, id, options);
        }
    }

    public sealed class UserPoolUserArgs : Pulumi.ResourceArgs
    {
        [Input("clientMetadata")]
        public Input<object>? ClientMetadata { get; set; }

        [Input("desiredDeliveryMediums")]
        private InputList<string>? _desiredDeliveryMediums;
        public InputList<string> DesiredDeliveryMediums
        {
            get => _desiredDeliveryMediums ?? (_desiredDeliveryMediums = new InputList<string>());
            set => _desiredDeliveryMediums = value;
        }

        [Input("forceAliasCreation")]
        public Input<bool>? ForceAliasCreation { get; set; }

        [Input("messageAction")]
        public Input<string>? MessageAction { get; set; }

        [Input("userAttributes")]
        private InputList<Inputs.UserPoolUserAttributeTypeArgs>? _userAttributes;
        public InputList<Inputs.UserPoolUserAttributeTypeArgs> UserAttributes
        {
            get => _userAttributes ?? (_userAttributes = new InputList<Inputs.UserPoolUserAttributeTypeArgs>());
            set => _userAttributes = value;
        }

        [Input("userPoolId", required: true)]
        public Input<string> UserPoolId { get; set; } = null!;

        [Input("username")]
        public Input<string>? Username { get; set; }

        [Input("validationData")]
        private InputList<Inputs.UserPoolUserAttributeTypeArgs>? _validationData;
        public InputList<Inputs.UserPoolUserAttributeTypeArgs> ValidationData
        {
            get => _validationData ?? (_validationData = new InputList<Inputs.UserPoolUserAttributeTypeArgs>());
            set => _validationData = value;
        }

        public UserPoolUserArgs()
        {
        }
    }
}
