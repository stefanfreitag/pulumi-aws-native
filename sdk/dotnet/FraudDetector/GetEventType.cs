// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FraudDetector
{
    public static class GetEventType
    {
        /// <summary>
        /// A resource schema for an EventType in Amazon Fraud Detector.
        /// </summary>
        public static Task<GetEventTypeResult> InvokeAsync(GetEventTypeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEventTypeResult>("aws-native:frauddetector:getEventType", args ?? new GetEventTypeArgs(), options.WithDefaults());

        /// <summary>
        /// A resource schema for an EventType in Amazon Fraud Detector.
        /// </summary>
        public static Output<GetEventTypeResult> Invoke(GetEventTypeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEventTypeResult>("aws-native:frauddetector:getEventType", args ?? new GetEventTypeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEventTypeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the event type.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetEventTypeArgs()
        {
        }
        public static new GetEventTypeArgs Empty => new GetEventTypeArgs();
    }

    public sealed class GetEventTypeInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the event type.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetEventTypeInvokeArgs()
        {
        }
        public static new GetEventTypeInvokeArgs Empty => new GetEventTypeInvokeArgs();
    }


    [OutputType]
    public sealed class GetEventTypeResult
    {
        /// <summary>
        /// The ARN of the event type.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The time when the event type was created.
        /// </summary>
        public readonly string? CreatedTime;
        /// <summary>
        /// The description of the event type.
        /// </summary>
        public readonly string? Description;
        public readonly ImmutableArray<Outputs.EventTypeEntityType> EntityTypes;
        public readonly ImmutableArray<Outputs.EventTypeEventVariable> EventVariables;
        public readonly ImmutableArray<Outputs.EventTypeLabel> Labels;
        /// <summary>
        /// The time when the event type was last updated.
        /// </summary>
        public readonly string? LastUpdatedTime;
        /// <summary>
        /// Tags associated with this event type.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetEventTypeResult(
            string? arn,

            string? createdTime,

            string? description,

            ImmutableArray<Outputs.EventTypeEntityType> entityTypes,

            ImmutableArray<Outputs.EventTypeEventVariable> eventVariables,

            ImmutableArray<Outputs.EventTypeLabel> labels,

            string? lastUpdatedTime,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Arn = arn;
            CreatedTime = createdTime;
            Description = description;
            EntityTypes = entityTypes;
            EventVariables = eventVariables;
            Labels = labels;
            LastUpdatedTime = lastUpdatedTime;
            Tags = tags;
        }
    }
}
