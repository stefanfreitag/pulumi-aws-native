// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive
{
    public static class GetInput
    {
        /// <summary>
        /// Resource Type definition for AWS::MediaLive::Input
        /// </summary>
        public static Task<GetInputResult> InvokeAsync(GetInputArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetInputResult>("aws-native:medialive:getInput", args ?? new GetInputArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::MediaLive::Input
        /// </summary>
        public static Output<GetInputResult> Invoke(GetInputInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetInputResult>("aws-native:medialive:getInput", args ?? new GetInputInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInputArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetInputArgs()
        {
        }
        public static new GetInputArgs Empty => new GetInputArgs();
    }

    public sealed class GetInputInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetInputInvokeArgs()
        {
        }
        public static new GetInputInvokeArgs Empty => new GetInputInvokeArgs();
    }


    [OutputType]
    public sealed class GetInputResult
    {
        public readonly string? Arn;
        public readonly ImmutableArray<Outputs.InputDestinationRequest> Destinations;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.InputDeviceSettings> InputDevices;
        public readonly ImmutableArray<string> InputSecurityGroups;
        public readonly ImmutableArray<Outputs.InputMediaConnectFlowRequest> MediaConnectFlows;
        public readonly string? Name;
        public readonly string? RoleArn;
        public readonly ImmutableArray<Outputs.InputSourceRequest> Sources;
        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaLive::Input` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? Tags;

        [OutputConstructor]
        private GetInputResult(
            string? arn,

            ImmutableArray<Outputs.InputDestinationRequest> destinations,

            string? id,

            ImmutableArray<Outputs.InputDeviceSettings> inputDevices,

            ImmutableArray<string> inputSecurityGroups,

            ImmutableArray<Outputs.InputMediaConnectFlowRequest> mediaConnectFlows,

            string? name,

            string? roleArn,

            ImmutableArray<Outputs.InputSourceRequest> sources,

            object? tags)
        {
            Arn = arn;
            Destinations = destinations;
            Id = id;
            InputDevices = inputDevices;
            InputSecurityGroups = inputSecurityGroups;
            MediaConnectFlows = mediaConnectFlows;
            Name = name;
            RoleArn = roleArn;
            Sources = sources;
            Tags = tags;
        }
    }
}
