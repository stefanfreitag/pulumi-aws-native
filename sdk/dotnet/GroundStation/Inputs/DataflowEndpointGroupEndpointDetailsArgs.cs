// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GroundStation.Inputs
{

    public sealed class DataflowEndpointGroupEndpointDetailsArgs : global::Pulumi.ResourceArgs
    {
        [Input("awsGroundStationAgentEndpoint")]
        public Input<Inputs.DataflowEndpointGroupAwsGroundStationAgentEndpointArgs>? AwsGroundStationAgentEndpoint { get; set; }

        [Input("endpoint")]
        public Input<Inputs.DataflowEndpointGroupDataflowEndpointArgs>? Endpoint { get; set; }

        [Input("securityDetails")]
        public Input<Inputs.DataflowEndpointGroupSecurityDetailsArgs>? SecurityDetails { get; set; }

        public DataflowEndpointGroupEndpointDetailsArgs()
        {
        }
        public static new DataflowEndpointGroupEndpointDetailsArgs Empty => new DataflowEndpointGroupEndpointDetailsArgs();
    }
}
