// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint
{
    public static class GetEmailChannel
    {
        /// <summary>
        /// Resource Type definition for AWS::Pinpoint::EmailChannel
        /// </summary>
        public static Task<GetEmailChannelResult> InvokeAsync(GetEmailChannelArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEmailChannelResult>("aws-native:pinpoint:getEmailChannel", args ?? new GetEmailChannelArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Pinpoint::EmailChannel
        /// </summary>
        public static Output<GetEmailChannelResult> Invoke(GetEmailChannelInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEmailChannelResult>("aws-native:pinpoint:getEmailChannel", args ?? new GetEmailChannelInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEmailChannelArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetEmailChannelArgs()
        {
        }
        public static new GetEmailChannelArgs Empty => new GetEmailChannelArgs();
    }

    public sealed class GetEmailChannelInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetEmailChannelInvokeArgs()
        {
        }
        public static new GetEmailChannelInvokeArgs Empty => new GetEmailChannelInvokeArgs();
    }


    [OutputType]
    public sealed class GetEmailChannelResult
    {
        public readonly string? ConfigurationSet;
        public readonly bool? Enabled;
        public readonly string? FromAddress;
        public readonly string? Id;
        public readonly string? Identity;
        public readonly string? RoleArn;

        [OutputConstructor]
        private GetEmailChannelResult(
            string? configurationSet,

            bool? enabled,

            string? fromAddress,

            string? id,

            string? identity,

            string? roleArn)
        {
            ConfigurationSet = configurationSet;
            Enabled = enabled;
            FromAddress = fromAddress;
            Id = id;
            Identity = identity;
            RoleArn = roleArn;
        }
    }
}
