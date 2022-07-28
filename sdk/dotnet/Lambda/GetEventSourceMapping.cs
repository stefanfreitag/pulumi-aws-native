// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda
{
    public static class GetEventSourceMapping
    {
        /// <summary>
        /// Resource Type definition for AWS::Lambda::EventSourceMapping
        /// </summary>
        public static Task<GetEventSourceMappingResult> InvokeAsync(GetEventSourceMappingArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetEventSourceMappingResult>("aws-native:lambda:getEventSourceMapping", args ?? new GetEventSourceMappingArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Lambda::EventSourceMapping
        /// </summary>
        public static Output<GetEventSourceMappingResult> Invoke(GetEventSourceMappingInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetEventSourceMappingResult>("aws-native:lambda:getEventSourceMapping", args ?? new GetEventSourceMappingInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetEventSourceMappingArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Event Source Mapping Identifier UUID.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetEventSourceMappingArgs()
        {
        }
        public static new GetEventSourceMappingArgs Empty => new GetEventSourceMappingArgs();
    }

    public sealed class GetEventSourceMappingInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Event Source Mapping Identifier UUID.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetEventSourceMappingInvokeArgs()
        {
        }
        public static new GetEventSourceMappingInvokeArgs Empty => new GetEventSourceMappingInvokeArgs();
    }


    [OutputType]
    public sealed class GetEventSourceMappingResult
    {
        /// <summary>
        /// The maximum number of items to retrieve in a single batch.
        /// </summary>
        public readonly int? BatchSize;
        /// <summary>
        /// (Streams) If the function returns an error, split the batch in two and retry.
        /// </summary>
        public readonly bool? BisectBatchOnFunctionError;
        /// <summary>
        /// (Streams) An Amazon SQS queue or Amazon SNS topic destination for discarded records.
        /// </summary>
        public readonly Outputs.EventSourceMappingDestinationConfig? DestinationConfig;
        /// <summary>
        /// Disables the event source mapping to pause polling and invocation.
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// The filter criteria to control event filtering.
        /// </summary>
        public readonly Outputs.EventSourceMappingFilterCriteria? FilterCriteria;
        /// <summary>
        /// The name of the Lambda function.
        /// </summary>
        public readonly string? FunctionName;
        /// <summary>
        /// (Streams) A list of response types supported by the function.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Lambda.EventSourceMappingFunctionResponseTypesItem> FunctionResponseTypes;
        /// <summary>
        /// Event Source Mapping Identifier UUID.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// (Streams) The maximum amount of time to gather records before invoking the function, in seconds.
        /// </summary>
        public readonly int? MaximumBatchingWindowInSeconds;
        /// <summary>
        /// (Streams) The maximum age of a record that Lambda sends to a function for processing.
        /// </summary>
        public readonly int? MaximumRecordAgeInSeconds;
        /// <summary>
        /// (Streams) The maximum number of times to retry when the function returns an error.
        /// </summary>
        public readonly int? MaximumRetryAttempts;
        /// <summary>
        /// (Streams) The number of batches to process from each shard concurrently.
        /// </summary>
        public readonly int? ParallelizationFactor;
        /// <summary>
        /// (ActiveMQ) A list of ActiveMQ queues.
        /// </summary>
        public readonly ImmutableArray<string> Queues;
        /// <summary>
        /// A list of SourceAccessConfiguration.
        /// </summary>
        public readonly ImmutableArray<Outputs.EventSourceMappingSourceAccessConfiguration> SourceAccessConfigurations;
        /// <summary>
        /// (Kafka) A list of Kafka topics.
        /// </summary>
        public readonly ImmutableArray<string> Topics;
        /// <summary>
        /// (Streams) Tumbling window (non-overlapping time window) duration to perform aggregations.
        /// </summary>
        public readonly int? TumblingWindowInSeconds;

        [OutputConstructor]
        private GetEventSourceMappingResult(
            int? batchSize,

            bool? bisectBatchOnFunctionError,

            Outputs.EventSourceMappingDestinationConfig? destinationConfig,

            bool? enabled,

            Outputs.EventSourceMappingFilterCriteria? filterCriteria,

            string? functionName,

            ImmutableArray<Pulumi.AwsNative.Lambda.EventSourceMappingFunctionResponseTypesItem> functionResponseTypes,

            string? id,

            int? maximumBatchingWindowInSeconds,

            int? maximumRecordAgeInSeconds,

            int? maximumRetryAttempts,

            int? parallelizationFactor,

            ImmutableArray<string> queues,

            ImmutableArray<Outputs.EventSourceMappingSourceAccessConfiguration> sourceAccessConfigurations,

            ImmutableArray<string> topics,

            int? tumblingWindowInSeconds)
        {
            BatchSize = batchSize;
            BisectBatchOnFunctionError = bisectBatchOnFunctionError;
            DestinationConfig = destinationConfig;
            Enabled = enabled;
            FilterCriteria = filterCriteria;
            FunctionName = functionName;
            FunctionResponseTypes = functionResponseTypes;
            Id = id;
            MaximumBatchingWindowInSeconds = maximumBatchingWindowInSeconds;
            MaximumRecordAgeInSeconds = maximumRecordAgeInSeconds;
            MaximumRetryAttempts = maximumRetryAttempts;
            ParallelizationFactor = parallelizationFactor;
            Queues = queues;
            SourceAccessConfigurations = sourceAccessConfigurations;
            Topics = topics;
            TumblingWindowInSeconds = tumblingWindowInSeconds;
        }
    }
}
