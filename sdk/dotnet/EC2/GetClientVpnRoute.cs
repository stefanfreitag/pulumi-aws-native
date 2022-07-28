// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetClientVpnRoute
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::ClientVpnRoute
        /// </summary>
        public static Task<GetClientVpnRouteResult> InvokeAsync(GetClientVpnRouteArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClientVpnRouteResult>("aws-native:ec2:getClientVpnRoute", args ?? new GetClientVpnRouteArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::ClientVpnRoute
        /// </summary>
        public static Output<GetClientVpnRouteResult> Invoke(GetClientVpnRouteInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetClientVpnRouteResult>("aws-native:ec2:getClientVpnRoute", args ?? new GetClientVpnRouteInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClientVpnRouteArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetClientVpnRouteArgs()
        {
        }
        public static new GetClientVpnRouteArgs Empty => new GetClientVpnRouteArgs();
    }

    public sealed class GetClientVpnRouteInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetClientVpnRouteInvokeArgs()
        {
        }
        public static new GetClientVpnRouteInvokeArgs Empty => new GetClientVpnRouteInvokeArgs();
    }


    [OutputType]
    public sealed class GetClientVpnRouteResult
    {
        public readonly string? Id;

        [OutputConstructor]
        private GetClientVpnRouteResult(string? id)
        {
            Id = id;
        }
    }
}
