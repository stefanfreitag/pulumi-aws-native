// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetInternetGateway
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::InternetGateway
        /// </summary>
        public static Task<GetInternetGatewayResult> InvokeAsync(GetInternetGatewayArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetInternetGatewayResult>("aws-native:ec2:getInternetGateway", args ?? new GetInternetGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::InternetGateway
        /// </summary>
        public static Output<GetInternetGatewayResult> Invoke(GetInternetGatewayInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetInternetGatewayResult>("aws-native:ec2:getInternetGateway", args ?? new GetInternetGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetInternetGatewayArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of internet gateway.
        /// </summary>
        [Input("internetGatewayId", required: true)]
        public string InternetGatewayId { get; set; } = null!;

        public GetInternetGatewayArgs()
        {
        }
        public static new GetInternetGatewayArgs Empty => new GetInternetGatewayArgs();
    }

    public sealed class GetInternetGatewayInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of internet gateway.
        /// </summary>
        [Input("internetGatewayId", required: true)]
        public Input<string> InternetGatewayId { get; set; } = null!;

        public GetInternetGatewayInvokeArgs()
        {
        }
        public static new GetInternetGatewayInvokeArgs Empty => new GetInternetGatewayInvokeArgs();
    }


    [OutputType]
    public sealed class GetInternetGatewayResult
    {
        /// <summary>
        /// ID of internet gateway.
        /// </summary>
        public readonly string? InternetGatewayId;
        /// <summary>
        /// Any tags to assign to the internet gateway.
        /// </summary>
        public readonly ImmutableArray<Outputs.InternetGatewayTag> Tags;

        [OutputConstructor]
        private GetInternetGatewayResult(
            string? internetGatewayId,

            ImmutableArray<Outputs.InternetGatewayTag> tags)
        {
            InternetGatewayId = internetGatewayId;
            Tags = tags;
        }
    }
}
