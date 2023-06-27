// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetPlacementGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::PlacementGroup
        /// </summary>
        public static Task<GetPlacementGroupResult> InvokeAsync(GetPlacementGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPlacementGroupResult>("aws-native:ec2:getPlacementGroup", args ?? new GetPlacementGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::PlacementGroup
        /// </summary>
        public static Output<GetPlacementGroupResult> Invoke(GetPlacementGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPlacementGroupResult>("aws-native:ec2:getPlacementGroup", args ?? new GetPlacementGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPlacementGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Group Name of Placement Group.
        /// </summary>
        [Input("groupName", required: true)]
        public string GroupName { get; set; } = null!;

        public GetPlacementGroupArgs()
        {
        }
        public static new GetPlacementGroupArgs Empty => new GetPlacementGroupArgs();
    }

    public sealed class GetPlacementGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Group Name of Placement Group.
        /// </summary>
        [Input("groupName", required: true)]
        public Input<string> GroupName { get; set; } = null!;

        public GetPlacementGroupInvokeArgs()
        {
        }
        public static new GetPlacementGroupInvokeArgs Empty => new GetPlacementGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetPlacementGroupResult
    {
        /// <summary>
        /// The Group Name of Placement Group.
        /// </summary>
        public readonly string? GroupName;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.PlacementGroupTag> Tags;

        [OutputConstructor]
        private GetPlacementGroupResult(
            string? groupName,

            ImmutableArray<Outputs.PlacementGroupTag> tags)
        {
            GroupName = groupName;
            Tags = tags;
        }
    }
}
