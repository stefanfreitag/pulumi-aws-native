// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Outputs
{

    [OutputType]
    public sealed class LogDeliveryConfigurationLogConfiguration
    {
        public readonly Outputs.LogDeliveryConfigurationCloudWatchLogsConfiguration? CloudWatchLogsConfiguration;
        public readonly string? EventSource;
        public readonly string? LogLevel;

        [OutputConstructor]
        private LogDeliveryConfigurationLogConfiguration(
            Outputs.LogDeliveryConfigurationCloudWatchLogsConfiguration? cloudWatchLogsConfiguration,

            string? eventSource,

            string? logLevel)
        {
            CloudWatchLogsConfiguration = cloudWatchLogsConfiguration;
            EventSource = eventSource;
            LogLevel = logLevel;
        }
    }
}
