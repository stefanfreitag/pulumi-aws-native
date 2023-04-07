// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMRServerless.Outputs
{

    /// <summary>
    /// Configuration for Auto Stop of Application
    /// </summary>
    [OutputType]
    public sealed class ApplicationAutoStopConfiguration
    {
        /// <summary>
        /// If set to true, the Application will automatically stop after being idle. Defaults to true.
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// The amount of time [in minutes] to wait before auto stopping the Application when idle. Defaults to 15 minutes.
        /// </summary>
        public readonly int? IdleTimeoutMinutes;

        [OutputConstructor]
        private ApplicationAutoStopConfiguration(
            bool? enabled,

            int? idleTimeoutMinutes)
        {
            Enabled = enabled;
            IdleTimeoutMinutes = idleTimeoutMinutes;
        }
    }
}
