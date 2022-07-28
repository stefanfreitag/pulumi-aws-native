// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppIntegrations
{
    public static class GetEventIntegration
    {
        /// <summary>
        /// Resource Type definition for AWS::AppIntegrations::EventIntegration
        /// </summary>
        public static Task<GetEventIntegrationResult> InvokeAsync(GetEventIntegrationArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetEventIntegrationResult>("aws-native:appintegrations:getEventIntegration", args ?? new GetEventIntegrationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AppIntegrations::EventIntegration
        /// </summary>
        public static Output<GetEventIntegrationResult> Invoke(GetEventIntegrationInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetEventIntegrationResult>("aws-native:appintegrations:getEventIntegration", args ?? new GetEventIntegrationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEventIntegrationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the event integration.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetEventIntegrationArgs()
        {
        }
        public static new GetEventIntegrationArgs Empty => new GetEventIntegrationArgs();
    }

    public sealed class GetEventIntegrationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the event integration.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetEventIntegrationInvokeArgs()
        {
        }
        public static new GetEventIntegrationInvokeArgs Empty => new GetEventIntegrationInvokeArgs();
    }


    [OutputType]
    public sealed class GetEventIntegrationResult
    {
        /// <summary>
        /// The associations with the event integration.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventIntegrationAssociation> Associations;
        /// <summary>
        /// The event integration description.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the event integration.
        /// </summary>
        public readonly string? EventIntegrationArn;
        /// <summary>
        /// The tags (keys and values) associated with the event integration.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventIntegrationTag> Tags;

        [OutputConstructor]
        private GetEventIntegrationResult(
            ImmutableArray<Outputs.EventIntegrationAssociation> associations,

            string? description,

            string? eventIntegrationArn,

            ImmutableArray<Outputs.EventIntegrationTag> tags)
        {
            Associations = associations;
            Description = description;
            EventIntegrationArn = eventIntegrationArn;
            Tags = tags;
        }
    }
}
