// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive
{
    public static class GetChannel
    {
        /// <summary>
        /// Resource Type definition for AWS::MediaLive::Channel
        /// </summary>
        public static Task<GetChannelResult> InvokeAsync(GetChannelArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetChannelResult>("aws-native:medialive:getChannel", args ?? new GetChannelArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::MediaLive::Channel
        /// </summary>
        public static Output<GetChannelResult> Invoke(GetChannelInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetChannelResult>("aws-native:medialive:getChannel", args ?? new GetChannelInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetChannelArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetChannelArgs()
        {
        }
        public static new GetChannelArgs Empty => new GetChannelArgs();
    }

    public sealed class GetChannelInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetChannelInvokeArgs()
        {
        }
        public static new GetChannelInvokeArgs Empty => new GetChannelInvokeArgs();
    }


    [OutputType]
    public sealed class GetChannelResult
    {
        public readonly string? Arn;
        public readonly Outputs.ChannelCdiInputSpecification? CdiInputSpecification;
        public readonly string? ChannelClass;
        public readonly ImmutableArray<Outputs.ChannelOutputDestination> Destinations;
        public readonly Outputs.ChannelEncoderSettings? EncoderSettings;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.ChannelInputAttachment> InputAttachments;
        public readonly Outputs.ChannelInputSpecification? InputSpecification;
        public readonly ImmutableArray<string> Inputs;
        public readonly string? LogLevel;
        public readonly string? Name;
        public readonly string? RoleArn;
        public readonly object? Tags;

        [OutputConstructor]
        private GetChannelResult(
            string? arn,

            Outputs.ChannelCdiInputSpecification? cdiInputSpecification,

            string? channelClass,

            ImmutableArray<Outputs.ChannelOutputDestination> destinations,

            Outputs.ChannelEncoderSettings? encoderSettings,

            string? id,

            ImmutableArray<Outputs.ChannelInputAttachment> inputAttachments,

            Outputs.ChannelInputSpecification? inputSpecification,

            ImmutableArray<string> inputs,

            string? logLevel,

            string? name,

            string? roleArn,

            object? tags)
        {
            Arn = arn;
            CdiInputSpecification = cdiInputSpecification;
            ChannelClass = channelClass;
            Destinations = destinations;
            EncoderSettings = encoderSettings;
            Id = id;
            InputAttachments = inputAttachments;
            InputSpecification = inputSpecification;
            Inputs = inputs;
            LogLevel = logLevel;
            Name = name;
            RoleArn = roleArn;
            Tags = tags;
        }
    }
}
