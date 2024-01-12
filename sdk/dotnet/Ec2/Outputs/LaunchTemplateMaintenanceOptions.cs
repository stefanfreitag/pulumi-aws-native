// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Outputs
{

    /// <summary>
    /// The maintenance options of your instance.
    /// </summary>
    [OutputType]
    public sealed class LaunchTemplateMaintenanceOptions
    {
        /// <summary>
        /// Disables the automatic recovery behavior of your instance or sets it to default.
        /// </summary>
        public readonly string? AutoRecovery;
        /// <summary>
        /// Disables the automatic reboot-migration behavior of your instance or sets it to default.
        /// </summary>
        public readonly string? RebootMigration;

        [OutputConstructor]
        private LaunchTemplateMaintenanceOptions(
            string? autoRecovery,

            string? rebootMigration)
        {
            AutoRecovery = autoRecovery;
            RebootMigration = rebootMigration;
        }
    }
}
