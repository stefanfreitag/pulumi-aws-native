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
    /// The ``AWS::ApiGatewayV2::Route`` resource creates a route for an API.
    /// </summary>
    [AwsNativeResourceType("aws-native:apigatewayv2:Route")]
    public partial class Route : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The API identifier.
        /// </summary>
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        /// <summary>
        /// Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Output("apiKeyRequired")]
        public Output<bool?> ApiKeyRequired { get; private set; } = null!;

        /// <summary>
        /// The authorization scopes supported by this route.
        /// </summary>
        [Output("authorizationScopes")]
        public Output<ImmutableArray<string>> AuthorizationScopes { get; private set; } = null!;

        /// <summary>
        /// The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        /// </summary>
        [Output("authorizationType")]
        public Output<string?> AuthorizationType { get; private set; } = null!;

        /// <summary>
        /// The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        /// </summary>
        [Output("authorizerId")]
        public Output<string?> AuthorizerId { get; private set; } = null!;

        /// <summary>
        /// The model selection expression for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Output("modelSelectionExpression")]
        public Output<string?> ModelSelectionExpression { get; private set; } = null!;

        /// <summary>
        /// The operation name for the route.
        /// </summary>
        [Output("operationName")]
        public Output<string?> OperationName { get; private set; } = null!;

        /// <summary>
        /// The request models for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Output("requestModels")]
        public Output<object?> RequestModels { get; private set; } = null!;

        /// <summary>
        /// The request parameters for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Output("requestParameters")]
        public Output<object?> RequestParameters { get; private set; } = null!;

        [Output("routeId")]
        public Output<string> RouteId { get; private set; } = null!;

        /// <summary>
        /// The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
        /// </summary>
        [Output("routeKey")]
        public Output<string> RouteKey { get; private set; } = null!;

        /// <summary>
        /// The route response selection expression for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Output("routeResponseSelectionExpression")]
        public Output<string?> RouteResponseSelectionExpression { get; private set; } = null!;

        /// <summary>
        /// The target for the route.
        /// </summary>
        [Output("target")]
        public Output<string?> Target { get; private set; } = null!;


        /// <summary>
        /// Create a Route resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Route(string name, RouteArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Route", name, args ?? new RouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Route(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:Route", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "apiId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Route resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Route Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Route(name, id, options);
        }
    }

    public sealed class RouteArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The API identifier.
        /// </summary>
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        /// <summary>
        /// Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Input("apiKeyRequired")]
        public Input<bool>? ApiKeyRequired { get; set; }

        [Input("authorizationScopes")]
        private InputList<string>? _authorizationScopes;

        /// <summary>
        /// The authorization scopes supported by this route.
        /// </summary>
        public InputList<string> AuthorizationScopes
        {
            get => _authorizationScopes ?? (_authorizationScopes = new InputList<string>());
            set => _authorizationScopes = value;
        }

        /// <summary>
        /// The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        /// </summary>
        [Input("authorizationType")]
        public Input<string>? AuthorizationType { get; set; }

        /// <summary>
        /// The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        /// </summary>
        [Input("authorizerId")]
        public Input<string>? AuthorizerId { get; set; }

        /// <summary>
        /// The model selection expression for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Input("modelSelectionExpression")]
        public Input<string>? ModelSelectionExpression { get; set; }

        /// <summary>
        /// The operation name for the route.
        /// </summary>
        [Input("operationName")]
        public Input<string>? OperationName { get; set; }

        /// <summary>
        /// The request models for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Input("requestModels")]
        public Input<object>? RequestModels { get; set; }

        /// <summary>
        /// The request parameters for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Input("requestParameters")]
        public Input<object>? RequestParameters { get; set; }

        /// <summary>
        /// The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
        /// </summary>
        [Input("routeKey", required: true)]
        public Input<string> RouteKey { get; set; } = null!;

        /// <summary>
        /// The route response selection expression for the route. Supported only for WebSocket APIs.
        /// </summary>
        [Input("routeResponseSelectionExpression")]
        public Input<string>? RouteResponseSelectionExpression { get; set; }

        /// <summary>
        /// The target for the route.
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        public RouteArgs()
        {
        }
        public static new RouteArgs Empty => new RouteArgs();
    }
}
