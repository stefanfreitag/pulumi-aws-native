// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Outputs
{

    [OutputType]
    public sealed class DeliveryStreamSplunkDestinationConfiguration
    {
        public readonly Outputs.DeliveryStreamSplunkBufferingHints? BufferingHints;
        public readonly Outputs.DeliveryStreamCloudWatchLoggingOptions? CloudWatchLoggingOptions;
        public readonly int? HecAcknowledgmentTimeoutInSeconds;
        public readonly string HecEndpoint;
        public readonly Pulumi.AwsNative.KinesisFirehose.DeliveryStreamSplunkDestinationConfigurationHecEndpointType HecEndpointType;
        public readonly string HecToken;
        public readonly Outputs.DeliveryStreamProcessingConfiguration? ProcessingConfiguration;
        public readonly Outputs.DeliveryStreamSplunkRetryOptions? RetryOptions;
        public readonly string? S3BackupMode;
        public readonly Outputs.DeliveryStreamS3DestinationConfiguration S3Configuration;

        [OutputConstructor]
        private DeliveryStreamSplunkDestinationConfiguration(
            Outputs.DeliveryStreamSplunkBufferingHints? bufferingHints,

            Outputs.DeliveryStreamCloudWatchLoggingOptions? cloudWatchLoggingOptions,

            int? hecAcknowledgmentTimeoutInSeconds,

            string hecEndpoint,

            Pulumi.AwsNative.KinesisFirehose.DeliveryStreamSplunkDestinationConfigurationHecEndpointType hecEndpointType,

            string hecToken,

            Outputs.DeliveryStreamProcessingConfiguration? processingConfiguration,

            Outputs.DeliveryStreamSplunkRetryOptions? retryOptions,

            string? s3BackupMode,

            Outputs.DeliveryStreamS3DestinationConfiguration s3Configuration)
        {
            BufferingHints = bufferingHints;
            CloudWatchLoggingOptions = cloudWatchLoggingOptions;
            HecAcknowledgmentTimeoutInSeconds = hecAcknowledgmentTimeoutInSeconds;
            HecEndpoint = hecEndpoint;
            HecEndpointType = hecEndpointType;
            HecToken = hecToken;
            ProcessingConfiguration = processingConfiguration;
            RetryOptions = retryOptions;
            S3BackupMode = s3BackupMode;
            S3Configuration = s3Configuration;
        }
    }
}
