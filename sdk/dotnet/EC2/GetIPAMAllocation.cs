// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetIPAMAllocation
    {
        /// <summary>
        /// Resource Schema of AWS::EC2::IPAMAllocation Type
        /// </summary>
        public static Task<GetIPAMAllocationResult> InvokeAsync(GetIPAMAllocationArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetIPAMAllocationResult>("aws-native:ec2:getIPAMAllocation", args ?? new GetIPAMAllocationArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Schema of AWS::EC2::IPAMAllocation Type
        /// </summary>
        public static Output<GetIPAMAllocationResult> Invoke(GetIPAMAllocationInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetIPAMAllocationResult>("aws-native:ec2:getIPAMAllocation", args ?? new GetIPAMAllocationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIPAMAllocationArgs : global::Pulumi.InvokeArgs
    {
        [Input("cidr", required: true)]
        public string Cidr { get; set; } = null!;

        /// <summary>
        /// Id of the allocation.
        /// </summary>
        [Input("ipamPoolAllocationId", required: true)]
        public string IpamPoolAllocationId { get; set; } = null!;

        /// <summary>
        /// Id of the IPAM Pool.
        /// </summary>
        [Input("ipamPoolId", required: true)]
        public string IpamPoolId { get; set; } = null!;

        public GetIPAMAllocationArgs()
        {
        }
        public static new GetIPAMAllocationArgs Empty => new GetIPAMAllocationArgs();
    }

    public sealed class GetIPAMAllocationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("cidr", required: true)]
        public Input<string> Cidr { get; set; } = null!;

        /// <summary>
        /// Id of the allocation.
        /// </summary>
        [Input("ipamPoolAllocationId", required: true)]
        public Input<string> IpamPoolAllocationId { get; set; } = null!;

        /// <summary>
        /// Id of the IPAM Pool.
        /// </summary>
        [Input("ipamPoolId", required: true)]
        public Input<string> IpamPoolId { get; set; } = null!;

        public GetIPAMAllocationInvokeArgs()
        {
        }
        public static new GetIPAMAllocationInvokeArgs Empty => new GetIPAMAllocationInvokeArgs();
    }


    [OutputType]
    public sealed class GetIPAMAllocationResult
    {
        /// <summary>
        /// Id of the allocation.
        /// </summary>
        public readonly string? IpamPoolAllocationId;

        [OutputConstructor]
        private GetIPAMAllocationResult(string? ipamPoolAllocationId)
        {
            IpamPoolAllocationId = ipamPoolAllocationId;
        }
    }
}
