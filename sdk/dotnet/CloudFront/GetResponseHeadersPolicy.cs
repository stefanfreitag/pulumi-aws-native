// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront
{
    public static class GetResponseHeadersPolicy
    {
        /// <summary>
        /// Resource Type definition for AWS::CloudFront::ResponseHeadersPolicy
        /// </summary>
        public static Task<GetResponseHeadersPolicyResult> InvokeAsync(GetResponseHeadersPolicyArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetResponseHeadersPolicyResult>("aws-native:cloudfront:getResponseHeadersPolicy", args ?? new GetResponseHeadersPolicyArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CloudFront::ResponseHeadersPolicy
        /// </summary>
        public static Output<GetResponseHeadersPolicyResult> Invoke(GetResponseHeadersPolicyInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetResponseHeadersPolicyResult>("aws-native:cloudfront:getResponseHeadersPolicy", args ?? new GetResponseHeadersPolicyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetResponseHeadersPolicyArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetResponseHeadersPolicyArgs()
        {
        }
        public static new GetResponseHeadersPolicyArgs Empty => new GetResponseHeadersPolicyArgs();
    }

    public sealed class GetResponseHeadersPolicyInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetResponseHeadersPolicyInvokeArgs()
        {
        }
        public static new GetResponseHeadersPolicyInvokeArgs Empty => new GetResponseHeadersPolicyInvokeArgs();
    }


    [OutputType]
    public sealed class GetResponseHeadersPolicyResult
    {
        public readonly string? Id;
        public readonly string? LastModifiedTime;
        public readonly Outputs.ResponseHeadersPolicyConfig? ResponseHeadersPolicyConfig;

        [OutputConstructor]
        private GetResponseHeadersPolicyResult(
            string? id,

            string? lastModifiedTime,

            Outputs.ResponseHeadersPolicyConfig? responseHeadersPolicyConfig)
        {
            Id = id;
            LastModifiedTime = lastModifiedTime;
            ResponseHeadersPolicyConfig = responseHeadersPolicyConfig;
        }
    }
}
