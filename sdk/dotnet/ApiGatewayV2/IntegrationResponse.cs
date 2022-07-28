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
    /// Resource Type definition for AWS::ApiGatewayV2::IntegrationResponse
    /// </summary>
    [Obsolete(@"IntegrationResponse is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:apigatewayv2:IntegrationResponse")]
    public partial class IntegrationResponse : global::Pulumi.CustomResource
    {
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        [Output("contentHandlingStrategy")]
        public Output<string?> ContentHandlingStrategy { get; private set; } = null!;

        [Output("integrationId")]
        public Output<string> IntegrationId { get; private set; } = null!;

        [Output("integrationResponseKey")]
        public Output<string> IntegrationResponseKey { get; private set; } = null!;

        [Output("responseParameters")]
        public Output<object?> ResponseParameters { get; private set; } = null!;

        [Output("responseTemplates")]
        public Output<object?> ResponseTemplates { get; private set; } = null!;

        [Output("templateSelectionExpression")]
        public Output<string?> TemplateSelectionExpression { get; private set; } = null!;


        /// <summary>
        /// Create a IntegrationResponse resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IntegrationResponse(string name, IntegrationResponseArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:IntegrationResponse", name, args ?? new IntegrationResponseArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IntegrationResponse(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:IntegrationResponse", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing IntegrationResponse resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IntegrationResponse Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new IntegrationResponse(name, id, options);
        }
    }

    public sealed class IntegrationResponseArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        [Input("contentHandlingStrategy")]
        public Input<string>? ContentHandlingStrategy { get; set; }

        [Input("integrationId", required: true)]
        public Input<string> IntegrationId { get; set; } = null!;

        [Input("integrationResponseKey", required: true)]
        public Input<string> IntegrationResponseKey { get; set; } = null!;

        [Input("responseParameters")]
        public Input<object>? ResponseParameters { get; set; }

        [Input("responseTemplates")]
        public Input<object>? ResponseTemplates { get; set; }

        [Input("templateSelectionExpression")]
        public Input<string>? TemplateSelectionExpression { get; set; }

        public IntegrationResponseArgs()
        {
        }
        public static new IntegrationResponseArgs Empty => new IntegrationResponseArgs();
    }
}
