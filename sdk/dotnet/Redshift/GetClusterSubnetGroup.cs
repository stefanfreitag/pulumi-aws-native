// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Redshift
{
    public static class GetClusterSubnetGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::Redshift::ClusterSubnetGroup
        /// </summary>
        public static Task<GetClusterSubnetGroupResult> InvokeAsync(GetClusterSubnetGroupArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClusterSubnetGroupResult>("aws-native:redshift:getClusterSubnetGroup", args ?? new GetClusterSubnetGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Redshift::ClusterSubnetGroup
        /// </summary>
        public static Output<GetClusterSubnetGroupResult> Invoke(GetClusterSubnetGroupInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetClusterSubnetGroupResult>("aws-native:redshift:getClusterSubnetGroup", args ?? new GetClusterSubnetGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClusterSubnetGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetClusterSubnetGroupArgs()
        {
        }
        public static new GetClusterSubnetGroupArgs Empty => new GetClusterSubnetGroupArgs();
    }

    public sealed class GetClusterSubnetGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetClusterSubnetGroupInvokeArgs()
        {
        }
        public static new GetClusterSubnetGroupInvokeArgs Empty => new GetClusterSubnetGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetClusterSubnetGroupResult
    {
        public readonly string? Description;
        public readonly string? Id;
        public readonly ImmutableArray<string> SubnetIds;
        public readonly ImmutableArray<Outputs.ClusterSubnetGroupTag> Tags;

        [OutputConstructor]
        private GetClusterSubnetGroupResult(
            string? description,

            string? id,

            ImmutableArray<string> subnetIds,

            ImmutableArray<Outputs.ClusterSubnetGroupTag> tags)
        {
            Description = description;
            Id = id;
            SubnetIds = subnetIds;
            Tags = tags;
        }
    }
}
