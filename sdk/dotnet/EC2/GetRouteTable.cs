// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetRouteTable
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::RouteTable
        /// </summary>
        public static Task<GetRouteTableResult> InvokeAsync(GetRouteTableArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRouteTableResult>("aws-native:ec2:getRouteTable", args ?? new GetRouteTableArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::RouteTable
        /// </summary>
        public static Output<GetRouteTableResult> Invoke(GetRouteTableInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRouteTableResult>("aws-native:ec2:getRouteTable", args ?? new GetRouteTableInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRouteTableArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The route table ID.
        /// </summary>
        [Input("routeTableId", required: true)]
        public string RouteTableId { get; set; } = null!;

        public GetRouteTableArgs()
        {
        }
        public static new GetRouteTableArgs Empty => new GetRouteTableArgs();
    }

    public sealed class GetRouteTableInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The route table ID.
        /// </summary>
        [Input("routeTableId", required: true)]
        public Input<string> RouteTableId { get; set; } = null!;

        public GetRouteTableInvokeArgs()
        {
        }
        public static new GetRouteTableInvokeArgs Empty => new GetRouteTableInvokeArgs();
    }


    [OutputType]
    public sealed class GetRouteTableResult
    {
        /// <summary>
        /// The route table ID.
        /// </summary>
        public readonly string? RouteTableId;
        /// <summary>
        /// Any tags assigned to the route table.
        /// </summary>
        public readonly ImmutableArray<Outputs.RouteTableTag> Tags;

        [OutputConstructor]
        private GetRouteTableResult(
            string? routeTableId,

            ImmutableArray<Outputs.RouteTableTag> tags)
        {
            RouteTableId = routeTableId;
            Tags = tags;
        }
    }
}
