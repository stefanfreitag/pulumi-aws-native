// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh
{
    public static class GetVirtualGateway
    {
        /// <summary>
        /// Resource Type definition for AWS::AppMesh::VirtualGateway
        /// </summary>
        public static Task<GetVirtualGatewayResult> InvokeAsync(GetVirtualGatewayArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVirtualGatewayResult>("aws-native:appmesh:getVirtualGateway", args ?? new GetVirtualGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AppMesh::VirtualGateway
        /// </summary>
        public static Output<GetVirtualGatewayResult> Invoke(GetVirtualGatewayInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVirtualGatewayResult>("aws-native:appmesh:getVirtualGateway", args ?? new GetVirtualGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVirtualGatewayArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetVirtualGatewayArgs()
        {
        }
        public static new GetVirtualGatewayArgs Empty => new GetVirtualGatewayArgs();
    }

    public sealed class GetVirtualGatewayInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetVirtualGatewayInvokeArgs()
        {
        }
        public static new GetVirtualGatewayInvokeArgs Empty => new GetVirtualGatewayInvokeArgs();
    }


    [OutputType]
    public sealed class GetVirtualGatewayResult
    {
        public readonly string? Arn;
        public readonly string? Id;
        public readonly string? ResourceOwner;
        public readonly Outputs.VirtualGatewaySpec? Spec;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        public readonly string? Uid;

        [OutputConstructor]
        private GetVirtualGatewayResult(
            string? arn,

            string? id,

            string? resourceOwner,

            Outputs.VirtualGatewaySpec? spec,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            string? uid)
        {
            Arn = arn;
            Id = id;
            ResourceOwner = resourceOwner;
            Spec = spec;
            Tags = tags;
            Uid = uid;
        }
    }
}
