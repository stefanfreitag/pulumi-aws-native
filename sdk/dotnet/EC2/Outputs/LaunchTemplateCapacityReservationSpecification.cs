// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    /// <summary>
    /// Specifies an instance's Capacity Reservation targeting option.
    /// </summary>
    [OutputType]
    public sealed class LaunchTemplateCapacityReservationSpecification
    {
        /// <summary>
        /// Indicates the instance's Capacity Reservation preferences.
        /// </summary>
        public readonly string? CapacityReservationPreference;
        public readonly Outputs.LaunchTemplateCapacityReservationTarget? CapacityReservationTarget;

        [OutputConstructor]
        private LaunchTemplateCapacityReservationSpecification(
            string? capacityReservationPreference,

            Outputs.LaunchTemplateCapacityReservationTarget? capacityReservationTarget)
        {
            CapacityReservationPreference = capacityReservationPreference;
            CapacityReservationTarget = capacityReservationTarget;
        }
    }
}
