// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Outputs
{

    [OutputType]
    public sealed class GatewayRouteGrpcGatewayRouteMatch
    {
        public readonly Outputs.GatewayRouteGatewayRouteHostnameMatch? Hostname;
        public readonly ImmutableArray<Outputs.GatewayRouteGrpcGatewayRouteMetadata> Metadata;
        public readonly string? ServiceName;

        [OutputConstructor]
        private GatewayRouteGrpcGatewayRouteMatch(
            Outputs.GatewayRouteGatewayRouteHostnameMatch? hostname,

            ImmutableArray<Outputs.GatewayRouteGrpcGatewayRouteMetadata> metadata,

            string? serviceName)
        {
            Hostname = hostname;
            Metadata = metadata;
            ServiceName = serviceName;
        }
    }
}
