// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class GatewayRouteHttpGatewayRouteMatchArgs : global::Pulumi.ResourceArgs
    {
        [Input("headers")]
        private InputList<Inputs.GatewayRouteHttpGatewayRouteHeaderArgs>? _headers;
        public InputList<Inputs.GatewayRouteHttpGatewayRouteHeaderArgs> Headers
        {
            get => _headers ?? (_headers = new InputList<Inputs.GatewayRouteHttpGatewayRouteHeaderArgs>());
            set => _headers = value;
        }

        [Input("hostname")]
        public Input<Inputs.GatewayRouteHostnameMatchArgs>? Hostname { get; set; }

        [Input("method")]
        public Input<string>? Method { get; set; }

        [Input("path")]
        public Input<Inputs.GatewayRouteHttpPathMatchArgs>? Path { get; set; }

        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("queryParameters")]
        private InputList<Inputs.GatewayRouteQueryParameterArgs>? _queryParameters;
        public InputList<Inputs.GatewayRouteQueryParameterArgs> QueryParameters
        {
            get => _queryParameters ?? (_queryParameters = new InputList<Inputs.GatewayRouteQueryParameterArgs>());
            set => _queryParameters = value;
        }

        public GatewayRouteHttpGatewayRouteMatchArgs()
        {
        }
        public static new GatewayRouteHttpGatewayRouteMatchArgs Empty => new GatewayRouteHttpGatewayRouteMatchArgs();
    }
}
