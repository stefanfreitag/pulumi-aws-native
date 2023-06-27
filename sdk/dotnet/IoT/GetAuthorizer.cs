// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetAuthorizer
    {
        /// <summary>
        /// Creates an authorizer.
        /// </summary>
        public static Task<GetAuthorizerResult> InvokeAsync(GetAuthorizerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAuthorizerResult>("aws-native:iot:getAuthorizer", args ?? new GetAuthorizerArgs(), options.WithDefaults());

        /// <summary>
        /// Creates an authorizer.
        /// </summary>
        public static Output<GetAuthorizerResult> Invoke(GetAuthorizerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAuthorizerResult>("aws-native:iot:getAuthorizer", args ?? new GetAuthorizerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAuthorizerArgs : global::Pulumi.InvokeArgs
    {
        [Input("authorizerName", required: true)]
        public string AuthorizerName { get; set; } = null!;

        public GetAuthorizerArgs()
        {
        }
        public static new GetAuthorizerArgs Empty => new GetAuthorizerArgs();
    }

    public sealed class GetAuthorizerInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("authorizerName", required: true)]
        public Input<string> AuthorizerName { get; set; } = null!;

        public GetAuthorizerInvokeArgs()
        {
        }
        public static new GetAuthorizerInvokeArgs Empty => new GetAuthorizerInvokeArgs();
    }


    [OutputType]
    public sealed class GetAuthorizerResult
    {
        public readonly string? Arn;
        public readonly string? AuthorizerFunctionArn;
        public readonly bool? EnableCachingForHttp;
        public readonly Pulumi.AwsNative.IoT.AuthorizerStatus? Status;
        public readonly ImmutableArray<Outputs.AuthorizerTag> Tags;
        public readonly string? TokenKeyName;
        public readonly object? TokenSigningPublicKeys;

        [OutputConstructor]
        private GetAuthorizerResult(
            string? arn,

            string? authorizerFunctionArn,

            bool? enableCachingForHttp,

            Pulumi.AwsNative.IoT.AuthorizerStatus? status,

            ImmutableArray<Outputs.AuthorizerTag> tags,

            string? tokenKeyName,

            object? tokenSigningPublicKeys)
        {
            Arn = arn;
            AuthorizerFunctionArn = authorizerFunctionArn;
            EnableCachingForHttp = enableCachingForHttp;
            Status = status;
            Tags = tags;
            TokenKeyName = tokenKeyName;
            TokenSigningPublicKeys = tokenSigningPublicKeys;
        }
    }
}
