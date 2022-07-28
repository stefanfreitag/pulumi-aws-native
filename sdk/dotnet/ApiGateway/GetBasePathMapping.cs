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
        /// Resource Type definition for AWS::ApiGateway::BasePathMapping
        /// </summary>
        public static Task<GetBasePathMappingResult> InvokeAsync(GetBasePathMappingArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetBasePathMappingResult>("aws-native:apigateway:getBasePathMapping", args ?? new GetBasePathMappingArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ApiGateway::BasePathMapping
        /// </summary>
        public static Output<GetBasePathMappingResult> Invoke(GetBasePathMappingInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetBasePathMappingResult>("aws-native:apigateway:getBasePathMapping", args ?? new GetBasePathMappingInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBasePathMappingArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The base path name that callers of the API must provide in the URL after the domain name.
        /// </summary>
        [Input("basePath", required: true)]
        public string BasePath { get; set; } = null!;

        /// <summary>
        /// The DomainName of an AWS::ApiGateway::DomainName resource.
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
        /// The base path name that callers of the API must provide in the URL after the domain name.
        /// </summary>
        [Input("basePath", required: true)]
        public Input<string> BasePath { get; set; } = null!;

        /// <summary>
        /// The DomainName of an AWS::ApiGateway::DomainName resource.
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
        public readonly string? Id;
        /// <summary>
        /// The ID of the API.
        /// </summary>
        public readonly string? RestApiId;
        /// <summary>
        /// The name of the API's stage.
        /// </summary>
        public readonly string? Stage;

        [OutputConstructor]
        private GetBasePathMappingResult(
            string? id,

            string? restApiId,

            string? stage)
        {
            Id = id;
            RestApiId = restApiId;
            Stage = stage;
        }
    }
}
