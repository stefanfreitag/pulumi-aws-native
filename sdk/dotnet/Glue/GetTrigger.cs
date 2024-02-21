// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    public static class GetTrigger
    {
        /// <summary>
        /// Resource Type definition for AWS::Glue::Trigger
        /// </summary>
        public static Task<GetTriggerResult> InvokeAsync(GetTriggerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTriggerResult>("aws-native:glue:getTrigger", args ?? new GetTriggerArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Glue::Trigger
        /// </summary>
        public static Output<GetTriggerResult> Invoke(GetTriggerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTriggerResult>("aws-native:glue:getTrigger", args ?? new GetTriggerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTriggerArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetTriggerArgs()
        {
        }
        public static new GetTriggerArgs Empty => new GetTriggerArgs();
    }

    public sealed class GetTriggerInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetTriggerInvokeArgs()
        {
        }
        public static new GetTriggerInvokeArgs Empty => new GetTriggerInvokeArgs();
    }


    [OutputType]
    public sealed class GetTriggerResult
    {
        public readonly ImmutableArray<Outputs.TriggerAction> Actions;
        public readonly string? Description;
        public readonly Outputs.TriggerEventBatchingCondition? EventBatchingCondition;
        public readonly string? Id;
        public readonly Outputs.TriggerPredicate? Predicate;
        public readonly string? Schedule;
        public readonly bool? StartOnCreation;
        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::Trigger` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? Tags;

        [OutputConstructor]
        private GetTriggerResult(
            ImmutableArray<Outputs.TriggerAction> actions,

            string? description,

            Outputs.TriggerEventBatchingCondition? eventBatchingCondition,

            string? id,

            Outputs.TriggerPredicate? predicate,

            string? schedule,

            bool? startOnCreation,

            object? tags)
        {
            Actions = actions;
            Description = description;
            EventBatchingCondition = eventBatchingCondition;
            Id = id;
            Predicate = predicate;
            Schedule = schedule;
            StartOnCreation = startOnCreation;
            Tags = tags;
        }
    }
}
