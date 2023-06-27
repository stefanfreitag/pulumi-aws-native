// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudTrail
{
    public static class GetEventDataStore
    {
        /// <summary>
        /// A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 90 to 2555 days (about three months to up to seven years).
        /// </summary>
        public static Task<GetEventDataStoreResult> InvokeAsync(GetEventDataStoreArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetEventDataStoreResult>("aws-native:cloudtrail:getEventDataStore", args ?? new GetEventDataStoreArgs(), options.WithDefaults());

        /// <summary>
        /// A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 90 to 2555 days (about three months to up to seven years).
        /// </summary>
        public static Output<GetEventDataStoreResult> Invoke(GetEventDataStoreInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetEventDataStoreResult>("aws-native:cloudtrail:getEventDataStore", args ?? new GetEventDataStoreInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEventDataStoreArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the event data store.
        /// </summary>
        [Input("eventDataStoreArn", required: true)]
        public string EventDataStoreArn { get; set; } = null!;

        public GetEventDataStoreArgs()
        {
        }
        public static new GetEventDataStoreArgs Empty => new GetEventDataStoreArgs();
    }

    public sealed class GetEventDataStoreInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the event data store.
        /// </summary>
        [Input("eventDataStoreArn", required: true)]
        public Input<string> EventDataStoreArn { get; set; } = null!;

        public GetEventDataStoreInvokeArgs()
        {
        }
        public static new GetEventDataStoreInvokeArgs Empty => new GetEventDataStoreInvokeArgs();
    }


    [OutputType]
    public sealed class GetEventDataStoreResult
    {
        /// <summary>
        /// The advanced event selectors that were used to select events for the data store.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventDataStoreAdvancedEventSelector> AdvancedEventSelectors;
        /// <summary>
        /// The timestamp of the event data store's creation.
        /// </summary>
        public readonly string? CreatedTimestamp;
        /// <summary>
        /// The ARN of the event data store.
        /// </summary>
        public readonly string? EventDataStoreArn;
        /// <summary>
        /// Indicates whether the event data store is ingesting events.
        /// </summary>
        public readonly bool? IngestionEnabled;
        /// <summary>
        /// Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        /// </summary>
        public readonly string? KmsKeyId;
        /// <summary>
        /// Indicates whether the event data store includes events from all regions, or only from the region in which it was created.
        /// </summary>
        public readonly bool? MultiRegionEnabled;
        /// <summary>
        /// The name of the event data store.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// Indicates that an event data store is collecting logged events for an organization.
        /// </summary>
        public readonly bool? OrganizationEnabled;
        /// <summary>
        /// The retention period, in days.
        /// </summary>
        public readonly int? RetentionPeriod;
        /// <summary>
        /// The status of an event data store. Values are STARTING_INGESTION, ENABLED, STOPPING_INGESTION, STOPPED_INGESTION and PENDING_DELETION.
        /// </summary>
        public readonly string? Status;
        public readonly ImmutableArray<Outputs.EventDataStoreTag> Tags;
        /// <summary>
        /// Indicates whether the event data store is protected from termination.
        /// </summary>
        public readonly bool? TerminationProtectionEnabled;
        /// <summary>
        /// The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.
        /// </summary>
        public readonly string? UpdatedTimestamp;

        [OutputConstructor]
        private GetEventDataStoreResult(
            ImmutableArray<Outputs.EventDataStoreAdvancedEventSelector> advancedEventSelectors,

            string? createdTimestamp,

            string? eventDataStoreArn,

            bool? ingestionEnabled,

            string? kmsKeyId,

            bool? multiRegionEnabled,

            string? name,

            bool? organizationEnabled,

            int? retentionPeriod,

            string? status,

            ImmutableArray<Outputs.EventDataStoreTag> tags,

            bool? terminationProtectionEnabled,

            string? updatedTimestamp)
        {
            AdvancedEventSelectors = advancedEventSelectors;
            CreatedTimestamp = createdTimestamp;
            EventDataStoreArn = eventDataStoreArn;
            IngestionEnabled = ingestionEnabled;
            KmsKeyId = kmsKeyId;
            MultiRegionEnabled = multiRegionEnabled;
            Name = name;
            OrganizationEnabled = organizationEnabled;
            RetentionPeriod = retentionPeriod;
            Status = status;
            Tags = tags;
            TerminationProtectionEnabled = terminationProtectionEnabled;
            UpdatedTimestamp = updatedTimestamp;
        }
    }
}
