// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics
{
    public static class GetChannel
    {
        /// <summary>
        /// Resource Type definition for AWS::IoTAnalytics::Channel
        /// </summary>
        public static Task<GetChannelResult> InvokeAsync(GetChannelArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetChannelResult>("aws-native:iotanalytics:getChannel", args ?? new GetChannelArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::IoTAnalytics::Channel
        /// </summary>
        public static Output<GetChannelResult> Invoke(GetChannelInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetChannelResult>("aws-native:iotanalytics:getChannel", args ?? new GetChannelInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetChannelArgs : global::Pulumi.InvokeArgs
    {
        [Input("channelName", required: true)]
        public string ChannelName { get; set; } = null!;

        public GetChannelArgs()
        {
        }
        public static new GetChannelArgs Empty => new GetChannelArgs();
    }

    public sealed class GetChannelInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("channelName", required: true)]
        public Input<string> ChannelName { get; set; } = null!;

        public GetChannelInvokeArgs()
        {
        }
        public static new GetChannelInvokeArgs Empty => new GetChannelInvokeArgs();
    }


    [OutputType]
    public sealed class GetChannelResult
    {
        public readonly Outputs.ChannelStorage? ChannelStorage;
        public readonly string? Id;
        public readonly Outputs.ChannelRetentionPeriod? RetentionPeriod;
        public readonly ImmutableArray<Outputs.ChannelTag> Tags;

        [OutputConstructor]
        private GetChannelResult(
            Outputs.ChannelStorage? channelStorage,

            string? id,

            Outputs.ChannelRetentionPeriod? retentionPeriod,

            ImmutableArray<Outputs.ChannelTag> tags)
        {
            ChannelStorage = channelStorage;
            Id = id;
            RetentionPeriod = retentionPeriod;
            Tags = tags;
        }
    }
}
