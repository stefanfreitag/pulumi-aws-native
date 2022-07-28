// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConvert
{
    public static class GetJobTemplate
    {
        /// <summary>
        /// Resource Type definition for AWS::MediaConvert::JobTemplate
        /// </summary>
        public static Task<GetJobTemplateResult> InvokeAsync(GetJobTemplateArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetJobTemplateResult>("aws-native:mediaconvert:getJobTemplate", args ?? new GetJobTemplateArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::MediaConvert::JobTemplate
        /// </summary>
        public static Output<GetJobTemplateResult> Invoke(GetJobTemplateInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetJobTemplateResult>("aws-native:mediaconvert:getJobTemplate", args ?? new GetJobTemplateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetJobTemplateArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetJobTemplateArgs()
        {
        }
        public static new GetJobTemplateArgs Empty => new GetJobTemplateArgs();
    }

    public sealed class GetJobTemplateInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetJobTemplateInvokeArgs()
        {
        }
        public static new GetJobTemplateInvokeArgs Empty => new GetJobTemplateInvokeArgs();
    }


    [OutputType]
    public sealed class GetJobTemplateResult
    {
        public readonly Outputs.JobTemplateAccelerationSettings? AccelerationSettings;
        public readonly string? Arn;
        public readonly string? Category;
        public readonly string? Description;
        public readonly ImmutableArray<Outputs.JobTemplateHopDestination> HopDestinations;
        public readonly string? Id;
        public readonly int? Priority;
        public readonly string? Queue;
        public readonly object? SettingsJson;
        public readonly string? StatusUpdateInterval;
        public readonly object? Tags;

        [OutputConstructor]
        private GetJobTemplateResult(
            Outputs.JobTemplateAccelerationSettings? accelerationSettings,

            string? arn,

            string? category,

            string? description,

            ImmutableArray<Outputs.JobTemplateHopDestination> hopDestinations,

            string? id,

            int? priority,

            string? queue,

            object? settingsJson,

            string? statusUpdateInterval,

            object? tags)
        {
            AccelerationSettings = accelerationSettings;
            Arn = arn;
            Category = category;
            Description = description;
            HopDestinations = hopDestinations;
            Id = id;
            Priority = priority;
            Queue = queue;
            SettingsJson = settingsJson;
            StatusUpdateInterval = statusUpdateInterval;
            Tags = tags;
        }
    }
}
