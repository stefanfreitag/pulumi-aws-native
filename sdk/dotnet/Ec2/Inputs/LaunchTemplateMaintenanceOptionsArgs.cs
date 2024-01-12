// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    /// <summary>
    /// The maintenance options of your instance.
    /// </summary>
    public sealed class LaunchTemplateMaintenanceOptionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Disables the automatic recovery behavior of your instance or sets it to default.
        /// </summary>
        [Input("autoRecovery")]
        public Input<string>? AutoRecovery { get; set; }

        /// <summary>
        /// Disables the automatic reboot-migration behavior of your instance or sets it to default.
        /// </summary>
        [Input("rebootMigration")]
        public Input<string>? RebootMigration { get; set; }

        public LaunchTemplateMaintenanceOptionsArgs()
        {
        }
        public static new LaunchTemplateMaintenanceOptionsArgs Empty => new LaunchTemplateMaintenanceOptionsArgs();
    }
}
