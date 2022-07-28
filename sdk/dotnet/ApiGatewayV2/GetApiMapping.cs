// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2
{
    public static class GetApiMapping
    {
        /// <summary>
        /// Resource Type definition for AWS::ApiGatewayV2::ApiMapping
        /// </summary>
        public static Task<GetApiMappingResult> InvokeAsync(GetApiMappingArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetApiMappingResult>("aws-native:apigatewayv2:getApiMapping", args ?? new GetApiMappingArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ApiGatewayV2::ApiMapping
        /// </summary>
        public static Output<GetApiMappingResult> Invoke(GetApiMappingInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetApiMappingResult>("aws-native:apigatewayv2:getApiMapping", args ?? new GetApiMappingInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApiMappingArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetApiMappingArgs()
        {
        }
        public static new GetApiMappingArgs Empty => new GetApiMappingArgs();
    }

    public sealed class GetApiMappingInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetApiMappingInvokeArgs()
        {
        }
        public static new GetApiMappingInvokeArgs Empty => new GetApiMappingInvokeArgs();
    }


    [OutputType]
    public sealed class GetApiMappingResult
    {
        public readonly string? ApiMappingKey;
        public readonly string? Id;
        public readonly string? Stage;

        [OutputConstructor]
        private GetApiMappingResult(
            string? apiMappingKey,

            string? id,

            string? stage)
        {
            ApiMappingKey = apiMappingKey;
            Id = id;
            Stage = stage;
        }
    }
}
