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
    public sealed class GatewayRouteGatewayRouteHostnameMatch
    {
        public readonly string? Exact;
        public readonly string? Suffix;

        [OutputConstructor]
        private GatewayRouteGatewayRouteHostnameMatch(
            string? exact,

            string? suffix)
        {
            Exact = exact;
            Suffix = suffix;
        }
    }
}
