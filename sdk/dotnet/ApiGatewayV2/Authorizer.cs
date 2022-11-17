// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2
{
    /// <summary>
    /// Resource Type definition for AWS::ApiGatewayV2::Authorizer
    /// </summary>
    [AwsNativeResourceType("aws-native:apigatewayv2:Authorizer")]
    public partial class Authorizer : global::Pulumi.CustomResource
    {
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        [Output("authorizerCredentialsArn")]
        public Output<string?> AuthorizerCredentialsArn { get; private set; } = null!;

        [Output("authorizerPayloadFormatVersion")]
        public Output<string?> AuthorizerPayloadFormatVersion { get; private set; } = null!;

        [Output("authorizerResultTtlInSeconds")]
        public Output<int?> AuthorizerResultTtlInSeconds { get; private set; } = null!;

        [Output("authorizerType")]
        public Output<string> AuthorizerType { get; private set; } = null!;

        [Output("authorizerUri")]
        public Output<string?> AuthorizerUri { get; private set; } = null!;

        [Output("enableSimpleResponses")]
        public Output<bool?> EnableSimpleResponses { get; private set; } = null!;

        [Output("identitySource")]
        public Output<ImmutableArray<string>> IdentitySource { get; private set; } = null!;

        [Output("identityValidationExpression")]
        public Output<string?> IdentityValidationExpression { get; private set; } = null!;

        [Output("jwtConfiguration")]
        public Output<Outputs.AuthorizerJWTConfiguration?> JwtConfiguration { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Authorizer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Authorizer(string name, AuthorizerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Authorizer", name, args ?? new AuthorizerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Authorizer(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Authorizer", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Authorizer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Authorizer Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Authorizer(name, id, options);
        }
    }

    public sealed class AuthorizerArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        [Input("authorizerCredentialsArn")]
        public Input<string>? AuthorizerCredentialsArn { get; set; }

        [Input("authorizerPayloadFormatVersion")]
        public Input<string>? AuthorizerPayloadFormatVersion { get; set; }

        [Input("authorizerResultTtlInSeconds")]
        public Input<int>? AuthorizerResultTtlInSeconds { get; set; }

        [Input("authorizerType", required: true)]
        public Input<string> AuthorizerType { get; set; } = null!;

        [Input("authorizerUri")]
        public Input<string>? AuthorizerUri { get; set; }

        [Input("enableSimpleResponses")]
        public Input<bool>? EnableSimpleResponses { get; set; }

        [Input("identitySource")]
        private InputList<string>? _identitySource;
        public InputList<string> IdentitySource
        {
            get => _identitySource ?? (_identitySource = new InputList<string>());
            set => _identitySource = value;
        }

        [Input("identityValidationExpression")]
        public Input<string>? IdentityValidationExpression { get; set; }

        [Input("jwtConfiguration")]
        public Input<Inputs.AuthorizerJWTConfigurationArgs>? JwtConfiguration { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        public AuthorizerArgs()
        {
        }
        public static new AuthorizerArgs Empty => new AuthorizerArgs();
    }
}
