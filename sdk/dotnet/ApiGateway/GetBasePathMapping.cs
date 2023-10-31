// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway
{
    public static class GetBasePathMapping
    {
        /// <summary>
        /// The ``AWS::ApiGateway::BasePathMapping`` resource creates a base path that clients who call your API must use in the invocation URL.
        /// </summary>
        public static Task<GetBasePathMappingResult> InvokeAsync(GetBasePathMappingArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetBasePathMappingResult>("aws-native:apigateway:getBasePathMapping", args ?? new GetBasePathMappingArgs(), options.WithDefaults());

        /// <summary>
        /// The ``AWS::ApiGateway::BasePathMapping`` resource creates a base path that clients who call your API must use in the invocation URL.
        /// </summary>
        public static Output<GetBasePathMappingResult> Invoke(GetBasePathMappingInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetBasePathMappingResult>("aws-native:apigateway:getBasePathMapping", args ?? new GetBasePathMappingInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBasePathMappingArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The base path name that callers of the API must provide as part of the URL after the domain name.
        /// </summary>
        [Input("basePath", required: true)]
        public string BasePath { get; set; } = null!;

        /// <summary>
        /// The domain name of the BasePathMapping resource to be described.
        /// </summary>
        [Input("domainName", required: true)]
        public string DomainName { get; set; } = null!;

        public GetBasePathMappingArgs()
        {
        }
        public static new GetBasePathMappingArgs Empty => new GetBasePathMappingArgs();
    }

    public sealed class GetBasePathMappingInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The base path name that callers of the API must provide as part of the URL after the domain name.
        /// </summary>
        [Input("basePath", required: true)]
        public Input<string> BasePath { get; set; } = null!;

        /// <summary>
        /// The domain name of the BasePathMapping resource to be described.
        /// </summary>
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        public GetBasePathMappingInvokeArgs()
        {
        }
        public static new GetBasePathMappingInvokeArgs Empty => new GetBasePathMappingInvokeArgs();
    }


    [OutputType]
    public sealed class GetBasePathMappingResult
    {
        /// <summary>
        /// The string identifier of the associated RestApi.
        /// </summary>
        public readonly string? RestApiId;
        /// <summary>
        /// The name of the associated stage.
        /// </summary>
        public readonly string? Stage;

        [OutputConstructor]
        private GetBasePathMappingResult(
            string? restApiId,

            string? stage)
        {
            RestApiId = restApiId;
            Stage = stage;
        }
    }
}
