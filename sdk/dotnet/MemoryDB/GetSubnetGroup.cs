// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MemoryDB
{
    public static class GetSubnetGroup
    {
        /// <summary>
        /// The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.
        /// </summary>
        public static Task<GetSubnetGroupResult> InvokeAsync(GetSubnetGroupArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSubnetGroupResult>("aws-native:memorydb:getSubnetGroup", args ?? new GetSubnetGroupArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::MemoryDB::SubnetGroup resource creates an Amazon MemoryDB Subnet Group.
        /// </summary>
        public static Output<GetSubnetGroupResult> Invoke(GetSubnetGroupInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSubnetGroupResult>("aws-native:memorydb:getSubnetGroup", args ?? new GetSubnetGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSubnetGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
        /// </summary>
        [Input("subnetGroupName", required: true)]
        public string SubnetGroupName { get; set; } = null!;

        public GetSubnetGroupArgs()
        {
        }
        public static new GetSubnetGroupArgs Empty => new GetSubnetGroupArgs();
    }

    public sealed class GetSubnetGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the subnet group. This value must be unique as it also serves as the subnet group identifier.
        /// </summary>
        [Input("subnetGroupName", required: true)]
        public Input<string> SubnetGroupName { get; set; } = null!;

        public GetSubnetGroupInvokeArgs()
        {
        }
        public static new GetSubnetGroupInvokeArgs Empty => new GetSubnetGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetSubnetGroupResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the subnet group.
        /// </summary>
        public readonly string? ARN;
        /// <summary>
        /// An optional description of the subnet group.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// A list of VPC subnet IDs for the subnet group.
        /// </summary>
        public readonly ImmutableArray<string> SubnetIds;
        /// <summary>
        /// An array of key-value pairs to apply to this subnet group.
        /// </summary>
        public readonly ImmutableArray<Outputs.SubnetGroupTag> Tags;

        [OutputConstructor]
        private GetSubnetGroupResult(
            string? aRN,

            string? description,

            ImmutableArray<string> subnetIds,

            ImmutableArray<Outputs.SubnetGroupTag> tags)
        {
            ARN = aRN;
            Description = description;
            SubnetIds = subnetIds;
            Tags = tags;
        }
    }
}
