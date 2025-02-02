// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    public sealed class CapacityReservationFleetInstanceTypeSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        [Input("availabilityZoneId")]
        public Input<string>? AvailabilityZoneId { get; set; }

        [Input("ebsOptimized")]
        public Input<bool>? EbsOptimized { get; set; }

        [Input("instancePlatform")]
        public Input<string>? InstancePlatform { get; set; }

        [Input("instanceType")]
        public Input<string>? InstanceType { get; set; }

        [Input("priority")]
        public Input<int>? Priority { get; set; }

        [Input("weight")]
        public Input<double>? Weight { get; set; }

        public CapacityReservationFleetInstanceTypeSpecificationArgs()
        {
        }
        public static new CapacityReservationFleetInstanceTypeSpecificationArgs Empty => new CapacityReservationFleetInstanceTypeSpecificationArgs();
    }
}
