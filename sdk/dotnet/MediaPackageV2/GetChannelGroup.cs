// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaPackageV2
{
    public static class GetChannelGroup
    {
        /// <summary>
        /// Definition of AWS::MediaPackageV2::ChannelGroup Resource Type
        /// </summary>
        public static Task<GetChannelGroupResult> InvokeAsync(GetChannelGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetChannelGroupResult>("aws-native:mediapackagev2:getChannelGroup", args ?? new GetChannelGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::MediaPackageV2::ChannelGroup Resource Type
        /// </summary>
        public static Output<GetChannelGroupResult> Invoke(GetChannelGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetChannelGroupResult>("aws-native:mediapackagev2:getChannelGroup", args ?? new GetChannelGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetChannelGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetChannelGroupArgs()
        {
        }
        public static new GetChannelGroupArgs Empty => new GetChannelGroupArgs();
    }

    public sealed class GetChannelGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetChannelGroupInvokeArgs()
        {
        }
        public static new GetChannelGroupInvokeArgs Empty => new GetChannelGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetChannelGroupResult
    {
        public readonly string? Arn;
        public readonly string? CreatedAt;
        public readonly string? Description;
        public readonly string? EgressDomain;
        public readonly string? ModifiedAt;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetChannelGroupResult(
            string? arn,

            string? createdAt,

            string? description,

            string? egressDomain,

            string? modifiedAt,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Arn = arn;
            CreatedAt = createdAt;
            Description = description;
            EgressDomain = egressDomain;
            ModifiedAt = modifiedAt;
            Tags = tags;
        }
    }
}
