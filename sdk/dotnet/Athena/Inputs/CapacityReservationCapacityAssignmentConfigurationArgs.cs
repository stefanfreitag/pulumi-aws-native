// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Athena.Inputs
{

    /// <summary>
    /// Assignment configuration to assign workgroups to a reservation
    /// </summary>
    public sealed class CapacityReservationCapacityAssignmentConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("capacityAssignments", required: true)]
        private InputList<Inputs.CapacityReservationCapacityAssignmentArgs>? _capacityAssignments;
        public InputList<Inputs.CapacityReservationCapacityAssignmentArgs> CapacityAssignments
        {
            get => _capacityAssignments ?? (_capacityAssignments = new InputList<Inputs.CapacityReservationCapacityAssignmentArgs>());
            set => _capacityAssignments = value;
        }

        public CapacityReservationCapacityAssignmentConfigurationArgs()
        {
        }
        public static new CapacityReservationCapacityAssignmentConfigurationArgs Empty => new CapacityReservationCapacityAssignmentConfigurationArgs();
    }
}
