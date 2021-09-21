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
    /// Resource Type definition for AWS::ApiGatewayV2::ApiMapping
    /// </summary>
    [Obsolete(@"ApiMapping is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:apigatewayv2:ApiMapping")]
    public partial class ApiMapping : Pulumi.CustomResource
    {
        [Output("apiId")]
        public Output<string> ApiId { get; private set; } = null!;

        [Output("apiMappingKey")]
        public Output<string?> ApiMappingKey { get; private set; } = null!;

        [Output("domainName")]
        public Output<string> DomainName { get; private set; } = null!;

        [Output("stage")]
        public Output<string> Stage { get; private set; } = null!;


        /// <summary>
        /// Create a ApiMapping resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApiMapping(string name, ApiMappingArgs args, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:ApiMapping", name, args ?? new ApiMappingArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApiMapping(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigatewayv2:ApiMapping", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ApiMapping resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApiMapping Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ApiMapping(name, id, options);
        }
    }

    public sealed class ApiMappingArgs : Pulumi.ResourceArgs
    {
        [Input("apiId", required: true)]
        public Input<string> ApiId { get; set; } = null!;

        [Input("apiMappingKey")]
        public Input<string>? ApiMappingKey { get; set; }

        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        [Input("stage", required: true)]
        public Input<string> Stage { get; set; } = null!;

        public ApiMappingArgs()
        {
        }
    }
}
