// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    public static class GetQueue
    {
        /// <summary>
        /// Resource Type definition for AWS::Connect::Queue
        /// </summary>
        public static Task<GetQueueResult> InvokeAsync(GetQueueArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetQueueResult>("aws-native:connect:getQueue", args ?? new GetQueueArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Connect::Queue
        /// </summary>
        public static Output<GetQueueResult> Invoke(GetQueueInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetQueueResult>("aws-native:connect:getQueue", args ?? new GetQueueInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetQueueArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) for the queue.
        /// </summary>
        [Input("queueArn", required: true)]
        public string QueueArn { get; set; } = null!;

        public GetQueueArgs()
        {
        }
        public static new GetQueueArgs Empty => new GetQueueArgs();
    }

    public sealed class GetQueueInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) for the queue.
        /// </summary>
        [Input("queueArn", required: true)]
        public Input<string> QueueArn { get; set; } = null!;

        public GetQueueInvokeArgs()
        {
        }
        public static new GetQueueInvokeArgs Empty => new GetQueueInvokeArgs();
    }


    [OutputType]
    public sealed class GetQueueResult
    {
        /// <summary>
        /// The description of the queue.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The identifier for the hours of operation.
        /// </summary>
        public readonly string? HoursOfOperationArn;
        /// <summary>
        /// The identifier of the Amazon Connect instance.
        /// </summary>
        public readonly string? InstanceArn;
        /// <summary>
        /// The maximum number of contacts that can be in the queue before it is considered full.
        /// </summary>
        public readonly int? MaxContacts;
        /// <summary>
        /// The name of the queue.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The outbound caller ID name, number, and outbound whisper flow.
        /// </summary>
        public readonly Outputs.QueueOutboundCallerConfig? OutboundCallerConfig;
        /// <summary>
        /// The Amazon Resource Name (ARN) for the queue.
        /// </summary>
        public readonly string? QueueArn;
        /// <summary>
        /// The quick connects available to agents who are working the queue.
        /// </summary>
        public readonly ImmutableArray<string> QuickConnectArns;
        /// <summary>
        /// The status of the queue.
        /// </summary>
        public readonly Pulumi.AwsNative.Connect.QueueStatus? Status;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        /// <summary>
        /// The type of queue.
        /// </summary>
        public readonly Pulumi.AwsNative.Connect.QueueType? Type;

        [OutputConstructor]
        private GetQueueResult(
            string? description,

            string? hoursOfOperationArn,

            string? instanceArn,

            int? maxContacts,

            string? name,

            Outputs.QueueOutboundCallerConfig? outboundCallerConfig,

            string? queueArn,

            ImmutableArray<string> quickConnectArns,

            Pulumi.AwsNative.Connect.QueueStatus? status,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            Pulumi.AwsNative.Connect.QueueType? type)
        {
            Description = description;
            HoursOfOperationArn = hoursOfOperationArn;
            InstanceArn = instanceArn;
            MaxContacts = maxContacts;
            Name = name;
            OutboundCallerConfig = outboundCallerConfig;
            QueueArn = queueArn;
            QuickConnectArns = quickConnectArns;
            Status = status;
            Tags = tags;
            Type = type;
        }
    }
}
