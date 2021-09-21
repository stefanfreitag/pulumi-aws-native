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
    public sealed class GatewayRouteGatewayRouteSpec
    {
        public readonly Outputs.GatewayRouteGrpcGatewayRoute? GrpcRoute;
        public readonly Outputs.GatewayRouteHttpGatewayRoute? Http2Route;
        public readonly Outputs.GatewayRouteHttpGatewayRoute? HttpRoute;

        [OutputConstructor]
        private GatewayRouteGatewayRouteSpec(
            Outputs.GatewayRouteGrpcGatewayRoute? grpcRoute,

            Outputs.GatewayRouteHttpGatewayRoute? http2Route,

            Outputs.GatewayRouteHttpGatewayRoute? httpRoute)
        {
            GrpcRoute = grpcRoute;
            Http2Route = http2Route;
            HttpRoute = httpRoute;
        }
    }
}
