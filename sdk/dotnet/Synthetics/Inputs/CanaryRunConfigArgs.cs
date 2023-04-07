// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Synthetics.Inputs
{

    public sealed class CanaryRunConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable active tracing if set to true
        /// </summary>
        [Input("activeTracing")]
        public Input<bool>? ActiveTracing { get; set; }

        /// <summary>
        /// Environment variable key-value pairs.
        /// </summary>
        [Input("environmentVariables")]
        public Input<object>? EnvironmentVariables { get; set; }

        /// <summary>
        /// Provide maximum memory available for canary in MB
        /// </summary>
        [Input("memoryInMB")]
        public Input<int>? MemoryInMB { get; set; }

        /// <summary>
        /// Provide maximum canary timeout per run in seconds
        /// </summary>
        [Input("timeoutInSeconds")]
        public Input<int>? TimeoutInSeconds { get; set; }

        public CanaryRunConfigArgs()
        {
        }
        public static new CanaryRunConfigArgs Empty => new CanaryRunConfigArgs();
    }
}
